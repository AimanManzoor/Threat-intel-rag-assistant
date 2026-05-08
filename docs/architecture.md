# Threat-Intel RAG Assistant — Architecture (v0.1)

A self-correcting Retrieval-Augmented Generation pipeline over Unit 42 threat intelligence content. Built with LangGraph, Cohere reranking, and Anthropic Claude (Haiku 4.5 + Sonnet 4.5) for cost-conscious model assignment.

This is **v0.1** — a deliberately scoped proof-of-architecture on 5 Unit 42 reports. The full Unit 42 archive is ~3,000 posts; v0.2 expands to that scale with prompt caching for contextual retrieval and a paid Cohere production key.

## Pipeline diagram

The system is a LangGraph `StateGraph` with seven nodes and two conditional edges. The retry edge from `self_check` back to `rewrite_query` is what makes this a graph rather than a chain.
## Stages

| Stage | Model | Purpose |
|---|---|---|
| `rewrite_query` | Haiku | Expand cybersec acronyms (CVE, IoC, TTP), add synonyms |
| `route` | Haiku | Classify simple vs multi-hop |
| `retrieve` | (no LLM) | Cohere similarity search, top-20 candidates |
| `tool_use` | (stub) | Multi-hop placeholder — falls back to retrieve in v0.1 |
| `rerank` | Cohere `rerank-english-v3.0` | Cross-encoder narrows top-20 → top-5 |
| `generate` | Sonnet | Grounded answer with inline source citations |
| `self_check` | Haiku | Score groundedness 0.0-1.0; triggers retry below 0.7 |

**Cost design:** ~80% of LLM calls use Haiku; only generation uses Sonnet.

## Why LangGraph instead of LCEL

Three features required graph semantics:

1. **Conditional routing** — `route` branches between `retrieve` and `tool_use` based on a runtime LLM classification.
2. **Cycles** — the `self_check → rewrite_query` retry edge requires graph topology; LCEL is acyclic.
3. **Shared mutable state** — every node reads and writes the full `RAGState` TypedDict, so the retriever's chunks remain in scope at the self-check step.

## Measured results (v0.1, 10-question eval)

| Metric | Value |
|---|---|
| Total questions | 10 |
| Successful runs | 10 |
| Errors | 0 |
| Answer match rate | 100.0% |
| Avg confidence (self-check) | 0.35 |
| Avg attempts | 1.7 |
| Median latency | 12.15s |
| P95 latency | 24.94s |
| Route distribution | simple=0, multi_hop=10 |

Full results: [`eval/results.json`](../eval/results.json). Summary: [`eval/summary.md`](../eval/summary.md).

## Honest weaknesses and v0.2 roadmap

**1. Router miscalibration.** All 10 queries classified as `multi_hop`, including simple lookups. The fallback to `retrieve` masks the issue but wastes tokens. **Fix:** add 4-6 few-shot examples to the routing prompt and re-measure route_distribution.

**2. Loose answer-match metric.** Expected substrings in v0.1 are domain-generic ("CVE", "actor"). **Fix:** rewrite expected_substrings as specific entities (threat actor names, CVE numbers, exact tool names) and add a `expected_doc_ids` field for retrieval-quality measurement.

**3. Low avg confidence (0.35).** Corpus is too small for most queries to be well-grounded. **Fix:** scale to 50+ docs in v0.2 with prompt caching to keep contextual generation under $2.

**4. High P95 latency (25s).** Driven by retry loop firing on low-confidence answers. **Fix:** skip retry on detected out-of-corpus refusals, parallelize rewrite + route, stream the generation step.

**5. Contextual retrieval disabled.** Implemented in `src/contextual.py` but disabled in v0.1 due to cost economics on long-form posts (Unit 42 articles are 50-60K tokens; full-doc context calls cost ~$0.06/chunk). **Fix in v0.2:** enable Anthropic prompt caching to drop per-chunk cost ~90%.

## Tech stack

| Layer | Tool |
|---|---|
| Orchestration | LangGraph |
| LLMs | Anthropic Claude (Haiku 4.5, Sonnet 4.5) |
| Embeddings | Cohere `embed-english-v3.0` (1024-dim) |
| Reranker | Cohere `rerank-english-v3.0` |
| Vector DB | Chroma (persistent, on-disk) |
| Data acquisition | requests + BeautifulSoup + markdownify, sitemap-driven |
| Eval | Custom Python harness, JSONL labeled set |

## Reproducing the results

```bash
git clone https://github.com/AimanManzoor/Threat-intel-rag-assistant.git
cd Threat-intel-rag-assistant
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add ANTHROPIC_API_KEY and COHERE_API_KEY

python -m src.scrape_unit42         # scrape 50 posts (or use the provided cache)
python -m src.build_vanilla_chunks  # chunk + populate cache
python src/build_index.py           # build dual Chroma indices
python -m src.graph "your question" # ad-hoc query
python -m eval.run_eval             # full 10-question eval
```
