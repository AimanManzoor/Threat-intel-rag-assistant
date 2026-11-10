"""Explicit, restart-safe index initialization for the Streamlit entrypoint."""
import hashlib
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data/chroma_db"
DOCS_PATH = ROOT / "data/processed"
COLLECTION = "contextual"
KEYS = ("ANTHROPIC_API_KEY", "COHERE_API_KEY")


def configure_credentials(secrets):
    for key in KEYS:
        if os.getenv(key):
            continue
        try:
            value = secrets[key]
        except (KeyError, FileNotFoundError):
            continue
        if isinstance(value, str) and value.strip():
            os.environ[key] = value.strip()
    return [key for key in KEYS if not os.getenv(key)]


def corpus_fingerprint(docs_path=DOCS_PATH):
    files = sorted(Path(docs_path).glob("*.md"))
    if not files:
        raise ValueError("No processed reports found")
    digest = hashlib.sha256()
    for path in files:
        digest.update(path.name.encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def index_count(db_path=DB_PATH, docs_path=DOCS_PATH):
    path = Path(db_path)
    if not (path / "chroma.sqlite3").is_file():
        return 0
    marker = path / "app_index.json"
    manifest = None
    if marker.exists():
        try:
            manifest = json.loads(marker.read_text())
        except (ValueError, OSError):
            return 0
        if (not isinstance(manifest, dict) or manifest.get("status") != "ready"
                or manifest.get("corpus_sha256") != corpus_fingerprint(docs_path)):
            return 0
    import chromadb
    from chromadb.errors import NotFoundError
    try:
        count = chromadb.PersistentClient(path=str(path.resolve())).get_collection(COLLECTION).count()
    except NotFoundError:
        return 0
    if manifest is not None and count != manifest.get("chunk_count"):
        return 0
    return count


def initialize_index(db_path=DB_PATH, docs_path=DOCS_PATH):
    """Reuse a nonempty index or build plain excerpt embeddings after user action."""
    import chromadb
    from chromadb.errors import NotFoundError
    from filelock import FileLock
    from langchain_cohere import CohereEmbeddings
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    path = Path(db_path)
    path.mkdir(parents=True, exist_ok=True)
    with FileLock(str(path / ".app_build.lock"), timeout=120):
        count = index_count(path, docs_path)
        if count:
            return count
        fingerprint = corpus_fingerprint(docs_path)
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
        documents, metadatas, ids = [], [], []
        for source in sorted(Path(docs_path).glob("*.md")):
            text = source.read_text(encoding="utf-8")
            match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
            metadata = {}
            if match:
                for line in match.group(1).splitlines():
                    key, separator, value = line.partition(":")
                    if separator:
                        metadata[key.strip()] = value.strip().strip('"')
                text = text[match.end():]
            for number, chunk in enumerate(splitter.split_text(text)):
                documents.append(chunk)
                ids.append(f"{fingerprint}:{source.stem}:{number}")
                metadatas.append({
                    "doc_id": source.stem, "chunk_index": number,
                    "title": metadata.get("title", ""), "url": metadata.get("url", ""),
                    "raw_chunk": chunk,
                })
        if not documents:
            raise ValueError("Processed reports contain no chunks")
        marker = path / "app_index.json"
        marker.write_text(json.dumps({"status": "building", "corpus_sha256": fingerprint}))
        client = chromadb.PersistentClient(path=str(path.resolve()))
        try:
            client.delete_collection(COLLECTION)
        except NotFoundError:
            pass
        collection = client.get_or_create_collection(COLLECTION, embedding_function=None)
        embeddings = CohereEmbeddings(model="embed-english-v3.0")
        for start in range(0, len(documents), 64):
            batch = documents[start:start + 64]
            vectors = embeddings.embed_documents(batch)
            collection.upsert(ids=ids[start:start + 64], documents=batch,
                              metadatas=metadatas[start:start + 64], embeddings=vectors)
        if collection.count() != len(documents):
            raise RuntimeError("Index build incomplete")
        marker.write_text(json.dumps({"status": "ready", "corpus_sha256": fingerprint,
                                      "chunk_count": len(documents)}))
        return len(documents)
