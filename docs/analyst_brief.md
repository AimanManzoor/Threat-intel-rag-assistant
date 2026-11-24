# Analyst evidence brief

After a successful CVE source lookup in Evidence graph (offline), download
a plain-text analyst brief containing source references, excerpts, scope,
truncation status and the graph fingerprint when recorded.

The formatter makes no additional tool or provider calls. It refuses failed,
unverified or inconsistent outcomes. It does not infer severity, exploitation,
actor attribution or remediation. Human review remains required.

Plain text avoids interpreting source material as HTML or Markdown.
The fingerprint identifies an artifact; it does not authenticate a publisher.

Five new regression tests cover source inclusion, no-match warnings, rejected
outcomes, truncation and absence of additional tool calls.
