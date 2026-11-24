"""Opt-in budgeted RAG controller. Structural evidence checks are not entailment."""
import json
import math
import re
from pathlib import Path
import time

from src.evidence_extract import FOOTER
from src.evidence_question import FIND_CVE, parse_question, run_question

ROOT = Path(__file__).resolve().parents[1]
MAX_CONTEXT = 8000
MAX_SOURCES = 4


def normalized(text):
    return " ".join(text.split())


def approved_bodies(root):
    root = Path(root).resolve()
    corpus = root / "data/processed"
    if corpus.is_symlink() or not corpus.resolve().is_relative_to(root):
        raise ValueError("Corpus scope violation.")
    files = sorted(corpus.glob("*.md"))
    if not 1 <= len(files) <= 50:
        raise ValueError("Expected 1-50 approved reports.")
    bodies = {}
    for path in files:
        if path.is_symlink() or path.resolve().parent != corpus.resolve():
            raise ValueError("Source scope violation.")
        with path.open("rb") as handle:
            raw = handle.read(1_000_001)
        if len(raw) > 1_000_000:
            raise ValueError("Source too large.")
        lines, body, started = raw.decode("utf-8").splitlines(), [], False
        for line in lines:
            if FOOTER.match(line):
                break
            if line.startswith("## "):
                started = True
            if started:
                body.append(line)
        bodies[path.stem] = normalized("\n".join(body))
    return bodies


def filter_evidence(candidates, bodies):
    if not isinstance(candidates, list) or len(candidates) > 20:
        raise ValueError("Retrieval result exceeds its contract.")
    accepted, seen = [], set()
    for item in candidates:
        if not isinstance(item, dict):
            raise ValueError("Invalid retrieval record.")
        doc_id, text = item.get("doc_id"), item.get("text")
        if not isinstance(doc_id, str) or not isinstance(text, str):
            continue
        passage = normalized(text)
        key = (doc_id, passage)
        if (doc_id in bodies and len(passage) >= 20 and len(text) <= 2000 and passage
                and passage in bodies[doc_id] and key not in seen):
            accepted.append({"doc_id": doc_id, "text": text})
            seen.add(key)
    return accepted


def bounded_context(documents, indices):
    if (not isinstance(indices, list) or len(indices) > MAX_SOURCES
            or any(type(index) is not int or not 0 <= index < len(documents) for index in indices)
            or len(set(indices)) != len(indices)):
        raise ValueError("Invalid rerank indices.")
    selected = []
    for index in indices:
        candidate = selected + [documents[index]]
        if len(json.dumps(candidate, ensure_ascii=False)) <= MAX_CONTEXT:
            selected = candidate
    return selected


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate response keys.")
        result[key] = value
    return result


def check_claims(text, evidence):
    if not isinstance(text, str) or len(text) > 12000:
        raise ValueError("Invalid model response size.")
    payload = json.loads(text, object_pairs_hook=unique_object)
    if not isinstance(payload, dict) or set(payload) != {"abstain", "claims"}:
        raise ValueError("Invalid response schema.")
    if type(payload["abstain"]) is not bool or not isinstance(payload["claims"], list):
        raise ValueError("Invalid response types.")
    claims = payload["claims"]
    if payload["abstain"]:
        if claims:
            raise ValueError("Abstention must not contain claims.")
        return []
    if not 1 <= len(claims) <= 3:
        raise ValueError("Expected 1-3 claims.")
    for claim in claims:
        if (not isinstance(claim, dict) or set(claim) != {"text", "source_id", "quote"}
                or any(not isinstance(claim[key], str) for key in claim)
                or not 1 <= len(claim["text"]) <= 500
                or len(normalized(claim["quote"])) < 20 or len(claim["quote"]) > 500):
            raise ValueError("Invalid claim fields.")
        if not any(
            doc["doc_id"] == claim["source_id"]
            and normalized(claim["quote"]) in normalized(doc["text"])
            for doc in evidence
        ):
            raise ValueError("Claim quote is absent from supplied evidence.")
    return claims


