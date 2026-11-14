"""Exact citation-ID checks, not an assessment of factual support."""
import re


def extract_citation_ids(answer):
    return list(dict.fromkeys(re.findall(r"\[([^\[\]\n]*)\]", answer)))


def assess_citations(answer, documents, reported=None):
    citations = extract_citation_ids(answer)
    allowed = sorted({
        doc.metadata.get("doc_id")
        for doc in documents
        if isinstance(doc.metadata.get("doc_id"), str)
        and doc.metadata["doc_id"].strip()
        and doc.metadata["doc_id"] != "unknown"
    })
    supplied = [] if reported is None else reported
    invalid = list(dict.fromkeys(
        value for value in citations + supplied if value not in allowed
    ))

    if invalid:
        status = "invalid_ids"
    elif reported is not None and set(reported) != set(citations):
        status = "inconsistent"
    elif not allowed:
        status = "no_sources"
    elif not citations:
        status = "missing_citations"
    else:
        status = "matched_ids"

    return {
        "status": status,
        "citations": citations,
        "invalid_ids": invalid,
        "allowed_source_ids": allowed,
    }


def validate_citations(state):
    report = assess_citations(
        state.get("answer", ""),
        state.get("reranked", []),
        state.get("citations"),
    )
    return {
        "citations": report["citations"],
        "citation_validation": report,
    }
