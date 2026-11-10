import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from src.app_runtime import configure_credentials, corpus_fingerprint, index_count, initialize_index


class AppRuntimeTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.docs = self.root / "processed"
        self.docs.mkdir()
        (self.docs / "report.md").write_text(
            '---\ntitle: "Test report"\nurl: https://example.org/report\n---\n'
            'The report identifies Jolly Scorpius as the group operating RansomHouse.'
        )
        self.db = self.root / "chroma"
        self.embeddings = Mock()
        self.embeddings.embed_documents.side_effect = lambda texts: [[1.0, 0.0, 1.0] for text in texts]
        embedding_patch = patch("langchain_cohere.CohereEmbeddings", return_value=self.embeddings)
        embedding_patch.start()
        self.addCleanup(embedding_patch.stop)

    def count(self):
        return index_count(self.db, self.docs)

    def build(self):
        return initialize_index(self.db, self.docs)

    def test_missing_index_does_not_create_database_or_call_embeddings(self):
        self.assertEqual(self.count(), 0)
        self.assertFalse(self.db.exists())
        self.embeddings.embed_documents.assert_not_called()

    def test_build_and_reuse_real_chroma_without_duplicate_embeddings(self):
        self.assertEqual(self.build(), 1)
        self.assertEqual(self.count(), 1)
        self.assertEqual(self.build(), 1)
        self.embeddings.embed_documents.assert_called_once()
        import chromadb
        row = chromadb.PersistentClient(path=str(self.db.resolve())).get_collection("contextual").get()
        self.assertEqual(row["metadatas"][0]["doc_id"], "report")
        self.assertIn("Jolly Scorpius", row["metadatas"][0]["raw_chunk"])

    def test_interrupted_build_is_not_ready_and_retry_does_not_duplicate_chunks(self):
        self.embeddings.embed_documents.side_effect = RuntimeError("provider unavailable")
        with self.assertRaises(RuntimeError):
            self.build()
        self.assertEqual(self.count(), 0)
        self.embeddings.embed_documents.side_effect = lambda texts: [[1.0, 0.0, 1.0] for text in texts]
        self.assertEqual(self.build(), 1)
        self.assertEqual(self.count(), 1)

    def test_changed_corpus_requires_rebuild(self):
        self.build()
        original = corpus_fingerprint(self.docs)
        (self.docs / "report.md").write_text("Changed report content.")
        self.assertNotEqual(corpus_fingerprint(self.docs), original)
        self.assertEqual(self.count(), 0)
        self.assertEqual(self.build(), 1)
        self.assertEqual(self.count(), 1)

    def test_malformed_manifest_is_not_ready_and_can_be_repaired(self):
        self.build()
        (self.db / "app_index.json").write_text("[]")
        self.assertEqual(self.count(), 0)
        self.assertEqual(self.build(), 1)

    def test_existing_legacy_collection_is_reused(self):
        self.build()
        (self.db / "app_index.json").unlink()
        self.assertEqual(self.count(), 1)
        self.assertEqual(self.build(), 1)
        self.embeddings.embed_documents.assert_called_once()

    def test_empty_corpus_fails_before_embedding(self):
        (self.docs / "report.md").unlink()
        with self.assertRaises(ValueError):
            self.build()
        self.embeddings.embed_documents.assert_not_called()

    def test_credentials_accept_cloud_secrets_preserve_environment_and_report_missing(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(len(configure_credentials({})), 2)
            self.assertEqual(configure_credentials({"ANTHROPIC_API_KEY": "test-a", "COHERE_API_KEY": "test-c"}), [])
            self.assertEqual(os.environ["ANTHROPIC_API_KEY"], "test-a")
            configure_credentials({"ANTHROPIC_API_KEY": "replacement"})
            self.assertEqual(os.environ["ANTHROPIC_API_KEY"], "test-a")
