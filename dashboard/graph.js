"use strict";

(() => {
  const data = window.THREAT_DATA;
  const selector = document.getElementById("cve-select");

  if (!data || !selector) return;

  const reports = data.nodes.filter(n => n.entity_type === "report");
  const cves = data.nodes.filter(n => n.entity_type === "cve");

  const section = document.createElement("section");
  section.className = "evidence-map";

  const heading = document.createElement("h2");
  heading.textContent = "Report-to-CVE evidence map";

  const description = document.createElement("p");
  description.className = "muted";
  description.textContent =
    "Blue boxes are reports. Green boxes are CVEs. Click a CVE to inspect its evidence below. Connections mean mentions, not exploitation.";

  const scroll = document.createElement("div");
  scroll.className = "graph-scroll";

  const namespace = "http://www.w3.org/2000/svg";

  function svgElement(tag, attributes, text) {
    const node = document.createElementNS(namespace, tag);

    for (const [name, value] of Object.entries(attributes || {})) {
      node.setAttribute(name, String(value));
    }

    if (text !== undefined) node.textContent = text;
    return node;
  }

  const height = Math.max(
    300,
    reports.length * 85 + 60,
    cves.length * 95 + 60
  );

  const svg = svgElement("svg", {
    viewBox: `0 0 900 ${height}`,
    role: "group",
    "aria-label": "Public report and CVE mention connections"
  });

  const positions = new Map();

  reports.forEach((report, index) => {
    positions.set(report.id, {
      x: 20,
      y: 55 + index * 85,
      width: 360
    });
  });

  cves.forEach((cve, index) => {
    positions.set(cve.id, {
      x: 610,
      y: 65 + index * 95,
      width: 260
    });
  });

  const connections = [];

  for (const link of data.links) {
    const from = positions.get(link.source);
    const to = positions.get(link.target);

    if (!from || !to) continue;

    const path = svgElement("path", {
      d: `M ${from.x + from.width} ${from.y}
          C 470 ${from.y}, 520 ${to.y}, ${to.x} ${to.y}`,
      class: "connection"
    });

    connections.push({ path, cveId: link.target });
    svg.append(path);
  }

  const cveButtons = [];

  function drawNode(record, isCve) {
    const position = positions.get(record.id);
    const group = svgElement("g", {
      transform: `translate(${position.x}, ${position.y})`
    });

    group.append(svgElement("title", {}, record.label));

    group.append(svgElement("rect", {
      x: 0,
      y: -25,
      width: position.width,
      height: 50,
      rx: 8,
      class: isCve ? "cve-box" : "report-box"
    }));

    const label = isCve || record.label.length <= 42
      ? record.label
      : record.label.slice(0, 39) + "…";

    group.append(svgElement("text", {
      x: 14,
      y: 6
    }, label));

    if (isCve) {
      group.setAttribute("class", "cve-node");
      group.setAttribute("role", "button");
      group.setAttribute("tabindex", "0");
      group.setAttribute("aria-label", `Inspect ${record.label}`);
      group.setAttribute("aria-pressed", "false");

      function chooseCve() {
        selector.value = record.id;
        selector.dispatchEvent(new Event("change", { bubbles: true }));
      }

      group.addEventListener("click", chooseCve);

      group.addEventListener("keydown", event => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          chooseCve();
        }
      });

      cveButtons.push({ group, id: record.id });
    }

    svg.append(group);
  }

  reports.forEach(report => drawNode(report, false));
  cves.forEach(cve => drawNode(cve, true));

  function highlightSelection() {
    for (const connection of connections) {
      connection.path.classList.toggle(
        "selected",
        connection.cveId === selector.value
      );
    }

    for (const button of cveButtons) {
      const selected = button.id === selector.value;
      button.group.classList.toggle("selected", selected);
      button.group.setAttribute("aria-pressed", String(selected));
    }
  }

  selector.addEventListener("change", highlightSelection);

  scroll.append(svg);
  section.append(heading, description, scroll);
  document.querySelector("main").before(section);

  highlightSelection();
})();
