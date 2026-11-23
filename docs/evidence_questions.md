# Question-driven CVE source lookup

## Implemented task
Ask which approved processed reports literally mention one exact CVE. This
deterministic adapter creates a fixed plan for the existing evidence harness
and assembles a source summary from its verified mention records.

It is not general question understanding, an LLM planner, exploitation analysis,
or multi-hop answer generation. The original Threat Q&A workspace remains
available separately with its existing provider configuration.

## Supported language
Examples:
- Which reports mention CVE-2025-20333?
- Please find reports for cve-2025-20362.
- List documents mentioning CVE-2025-20363.
- Where is CVE-2025-20333 mentioned?
- CVE-2025-20333

Input is a single printable line of 1-1000 characters. Normalize spaces and
identifier case, require one distinct exact CVE-shaped token, then match the
whole request against explicit source-lookup patterns. This checks a limited
permitted language, not whether an arbitrary request is malicious.

Multiple/no CVEs, attribution/exploitation questions, exclusions, requested
counts, external fetches and appended instructions ask for clarification.
Unsupported requests are not partially answered. Invalid input is rejected.
No source tool runs for either outcome.

A syntactically matching identifier is not checked against a CVE registry.
No match means absent from this scoped local graph, not nonexistent or unexploited.

## Fixed tool boundary
The adapter emits only:

    {"tool":"graph_neighborhood","node_id":"cve:CVE-2025-20333","max_hops":1,"max_edges":20}

Questions cannot override hop/edge budgets, choose a source path, execute code
or request another tool. The existing harness verifies source bytes and literal
mention edges before returning evidence. The adapter additionally checks that
returned edges are one-hop mentions of the requested CVE from report nodes.

One ready request attempts one harness call and zero provider calls. Up to 20
report mentions can be returned; truncation is displayed as an incomplete result.
Completed is a software/source-contract outcome, not proof of a threat claim.

## Result and interface
Each result includes status, fixed plan, normalized CVE, source files and line
references, bounded excerpts, tool/provider counts and human-review requirement.
A successful result includes the harness receipt. The summary is deterministic;
it is not composed by an LLM.

The dashboard adds a source-question form inside Evidence graph (offline).
It keeps results across reruns but hides them after the question or graph artifact
changes until resubmitted. Exports do not include the raw question. The question
still exists in the application's session input state; do not enter secrets.

Run:

    python -m src.evidence_question --question "Which reports mention CVE-2025-20333?"

CLI exit 0: completed or scoped no_matches. Exit 1: clarification, rejection or
verification failure. No new dependency, API key, index build or Graphify rebuild
is needed for this milestone.

## Reference evaluation
Versioned cases: eval/graph_question_cases_v1.json.
Run:

    python -m eval.evaluate_graph_questions

Fifteen developer-authored cases cover supported forms, an unknown identifier,
missing/multiple CVEs, malformed identifiers, unsupported attribution, negation,
requested counts, external fetches and tool-override attempts.
Checks include status, CVE scope, exact source files, fixed plan, tool counts,
zero provider calls and human review.

The detailed report eval/verification_graph_questions.json is ignored by Git.
A reference mismatch returns exit 1; an invalid reference returns exit 2.
GitHub Actions runs this evaluation after the regression suite.

The software suite grows from 41 to 54 tests. New tests include wrong returned-CVE
rejection, source references, a deliberately wrong reference answer, truncation,
failed source verification, CLI exits and dashboard persistence/clarification.
Tests use controlled fixtures and the committed public corpus without provider calls.

Passing these cases does not establish general language understanding, factual
accuracy, universal prompt-injection protection or production security. They
exercise the supported contract. Human review and the graph's extraction/scope
limitations still apply.

## Next research comparison
Freeze separate supported and held-out paraphrase/challenge cases, then compare
an opt-in LLM planner with this deterministic baseline under the same fixed plan,
source access, tool budget and reference answers. Measure intent correctness,
clarification behavior, source correctness, latency and provider usage separately.
Do not let a planner alter the harness or reference expectations.
