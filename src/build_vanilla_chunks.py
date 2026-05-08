"""Build chunks WITHOUT contextual generation — populates cache for build_index.py.
Cost: $0. Use this when budget doesn't allow full contextual retrieval."""
import json
from dataclasses import asdict
from src.contextual import CACHE_PATH, ContextualChunk, load_documents, chunk_document


def main():
    docs = load_documents()
    chunks = []
    for doc_id, parsed in docs.items():
        body = parsed["body"]
        title = parsed["metadata"].get("title", "")
        url = parsed["metadata"].get("url", "")
        for i, chunk_text in enumerate(chunk_document(body)):
            chunks.append(ContextualChunk(
                doc_id=doc_id,
                chunk_index=i,
                chunk_text=chunk_text,
                context="",
                embedding_text=chunk_text,
                title=title,
                url=url,
            ))
    CACHE_PATH.write_text(json.dumps([asdict(c) for c in chunks], indent=2))
    print(f"✓ Wrote {len(chunks)} vanilla chunks to {CACHE_PATH.name}")
    print("Cost: $0 (no LLM calls)")


if __name__ == "__main__":
    main()
