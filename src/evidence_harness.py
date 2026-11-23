"""Permission, provenance and traversal limits for an offline evidence-graph tool."""
import argparse
import hashlib
import json
from pathlib import Path

from src.evidence_extract import extract_mentions, PROFILE

ROOT = Path(__file__).resolve().parents[1]
NODE_KEYS = ("id", "label", "file_type", "entity_type", "source_file", "source_location")
EDGE_KEYS = ("source", "target", "relation", "confidence", "source_file", "source_location")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON keys.")
        result[key] = value
    return result


def validate_plan(plan):
    if not isinstance(plan, dict) or set(plan) != {"tool", "node_id", "max_hops", "max_edges"}:
        raise ValueError("Unexpected plan fields.")
    if plan["tool"] != "graph_neighborhood":
        raise ValueError("Tool is not permitted.")
    node = plan["node_id"]
    if not isinstance(node, str) or not node or len(node) > 180 or not node.isprintable():
        raise ValueError("Invalid node identifier.")
    for key, low, high in [("max_hops", 1, 2), ("max_edges", 1, 20)]:
        if type(plan[key]) is not int or not low <= plan[key] <= high:
            raise ValueError("Plan exceeds traversal limits.")


def projected(rows, keys):
    if not isinstance(rows, list) or any(
        not isinstance(row, dict) or any(not isinstance(row.get(key), str) for key in keys)
        for row in rows
    ):
        raise ValueError("Invalid graph record.")
    return sorted(tuple(row[key] for key in keys) for row in rows)


def load_verified_graph(root=ROOT):
    root = Path(root).resolve()
    path = root / "data/evidence_graph.json"
    if path.is_symlink():
        raise ValueError("Graph artifact symlinks are not supported.")
    with path.open("rb") as handle:
        raw = handle.read(2_000_001)
    if len(raw) > 2_000_000:
        raise ValueError("Graph exceeds 2 MB.")
    graph = json.loads(raw, object_pairs_hook=unique_object)
    if not isinstance(graph, dict):
        raise ValueError("Graph must be an object.")
    metadata = graph.get("graph", {})
    if (not isinstance(metadata, dict) or type(metadata.get("schema_version")) is not int
            or metadata.get("schema_version") != 1
            or metadata.get("evidence_profile") != PROFILE
            or graph.get("directed") is not True or graph.get("multigraph") is not False):
        raise ValueError("Unsupported graph schema/profile.")
    if not isinstance(graph.get("nodes"), list) or len(graph["nodes"]) > 500:
        raise ValueError("Node budget exceeded.")
    if not isinstance(graph.get("links"), list) or len(graph["links"]) > 1000:
        raise ValueError("Edge budget exceeded.")
    expected = extract_mentions(root)
    if metadata.get("source_manifest") != expected["sources"]:
        raise ValueError("Source hashes changed; rebuild the graph.")
    if (projected(graph["nodes"], NODE_KEYS) != projected(expected["nodes"], NODE_KEYS)
            or projected(graph["links"], EDGE_KEYS) != projected(expected["edges"], EDGE_KEYS)):
        raise ValueError("Graph does not match deterministic source extraction.")
    return {
        "nodes": expected["nodes"],
        "links": [{**edge, "excerpt": expected["excerpts"][(edge["source"], edge["target"])]}
                  for edge in expected["edges"]],
        "sources": expected["sources"], "artifact_sha256": hashlib.sha256(raw).hexdigest(),
        "graphify_version": metadata.get("graphify_version"),
    }


def run_graph_plan(plan, *, root=ROOT):
    receipt = {"status": "rejected", "tool_calls": 0, "provider_calls": 0,
               "human_review_required": True, "nodes": [], "edges": [], "truncated": False}
    try:
        validate_plan(plan)
    except ValueError:
        return {**receipt, "reason": "Plan rejected by the permitted tool/argument contract."}
    receipt["tool_calls"] = 1
    try:
        graph = load_verified_graph(root)
    except (OSError, ValueError, UnicodeError):
        return {**receipt, "status": "verification_failed",
                "reason": "Graph or source verification failed. Review/rebuild the local artifact."}
    by_id = {node["id"]: node for node in graph["nodes"]}
    seed = plan["node_id"]
    if seed not in by_id:
        return {**receipt, "status": "no_matches", "reason": "Node is absent from this scoped graph."}
    frontier, visited, chosen, seen_edges = {seed}, {seed}, [], set()
    truncated = False
    for hop in range(1, plan["max_hops"] + 1):
        following = set()
        for index, edge in enumerate(graph["links"]):
            endpoints = {edge["source"], edge["target"]}
            if not endpoints.intersection(frontier) or index in seen_edges:
                continue
            if len(chosen) >= plan["max_edges"]:
                truncated = True
                continue
            seen_edges.add(index)
            chosen.append({**edge, "hop": hop})
            following.update(endpoints - visited)
        visited.update(following)
        frontier = following
        if not frontier:
            break
    selected_ids = {seed}
    for edge in chosen:
        selected_ids.update((edge["source"], edge["target"]))
    return {
        **receipt, "status": "completed" if chosen else "no_matches",
        "plan": dict(plan), "truncated": truncated,
        "nodes": [by_id[node] for node in sorted(selected_ids)], "edges": chosen,
        "artifact_sha256": graph["artifact_sha256"],
        "checks": {"source_hashes": "matched", "literal_mentions": "matched",
                   "scope": "approved processed-report corpus"},
        "notice": "Edges mean literal report-body mentions. Traversal is undirected navigation, "
                  "not proof of exploitation, causality, answer correctness or multi-hop reasoning.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--node", default="cve:CVE-2025-20333")
    parser.add_argument("--hops", type=int, default=1)
    parser.add_argument("--max-edges", type=int, default=20)
    args = parser.parse_args()
    report = run_graph_plan({"tool": "graph_neighborhood", "node_id": args.node,
                             "max_hops": args.hops, "max_edges": args.max_edges})
    print(json.dumps(report, indent=2, ensure_ascii=False))
    raise SystemExit(0 if report["status"] in {"completed", "no_matches"} else 1)


if __name__ == "__main__":
    main()
