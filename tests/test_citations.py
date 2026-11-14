import types
import unittest

from src.citations import assess_citations, extract_citation_ids
from tests.test_routing import controlled_graph


class CitationTests(unittest.TestCase):
    def setUp(self):
        self.docs = [
            types.SimpleNamespace(metadata={"doc_id": "report-1"})
        ]

    def test_exact_ids_and_duplicates(self):
        result = assess_citations(
            "Claim [report-1] [report-1]", self.docs, ["report-1"]
        )
        self.assertEqual(result["status"], "matched_ids")
        self.assertEqual(result["citations"], ["report-1"])

    def test_unknown_and_empty_ids(self):
        result = assess_citations("Claim [invented] []", self.docs)
        self.assertEqual(result["status"], "invalid_ids")
        self.assertEqual(result["invalid_ids"], ["invented", ""])

    def test_case_and_whitespace_are_not_silently_repaired(self):
        for citation in ("Report-1", " report-1 "):
            with self.subTest(citation=citation):
                result = assess_citations(
                    "Claim [" + citation + "]", self.docs
                )
                self.assertEqual(result["status"], "invalid_ids")

    def test_missing_citations(self):
        result = assess_citations("Uncited claim", self.docs, [])
        self.assertEqual(result["status"], "missing_citations")

    def test_no_sources_and_unknown_metadata(self):
        self.assertEqual(
            assess_citations("No context", [])["status"], "no_sources"
        )
        documents = [
            types.SimpleNamespace(metadata={"doc_id": "unknown"})
        ]
        self.assertEqual(
            assess_citations("Claim [unknown]", documents)["status"],
            "invalid_ids",
        )

    def test_reported_ids_must_match_answer(self):
        self.assertEqual(
            assess_citations("Claim [report-1]", self.docs, [])["status"],
            "inconsistent",
        )
        self.assertEqual(
            assess_citations(
                "Claim [report-1]", self.docs, ["invented"]
            )["status"],
            "invalid_ids",
        )

    def test_parser_preserves_order_and_full_identifiers(self):
        self.assertEqual(
            extract_citation_ids("[a.md] [b/path] [a.md]"),
            ["a.md", "b/path"],
        )

    def test_graph_runs_check_even_with_high_self_score(self):
        graph, calls, router, multi_hop = controlled_graph(1.0)
        result = graph.invoke({"query": "Question", "attempts": 0})
        self.assertEqual(result["confidence"], 1.0)
        self.assertEqual(
            result["citation_validation"]["status"], "no_sources"
        )
        self.assertEqual(result["attempts"], 1)
        router.assert_not_called()
        multi_hop.assert_not_called()
