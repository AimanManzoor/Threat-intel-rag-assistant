import ast
import importlib.util
import io
import json
import sys
import tempfile
import types
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def controlled_graph(score):
    tree = ast.parse((ROOT / "src/nodes.py").read_text())
    route = next(
        n for n in tree.body
        if isinstance(n, ast.FunctionDef) and n.name == "route"
    )
    router_model = Mock(
        side_effect=AssertionError("Router model must not be called")
    )
    namespace = {
        "_haiku": types.SimpleNamespace(invoke=router_model),
        "HumanMessage": lambda **kwargs: kwargs,
        "ROUTE_PROMPT": "{query}",
    }
    exec(
        compile(ast.Module(body=[route], type_ignores=[]), "route", "exec"),
        namespace,
    )
    calls = []

    def record(name, function):
        def run(state):
            calls.append(name)
            return function(state)
        return run

    nodes = types.ModuleType("src.nodes")
    nodes.rewrite_query = record(
        "rewrite_query", lambda s: {"rewritten": s["query"]}
    )
    nodes.route = record("route", namespace["route"])
    nodes.retrieve = record("retrieve", lambda s: {"chunks": []})
    nodes.rerank = record("rerank", lambda s: {"reranked": []})
    nodes.generate = record(
        "generate",
        lambda s: {"answer": "controlled answer", "citations": []},
    )
    nodes.self_check = record(
        "self_check",
        lambda s: {
            "confidence": score,
            "attempts": s.get("attempts", 0) + 1,
        },
    )
    nodes.tool_use = Mock(
        side_effect=AssertionError("Multi-hop stub must not run")
    )
    with patch.dict(sys.modules, {"src.nodes": nodes}):
        module = load_module(
            "controlled_routing_graph", ROOT / "src/graph.py"
        )
    return module.app, calls, router_model, nodes.tool_use


class RoutingTests(unittest.TestCase):
    def test_simple_path_skips_multi_hop(self):
        app, calls, router, multi_hop = controlled_graph(1.0)
        result = app.invoke({
            "query": "Which CVEs are discussed?",
            "attempts": 0,
            "route": "multi_hop",
        })
        self.assertEqual(result["route"], "simple")
        self.assertEqual(calls, [
            "rewrite_query", "route", "retrieve",
            "rerank", "generate", "self_check",
        ])
        router.assert_not_called()
        multi_hop.assert_not_called()

    def test_retry_stops_after_two_attempts(self):
        app, calls, router, multi_hop = controlled_graph(0.0)
        result = app.invoke({"query": "A question", "attempts": 0})
        self.assertEqual(result["attempts"], 2)
        self.assertEqual(calls.count("retrieve"), 2)
        router.assert_not_called()
        multi_hop.assert_not_called()

    def test_recorder_preserves_evidence_and_errors(self):
        recorder = load_module(
            "verified_eval_test", ROOT / "eval/run_verified.py"
        )

        class FakeRateLimitError(Exception):
            status_code = 429

        document = types.SimpleNamespace(
            metadata={"doc_id": "doc1", "raw_chunk": "source evidence"},
            page_content="embedding text",
        )
        app = Mock()
        app.invoke.side_effect = [
            {
                "answer": "supported answer",
                "citations": ["doc1"],
                "route": "simple",
                "reranked": [document],
            },
            FakeRateLimitError(),
        ]
        baseline = ROOT / "eval/results.json"
        before = baseline.read_bytes()

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "verification.json"
            with redirect_stdout(io.StringIO()):
                recorder.capture_run(app, [
                    {
                        "id": "q1",
                        "query": "one",
                        "expected_substrings": ["supported"],
                    },
                    {"id": "q2", "query": "two"},
                ], output)
            saved = json.loads(output.read_text())

        self.assertEqual(
            saved["results"][0]["evidence_chunks"][0]["text"],
            "source evidence",
        )
        self.assertEqual(saved["results"][1]["status_code"], 429)
        self.assertEqual(baseline.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
