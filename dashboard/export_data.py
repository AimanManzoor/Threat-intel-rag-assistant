"""Export or check the dashboard's verified evidence snapshot."""
import argparse
import json
from pathlib import Path

from src.evidence_harness import load_verified_graph

ROOT = Path(__file__).resolve().parents[1]


def render_snapshot(root=ROOT):
    graph = load_verified_graph(root)

    snapshot = {
        "nodes": graph["nodes"],
        "links": graph["links"],
        "graph_sha256": graph["artifact_sha256"],
    }

    serialized = json.dumps(snapshot, ensure_ascii=True)
    serialized = serialized.replace("<", "\\u003c").replace(">", "\\u003e")

    return "window.THREAT_DATA = " + serialized + ";\n"


def export(root=ROOT, *, check=False):
    root = Path(root)
    expected = render_snapshot(root)
    destination = root / "dashboard/data.js"

    if check:
        if not destination.is_file():
            raise ValueError("Dashboard snapshot is missing. Rebuild it first.")

        if destination.read_text(encoding="utf-8") != expected:
            raise ValueError(
                "Dashboard snapshot is stale. "
                "Run python -m dashboard.export_data and review the changes."
            )

        print("PASS: dashboard snapshot matches verified evidence.")
        return

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(expected, encoding="utf-8")
    print("Verified evidence exported to dashboard/data.js")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    try:
        export(check=args.check)
    except (OSError, ValueError) as error:
        parser.exit(1, f"STOP: {error}\n")


if __name__ == "__main__":
    main()
