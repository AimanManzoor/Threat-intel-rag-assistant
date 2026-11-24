"""Export verified public evidence for the HTML dashboard."""
import json
from pathlib import Path

from src.evidence_harness import load_verified_graph

ROOT = Path(__file__).resolve().parents[1]


def main():
    graph = load_verified_graph(ROOT)

    snapshot = {
        "nodes": graph["nodes"],
        "links": graph["links"],
        "graph_sha256": graph["artifact_sha256"],
    }

    # Escape markup so source text stays data rather than executable HTML.
    serialized = json.dumps(snapshot, ensure_ascii=True)
    serialized = serialized.replace("<", "\\u003c").replace(">", "\\u003e")

    destination = ROOT / "dashboard/data.js"
    destination.write_text(
        "window.THREAT_DATA = " + serialized + ";\n",
        encoding="utf-8",
    )

    print("Verified evidence exported to dashboard/data.js")


if __name__ == "__main__":
    main()
