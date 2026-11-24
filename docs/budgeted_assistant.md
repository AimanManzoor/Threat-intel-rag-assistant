# Budgeted evidence-first assistant

## Implemented scope
An opt-in workspace alongside the existing Threat Q&A, evidence graph and corpus
audit views. This adds a fixed orchestration/controller harness with permitted
operations and output checks, not an autonomous multi-agent system.

Supported exact-CVE source requests use the existing deterministic graph lookup
with zero provider calls. Unknown CVEs do not fall back to paid retrieval.
Unsupported requests containing a CVE ask for clarification.
Other questions can use paid RAG only when the operator selects that option and
supplies a model ID available in their account. There is no automatic model upgrade
or selection of a supposedly cheapest model.

## Paid request policy
1. Read approved data/processed bodies using the existing graph body/footer rule.
2. Require an already available index; no index is built by this workspace.
3. Embed the original question once, without an LLM query rewrite.
4. Retrieve at most 20 local candidate excerpts.
5. Keep only excerpts with a known local document ID and a whitespace-normalized,
   case-sensitive contiguous match in the approved body. Reject unknown sources,
   navigation/footer-only content and excerpts over 2000 characters.
6. If no excerpt survives, abstain before reranking/generation.
7. Rerank once. Pass at most four whole excerpts and at most 8000 serialized
   context characters to one generation request with max_tokens=1024.
8. Require strict JSON, up to three claims, allowed source IDs and quotes
   present in the supplied excerpts after whitespace normalization. Withhold incomplete/malformed/mismatched
   outputs. No automatic regeneration or model self-score calls.
9. All generated claims remain candidates requiring human review.

The existing vector index is not cleaned or rebuilt. The new request-time gate
rejects candidate chunks outside the supported body; mixed body/footer chunks
can be rejected too. This can reduce recall and answer coverage. The body
heuristic can omit legitimate report material and needs separate evaluation.

## Cost and execution limits
At most three deliberate SDK provider operations per paid request:
Cohere query embedding, Cohere reranking, Anthropic generation.
Reserve/count each attempt before execution, including failed attempts.
Anthropic max_retries=0 and Cohere request_options.max_retries=0 disable
configured SDK retries. No LLM tools are bound; a model cannot choose a command,
provider, file path or extra operation through its response.

The old typical one-pass path uses rewrite, embedding, reranking, generation and
self-scoring, and may repeat. These are structural path comparisons, not measured
billing savings. The old workflow remains available unchanged for comparison.

This is not a dollar, account-wide, persistent session or wall-clock budget.
SDK timeout=30 seconds is not a total-request deadline. Character bounds are not
input-token guarantees. Failures may still incur charges. Local Chroma operations
and provider-side behavior are not a counted global network/security boundary.

The receipt records stage attempts, latency, rejected-excerpt count and SDK-reported
usage when supplied. Missing usage remains unknown (empty), not zero cost.
No model answer, latency or monetary improvement has been measured with live calls.

## Accuracy boundary
Exact quote presence and source membership do not establish that a quote entails
a generated claim. A regression case explicitly demonstrates this limitation.
This is why the status is evidence_checked_requires_review, never verified truth.
No-match and abstention outcomes do not establish absence of a threat.

Generated content is data. Nothing in the output is evaluated as code or executed.
Source instructions may still influence the model's text; the fixed operation
policy does not make the model universally immune to prompt injection.

## Configuration and use
Paid RAG is server-disabled by default. The owner must set THREAT_ENABLE_PAID_RAG=1
in the server environment, or the same setting as true in Streamlit secrets, before
the paid checkbox is enabled. The request still requires the checkbox to be selected.
The server flag is a feature toggle, not authentication or an account spending limit.
Keep it disabled in public deployments until access and rate/usage controls exist.
It governs only this new workspace; it does not disable the legacy Threat Q&A flow.
For a controlled local test, set the flag in the Terminal environment before starting
the app. Never use private keys as the flag or model ID.

Open the app and choose Budgeted assistant (opt-in). Leave paid RAG disabled to
try an exact-CVE source lookup. To try paid RAG, configure existing provider keys,
choose a currently available Anthropic model ID and explicitly enable the option.
No keys or model availability were live-verified for this milestone.
Do not paste keys into model-ID or question fields.

Embedding and rerank model names match the existing index/workflow. Provider
availability must be verified; switching embeddings requires an explicit index
migration, not a silent fallback. New module dependencies are already in the
repository requirements. No package installation beyond those requirements is added.

Results are session-local across ordinary UI reruns; clicking Run again starts a
new request and can incur charges. Downloads contain the report, not API keys or
the raw question. Approved public excerpts and generated candidate claims can be
included; use approved data and review before sharing.

## Verification and next experiment
Sixteen new offline tests cover free routing, paid opt-in, operation limits,
source-body checks, exact quotes, schema/completion errors, no retries, output
redaction, context limits, UI behavior and SDK request configuration. Full suite:
82 regression tests; 15 existing source-question reference cases remain separate.
Tests use controlled adapters and make no provider calls.

Run:

    python -m unittest discover -s tests -v
    python -m eval.evaluate_graph_questions

Before selecting a default model or claiming improved accuracy/savings, freeze
answer/reference tasks and compare the legacy and budgeted modes on the same
questions, corpus and provider/model versions. Have a reviewer grade claim support,
source correctness, abstention and answer coverage, and record reported usage and
latency. Use a small explicit live budget. Keep outcome judgments separate from
the model's own self-score.

References:
- https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- https://github.com/anthropics/anthropic-sdk-python
- https://github.com/cohere-ai/cohere-python
