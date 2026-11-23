"""Build the bundled graph with Graphify; no API calls or semantic backend."""
from importlib.metadata import version
from pathlib import Path

from src.evidence_extract import extract_mentions, PROFILE

ROOT = Path(__file__).resolve().parents[1]


def build_artifact(root=ROOT):
    from graphify.build import build
    from graphify.export import to_json

    if version("graphifyy") != "0.9.109":
        raise ValueError("Use the pinned graphifyy==0.9.109 build environment.")
    root = Path(root).resolve()
    extraction = extract_mentions(root)
    graph = build([extraction], directed=True, dedup=False, root=root)
    graph.graph.update({
        "evidence_profile": PROFILE, "source_manifest": extraction["sources"],
        "scope": "data/processed report-body CVE mentions; heuristic footer exclusion",
        "reviewed_graphify_fork_commit": "d4a5b323ef8501518b82c58a05fe21b35ce24992",
        "provider_calls": 0,
    })
    destination = root / "data/evidence_graph.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not to_json(graph, {}, str(destination), force=True):
        raise ValueError("Graphify did not export the graph.")
    print(f"Graphify {version('graphifyy')}: {len(extraction['sources'])} reports, "
          f"{graph.number_of_nodes()} nodes, {graph.number_of_edges()} mention edges.")
    print("Graph:", destination)
    return destination


if __name__ == "__main__":
    build_artifact()
