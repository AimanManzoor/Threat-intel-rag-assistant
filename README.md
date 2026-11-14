# Threat-Intel RAG Assistant 🛡️

Self-correcting Retrieval-Augmented Generation pipeline over Unit 42 threat intelligence content (Palo Alto Networks' threat research arm). Built with LangGraph, Anthropic Claude, and Cohere — engineered for cybersecurity-domain question answering with grounded citations to source reports.

**Read the [architecture document](docs/architecture.md)** for design rationale, the StateGraph diagram, measured eval results, and the v0.2 roadmap.

## Highlights (v0.1)

- LangGraph workflow with deterministic simple retrieval and bounded answer-check retries
- Sitemap-driven scraper for Unit 42 (robots.txt-respecting, polite rate-limiting, raw HTML + processed markdown separation)
- Dual-collection ablation infrastructure (vanilla + contextual Chroma indices)
- Cohere `embed-english-v3.0` + `rerank-english-v3.0` for retrieval and reranking
- 10-question domain-specific evaluation harness with measured metrics
- Initial evaluation and evidence-recording workflow; factual correctness, citation validation and rate-limit handling remain under improvement

## Planned v0.2 extensions

- Multi-agent architecture (supervisor + researcher + synthesizer + verifier) using LangGraph's supervisor pattern
- Potential Anthropic prompt caching for contextual retrieval (cost savings not measured in this project)
- Expansion to full 50-document corpus
- Hybrid BM25 + dense retrieval for CVE/IoC exact-match queries

## Tech stack

Python · LangGraph · LangChain · Anthropic Claude (Haiku 4.5 + Sonnet 4.5) · Cohere · Chroma · BeautifulSoup · markdownify

## Quick start

### Streamlit interface

The repository includes `app.py`, a Threat Intel interface for the current graph.
It replaces the locally copied Helios Solar labels, links, examples, and unsupported
accuracy caption. It displays model self-scores separately from measured accuracy,
retains results across UI reruns, exposes the full retrieved excerpts, and flags
citation IDs that do not exactly match those excerpts' source IDs.

After installing dependencies and configuring local API keys:

```bash
python -m streamlit run app.py --server.address 127.0.0.1
```

The app reuses a nonempty local `contextual` collection. If no usable index exists,
it waits for an explicit **Initialize search index** click before making Cohere
embedding calls. This hosted bootstrap embeds plain excerpts from `data/processed/`
without LLM context generation. Cloud storage resets can require initialization
again. Initialization and questions use the configured provider APIs.

See [Streamlit deployment](docs/streamlit_deployment.md) for setup, secret handling,
index lifecycle, validation limits, and the hosted verification checklist.

### CLI setup

```bash
git clone https://github.com/AimanManzoor/Threat-intel-rag-assistant.git
cd Threat-intel-rag-assistant
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # fill in ANTHROPIC_API_KEY and COHERE_API_KEY

python -m src.scrape_unit42         # scrape from Unit 42 sitemap
python -m src.build_vanilla_chunks  # chunk and cache
python src/build_index.py           # build Chroma indices
python -m src.graph "your question" # run a query
python -m eval.run_eval             # full evaluation
```

## Repo structure
src/
├── scrape_unit42.py    # Sitemap-driven scraper
├── contextual.py        # Chunking + (optional) LLM context generation
├── build_vanilla_chunks.py
├── build_index.py       # Dual Chroma collection builder
├── state.py             # RAGState TypedDict schema
├── nodes.py             # Six graph nodes (rewrite, route, retrieve, rerank, generate, self_check)
└── graph.py             # LangGraph StateGraph wiring
eval/
├── questions.jsonl      # 10 labeled questions
├── run_eval.py          # Evaluation runner
└── summary.md           # Latest metrics
docs/
└── architecture.md      # Design rationale + measured results + v0.2 roadmap
data/
├─ raw/                 # Scraped HTML (gitignored, regenerable)
└── processed/           # Cleaned markdown corpus
## Sister project

This is a domain transfer of [Advanced_Rag_LangGraph](https://github.com/AimanManzoor/Advanced_Rag_LangGraph), which is the v1 self-correcting RAG on a synthetic corpus. Same architecture, different data layer — demonstrating that the pipeline code is corpus-agnostic.

## License

MIT


## Routing correction and offline checks

The current route selects `simple` without a router LLM call.
The multi-hop node is a reserved stub and is not selected by this baseline.
Answer checking still permits two total attempts; reaching that cap does not guarantee correctness.

Run offline checks: `python -m unittest discover -s tests -v`.
These use the actual graph wiring and route function with controlled external nodes.
They verify routing, retry bounds and recorder checkpointing without API calls.

`eval/run_verified.py` records fresh answers and their generation-context chunks.
Its generated `eval/verification_*.json` reports remain local.
The committed evaluation summary is a historical baseline: generic keyword matches are not factual-accuracy measurements.
Exact citation-ID validation is implemented. Corpus cleanup, rate-limit backoff and stronger factual-answer evaluation remain pending.



## Exact citation-ID validation

The graph runs a deterministic citation check after the final model self-check.
It extracts bracketed IDs from the answer and compares them with exact source
IDs from the reranked excerpts supplied to generation. It also checks consistency
with the reported citation list. This adds no provider calls or retries.

The result includes citation_validation with status, parsed citations,
invalid IDs, and allowed source IDs.

Statuses:
- matched_ids
- invalid_ids
- inconsistent
- missing_citations
- no_sources

Case and whitespace are not silently repaired.

The Streamlit interface displays answers with citation problems as candidates
requiring review. The original text remains available in an expander.
CLI/API results preserve the candidate and include the validation report;
callers must inspect that report before using an answer.

Matching IDs establishes reference membership only. It does not establish
factual correctness, claim support, retrieval relevance, or correct abstention.
An uncited refusal can require review too; this check does not interpret refusals.

The offline suite now contains 27 tests. Checks cover unknown and missing IDs,
case and whitespace, full identifiers, inconsistent citation lists, and a high
model self-score that still fails citation validation.

Verification recordings retain the validation report and a fingerprint of
the checker source. Historical evaluation files are unchanged.
These tests do not establish a factual-accuracy score.

Run checks:
    python -m unittest discover -s tests -v
