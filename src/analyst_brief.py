"""Readable evidence handoff from an existing verified source lookup."""
import re


def make_brief(report):
    status = report.get("status")
    sources = report.get("sources")
    cve = report.get("cve_id")
    if (
        status not in ("completed", "no_matches")
        or report.get("human_review_required") is not True
        or report.get("provider_calls") != 0
        or report.get("tool_calls") != 1
        or not isinstance(cve, str)
        or not re.fullmatch(r"CVE-[0-9]{4}-[0-9]{4,}", cve)
        or not isinstance(sources, list)
        or len(sources) > 20
        or bool(sources) != (status == "completed")
    ):
        raise ValueError("A successful, scoped source lookup is required.")

    receipt = report.get("receipt", {})
    fingerprint = receipt.get("artifact_sha256")
    if fingerprint is not None and (
        not isinstance(fingerprint, str)
        or not re.fullmatch(r"[0-9a-f]{64}", fingerprint)
    ):
        raise ValueError("Invalid artifact fingerprint.")

    lines = [
        "THREAT INTEL — ANALYST EVIDENCE BRIEF",
        f"CVE: {cve}",
        f"Lookup status: {status}",
        f"Returned source reports: {len(sources)}",
        "Scope: approved local processed-report body mentions.",
        "Human review: REQUIRED",
        "Provider calls for lookup: 0",
        "Tool output: " + (
            "PARTIAL — edge limit reached."
            if receipt.get("truncated") else "Not marked as truncated."
        ),
        "Artifact SHA-256: " + (
            fingerprint or "Not recorded for this lookup outcome."
        ),
        "",
        "SOURCE OBSERVATIONS",
    ]

    if not sources:
        lines.append("No mention was found in this scoped graph.")

    for number, source in enumerate(sources, 1):
        fields = ("report_title", "source_file", "source_location", "excerpt")
        if not isinstance(source, dict) or any(
            not isinstance(source.get(key), str) for key in fields
        ):
            raise ValueError("Invalid source observation.")
        lines.append(f"\nSource {number}:")
        for key in fields:
            lines.append(key.replace("_", " ").title() + ":")
            lines.extend("    " + line for line in source[key].splitlines())

    lines.extend([
        "",
        "INTERPRETATION LIMITS",
        "A mention is not proof of exploitation, CVE validity or factual truth.",
        "No match is not proof that a threat is absent.",
        "This brief is formatted mechanically; no severity or attribution is inferred.",
        "",
        "REVIEWER TASKS",
        "- Inspect the complete report and its publication date.",
        "- Corroborate relevant claims with authoritative advisories.",
        "- Assess exposure of your own assets separately.",
    ])
    return "\n".join(lines) + "\n"
