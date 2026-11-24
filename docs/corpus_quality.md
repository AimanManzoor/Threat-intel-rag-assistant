# Corpus-quality dashboard

Audits only data/processed Markdown files, without provider calls or source writes.
These files are index-eligible; the audit does not establish index readiness.

Checks declared title/date/URL metadata, dates, source fingerprints, normalized-body
duplicate candidates and graph-body versus footer-only CVE literals.

Metadata parsing supports this repository's flat frontmatter profile, not general
YAML. Publication dates and URLs remain declarations, not authenticated facts.
Body selection follows the existing graph heuristic. The vector index builder
can still embed footers; this audit does not clean or rebuild that index.

Duplicate candidates are not automatically merged or deleted. Zero CVEs is not
a failure. Missing/unreadable fields remain unavailable rather than fabricated.

Limits: 50 files, 1 MB per source, no symlinks or paths outside the project.
File limits are not an execution-time guarantee. Fingerprints identify bytes,
not publisher authenticity.

Seven new tests cover metadata, dates, URLs, footer scope, duplicates, read-only
behavior, source limits and offline UI operation.

Run: python -m unittest discover -s tests -v
Open Streamlit and select Corpus quality (offline).
