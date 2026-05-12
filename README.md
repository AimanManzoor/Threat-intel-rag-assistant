# Threat-Intel RAG Assistant 🛡️

Self-correcting Retrieval-Augmented Generation pipeline over Unit 42 threat intelligence content (Palo Alto Networks' threat research arm). Built with LangGraph, Anthropic Claude, and Cohere — engineered for cybersecurity-domain question answering with grounded citations to source reports.

**Read the [architecture document](docs/architecture.md)** for design rationale, the StateGraph diagram, measured eval results, and the v0.2 roadmap.

## Highlights (v0.1)

- LangGraph StateGraph with conditional routing and bounded retry loops
- Sitemap-driven scraper for Unit 42 (robots.txt-respecting, polite rate-limiting, raw HTML + processed markdown separation)
- Dual-collection ablation infrastructure (vanilla + contextual Chroma indices)
- Cohere `embed-english-v3.0` + `rerank-english-v3.0` for retrieval and reranking
- 10-question domain-specific evaluation harness with measured metrics
- 100% answer match on labeled eval · 0 errors · correct refusal on out-of-corpus queries

## v0.2 In Progress

- Multi-agent architecture (supervisor + researcher + synthesizer + verifier) using LangGraph's supervisor pattern
- Anthropic prompt caching for contextual retrieval (~90% cost reduction on long-form posts)
- Expansion to full 50-document corpus
- Hybrid BM25 + dense retrieval for CVE/IoC exact-match queries

## Tech stack

Python · LangGraph · LangChain · Anthropic Claude (Haiku 4.5 + Sonnet 4.5) · Cohere · Chroma · BeautifulSoup · markdownify

## Quick start

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
