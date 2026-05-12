# BUGS.md — Debugging Journal

A running log of real bugs hit during development of this project — with hypotheses, fixes, and lessons learned. The messy middle most portfolios hide.

---

## 2026-05-08 — Contextual.py crashed mid-doc-10, cache empty, $4 lost
**Symptom:** `contextual.py` crashed on doc 10 with a rate-limit error after running for 30+ minutes. Checked `data/.contextual_chunks_cache.json` — file didn't exist. All progress lost.
**Hypothesis:** Original script wrote cache only at end of all docs, not after each. Crash before the final write meant nothing saved.
**Fix:** Rewrote `build_contextual_chunks()` to checkpoint after every document. Re-runs skip already-processed doc_ids and resume from the last checkpoint.
**Lesson:** Any long-running paid script must be **resumable**. Save state per unit of work, not at the end. Assume the script will crash.
**Cost:** ~$4 in Anthropic tokens

---

## 2026-05-08 — Anthropic credit balance hit zero mid-run
**Symptom:** `BadRequestError: 400 - "Your credit balance is too low to access the Anthropic API."` raised partway through generating contextual chunks.
**Hypothesis:** Each contextual chunk call sends the full document as input. Unit 42 posts run 50-60K tokens, so per-chunk cost was ~$0.06 — far higher than I estimated.
**Fix:** Topped up credits. Decided to disable contextual generation in v0.1 and ship vanilla retrieval instead. Prompt caching is on the v0.2 roadmap (~90% cost reduction).
**Lesson:** Smoke-test the most expensive operation on the smallest unit (1 doc) before running on the full corpus. Token economics drive architecture decisions.

---

## 2026-05-08 — Cohere trial rate limit (100K tokens/min) hit at 379 chunks
**Symptom:** `TooManyRequestsError` from Cohere's embed API when running `build_index.py`. 379 chunks × ~250 tokens each = ~95K tokens, right at the trial-tier cliff.
**Hypothesis:** Trial Cohere keys cap at 100K tokens/min. Embedding all chunks in one batch exceeded that.
**Fix:** Reduced corpus from 10 docs to 5 docs (~200 chunks, ~50K tokens) to stay comfortably under the limit. v0.2 plan: paid production key.
**Lesson:** Free-tier limits are real architectural constraints, not "deal with it later" problems. Either batch with backoff, or scope smaller.

---

## 2026-05-08 — `mv` command with inline comments destroyed file targets
**Symptom:** `mv data/processed/unit42_03*.md data/processed_full/ # archives 30-39` failed with `mv: 30-39 is not a directory`.
**Hypothesis:** Pasted as one block, the shell didn't process `#` as a comment — it treated comment text as additional arguments to `mv`.
**Fix:** Removed inline comments. Used `ls | sort | tail -n +6 | xargs -I {} mv {} data/processed_full/` — one operation, no comment ambiguity.
**Lesson:** Inline shell comments don't survive multi-command paste reliably. Strip comments before copy-paste.

---

## 2026-05-08 — Heredoc paste-failure: shell command landed inside Python file
**Symptom:** `python src/build_index.py` failed with `SyntaxError: invalid syntax` on line 1. Line 1 was `echo "data/chroma_db/" >> .gitignore`.
**Hypothesis:** When pasting Python into nano, the trailing shell command got copied in. The Python interpreter doesn't understand shell.
**Fix:** Opened `build_index.py`, deleted the rogue first line, saved. Ran the `echo` command separately in the shell.
**Lesson:** Watch the terminal prompt **before every paste**. If you're in nano (file editor), you're pasting into a Python file. If you're in the shell, you're running a command. Different contexts.

---

## 2026-05-08 — `cat` with no filename hung waiting for keyboard input
**Symptom:** Ran `cat` alone, then typed several commands hoping they'd execute. Nothing ran — output just echoed lines back.
**Hypothesis:** `cat` with no argument reads from stdin (keyboard) by default. Every line typed was being echoed, not executed.
**Fix:** `Ctrl + D` to send EOF, or `Ctrl + C` to force-quit. Returned to shell prompt.
**Lesson:** `cat <filename>` reads a file. `cat` alone reads keyboard input. To exit cat: Ctrl+D (clean) or Ctrl+C (force).

---

## 2026-05-09 — Venv deactivated between sessions, packages "missing"
**Symptom:** Returned to terminal next morning. Ran `python src/contextual.py` and got `ModuleNotFoundError: No module named 'langchain_anthropic'`.
**Hypothesis:** Closed terminal exited the venv. Without re-activating, Python used the system interpreter, which doesn't have the project's packages.
**Fix:** `source .venv/bin/activate` — prompt now shows `(.venv)`.
**Lesson:** Venvs don't persist across terminal sessions. First command after `cd <project>` should always be `source .venv/bin/activate`.
