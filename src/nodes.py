"""Graph nodes — six pure functions on RAGState."""
from pathlib import Path
import re

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_chroma import Chroma
from langchain_cohere import CohereEmbeddings, CohereRerank
from langchain_core.messages import HumanMessage

from src.state import RAGState

load_dotenv()
CHROMA_DIR = Path(__file__).parent.parent / "data" / "chroma_db"

_haiku = ChatAnthropic(model="claude-haiku-4-5-20251001", max_tokens=512)
_sonnet = ChatAnthropic(model="claude-sonnet-4-5-20250929", max_tokens=1024)
_embeddings = CohereEmbeddings(model="embed-english-v3.0")
_reranker = CohereRerank(model="rerank-english-v3.0", top_n=5)
_vector_store = Chroma(
    collection_name="contextual",
    embedding_function=_embeddings,
    persist_directory=str(CHROMA_DIR),
)


REWRITE_PROMPT = """Rewrite this cybersecurity query for retrieval against threat intelligence reports.
Expand acronyms (CVE, IoC, TTP, APT), add synonyms for threat actors and malware, keep under 30 words.
Output only the rewritten query.

Query: {query}"""

def rewrite_query(state):
    r = _haiku.invoke([HumanMessage(content=REWRITE_PROMPT.format(query=state["query"]))])
    return {"rewritten": r.content.strip()}


ROUTE_PROMPT = """Classify a threat-intel query:
- "simple": single-report lookup
- "multi_hop": needs multiple reports or comparison
Output: simple OR multi_hop.

Query: {query}"""

def route(state):
    r = _haiku.invoke([HumanMessage(content=ROUTE_PROMPT.format(query=state["rewritten"]))])
    return {"route": "multi_hop" if "multi" in r.content.lower() else "simple"}


def retrieve(state):
    return {"chunks": _vector_store.similarity_search(state["rewritten"], k=20)}


def rerank(state):
    chunks = state.get("chunks", [])
    if not chunks:
        return {"reranked": []}
    return {"reranked": _reranker.compress_documents(documents=chunks, query=state["rewritten"])}


GENERATE_PROMPT = """You are a threat intelligence analyst. Answer using ONLY the provided Unit 42 excerpts.
- If context lacks the answer: "The provided Unit 42 reports don't contain enough information to answer that."
- Cite source IDs in [brackets] inline.
- Be concise (under 200 words).

Context:
{context}

Question: {query}

Answer:"""

def generate(state):
    chunks = state.get("reranked", [])
    if not chunks:
        return {"answer": "No relevant context found.", "citations": []}
    context_text = "\n\n".join([
        f"[{c.metadata.get('doc_id', 'unknown')}]\n{c.metadata.get('raw_chunk', c.page_content)}"
        for c in chunks
    ])
    r = _sonnet.invoke([HumanMessage(content=GENERATE_PROMPT.format(context=context_text, query=state["query"]))])
    citations = list(set(re.findall(r"\[([\w_-]+)\]", r.content)))
    return {"answer": r.content.strip(), "citations": citations}


SELF_CHECK_PROMPT = """Score how grounded this answer is in the chunks (0.0-1.0).
1.0 = every claim supported. 0.5 = partial. 0.0 = fabricated.
Output exactly one number, nothing else.

Chunks:
{context}

Answer: {answer}

Score:"""

def self_check(state):
    chunks = state.get("reranked", [])
    answer = state.get("answer", "")
    attempts = state.get("attempts", 0) + 1
    if not chunks or not answer or "don't contain" in answer:
        return {"confidence": 0.0, "attempts": attempts}
    context_text = "\n\n".join([c.page_content for c in chunks])
    r = _haiku.invoke([HumanMessage(content=SELF_CHECK_PROMPT.format(context=context_text, answer=answer))])
    try:
        confidence = max(0.0, min(1.0, float(r.content.strip().split()[0])))
    except (ValueError, IndexError):
        confidence = 0.5
    return {"confidence": confidence, "attempts": attempts}


def tool_use(state):
    """Stub for multi-hop. Falls back to retrieve in v0.1."""
    return retrieve(state)

