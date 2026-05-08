

"""Build vanilla + contextual Chroma collections from the chunks cache."""
from pathlib import Path
import sys

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_cohere import CohereEmbeddings
from langchain_core.documents import Document

sys.path.insert(0, str(Path(__file__).parent.parent))
from src.contextual import build_contextual_chunks

load_dotenv()

CHROMA_DIR = Path(__file__).parent.parent / "data" / "chroma_db"
VANILLA = "vanilla"
CONTEXTUAL = "contextual"


def get_embeddings():
    return CohereEmbeddings(model="embed-english-v3.0")


def build_indices():
    chunks = build_contextual_chunks(use_cache=True)
    embeddings = get_embeddings()

    vanilla_docs = [
        Document(
            page_content=c.chunk_text,
            metadata={"doc_id": c.doc_id, "chunk_index": c.chunk_index, "title": c.title, "url": c.url},
        )
        for c in chunks
    ]
    contextual_docs = [
        Document(
            page_content=c.embedding_text,
            metadata={
                "doc_id": c.doc_id,
                "chunk_index": c.chunk_index,
                "raw_chunk": c.chunk_text,
                "title": c.title,
                "url": c.url,
            },
        )
        for c in chunks
    ]

    print(f"Building vanilla collection ({len(vanilla_docs)} chunks)...")
    Chroma.from_documents(vanilla_docs, embeddings, collection_name=VANILLA, persist_directory=str(CHROMA_DIR))
    print(f"Building contextual collection ({len(contextual_docs)} chunks)...")
    Chroma.from_documents(contextual_docs, embeddings, collection_name=CONTEXTUAL, persist_directory=str(CHROMA_DIR))
    print(f"\n✓ Both collections persisted to {CHROMA_DIR}")


def compare(query, k=3):
    embeddings = get_embeddings()
    v = Chroma(collection_name=VANILLA, embedding_function=embeddings, persist_directory=str(CHROMA_DIR))
    c = Chroma(collection_name=CONTEXTUAL, embedding_function=embeddings, persist_directory=str(CHROMA_DIR))
    print(f"\n{'='*70}\nQuery: {query}\n{'='*70}")
    print("\n--- VANILLA ---")
    for i, d in enumerate(v.similarity_search(query, k=k), 1):
        print(f"  {i}. [{d.metadata['doc_id']}] {d.page_content[:120].strip()}...")
    print("\n--- CONTEXTUAL ---")
    for i, d in enumerate(c.similarity_search(query, k=k), 1):
        raw = d.metadata.get("raw_chunk", d.page_content)
        print(f"  {i}. [{d.metadata['doc_id']}] {raw[:120].strip()}...")


if __name__ == "__main__":
    if not CHROMA_DIR.exists() or not any(CHROMA_DIR.iterdir()):
        build_indices()
    else:
        print(f"(reusing existing indices at {CHROMA_DIR})\n")
    test_queries = [
        "What threat actors are exploiting Cisco vulnerabilities?",
        "How do ransomware groups exfiltrate data?",
        "What CVEs were used in supply chain attacks?",
    ]
    for q in test_queries:
        compare(q)
