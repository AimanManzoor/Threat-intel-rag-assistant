"""StateGraph wiring."""
from langgraph.graph import StateGraph, START, END

from src.state import RAGState
from src.nodes import rewrite_query, route as route_node, retrieve, rerank, generate, self_check, tool_use


def route_branch(state):
    return state.get("route", "simple")


def confidence_branch(state):
    if state.get("attempts", 0) >= 2:
        return "done"
    if state.get("confidence", 0.0) < 0.7:
        return "retry"
    return "done"


def build_graph():
    g = StateGraph(RAGState)
    g.add_node("rewrite_query", rewrite_query)
    g.add_node("route", route_node)
    g.add_node("retrieve", retrieve)
    g.add_node("tool_use", tool_use)
    g.add_node("rerank", rerank)
    g.add_node("generate", generate)
    g.add_node("self_check", self_check)

    g.add_edge(START, "rewrite_query")
    g.add_edge("rewrite_query", "route")
    g.add_conditional_edges("route", route_branch, {"simple": "retrieve", "multi_hop": "tool_use"})
    g.add_edge("retrieve", "rerank")
    g.add_edge("tool_use", "rerank")
    g.add_edge("rerank", "generate")
    g.add_edge("generate", "self_check")
    g.add_conditional_edges("self_check", confidence_branch, {"retry": "rewrite_query", "done": END})
    return g.compile()


app = build_graph()


if __name__ == "__main__":
    import sys
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "What threat actors are exploiting Cisco ASA zero-days?"
    print(f"Query: {query}\n\nRunning graph...\n")
    result = app.invoke({"query": query, "attempts": 0})
    print("=" * 60)
    print("FINAL ANSWER")
    print("=" * 60)
    print(result.get("answer", "(none)"))
    print(f"\nRoute:       {result.get('route', '?')}")
    print(f"Citations:   {result.get('citations', [])}")
    print(f"Confidence:  {result.get('confidence', 0.0):.2f}")
    print(f"Attempts:    {result.get('attempts', 0)}")
    print(f"Rewritten:   {result.get('rewritten', '?')}")
