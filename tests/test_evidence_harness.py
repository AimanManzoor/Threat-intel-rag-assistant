import copy
import json
from pathlib import Path
import tempfile
import unittest

from src.evidence_extract import extract_mentions, PROFILE
from src.evidence_harness import load_verified_graph, run_graph_plan

DEFAULT_PLAN = {"tool": "graph_neighborhood", "node_id": "cve:CVE-2025-2222",
                "max_hops": 2, "max_edges": 20}


class EvidenceHarnessTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.corpus = self.root / "data/processed"
        self.corpus.mkdir(parents=True)
        (self.corpus / "a.md").write_text(
            "# Report A\nCVE-2099-0000 navigation\n## Summary\n"
            "CVE-2025-1111 and CVE-2025-2222.\n"
            "### Related Articles\nCVE-2099-9999 footer\n")
        (self.corpus / "b.md").write_text("# Report B\n## Summary\nCVE-2025-2222.\n")
        self.extraction = extract_mentions(self.root)
        self.graph = {
            "directed": True, "multigraph": False,
            "graph": {"schema_version": 1, "evidence_profile": PROFILE,
                      "source_manifest": self.extraction["sources"],
                      "graphify_version": "fixture"},
            "nodes": self.extraction["nodes"], "links": self.extraction["edges"],
        }
        self.path = self.root / "data/evidence_graph.json"
        self.write_graph()

    def write_graph(self):
        self.path.write_text(json.dumps(self.graph))

    def test_extraction_excludes_navigation_and_footer(self):
        ids = {node["id"] for node in self.extraction["nodes"]}
        self.assertNotIn("cve:CVE-2099-0000", ids)
        self.assertNotIn("cve:CVE-2099-9999", ids)
        self.assertEqual(len(self.extraction["edges"]), 3)
        self.assertTrue(all(edge["relation"] == "mentions" for edge in self.extraction["edges"]))

    def test_source_locations_and_excerpts(self):
        graph = load_verified_graph(self.root)
        for edge in graph["links"]:
            number = int(edge["source_location"][1:])
            line = (self.root / edge["source_file"]).read_text().splitlines()[number - 1]
            self.assertIn(edge["target"].removeprefix("cve:"), line)
            self.assertIn(edge["target"].removeprefix("cve:"), edge["excerpt"])

    def test_plan_rejection_precedes_any_file_access(self):
        cases = [{"tool": "shell", "node_id": "x", "max_hops": 1, "max_edges": 1},
                 {**DEFAULT_PLAN, "path": "/private/file"},
                 {**DEFAULT_PLAN, "max_hops": 3},
                 {**DEFAULT_PLAN, "max_hops": True},
                 {**DEFAULT_PLAN, "max_edges": 21},
                 {**DEFAULT_PLAN, "max_edges": 0}]
        for plan in cases:
            receipt = run_graph_plan(plan, root=self.root / "absent")
            self.assertEqual((receipt["status"], receipt["tool_calls"]), ("rejected", 0))

    def test_bounded_traversal_and_provider_budget(self):
        receipt = run_graph_plan({**DEFAULT_PLAN, "max_edges": 1}, root=self.root)
        self.assertEqual(receipt["status"], "completed")
        self.assertEqual(len(receipt["edges"]), 1)
        self.assertLessEqual(len(receipt["nodes"]), 2)
        self.assertTrue(receipt["truncated"])
        self.assertEqual((receipt["tool_calls"], receipt["provider_calls"]), (1, 0))
        self.assertTrue(receipt["human_review_required"])

    def test_two_hops_and_deterministic_results(self):
        first = run_graph_plan(DEFAULT_PLAN, root=self.root)
        self.assertEqual(first, run_graph_plan(DEFAULT_PLAN, root=self.root))
        self.assertEqual(len(first["edges"]), 3)
        self.assertTrue(all(edge["hop"] <= 2 for edge in first["edges"]))
        self.assertEqual(len({node["id"] for node in first["nodes"]}), 4)

    def test_unknown_node_is_not_a_safety_verdict(self):
        receipt = run_graph_plan({**DEFAULT_PLAN, "node_id": "cve:CVE-2000-0000"}, root=self.root)
        self.assertEqual(receipt["status"], "no_matches")
        self.assertEqual(receipt["edges"], [])
        self.assertTrue(receipt["human_review_required"])

    def test_stale_source_fails_verification(self):
        (self.corpus / "a.md").write_text("# Changed\n## Summary\nCVE-2025-1111\n")
        receipt = run_graph_plan(DEFAULT_PLAN, root=self.root)
        self.assertEqual(receipt["status"], "verification_failed")
        self.assertEqual(receipt["edges"], [])

    def test_forged_relationship_and_missing_edge_rejected(self):
        original = copy.deepcopy(self.graph)
        self.graph["links"][0]["relation"] = "exploits"
        self.write_graph()
        self.assertEqual(run_graph_plan(DEFAULT_PLAN, root=self.root)["status"], "verification_failed")
        self.graph = original
        self.graph["links"].pop()
        self.write_graph()
        self.assertEqual(run_graph_plan(DEFAULT_PLAN, root=self.root)["status"], "verification_failed")

    def test_path_substitution_and_duplicate_ids_rejected(self):
        original = copy.deepcopy(self.graph)
        self.graph["links"][0]["source_file"] = "../private.env"
        self.write_graph()
        self.assertEqual(run_graph_plan(DEFAULT_PLAN, root=self.root)["status"], "verification_failed")
        self.graph = original
        self.graph["nodes"].append(copy.deepcopy(self.graph["nodes"][0]))
        self.write_graph()
        self.assertEqual(run_graph_plan(DEFAULT_PLAN, root=self.root)["status"], "verification_failed")

    def test_unsupported_schema_and_duplicate_json_keys_rejected(self):
        self.graph["graph"]["schema_version"] = 99
        self.write_graph()
        self.assertEqual(run_graph_plan(DEFAULT_PLAN, root=self.root)["status"], "verification_failed")
        self.path.write_text('{"nodes":[],"nodes":[]}')
        self.assertEqual(run_graph_plan(DEFAULT_PLAN, root=self.root)["status"], "verification_failed")

    def test_source_is_unchanged_and_input_plan_is_not_mutated(self):
        before = {path: path.read_bytes() for path in self.corpus.glob("*.md")}
        plan = copy.deepcopy(DEFAULT_PLAN)
        run_graph_plan(plan, root=self.root)
        self.assertEqual(plan, DEFAULT_PLAN)
        self.assertEqual(before, {path: path.read_bytes() for path in self.corpus.glob("*.md")})

    def test_source_symlink_and_size_limit(self):
        outside = self.root / "outside.md"
        outside.write_text("PRIVATE_DATA")
        (self.corpus / "linked.md").symlink_to(outside)
        with self.assertRaises(ValueError):
            extract_mentions(self.root)
        (self.corpus / "linked.md").unlink()
        (self.corpus / "large.md").write_text("x" * 1_000_001)
        with self.assertRaises(ValueError):
            extract_mentions(self.root)


if __name__ == "__main__":
    unittest.main()
