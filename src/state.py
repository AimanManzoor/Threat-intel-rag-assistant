"""RAGState — schema flowing through the LangGraph."""
from typing import TypedDict, List, Literal, Optional
from langchain_core.documents import Document


class RAGState(TypedDict, total=False):
    query: str
    rewritten: str
    route: Literal["simple", "multi_hop"]
    chunks: List[Document]
    reranked: List[Document]
    answer: str
    citations: List[str]
    confidence: float
    attempts: int
    tool_calls: Optional[List[dict]]

