import copy
import json
import os
from pathlib import Path
import tempfile
import types
import unittest
from unittest.mock import Mock, patch

from streamlit.testing.v1 import AppTest
from src.budgeted_rag import (
    approved_bodies, bounded_context, check_claims, filter_evidence, run_budgeted,
)

ROOT = Path(__file__).resolve().parents[1]
PASSAGE = "RansomHouse encryption uses a documented mechanism in this controlled source."


class FakeServices:
    def __init__(self):
        self.calls = []
        self.candidates = [{"doc_id": "a", "text": PASSAGE}]
        self.indices = [0]
        self.response = {
            "complete": True,
            "text": json.dumps({"abstain": False, "claims": [
                {"text": PASSAGE, "source_id": "a", "quote": PASSAGE}]}),
            "usage": {"input_tokens": 100, "output_tokens": 50},
        }

    def embed(self, question):
        self.calls.append("embedding")
        return {"vector": [.1], "usage": {"input_tokens": 5}}

    def retrieve(self, vector):
        self.calls.append("retrieve")
        return self.candidates

    def rerank(self, question, evidence):
        self.calls.append("rerank")
        return {"indices": self.indices, "usage": {"search_units": 1}}

    def generate(self, question, evidence):
        self.calls.append("generation")
        return self.response


class BudgetedRAGTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        corpus = self.root / "data/processed"
        corpus.mkdir(parents=True)
        (corpus / "a.md").write_text(
            "# Report\n## Summary\n" + PASSAGE +
            "\n### Related Articles\nFooter-only material that is not source-body evidence.\n")
        self.services = FakeServices()
        self.factory = Mock(return_value=self.services)

    def run_paid(self):
        return run_budgeted("What does the source say about RansomHouse encryption?",
                            allow_paid=True, model="claude-test-model", root=self.root, factory=self.factory)

    def test_exact_cve_uses_zero_provider_operations(self):
        result = run_budgeted("CVE-2025-20333", allow_paid=True, model="claude-test-model", factory=self.factory)
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["provider_calls"], 0)
        self.factory.assert_not_called()

    def test_unknown_cve_and_unsupported_cve_request_stay_free(self):
        for question, status in [("CVE-2099-99999", "no_matches"),
                                 ("Who exploits CVE-2025-20333?", "clarification_required"),
                                 ("Which reports mention CVE-25-1234?", "clarification_required")]:
            result = run_budgeted(question, allow_paid=True, model="claude-test-model", factory=self.factory)
            self.assertEqual(result["status"], status)
            self.assertEqual(result["provider_calls"], 0)
        self.factory.assert_not_called()

    def test_paid_opt_in_and_model_configuration(self):
        for allowed, model, status in [(False, "", "paid_disabled"),
                                       (True, "", "configuration_error")]:
            result = run_budgeted("A broader question", allow_paid=allowed, model=model, factory=self.factory)
            self.assertEqual(result["status"], status)
        self.factory.assert_not_called()

    def test_three_operations_and_quote_checks(self):
        result = self.run_paid()
        self.assertEqual(result["status"], "evidence_checked_requires_review")
        self.assertEqual(result["provider_calls"], 3)
        self.assertEqual([event["stage"] for event in result["provider_attempts"]],
                         ["embedding", "rerank", "generation"])
        self.assertLessEqual(result["context_chars"], 8000)
        self.assertTrue(result["human_review_required"])
        self.assertEqual(len(result["claims"]), 1)

    def test_missing_or_footer_evidence_abstains_before_generation(self):
        for candidate in [
            [], [{"doc_id": "unknown", "text": PASSAGE}],
            [{"doc_id": "a", "text": "Footer-only material that is not source-body evidence."}],
        ]:
            self.services.candidates = candidate
            result = self.run_paid()
            self.assertEqual(result["status"], "abstained")
            self.assertEqual(result["provider_calls"], 1)
            self.assertEqual(result["claims"], [])

    def test_provider_error_is_not_retried_or_exposed(self):
        self.services.embed = Mock(side_effect=RuntimeError("PRIVATE_API_KEY"))
        result = self.run_paid()
        self.services.embed.assert_called_once()
        self.assertEqual(result["provider_calls"], 1)
        self.assertEqual(result["status"], "operation_failed")
        self.assertNotIn("PRIVATE_API_KEY", json.dumps(result))

    def test_bad_quotes_and_incomplete_response_release_no_claims(self):
        payload = {"abstain": False, "claims": [
            {"text": "Candidate claim", "source_id": "a",
             "quote": "An invented quote that the supplied source does not contain."}]}
        self.services.response["text"] = json.dumps(payload)
        result = self.run_paid()
        self.assertEqual((result["status"], result["claims"]), ("requires_review", []))
        self.services.response["complete"] = False
        result = self.run_paid()
        self.assertEqual(result["status"], "requires_review")
        self.assertEqual(result["provider_calls"], 3)

    def test_quote_membership_does_not_claim_entailment(self):
        self.services.response["text"] = json.dumps({
            "abstain": False, "claims": [{
                "text": "Every deployment is safe, an unsupported assertion.",
                "source_id": "a", "quote": PASSAGE}]})
        result = self.run_paid()
        self.assertEqual(result["status"], "evidence_checked_requires_review")
        self.assertTrue(result["human_review_required"])
        self.assertIn("human review", result["message"])

    def test_source_scope_failure_precedes_provider_operations(self):
        outside = self.root / "outside.md"
        outside.write_text("PRIVATE_CONTENT")
        (self.root / "data/processed/linked.md").symlink_to(outside)
        result = self.run_paid()
        self.assertEqual(result["status"], "source_error")
        self.factory.assert_not_called()

    def test_bad_rerank_result_stops_before_generation(self):
        self.services.indices = [99]
        result = self.run_paid()
        self.assertEqual(result["status"], "operation_failed")
        self.assertEqual(result["provider_calls"], 2)
        self.assertNotIn("generation", self.services.calls)

    def test_context_limits_keep_whole_excerpts(self):
        docs = [{"doc_id": str(i), "text": "x" * 2000} for i in range(4)]
        selected = bounded_context(docs, [0, 1, 2, 3])
        self.assertLessEqual(len(json.dumps(selected, ensure_ascii=False)), 8000)
        self.assertTrue(all(len(doc["text"]) == 2000 for doc in selected))
        with self.assertRaises(ValueError):
            bounded_context(docs, [0, 0])

    def test_response_schema_abstention_and_duplicate_keys(self):
        self.assertEqual(check_claims('{"abstain":true,"claims":[]}', []), [])
        with self.assertRaises(ValueError):
            check_claims('{"abstain":true,"abstain":false,"claims":[]}', [])
        with self.assertRaises(ValueError):
            check_claims('{"abstain":false,"claims":[]}', [])

    def test_invalid_question_never_calls_factory(self):
        for question in ["", "x" * 1001, None]:
            result = run_budgeted(question, allow_paid=True, model="claude-test-model", factory=self.factory)
            self.assertEqual(result["status"], "rejected")
            self.assertEqual(result["provider_calls"], 0)
        self.factory.assert_not_called()


