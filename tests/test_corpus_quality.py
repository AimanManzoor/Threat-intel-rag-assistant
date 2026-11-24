from datetime import date
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from streamlit.testing.v1 import AppTest
from src.corpus_quality import audit_corpus

ROOT = Path(__file__).resolve().parents[1]


class CorpusQualityTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.corpus = self.root / "data/processed"
        self.corpus.mkdir(parents=True)

    def write(self, name="a.md", title="Alpha", published="2025-01-01",
              url="https://unit42.paloaltonetworks.com/example/",
              body="## Summary\nOrdinary text\n"):
        path = self.corpus / name
        path.write_text(
            "---\ntitle: " + title + "\ndate: " + published +
            "\nurl: " + url + "\n---\n" + body,
            encoding="utf-8",
        )
        return path

    def audit(self):
        return audit_corpus(self.root, as_of=date(2026, 1, 1))

    def test_valid_metadata_and_zero_cves(self):
        self.write()
        row = self.audit()["rows"][0]
        self.assertEqual(row["issues"], "")
        self.assertEqual(row["age_days"], 365)
        self.assertEqual(row["retained_cve_count"], 0)
        self.assertEqual(len(row["sha256"]), 64)

    def test_missing_metadata_is_visible(self):
        (self.corpus / "a.md").write_text("# Report\n## Summary\nText\n")
        row = self.audit()["rows"][0]
        self.assertIn("missing_frontmatter", row["issues"])
        self.assertIn("missing_date", row["issues"])
        self.assertIsNone(row["age_days"])

    def test_invalid_dates_urls_and_future_dates(self):
        self.write(published="2025-99-01", url="https://SECRET:pass@example.com/")
        self.write(name="b.md", title="Beta", published="2027-01-01")
        report = self.audit()
        self.assertIn("invalid_publication_date", report["rows"][0]["issues"])
        self.assertIn("invalid_source_url", report["rows"][0]["issues"])
        self.assertIn("future_declared_date", report["rows"][1]["issues"])
        self.assertNotIn("SECRET", json.dumps(report))

    def test_footer_and_navigation_are_not_retained_body(self):
        self.write(body=(
            "CVE-2099-9999 navigation\n## Summary\nCVE-2025-1111.\n"
            "### Related Articles\nCVE-2025-2222\n"
        ))
        row = self.audit()["rows"][0]
        self.assertEqual(row["retained_cves"], "CVE-2025-1111")
        self.assertEqual(row["footer_only_cves"], "CVE-2025-2222")

    def test_duplicate_candidates_and_exact_duplicates(self):
        first = self.write()
        self.write(name="b.md", title="Different title")
        (self.corpus / "c.md").write_bytes(first.read_bytes())
        summary = self.audit()["summary"]
        self.assertEqual(summary["duplicate_body_groups"], 1)
        self.assertEqual(summary["raw_duplicate_groups"], 1)

    def test_read_only_and_rejected_sources(self):
        first = self.write()
        before = first.read_bytes()
        outside = self.root / "outside.md"
        outside.write_text("SECRET")
        (self.corpus / "linked.md").symlink_to(outside)
        (self.corpus / "large.md").write_text("x" * 1_000_001)
        report = self.audit()
        issues = " ".join(row["issues"] for row in report["rows"])
        self.assertIn("unsafe_source_path", issues)
        self.assertIn("oversized_source", issues)
        self.assertNotIn("SECRET", json.dumps(report))
        self.assertEqual(first.read_bytes(), before)

    def test_offline_workspace_skips_credentials_and_index(self):
        with patch("src.app_runtime.configure_credentials") as credentials, \
                patch("src.app_runtime.index_count") as index, \
                patch("src.app_runtime.initialize_index") as initialize:
            page = AppTest.from_file(str(ROOT / "app.py"), default_timeout=15)
            page.session_state["workspace"] = "Corpus quality (offline)"
            page.run()
            self.assertFalse(page.exception)
            self.assertEqual(page.metric[0].value, "5")
            credentials.assert_not_called()
            index.assert_not_called()
            initialize.assert_not_called()


if __name__ == "__main__":
    unittest.main()
