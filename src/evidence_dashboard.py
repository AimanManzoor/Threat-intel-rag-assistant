"""Offline source-graph dashboard. No embeddings, providers or model calls."""
import json

from src.evidence_harness import load_verified_graph, run_graph_plan


def graph_dot(receipt):
    lines = ["digraph Evidence {", "rankdir=LR;", 'node [style=filled,fontname="Helvetica"];']
    for node in receipt["nodes"]:
        color = "#CFE8FF" if node["entity_type"] == "report" else "#FFE6AA"
        label = node["label"] if node["entity_type"] == "cve" else node["label"][:65]
        lines.append(json.dumps(node["id"]) + " [label=" + json.dumps(label) +
                     ", fillcolor=" + json.dumps(color) + "];")
    for edge in receipt["edges"]:
        lines.append(json.dumps(edge["source"]) + " -> " + json.dumps(edge["target"]) +
                     ' [label="mentions"];')
    lines.append("}")
    return "\n".join(lines)


def render_evidence_dashboard(root):
    import streamlit as st

    st.subheader("Source-linked CVE evidence graph")
    st.caption("Built with Graphify 0.9.109. Offline exploration; no provider calls or API keys.")
    st.warning(
        "Edges mean literal mentions in the processed report body. They do not "
        "establish exploitation, causality, CVE validity, or answer correctness. "
        "Two-hop navigation is not implemented multi-hop RAG reasoning."
    )
    try:
        graph = load_verified_graph(root)
    except (OSError, ValueError, UnicodeError):
        st.session_state.pop("evidence_graph_receipt", None)
        st.error("Graph verification failed. Review the corpus and rebuild using src.build_evidence_graph.")
        return
    a, b, c = st.columns(3)
    a.metric("Processed reports", len(graph["sources"]))
    b.metric("CVE identifiers", sum(node["entity_type"] == "cve" for node in graph["nodes"]))
    c.metric("Verified mention edges", len(graph["links"]))
    st.caption(
        "Scope: data/processed only. Known footer sections and content before the "
        "first level-2 heading are excluded by a heuristic. Other report facts, "
        "malware, actors and the processed_full folder are not represented."
    )
    by_id = {node["id"]: node for node in graph["nodes"]}
    options = sorted(by_id, key=lambda key: (by_id[key]["entity_type"] != "cve", key))
    with st.form("evidence_graph_form"):
        node_id = st.selectbox("Start node", options, format_func=lambda key: by_id[key]["label"])
        hops = st.slider("Maximum navigation hops", min_value=1, max_value=2, value=1)
        edges = st.slider("Maximum returned edges", min_value=1, max_value=20, value=10)
        submitted = st.form_submit_button("Explore evidence")
    plan = {"tool": "graph_neighborhood", "node_id": node_id, "max_hops": hops, "max_edges": edges}
    key = (graph["artifact_sha256"], node_id, hops, edges)
    if submitted:
        st.session_state["evidence_graph_receipt"] = (key, run_graph_plan(plan, root=root))
    stored = st.session_state.get("evidence_graph_receipt")
    if stored is None or stored[0] != key:
        st.info("Choose a node and explore its bounded source connections.")
        return
    receipt = stored[1]
    st.write("Harness status:", receipt["status"])
    if receipt["status"] not in {"completed", "no_matches"}:
        st.error(receipt["reason"])
        return
    st.graphviz_chart(graph_dot(receipt))
    if receipt["truncated"]:
        st.info("The edge limit was reached; this view is incomplete.")
    if receipt["edges"]:
        st.dataframe([
            {"Report": by_id[edge["source"]]["label"],
             "CVE": by_id[edge["target"]]["label"],
             "Relationship": edge["relation"],
             "Source": edge["source_file"], "Location": edge["source_location"],
             "Traversal hop": edge["hop"]}
            for edge in receipt["edges"]
        ], hide_index=True)
        selected = st.selectbox(
            "Inspect source evidence", list(range(len(receipt["edges"]))),
            format_func=lambda index: by_id[receipt["edges"][index]["target"]]["label"],
        )
        evidence = receipt["edges"][selected]
        st.code(evidence["source_file"] + ":" + evidence["source_location"], language=None)
        st.text(evidence["excerpt"])
        st.caption("Bounded source excerpt; the line reference points to the complete local report.")
    else:
        st.info("No mention edges found for this node. This does not establish absence of a threat.")
    with st.expander("Inspect the tool plan and verification receipt"):
        st.json(receipt)
    st.download_button(
        "Download graph investigation receipt", json.dumps(receipt, indent=2),
        file_name="threat_graph_receipt.json", mime="application/json",
    )