class BudgetedUITests(unittest.TestCase):
    def page(self):
        page = AppTest.from_file(str(ROOT / "app.py"), default_timeout=30)
        page.session_state["workspace"] = "Budgeted assistant (opt-in)"
        return page.run()

    def submit(self, question):
        page = self.page()
        next(field for field in page.text_input if field.label == "Question for budgeted assistant").set_value(question)
        next(button for button in page.button if button.label == "Run budgeted request").click().run()
        self.assertFalse(page.exception)
        return page, json.loads(page.json[0].value)

    def test_graph_lookup_without_credentials_or_index(self):
        with patch("src.app_runtime.configure_credentials") as credentials, \
                patch("src.app_runtime.index_count") as index:
            page, result = self.submit("CVE-2025-20333")
            self.assertEqual(result["provider_calls"], 0)
            self.assertEqual(result["route"], "deterministic_graph")
            credentials.assert_not_called()
            index.assert_not_called()

    def test_paid_operations_disabled_by_default(self):
        with patch("src.budgeted_ui.paid_enabled", return_value=False):
            page, result = self.submit("What does the RansomHouse report describe?")
        self.assertTrue(page.checkbox[0].disabled)
        self.assertEqual(result["status"], "paid_disabled")
        self.assertEqual(result["provider_calls"], 0)


class LiveAdapterTests(unittest.TestCase):
    def test_sdk_retries_are_disabled_and_generation_is_bounded(self):
        from src.budgeted_live import LiveServices
        cohere_client, anthropic_client, collection = Mock(), Mock(), Mock()
        cohere_client.embed.return_value = types.SimpleNamespace(
            embeddings=types.SimpleNamespace(float=[[.1]]), meta=None)
        cohere_client.rerank.return_value = types.SimpleNamespace(
            results=[types.SimpleNamespace(index=0)], meta=None)
        anthropic_client.messages.create.return_value = types.SimpleNamespace(
            content=[types.SimpleNamespace(type="text", text='{"abstain":true,"claims":[]}')],
            stop_reason="end_turn", usage=types.SimpleNamespace(input_tokens=10, output_tokens=5))
        collection.count.return_value = 1
        collection.query.return_value = {
            "metadatas": [[{"doc_id": "a", "raw_chunk": PASSAGE}]], "documents": [[PASSAGE]]}
        cohere_module = types.SimpleNamespace(ClientV2=Mock(return_value=cohere_client))
        anthropic_module = types.SimpleNamespace(Anthropic=Mock(return_value=anthropic_client))
        chroma_module = types.SimpleNamespace(PersistentClient=Mock())
        chroma_module.PersistentClient.return_value.get_collection.return_value = collection
        config_module = types.SimpleNamespace(Settings=Mock())
        modules = {"cohere": cohere_module, "anthropic": anthropic_module,
                   "chromadb": chroma_module, "chromadb.config": config_module}
        with patch.dict("sys.modules", modules), patch.dict(os.environ, {
                "ANTHROPIC_API_KEY": "test-a", "COHERE_API_KEY": "test-c"}), \
                patch("src.app_runtime.index_count", return_value=1):
            services = LiveServices(ROOT, "test-model")
            services.embed("Question")
            services.retrieve([.1])
            services.rerank("Question", [{"doc_id": "a", "text": PASSAGE}])
            services.generate("Question", [{"doc_id": "a", "text": PASSAGE}])
        self.assertEqual(anthropic_module.Anthropic.call_args.kwargs["max_retries"], 0)
        self.assertEqual(cohere_client.embed.call_args.kwargs["request_options"]["max_retries"], 0)
        self.assertEqual(cohere_client.rerank.call_args.kwargs["request_options"]["max_retries"], 0)
        generation = anthropic_client.messages.create.call_args.kwargs
        self.assertEqual(generation["max_tokens"], 1024)
        self.assertNotIn("tools", generation)


if __name__ == "__main__":
    unittest.main()
