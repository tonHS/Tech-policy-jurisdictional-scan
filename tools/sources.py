"""Rebuild the "Cited in the current edition" section of SOURCES.md from scan.json.

Run from the repo folder:  python3 tools/sources.py

Only the text between the two marker comments in SOURCES.md is replaced.
Everything else in the file (monitored sources, update log) is left as is.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
START = "<!-- cited:start -->"
END = "<!-- cited:end -->"


def build(data):
    lines = [f"_Generated from `scan.json` (current to {data['asOf']}). Do not edit by hand._", ""]

    brief = data.get("brief", [])
    if brief:
        lines.append("### Monthly brief")
        lines.append("")
        for b in brief:
            lines.append(f"- **{b['title']}**")
            for label, url in b.get("sources", []):
                lines.append(f"  - [{label}]({url})")
        lines.append("")

    comp = data.get("compare")
    if comp:
        lines.append("### Where each country stands (comparison grid)")
        lines.append("")
        for j, cells in comp["rows"].items():
            for topic, cell in zip(comp["topics"], cells):
                srcs = cell[2] if len(cell) > 2 else []
                lines.append(f"- **{j} · {topic}**: {cell[1]}")
                for label, url in srcs:
                    lines.append(f"  - [{label}]({url})")
        lines.append("")

    lines.append("### Items")
    lines.append("")
    items = sorted(data.get("items", []), key=lambda i: i["date"], reverse=True)
    for i in items:
        where = i.get("jur", "")
        if i.get("also"):
            where += " + " + ", ".join(i["also"])
        if i.get("sub"):
            where += f" ({i['sub']})"
        when = i.get("dateText") or i["date"]
        lines.append(f"- **{i['title']}** · {where} · {when} · last checked {i['checked']}")
        if i.get("cite"):
            lines.append(f"  - Citation: {i['cite']}")
        for label, url in i.get("sources", []):
            lines.append(f"  - [{label}]({url})")
    lines.append("")

    urls = {u for i in data.get("items", []) for _, u in i.get("sources", [])}
    urls |= {u for b in brief for _, u in b.get("sources", [])}
    if comp:
        urls |= {u for cells in comp["rows"].values() for c in cells if len(c) > 2 for _, u in c[2]}
    lines.append(f"_{len(items)} items, {len(urls)} unique source links._")
    return "\n".join(lines)


def main():
    data = json.loads((ROOT / "scan.json").read_text(encoding="utf-8"))
    path = ROOT / "SOURCES.md"
    text = path.read_text(encoding="utf-8")
    if START not in text or END not in text:
        sys.exit("SOURCES.md is missing the cited:start / cited:end markers.")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    path.write_text(f"{head}{START}\n{build(data)}\n{END}{tail}", encoding="utf-8")
    print("SOURCES.md updated.")


if __name__ == "__main__":
    main()
