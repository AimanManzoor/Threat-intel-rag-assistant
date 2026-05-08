"""Contextual retrieval for Unit 42 threat intel corpus.

Same Anthropic technique as Advanced_Rag_Graph project, with adaptations for long-form posts:
- Larger chunks (1000 chars) since posts are 5-15x longer than Helios docs
- Strips YAML frontmatter before chunking (frontmatter is metadata, not content)
- Caches chunks + LLM-generated contexts to disk
"""
import re
import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

DATA_DIR = Path(__file__).parent.parent / "data" / "processed"
CACHE_PATH = Path(__file__).parent.parent / "data" / ".contextual_chunks_cache.json"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150


@dataclass
class ContextualChunk:
    doc_id: str
    chunk_index: int
    chunk_text: str
    context: str
    embedding_text: str
    title: str = ""
    url: str = ""


CONTEXT_PROMPT = """<document>
{document}
</document>

Here is the chunk we want to situate within the whole document:
<chunk>
{chunk}
</chunk>

Please give a short succinct context (1-2 sentences) to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk. Answer only with the succinct context and nothing else."""


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_doc(text: str) -> dict:
    """Split a markdown file into frontmatter dict + body string."""
    fm_match = FRONTMATTER_RE.match(text)
    metadata = {}
    if fm_match:
        for line in fm_match.group(1).splitlines():
            if ":" in line:
                key, _, value = line.partition(":")
                metadata[key.strip()] = value.strip().strip('"')
        body = text[fm_match.end():]
    else:
        body = text
    return {"metadata": metadata, "body": body.strip()}


def load_documents() -> dict:
    """Load all .md files in data/processed/. Returns {doc_id: parsed_dict}."""
    docs = {}
    for path in sorted(DATA_DIR.glob("*.md")):
        parsed = parse_doc(path.read_text())
        docs[path.stem] = parsed
    return docs


def chunk_document(text: str) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n## ", "\n### ", "\n\n", "\n", ". ", " ", ""],
    )
    return splitter.split_text(text)


def generate_context(document: str, chunk: str, llm: ChatAnthropic) -> str:
    prompt = CONTEXT_PROMPT.format(document=document, chunk=chunk)
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content.strip()


def build_contextual_chunks(use_cache: bool = True) -> List[ContextualChunk]:
    if use_cache and CACHE_PATH.exists():
        print(f"Loading cached chunks from {CACHE_PATH.name}")
        return [ContextualChunk(**c) for c in json.loads(CACHE_PATH.read_text())]

    llm = ChatAnthropic(model="claude-haiku-4-5-20251001", max_tokens=200)
    docs = load_documents()
    contextual_chunks: List[ContextualChunk] = []

    for doc_id, parsed in docs.items():
        body = parsed["body"]
        title = parsed["metadata"].get("title", "")
        url = parsed["metadata"].get("url", "")
        chunks = chunk_document(body)
        for i, chunk in enumerate(chunks):
            print(f"  [{doc_id}] chunk {i+1}/{len(chunks)}", end=" ", flush=True)
            context = generate_context(body, chunk, llm)
            print("✓")
            contextual_chunks.append(ContextualChunk(
                doc_id=doc_id,
                chunk_index=i,
                chunk_text=chunk,
                context=context,
                embedding_text=f"{context}\n\n{chunk}",
                title=title,
                url=url,
            ))

    CACHE_PATH.write_text(json.dumps([asdict(c) for c in contextual_chunks], indent=2))
    print(f"\nCached {len(contextual_chunks)} chunks → {CACHE_PATH.name}")
    return contextual_chunks


if __name__ == "__main__":
    print(f"Building contextual chunks for Unit 42 corpus ({CHUNK_SIZE}-char chunks)...\n")
    chunks = build_contextual_chunks(use_cache=False)
    print(f"\n=== {len(chunks)} contextual chunks generated ===\n")
    if chunks:
        sample = chunks[len(chunks) // 2]  # middle chunk
        print(f"Sample chunk from: {sample.doc_id}")
        print(f"Title:   {sample.title}")
        print(f"Context: {sample.context}")
        print(f"Chunk:   {sample.chunk_text[:200]}...")
