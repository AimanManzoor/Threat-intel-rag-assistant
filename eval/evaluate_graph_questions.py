"""Evaluate versioned exact-CVE source lookup contracts without providers."""
import hashlib
import json
from pathlib import Path

from src.evidence_question import run_question

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {"id", "question", "expected_status", "expected_cve", "expected_tool_calls", "expected_source_files"}


def evaluate_cases(reference, *, root=ROOT):
    if (not isinstance(reference, dict) or type(reference.get("schema_version")) is not int
            or reference.get("schema_version") != 1 or reference.get("suite_id") != "graph_source_lookup_v1"):
        raise ValueError("Unsupported source-lookup reference.")
    cases = reference.get("cases")
    if not isinstance(cases, list) or not 1 <= len(cases) <= 100:
        raise ValueError("Expected 1-100 reference cases.")
    seen = set()
    for case in cases:
        if not isinstance(case, dict) or set(case) != FIELDS:
            raise ValueError("Unexpected reference case fields.")
        if (not isinstance(case["id"], str) or not case["id"] or case["id"] in seen
                or not isinstance(case["question"], str) or len(case["question"]) > 1000
                or not isinstance(case["expected_status"], str)
                or case["expected_status"] not in {"completed", "no_matches", "clarification_required", "rejected"}
                or type(case["expected_tool_calls"]) is not int or case["expected_tool_calls"] not in (0, 1)
                or (case["expected_cve"] is not None and not isinstance(case["expected_cve"], str))
                or not isinstance(case["expected_source_files"], list)
                or any(not isinstance(name, str) for name in case["expected_source_files"])):
            raise ValueError("Invalid reference values.")
        seen.add(case["id"])
    results = []
    for case in cases:
        report = run_question(case["question"], root=root)
        sources = sorted({source["source_file"] for source in report["sources"]})
        plan = report.get("plan")
        checks = {
            "status": report["status"] == case["expected_status"],
            "cve_scope": report["cve_id"] == case["expected_cve"],
            "tool_calls": report["tool_calls"] == case["expected_tool_calls"],
            "zero_provider_calls": report["provider_calls"] == 0,
            "human_review": report["human_review_required"] is True,
            "source_files": sources == sorted(case["expected_source_files"]),
            "fixed_plan": plan is None or (
                plan["tool"] == "graph_neighborhood" and plan["max_hops"] == 1
                and plan["max_edges"] == 20 and plan["node_id"] == "cve:" + report["cve_id"]),
        }
        failures = [name for name, passed in checks.items() if not passed]
        results.append({"id": case["id"], "passed": not failures, "failed_checks": failures,
                        "actual_status": report["status"], "actual_source_files": sources})
    return {
        "suite_id": reference["suite_id"],
        "reference_sha256": hashlib.sha256(json.dumps(reference, sort_keys=True).encode()).hexdigest(),
        "case_count": len(cases), "passed": sum(row["passed"] for row in results),
        "failed": sum(not row["passed"] for row in results), "results": results,
        "notice": "Controlled contract checks, not a factual-accuracy or general language-understanding score.",
    }


def main():
    try:
        reference = json.loads((ROOT / "eval/graph_question_cases_v1.json").read_text())
        report = evaluate_cases(reference)
    except (OSError, ValueError) as exc:
        print("Reference evaluation stopped:", type(exc).__name__)
        raise SystemExit(2)
    destination = ROOT / "eval/verification_graph_questions.json"
    destination.write_text(json.dumps(report, indent=2) + "\n")
    for result in report["results"]:
        print(("PASS" if result["passed"] else "FAIL"), result["id"], result["actual_status"])
    print(f"{report['passed']}/{report['case_count']} reference cases passed.")
    print(report["notice"])
    print("Detailed local report:", destination)
    raise SystemExit(0 if report["failed"] == 0 else 1)


if __name__ == "__main__":
    main()
