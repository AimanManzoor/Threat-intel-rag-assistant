import os
from pathlib import Path
import unittest
from unittest.mock import patch

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]


class EvidenceDashboardTests(unittest.TestCase):
    def page(self):
        page = AppTest.from_file(str(ROOT / "app.py"), default_timeout=15)
        page.session_state["workspace"] = "Evidence graph (offline)"
        return page.run()

    def test_offline_dashboard_never_initializes_providers_or_index(self):
        with patch.dict(os.environ, {}, clear=True), \
                patch("src.app_runtime.configure_credentials") as credentials, \
                patch("src.app_runtime.index_count") as index, \
                patch("src.app_runtime.initialize_index") as initialize:
            page = self.page()
            self.assertFalse(page.exception)
            self.assertEqual([metric.value for metric in page.metric], ["5", "3", "3"])
            next(button for button in page.button if button.label == "Explore evidence").click().run()
            self.assertFalse(page.exception)
            receipt = page.json[0].value
            self.assertIn('"provider_calls": 0', receipt)
            self.assertIn("CVE-2025-20333", receipt)
            credentials.assert_not_called()
            index.assert_not_called()
            initialize.assert_not_called()

    def test_changing_plan_hides_old_receipt_until_resubmitted(self):
        page = self.page()
        next(button for button in page.button if button.label == "Explore evidence").click().run()
        self.assertEqual(len(page.json), 1)
        page.slider[0].set_value(2).run()
        self.assertFalse(page.exception)
        self.assertEqual(len(page.json), 0)
        page.slider[1].set_value(1)
        next(button for button in page.button if button.label == "Explore evidence").click().run()
        self.assertFalse(page.exception)
        self.assertIn('"truncated": true', page.json[0].value)


if __name__ == "__main__":
    unittest.main()
