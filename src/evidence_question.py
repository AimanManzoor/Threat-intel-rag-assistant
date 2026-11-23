"""Deterministic CVE-source lookup baseline; not general question understanding."""
import argparse
import json
import re

from src.evidence_harness import ROOT, run_graph_plan

TOKEN = r"CVE-[0-9]{4}-[0-9]{4,}"
FIND_CVE = re.compile(r"(?<![A-Za-z0-9_-])" + TOKEN + r"(?![A-Za-z0-9_-])", re.I | re.ASCII)
PATTERNS = [
    TOKEN,
    r"(?:which|what) (?:reports|sources|documents) (?:mention|reference|contain) " + TOKEN,
    r"(?:show|list|find|retrieve) (?:the )?(?:reports|sources|documents) "
    r"(?:(?:that )?(?:mention|reference|contain)|mentioning|referencing|for) " + TOKEN,
    r"where is " + TOKEN + r" (?:mentioned|referenced)",
]
SUPPORTED = re.compile(
    r"(?:please )?(?:" + "|".join(PATTERNS) + r")(?: please)?[?.!]?",
    re.I | re.ASCII,
)


def parse_question(question):
    base = {"cve_id": None, "plan": None}
    if (not isinstance(question, str) or not question.strip()
            or len(question) > 1000 or not question.isprintable()):
        return {**base, "status": "rejected", "reason": "invalid_input",
                "message": "Enter a single-line source lookup of 1-1000 printable characters."}
    normalized = " ".join(question.strip().split())
    identifiers = list(dict.fromkeys(value.upper() for value in FIND_CVE.findall(normalized)))
    if len(identifiers) != 1:
        reason = "missing_cve" if not identifiers else "multiple_cves"
        return {**base, "status": "clarification_required", "reason": reason,
                "message": "Provide one exact CVE identifier for a source lookup."}
    if len(identifiers[0]) > 128 or not SUPPORTED.fullmatch(normalized):
        return {**base, "status": "clarification_required", "reason": "unsupported_request",
                "message": "I only retrieve literal CVE mentions. Try: Which reports mention CVE-2025-20333?"}
    cve = identifiers[0]
    return {"status": "ready", "reason": "supported_lookup", "cve_id": cve,
            "message": "Supported exact-CVE source lookup.",
            "plan": {"tool": "graph_neighborhood", "node_id": "cve:" + cve,
                     "max_hops": 1, "max_edges": 20}}


def run_question(question, *, root=ROOT):
    parsed = parse_question(question)
    report = {
        "status": parsed["status"], "reason": parsed["reason"], "message": parsed["message"],
        "cve_id": parsed["cve_id"], "plan": parsed["plan"], "sources": [],
        "tool_calls": 0, "provider_calls": 0, "human_review_required": True,
    }
    if parsed["status"] != "ready":
        return report
    receipt = run_graph_plan(parsed["plan"], root=root)
    report.update(tool_calls=receipt["tool_calls"], provider_calls=receipt["provider_calls"])
    if receipt["status"] not in {"completed", "no_matches"}:
        return {**report, "status": "verification_failed", "reason": "harness_failure",
                "message": "Evidence verification failed; no source summary was produced."}
    by_id = {node["id"]: node for node in receipt["nodes"]}
    sources = []
    for edge in receipt["edges"]:
        source = by_id.get(edge["source"], {})
        if (edge["target"] != parsed["plan"]["node_id"] or edge.get("hop") != 1
                or edge["relation"] != "mentions" or edge["confidence"] != "EXTRACTED"
                or source.get("entity_type") != "report"
                or source.get("source_file") != edge["source_file"]):
            return {**report, "status": "verification_failed", "reason": "returned_scope_mismatch",
                    "message": "Returned evidence did not match the requested CVE source scope."}
        sources.append({
            "report_id": edge["source"], "report_title": source["label"],
            "source_file": edge["source_file"], "source_location": edge["source_location"],
            "excerpt": edge["excerpt"],
        })
    if (receipt["tool_calls"] != 1 or receipt["provider_calls"] != 0
            or len(sources) > 20
            or len({source["report_id"] for source in sources}) != len(sources)
            or (receipt["status"] == "no_matches" and sources)
            or (receipt["status"] == "completed" and not sources)):
        return {**report, "status": "verification_failed", "reason": "returned_contract_mismatch",
                "message": "Returned evidence violated the source-lookup contract."}
    if sources:
        message = f"Returned {len(sources)} report mention(s) for {parsed['cve_id']} in this scoped corpus."
        if receipt["truncated"]:
            message += " The edge limit was reached; this result is incomplete."
    else:
        message = (f"No mention of {parsed['cve_id']} was found in this scoped graph. "
                   "This does not establish that the CVE is nonexistent or unexploited.")
    return {**report, "status": receipt["status"], "reason": "source_lookup",
            "message": message, "sources": sources, "receipt": receipt}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--question", required=True)
    args = parser.parse_args()
    report = run_question(args.question)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    raise SystemExit(0 if report["status"] in {"completed", "no_matches"} else 1)


if __name__ == "__main__":
    main()
