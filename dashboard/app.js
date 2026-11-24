"use strict";

const element = id => document.getElementById(id);

function textElement(tag, text) {
  const node = document.createElement(tag);
  node.textContent = text;
  return node;
}

function startDashboard() {
  const data = window.THREAT_DATA;

  if (!data) {
    element("status").textContent =
      "Evidence could not load. Run the export command and refresh.";
    return;
  }

  const reports = data.nodes.filter(node => node.entity_type === "report");
  const cves = data.nodes.filter(node => node.entity_type === "cve");
  const byId = new Map(data.nodes.map(node => [node.id, node]));

  element("reports").textContent = reports.length;
  element("cves").textContent = cves.length;
  element("connections").textContent = data.links.length;
  element("fingerprint").textContent = data.graph_sha256;

  const selector = element("cve-select");

  for (const cve of cves) {
    const option = textElement("option", cve.label);
    option.value = cve.id;
    selector.append(option);
  }

  function renderEvidence() {
    const results = element("results");
    results.replaceChildren();

    if (!selector.value) {
      element("status").textContent =
        "Choose an identifier to see matching report excerpts.";
      return;
    }

    const matches = data.links.filter(
      link => link.target === selector.value
    );

    element("status").textContent =
      `${matches.length} report connection(s) in this saved snapshot.`;

    if (!matches.length) {
      results.append(textElement(
        "p",
        "No matches in this corpus. This does not establish absence of a threat."
      ));
      return;
    }

    for (const link of matches) {
      const report = byId.get(link.source);
      const article = document.createElement("article");

      article.append(
        textElement("h2", report ? report.label : link.source),
        textElement("p", `Source location: ${link.source_location}`),
        textElement("blockquote", link.excerpt),
        textElement("code", link.source_file)
      );

      results.append(article);
    }
  }

  selector.addEventListener("change", renderEvidence);
  renderEvidence();
}

startDashboard();
