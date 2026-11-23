"""Deterministic report-body CVE mentions; no semantic or exploitation inference."""
import hashlib
from pathlib import Path
import re

CVE = re.compile(r"\bCVE-\d{4}-\d{4,}\b", re.IGNORECASE)
FOOTER = re.compile(r"^#{2,3}\s+(?:Tags|Table of Contents|Related(?:\s+.*)?)\s*$", re.IGNORECASE)
PROFILE = "threat_report_cve_v1"


def extract_mentions(root):
    root = Path(root).resolve()
    corpus = root / "data/processed"
    if corpus.is_symlink() or not corpus.resolve().is_relative_to(root):
        raise ValueError("Corpus must stay inside the project root.")
    files = sorted(corpus.glob("*.md"))
    if not 1 <= len(files) <= 50:
        raise ValueError("Expected 1-50 approved processed reports.")
    nodes, edges, sources, excerpts = {}, [], {}, {}
    for path in files:
        if path.is_symlink() or path.resolve().parent != corpus.resolve():
            raise ValueError("Source symlinks or paths outside the approved corpus are not supported.")
        with path.open("rb") as handle:
            raw = handle.read(1_000_001)
        if len(raw) > 1_000_000:
            raise ValueError("A processed source exceeds 1 MB.")
        text = raw.decode("utf-8")
        name = path.relative_to(root).as_posix()
        sources[name] = hashlib.sha256(raw).hexdigest()
        lines = text.splitlines()
        title = next((line[2:].strip() for line in lines if line.startswith("# ")), path.stem)[:180]
        report_id = "report:" + path.stem
        nodes[report_id] = {
            "id": report_id, "label": title, "file_type": "document",
            "entity_type": "report", "source_file": name, "source_location": "L1",
        }
        started, seen = False, set()
        for number, line in enumerate(lines, 1):
            if FOOTER.match(line):
                break
            if line.startswith("## "):
                started = True
            if not started:
                continue
            for match in CVE.finditer(line):
                cve = match.group().upper()
                if len(cve) > 128:
                    raise ValueError("Oversized CVE literal.")
                if cve in seen:
                    continue
                seen.add(cve)
                cve_id = "cve:" + cve
                nodes.setdefault(cve_id, {
                    "id": cve_id, "label": cve, "file_type": "concept",
                    "entity_type": "cve", "source_file": name, "source_location": f"L{number}",
                })
                excerpts[(report_id, cve_id)] = line[max(0, match.start() - 100):match.end() + 200]
                edges.append({
                    "source": report_id, "target": cve_id, "relation": "mentions",
                    "confidence": "EXTRACTED", "confidence_score": 1.0,
                    "source_file": name, "source_location": f"L{number}",
                })
    if len(nodes) > 500 or len(edges) > 1000:
        raise ValueError("Graph exceeds this prototype's node or edge budget.")
    return {
        "nodes": sorted(nodes.values(), key=lambda node: node["id"]),
        "edges": sorted(edges, key=lambda edge: (edge["source"], edge["target"])),
        "sources": sources, "excerpts": excerpts,
    }
