# Streamlit app deployment

## Scope and validation

`app.py` is the browser interface to `src.graph.app` in this repository. It is
configured for the Unit 42 Threat Intel corpus, not the separate Helios Solar demo.
The backend still uses deterministic simple retrieval and at most two answer-check
attempts. Displayed self-scores are not factual-accuracy measurements.

The deployment preparation was verified with Streamlit 1.57.0, Chroma 1.5.9, and
LangGraph 1.1.10. Eighteen tests cover the three existing routing/recorder checks,
eight runtime/index checks, and seven Streamlit AppTest interaction checks. The
index tests use real temporary Chroma stores and mocked Cohere embedding responses;
the UI tests use a controlled graph. No paid provider calls were used in those tests.
This does not establish hosted connectivity, live answer correctness, or a deployed URL.

## Local run

From the repository root, activate the existing virtual environment and run:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m streamlit run app.py --server.address 127.0.0.1
```

Configure `ANTHROPIC_API_KEY` and `COHERE_API_KEY` in the local `.env`, in Streamlit
secrets, or as environment variables. Environment values take precedence. Do not
commit `.env` or `.streamlit/secrets.toml`; both are ignored by Git.

## Community Cloud form

Sign in at https://share.streamlit.io/ and connect the GitHub account that owns the
repository. Create an app using these form values; they are not terminal commands:

| Form field | Value |
|---|---|
| Repository | `AimanManzoor/Threat-intel-rag-assistant` |
| Branch | `main` |
| Main file path | `app.py` |
| Python version, under Advanced settings | `3.12` |

In Advanced settings, set the two keys in the Secrets field. Use the actual values
only in that private field, replacing the placeholders below:

```toml
ANTHROPIC_API_KEY = "your-anthropic-key"
COHERE_API_KEY = "your-cohere-key"
```

Deploy, open the resulting `streamlit.app` address, and check the startup messages.
Missing keys produce setup instructions and a disabled query button, rather than
initializing provider clients during page import. Index startup failures and query
errors are displayed by type without exposing raw exception messages.

Official instructions:
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management

## Search index lifecycle

The Mac's `data/chroma_db/` is ignored by Git and is not copied to the host. A new
host therefore starts with no local index. With credentials configured, click
**Initialize search index** once. This incurs Cohere embedding calls and creates
the `contextual` collection used by the graph. This name is retained for compatibility;
the hosted bootstrap itself embeds plain report excerpts, without LLM summaries.
The separate CLI contextual-generation experiment remains available independently.

The bootstrap reads only `data/processed/*.md`, strips YAML frontmatter, chunks the
bodies, and stores document IDs, chunk indices, titles, URLs and raw text. It does
not scrape new content, expand to `processed_full`, or clean article navigation.

A file lock prevents concurrent builds in the same local directory. App-managed
indices record a corpus fingerprint, chunk count and build status in `app_index.json`.
Incomplete, malformed, or stale builds are not considered ready. Explicit
initialization replaces an unusable managed collection and verifies its final count.
Deterministic IDs and collection replacement avoid duplicate chunks on a retry.
A nonempty legacy collection without a manifest is reused without re-embedding;
its content and completeness cannot be independently verified by this readiness check.

Community Cloud does not guarantee persistence of local files. After a storage reset,
the app may require initialization and billable embeddings again. This is a small
prototype strategy, not durable vector-database hosting. The initialization button
is available to app viewers with configured server credentials; choose appropriate
app sharing settings and monitor provider usage when sharing the prototype.

## Hosted verification checklist

1. Confirm the page title is Threat-Intel RAG Assistant and the index is ready.
2. Ask which group operates RansomHouse. Compare the answer with Jolly Scorpius and
   inspect the RansomHouse excerpt and its full source ID.
3. Ask what bootkit mechanism is associated with RayInitiator in the Cisco report.
   Check for the GRUB bootkit explanation and supporting source.
4. Ask for Anthropic revenue in 2025. The reports should not support an answer;
   verify that the assistant appropriately refuses rather than fabricating a number.
5. Confirm the route is `simple`, source IDs are exact, and errors are handled visibly.

These are smoke checks, not a comprehensive accuracy benchmark. Refusals currently
may consume two backend attempts. Retrieval noise, source-ID generation errors,
rate-limit backoff and stronger reference evaluation remain separate improvement work.
