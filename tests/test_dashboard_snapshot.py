from pathlib import Path
import shutil
import tempfile
import unittest

from dashboard.export_data import ROOT, export


class DashboardSnapshotTests(unittest.TestCase):
    def fixture(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)

        shutil.copytree(
            ROOT / "data/processed",
            root / "data/processed",
        )
        shutil.copyfile(
            ROOT / "data/evidence_graph.json",
            root / "data/evidence_graph.json",
        )
        return root

    def test_export_then_check_succeeds(self):
        root = self.fixture()
        export(root)

        path = root / "dashboard/data.js"
        before = path.read_bytes()

        export(root, check=True)

        self.assertEqual(path.read_bytes(), before)

    def test_edited_snapshot_is_rejected_without_repairing_it(self):
        root = self.fixture()
        export(root)

        path = root / "dashboard/data.js"
        path.write_text("window.THREAT_DATA = {};\n", encoding="utf-8")
        before = path.read_bytes()

        with self.assertRaisesRegex(ValueError, "stale"):
            export(root, check=True)

        self.assertEqual(path.read_bytes(), before)

    def test_changed_source_stops_export_and_preserves_snapshot(self):
        root = self.fixture()
        export(root)

        destination = root / "dashboard/data.js"
        before = destination.read_bytes()

        source = next((root / "data/processed").glob("*.md"))
        with source.open("a", encoding="utf-8") as handle:
            handle.write("\nChanged source content.\n")

        with self.assertRaises(ValueError):
            export(root)

        self.assertEqual(destination.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
