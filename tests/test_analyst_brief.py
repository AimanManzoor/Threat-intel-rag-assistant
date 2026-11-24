import copy
import unittest
from unittest.mock import patch

from src.analyst_brief import make_brief
from src.evidence_question import run_question


class AnalystBriefTests(unittest.TestCase):
    def setUp(self):
        self.report = run_question("CVE-2025-20333")

    def test_completed_brief_contains_source_and_fingerprint(self):
        text = make_brief(self.report)
        self.assertIn("CVE-2025-20333", text)
        self.assertIn(self.report["sources"][0]["source_file"], text)
        self.assertIn(self.report["receipt"]["artifact_sha256"], text)
        self.assertIn("Human review: REQUIRED", text)

    def test_no_match_retains_scope_warning(self):
        text = make_brief(run_question("CVE-2099-99999"))
        self.assertIn("No mention was found in this scoped graph.", text)
        self.assertIn("No match is not proof", text)

    def test_unverified_or_inconsistent_results_are_refused(self):
        for change in [
            {"status": "verification_failed"},
            {"human_review_required": False},
            {"provider_calls": 1},
            {"sources": []},
        ]:
            with self.subTest(change=change), self.assertRaises(ValueError):
                make_brief({**self.report, **change})

    def test_truncated_result_is_disclosed(self):
        report = copy.deepcopy(self.report)
        report["receipt"]["truncated"] = True
        self.assertIn("PARTIAL", make_brief(report))

    def test_formatter_makes_no_additional_tool_calls(self):
        with patch("src.evidence_question.run_graph_plan") as tool:
            make_brief(self.report)
            tool.assert_not_called()


if __name__ == "__main__":
    unittest.main()