def run_budgeted(question, *, allow_paid=False, model="", root=ROOT, factory=None):
    started = time.perf_counter()
    report = {
        "status": "rejected", "route": "none", "human_review_required": True,
        "provider_attempts": [], "provider_calls": 0, "local_retrieval_attempts": 0,
        "claims": [], "evidence": [], "context_chars": 0,
        "limits": {"provider_calls": 3, "generation_calls": 1, "sources": 4,
                   "context_chars": MAX_CONTEXT, "output_tokens": 1024},
    }

    def finish(status, message):
        report.update(status=status, message=message,
                      provider_calls=len(report["provider_attempts"]),
                      elapsed_ms=round((time.perf_counter() - started) * 1000, 2))
        return report

    parsed = parse_question(question)
    if parsed["status"] == "rejected":
        return finish("rejected", parsed["message"])
    if parsed["status"] == "ready":
        result = run_question(question, root=root)
        report.update(route="deterministic_graph", source_lookup=result)
        return finish(result["status"], result["message"])
    if FIND_CVE.search(question) or re.search(r"\bCVEs?\b", question, re.I | re.ASCII):
        return finish("clarification_required", parsed["message"])
    if type(allow_paid) is not bool or not allow_paid:
        return finish("paid_disabled", "Paid RAG is disabled. Exact-CVE source lookups remain available.")
    if not isinstance(model, str) or not re.fullmatch(r"claude-[A-Za-z0-9._-]{1,100}", model.strip()):
        return finish("configuration_error", "Provide a currently available model ID from your account.")

    def call(stage, function, *args):
        if len(report["provider_attempts"]) >= 3:
            raise ValueError("Provider-call budget exhausted.")
        event = {"stage": stage, "status": "attempted", "usage": {}}
        report["provider_attempts"].append(event)
        before = time.perf_counter()
        try:
            response = function(*args)
            usage = response.get("usage", {})
            event["usage"] = {
                key: value for key, value in usage.items()
                if key in {"input_tokens", "output_tokens", "search_units"}
                and type(value) in (int, float) and math.isfinite(value) and value >= 0
            }
            event["status"] = "returned"
            return response
        except Exception as error:
            event.update(status="failed", error_type=type(error).__name__)
            raise
        finally:
            event["elapsed_ms"] = round((time.perf_counter() - before) * 1000, 2)

    try:
        bodies = approved_bodies(root)
    except (OSError, ValueError):
        return finish("source_error", "Approved source bodies could not be loaded.")
    try:
        if factory is None:
            from src.budgeted_live import LiveServices
            factory = LiveServices
        services = factory(root, model.strip())
    except Exception:
        return finish("configuration_error", "Check the index, credentials and selected model; no provider operation attempted.")
    report.update(route="budgeted_rag", model=model.strip())
    try:
        embedded = call("embedding", services.embed, question)
        report["local_retrieval_attempts"] = 1
        candidates = services.retrieve(embedded["vector"])
        accepted = filter_evidence(candidates, bodies)
        report["rejected_excerpts"] = len(candidates) - len(accepted)
        if not accepted:
            return finish("abstained", "No retrieved excerpt passed the approved-body check.")
        ranked = call("rerank", services.rerank, question, accepted)
        evidence = bounded_context(accepted, ranked["indices"])
        report.update(evidence=evidence,
                      context_chars=len(json.dumps(evidence, ensure_ascii=False)))
        if not evidence:
            return finish("abstained", "No evidence fits the context policy.")
        response = call("generation", services.generate, question, evidence)
    except Exception:
        return finish("operation_failed", "A provider or local retrieval operation failed; no automatic retry was made.")
    try:
        if response.get("complete") is not True:
            raise ValueError("Incomplete generation.")
        claims = check_claims(response["text"], report["evidence"])
    except (ValueError, KeyError, TypeError):
        return finish("requires_review", "Model output failed schema, completion or quote checks. No claims released.")
    if not claims:
        return finish("abstained", "The model reported insufficient evidence.")
    report["claims"] = claims
    return finish("evidence_checked_requires_review",
                  "Source IDs and quote text passed membership checks (whitespace-normalized). Claim support still requires human review.")
