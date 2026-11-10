import os
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import streamlit as st
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]


def button(app, label):
    return next(item for item in app.button if item.label == label)


class StreamlitAppTests(unittest.TestCase):
    def setUp(self):
        st.cache_resource.clear()
        dotenv = patch("dotenv.load_dotenv")
        dotenv.start()
        self.addCleanup(dotenv.stop)
        environment = patch.dict(os.environ, {
            "ANTHROPIC_API_KEY": "test-a", "COHERE_API_KEY": "test-c",
        })
        environment.start()
        self.addCleanup(environment.stop)
        self.graph = Mock()
        self.graph.invoke.return_value = {
            "answer": "Jolly Scorpius [report]", "route": "simple",
            "confidence": 0.8, "attempts": 1, "citations": ["report"],
            "reranked": [types.SimpleNamespace(
                metadata={"doc_id": "report", "raw_chunk": "Source evidence"},
                page_content="embedding text")],
        }
        graph_module = types.ModuleType("src.graph")
        graph_module.app = self.graph
        modules = patch.dict(sys.modules, {"src.graph": graph_module})
        modules.start()
        self.addCleanup(modules.stop)
        count = patch("src.app_runtime.index_count", return_value=2)
        self.count = count.start()
        self.addCleanup(count.stop)
        initialize = patch("src.app_runtime.initialize_index", return_value=2)
        self.initialize = initialize.start()
        self.addCleanup(initialize.stop)
        self.addCleanup(st.cache_resource.clear)

    def page(self):
        page = AppTest.from_file(str(ROOT / "app.py")).run(timeout=15)
        self.assertEqual(len(page.exception), 0)
        return page

    def ask(self, page):
        page.text_input[0].set_value("Which group operates RansomHouse?").run()
        button(page, "Run query").click().run(timeout=15)
        self.assertEqual(len(page.exception), 0)
        return page

    def test_missing_credentials_render_setup_without_query_calls(self):
        with patch.dict(os.environ, {}, clear=True):
            page = self.page()
        self.assertTrue(button(page, "Run query").disabled)
        self.assertIn("Threat-Intel", page.title[0].value)
        self.graph.invoke.assert_not_called()

    def test_missing_index_requires_explicit_initialization(self):
        self.count.return_value = 0
        page = self.page()
        self.assertTrue(button(page, "Run query").disabled)
        self.initialize.assert_not_called()
        def initialize():
            self.count.return_value = 2
            return 2
        self.initialize.side_effect = initialize
        button(page, "Initialize search index").click().run(timeout=15)
        self.initialize.assert_called_once()
        self.assertFalse(button(page, "Run query").disabled)
        self.graph.invoke.assert_not_called()

    def test_example_populates_query_without_submitting(self):
        page = self.page()
        example = next(b for b in page.button if b.label.startswith("According to"))
        example.click().run()
        self.assertIn("RansomHouse", page.text_input[0].value)
        self.graph.invoke.assert_not_called()

    def test_query_calls_correct_graph_and_displays_persistent_result(self):
        page = self.ask(self.page())
        self.graph.invoke.assert_called_once_with({
            "query": "Which group operates RansomHouse?", "attempts": 0,
        })
        self.assertIn("simple", [metric.value for metric in page.metric])
        self.assertIn("report", [code.value for code in page.code])
        page.run()
        self.assertEqual(len(page.metric), 4)
        self.graph.invoke.assert_called_once()

    def test_rate_limit_is_displayed_without_exposing_exception_message(self):
        class RateLimitError(Exception):
            status_code = 429
        self.graph.invoke.side_effect = RateLimitError("PRIVATE_CREDENTIAL_VALUE")
        page = self.ask(self.page())
        self.assertIn("rate limit", page.error[0].value)
        self.assertNotIn("PRIVATE_CREDENTIAL_VALUE", page.error[0].value)
        self.assertEqual(len(page.metric), 0)

    def test_invalid_citation_ids_are_flagged(self):
        self.graph.invoke.return_value["citations"] = ["wrong-id"]
        page = self.ask(self.page())
        self.assertTrue(any("do not exactly match" in warning.value for warning in page.warning))

    def test_index_open_error_is_displayed_and_query_is_disabled(self):
        self.count.side_effect = RuntimeError("PRIVATE_PATH")
        page = self.page()
        self.assertIn("RuntimeError", page.error[0].value)
        self.assertNotIn("PRIVATE_PATH", page.error[0].value)
        self.assertTrue(button(page, "Run query").disabled)


if __name__ == "__main__":
    unittest.main()
