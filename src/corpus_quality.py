"""Read-only quality audit of index-eligible processed reports."""
from collections import Counter
from datetime import date
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

from src.evidence_extract import CVE, FOOTER

ROOT = Path(__file__).resolve().parents[1]


def metadata(lines):
    values, issues = {}, []
    if not lines or lines[0] != "---":
        return values, ["missing_frontmatter"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return values, ["unterminated_frontmatter"]
    for line in lines[1:end]:
        key, separator, value = line.partition(":")
        key = key.strip()
        if not separator or key not in {"title", "date", "url"}:
            continue
        if key in values:
            issues.append("duplicate_metadata_" + key)
            continue
        value = value.strip()
        if value[:1] in ("'", '"'):
            if len(value) < 2 or value[-1] != value[0]:
                issues.append("unsupported_metadata_" + key)
                value = ""
            else:
                value = value[1:-1]
        if value in ("|", ">"):
            issues.append("unsupported_metadata_" + key)
            value = ""
        values[key] = value
    return values, issues


def approved_url(value):
    try:
        parsed = urlsplit(value)
        return (
            parsed.scheme == "https"
            and parsed.hostname == "unit42.paloaltonetworks.com"
            and not parsed.username
            and not parsed.password
            and parsed.port in (None, 443)
        )
    except ValueError:
        return False


def audit_corpus(root=ROOT, *, as_of=None):
    root = Path(root).resolve()
    day = as_of or date.today()
    if type(day) is not date:
        raise ValueError("as_of must be a date.")
    corpus = root / "data/processed"
    if corpus.is_symlink() or not corpus.resolve().is_relative_to(root):
        raise ValueError("Corpus must remain inside the project.")
    paths = sorted(corpus.glob("*.md"))
    if len(paths) > 50:
        raise ValueError("This audit supports at most 50 processed reports.")

    rows = []
    for path in paths:
        row = {
            "file": path.relative_to(root).as_posix(),
            "title": "", "published": "", "source_url": "",
            "age_days": None, "sha256": None, "body_sha256": None,
            "retained_cve_count": None, "footer_only_cve_count": None,
            "retained_cves": "", "footer_only_cves": "",
            "footer_start_line": None, "issues": [],
        }
        try:
            if path.is_symlink() or path.resolve().parent != corpus.resolve():
                raise ValueError("unsafe_source_path")
            with path.open("rb") as handle:
                raw = handle.read(1_000_001)
            if len(raw) > 1_000_000:
                raise ValueError("oversized_source")
            row["sha256"] = hashlib.sha256(raw).hexdigest()
            lines = raw.decode("utf-8").splitlines()
            values, issues = metadata(lines)
            row["issues"].extend(issues)
            for key in ("title", "date", "url"):
                if not values.get(key):
                    row["issues"].append("missing_" + key)
            row["title"] = values.get("title", "")
            row["published"] = values.get("date", "")
            url = values.get("url", "")
            if url:
                if approved_url(url):
                    row["source_url"] = url
                else:
                    row["source_url"] = "(invalid URL)"
                    row["issues"].append("invalid_source_url")
            if row["published"]:
                try:
                    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", row["published"]):
                        raise ValueError
                    published = date.fromisoformat(row["published"])
                    row["age_days"] = (day - published).days
                    if row["age_days"] < 0:
                        row["issues"].append("future_declared_date")
                except ValueError:
                    row["issues"].append("invalid_publication_date")

            body, footer, started = [], [], False
            for number, line in enumerate(lines, 1):
                if FOOTER.match(line):
                    footer = lines[number - 1:]
                    row["footer_start_line"] = number
                    break
                if line.startswith("## "):
                    started = True
                if started:
                    body.append(line)
            normalized = " ".join(" ".join(body).split()).casefold()
            if normalized:
                row["body_sha256"] = hashlib.sha256(normalized.encode()).hexdigest()
            else:
                row["issues"].append("graph_body_structure_missing")
            kept = {value.upper() for value in CVE.findall("\n".join(body))}
            footer_only = {
                value.upper() for value in CVE.findall("\n".join(footer))
            } - kept
            row["retained_cve_count"] = len(kept)
            row["footer_only_cve_count"] = len(footer_only)
            row["retained_cves"] = ", ".join(sorted(kept))
            row["footer_only_cves"] = ", ".join(sorted(footer_only))
        except UnicodeError:
            row["issues"].append("invalid_utf8")
        except OSError:
            row["issues"].append("read_error")
        except ValueError as error:
            row["issues"].append(str(error))
        rows.append(row)

    raw_counts = Counter(row["sha256"] for row in rows if row["sha256"])
    body_counts = Counter(row["body_sha256"] for row in rows if row["body_sha256"])
    for row in rows:
        row["duplicate_body_count"] = body_counts.get(row["body_sha256"], 0)
        if row["duplicate_body_count"] > 1:
            row["issues"].append("duplicate_body_candidate")
        if raw_counts.get(row["sha256"], 0) > 1:
            row["issues"].append("exact_file_duplicate")
        row["issues"] = "; ".join(row["issues"])

    return {
        "schema_version": 1, "as_of": day.isoformat(),
        "scope": "data/processed only; eligibility does not establish index readiness",
        "provider_calls": 0,
        "summary": {
            "files": len(rows),
            "reports_with_flags": sum(bool(row["issues"]) for row in rows),
            "duplicate_body_groups": sum(count > 1 for count in body_counts.values()),
            "raw_duplicate_groups": sum(count > 1 for count in raw_counts.values()),
            "footer_only_cve_pairs": sum(row["footer_only_cve_count"] or 0 for row in rows),
        },
        "rows": rows,
    }


def render_dashboard(root=ROOT):
    import streamlit as st

    st.subheader("Corpus quality — index-eligible files")
    st.caption(
        "Read-only checks of declared metadata and extraction coverage. "
        "File presence does not establish index readiness or factual correctness."
    )
    try:
        report = audit_corpus(root)
    except (OSError, ValueError):
        st.error("Cannot audit this corpus. Check the local path and file limits.")
        return
    summary = report["summary"]
    columns = st.columns(4)
    for column, label, key in [
        (columns[0], "Processed files", "files"),
        (columns[1], "Reports with flags", "reports_with_flags"),
        (columns[2], "Duplicate body groups", "duplicate_body_groups"),
        (columns[3], "Footer-only CVE/file pairs", "footer_only_cve_pairs"),
    ]:
        column.metric(label, summary[key])
    st.warning(
        "Footer exclusion describes the graph extractor. The current vector index "
        "builder can still embed footer text; this audit does not clean or rebuild it."
    )
    st.caption(
        "Publication dates are declared metadata, not independently verified dates. "
        "Age alone does not make a report invalid. Zero retained CVEs is not a quality failure."
    )
    if not report["rows"]:
        st.warning("No processed Markdown reports found.")
        return
    fields = (
        "file", "title", "published", "age_days", "issues",
        "duplicate_body_count", "retained_cve_count",
        "footer_only_cve_count", "footer_start_line",
    )
    st.dataframe(
        [{key: row[key] for key in fields} for row in report["rows"]],
        hide_index=True,
    )
    selected = st.selectbox("Inspect report provenance", [row["file"] for row in report["rows"]])
    st.json(next(row for row in report["rows"] if row["file"] == selected))
    st.caption(
        "CVE counts are unique within each file, not across the corpus. "
        "Unavailable files have null counts. Duplicate bodies are review candidates, not automatic deletions."
    )
    st.download_button(
        "Download corpus audit",
        json.dumps(report, indent=2, allow_nan=False),
        file_name="corpus_quality.json",
        mime="application/json",
    )


if __name__ == "__main__":
    print(json.dumps(audit_corpus(), indent=2, allow_nan=False))
