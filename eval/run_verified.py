import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter


def capture_run(app, questions, output):
    report = {
        "run_time_utc": datetime.now(timezone.utc).isoformat(),
        "source_hashes": {
            name: hashlib.sha256(Path(name).read_bytes()).hexdigest()
            for name in ["src/graph.py", "src/nodes.py", "src/citations.py", "eval/questions.jsonl"]
        },
        "results": [],
    }

    for q in questions:
        start = perf_counter()
        row = {"id": q["id"], "query": q["query"]}

        try:
            r = app.invoke({"query": q["query"], "attempts": 0})
            row.update({key: r.get(key) for key in [
                "answer", "citations", "route", "rewritten", "attempts", "confidence", "citation_validation"
            ]})

            row["evidence_chunks"] = [{
                "doc_id": d.metadata.get("doc_id"),
                "chunk_index": d.metadata.get("chunk_index"),
                "url": d.metadata.get("url"),
                "text": d.metadata.get("raw_chunk", d.page_content),
            } for d in r.get("reranked", [])]

            row["legacy_keyword_match"] = any(
                term.lower() in (r.get("answer") or "").lower()
                for term in q.get("expected_substrings", [])
            )

        except Exception as error:
            row["error_type"] = type(error).__name__
            row["status_code"] = getattr(error, "status_code", None)

        row["elapsed_s"] = round(perf_counter() - start, 3)
        report["results"].append(row)
        output.write_text(
            json.dumps(report, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        print(
            q["id"], row.get("route", "ERROR"),
            row.get("error_type", "saved"), flush=True,
        )

    return report


def main():
    import os

    if not Path("src/scrape_unit42.py").is_file():
        raise SystemExit("Run from your Threat-intel-rag-assistant project folder.")

    from dotenv import load_dotenv
    load_dotenv(Path(".env"))

    missing = [
        key for key in ["ANTHROPIC_API_KEY", "COHERE_API_KEY"]
        if not os.getenv(key)
    ]
    if missing:
        raise SystemExit("Configure these in your local .env: " + ", ".join(missing))

    index = Path("data/chroma_db")
    if not index.is_dir() or not any(index.iterdir()):
        raise SystemExit("Existing Chroma index not found; stop before rebuilding it.")

    from src.graph import app

    questions = [
        json.loads(line)
        for line in Path("eval/questions.jsonl").read_text().splitlines()
        if line.strip()
    ][:10]

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    output = Path("eval") / f"verification_{stamp}.json"

    capture_run(app, questions, output)
    print("Saved verification report:", output)


if __name__ == "__main__":
    main()
