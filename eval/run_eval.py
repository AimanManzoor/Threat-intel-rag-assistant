
"""Evaluation harness for the Unit 42 RAG."""
import json
import time
from pathlib import Path
from statistics import median

from src.graph import app

EVAL_DIR = Path(__file__).parent
QUESTIONS_PATH = EVAL_DIR / "questions.jsonl"
RESULTS_PATH = EVAL_DIR / "results.json"
SUMMARY_PATH = EVAL_DIR / "summary.md"


def load_questions():
    return [json.loads(line) for line in open(QUESTIONS_PATH) if line.strip()]


def evaluate_one(q):
    start = time.time()
    base = {
        "id": q["id"],
        "query": q["query"],
        "expected_substrings": q.get("expected_substrings", []),
        "answer": "",
        "citations": [],
        "reranked_docs": [],
        "confidence": 0.0,
        "attempts": 0,
        "route": "?",
        "rewritten": "",
        "answer_match": False,
        "latency": 0.0,
        "error": None,
    }
    try:
        result = app.invoke({"query": q["query"], "attempts": 0})
        base["latency"] = time.time() - start
        answer_lower = result.get("answer", "").lower()
        base["answer"] = result.get("answer", "")
        base["citations"] = result.get("citations", [])
        base["reranked_docs"] = [d.metadata.get("doc_id") for d in result.get("reranked", [])]
        base["confidence"] = result.get("confidence", 0.0)
        base["attempts"] = result.get("attempts", 0)
        base["route"] = result.get("route", "?")
        base["rewritten"] = result.get("rewritten", "")
        base["answer_match"] = any(s.lower() in answer_lower for s in q.get("expected_substrings", []))
    except Exception as e:
        base["error"] = str(e)
        base["latency"] = time.time() - start
    return base


def summarize(results):
    ok = [r for r in results if r.get("error") is None]
    n = len(ok) or 1
    return {
        "total_questions": len(results),
        "successful_runs": len(ok),
        "errored_runs": len(results) - len(ok),
        "answer_match_rate": sum(r["answer_match"] for r in ok) / n,
        "avg_confidence": sum(r["confidence"] for r in ok) / n,
        "avg_attempts": sum(r["attempts"] for r in ok) / n,
        "median_latency_s": median(r["latency"] for r in ok) if ok else 0,
        "p95_latency_s": sorted(r["latency"] for r in ok)[int(len(ok) * 0.95)] if len(ok) > 1 else 0,
        "route_distribution": {
            "simple": sum(1 for r in ok if r["route"] == "simple"),
            "multi_hop": sum(1 for r in ok if r["route"] == "multi_hop"),
        },
    }


def write_summary(metrics, results):
    lines = [
        "# Eval Summary — Unit 42 Threat Intel RAG (v0.1)",
        "",
        f"- **Total questions:** {metrics['total_questions']}",
        f"- **Successful runs:** {metrics['successful_runs']}",
        f"- **Errors:** {metrics['errored_runs']}",
        f"- **Answer match rate:** {metrics['answer_match_rate']:.1%}",
        f"- **Avg confidence:** {metrics['avg_confidence']:.2f}",
        f"- **Avg attempts:** {metrics['avg_attempts']:.2f}",
        f"- **Median latency:** {metrics['median_latency_s']:.2f}s",
        f"- **P95 latency:** {metrics['p95_latency_s']:.2f}s",
        f"- **Routes:** simple={metrics['route_distribution']['simple']}, multi_hop={metrics['route_distribution']['multi_hop']}",
        "",
        "## Failures",
        "",
    ]
    failures = [r for r in results if r.get("error") or not r.get("answer_match")]
    if not failures:
        lines.append("_No failures._")
    for r in failures:
        lines.append(f"### {r.get('id', '?')}: {r.get('query', '?')}")
        if r.get("error"):
            lines.append(f"- ERRORED: `{r['error']}`")
        lines.append(f"- Expected substrings: `{r.get('expected_substrings', [])}`")
        lines.append(f"- Cited: `{r.get('citations', [])}`")
        lines.append(f"- Reranked top-5: `{r.get('reranked_docs', [])}`")
        lines.append(f"- Confidence: {r.get('confidence', 0.0):.2f}")
        lines.append(f"- Answer: {r.get('answer', '')[:200]}...")
        lines.append("")
    SUMMARY_PATH.write_text("\n".join(lines))


def main():
    questions = load_questions()
    print(f"Loaded {len(questions)} questions\n")
    results = []
    for i, q in enumerate(questions, 1):
        print(f"[{i}/{len(questions)}] {q['id']}: {q['query'][:60]}...", end=" ", flush=True)
        r = evaluate_one(q)
        if r.get("error"):
            print(f"ERROR: {r['error']}")
        else:
            mark = "✓" if r["answer_match"] else "✗"
            print(f"[{mark}] conf={r['confidence']:.2f} {r['latency']:.1f}s")
        results.append(r)
    metrics = summarize(results)
    RESULTS_PATH.write_text(json.dumps({"metrics": metrics, "results": results}, indent=2))
    write_summary(metrics, results)
    print("\n" + "=" * 60)
    print("EVAL COMPLETE")
    print("=" * 60)
    for k, v in metrics.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
