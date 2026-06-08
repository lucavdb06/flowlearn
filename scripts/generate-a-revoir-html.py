#!/usr/bin/env python3
"""Generate one charte HTML sibling per markdown file in 3-a-revoir/."""

from __future__ import annotations

import html as html_lib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJET = ROOT / "1-document" / "projet"
AREVOIR = PROJET / "3-a-revoir"

META = {
    "formation": "T-ESP-800",
    "version": "v0.1 — brouillon",
    "date": "Juin 2026",
    "responsable": "Jean-Baptiste Vigreux — Porteur de projet",
    "statut": "À revoir",
}


def esc(text: str) -> str:
    return html_lib.escape(text.strip())


def css_href_for(md_path: Path) -> str:
    rel = md_path.parent.relative_to(PROJET)
    ups = "../" * len(rel.parts)
    return f"{ups}2-en-cours/charte-graphique/flowlearn-document.css"


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    in_table = False
    in_ul = False
    in_ol = False

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def close_table():
        nonlocal in_table
        if in_table:
            out.append("</tbody></table>")
            in_table = False

    def inline(s: str) -> str:
        s = re.sub(r"`([^`]+)`", r'<span class="mono">\1</span>', s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        return s

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            close_lists()
            close_table()
            lang = stripped[3:].strip()
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(html_lib.escape(lines[i]))
                i += 1
            i += 1
            cls = "mermaid-block" if lang == "mermaid" else "code-block"
            out.append(f'<pre class="{cls}"><code>{"".join(code_lines)}</code></pre>')
            continue

        if stripped.startswith("|") and "|" in stripped[1:]:
            close_lists()
            if not in_table:
                out.append('<table class="no-break">')
                in_table = True
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if all(re.match(r"^[-:]+$", c) for c in cells):
                i += 1
                continue
            if i + 1 < len(lines) and re.match(r"^\|[-| :]+\|$", lines[i + 1].strip()):
                out.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells) + "</tr></thead><tbody>")
                i += 2
                continue
            if "<thead>" not in "".join(out[-5:]) and "<tbody>" not in "".join(out[-3:]):
                out.append("<tbody>")
            out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells) + "</tr>")
            i += 1
            continue
        else:
            close_table()

        if stripped in ("---", "***"):
            close_lists()
            out.append('<div class="flourish"></div>')
            i += 1
            continue

        m = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if m:
            close_lists()
            level = len(m.group(1))
            tag = f"h{min(level + 1, 4)}"
            cls = ' class="section-title"' if level == 1 else ""
            out.append(f"<{tag}{cls}>{inline(m.group(2))}</{tag}>")
            i += 1
            continue

        if re.match(r"^[-*]\s+", stripped):
            if not in_ul:
                close_lists()
                out.append('<ul class="bullet-list">')
                in_ul = True
            out.append(f"<li>{inline(re.sub(r'^[-*]\s+', '', stripped))}</li>")
            i += 1
            continue

        if re.match(r"^\d+\.\s+", stripped):
            if not in_ol:
                close_lists()
                out.append('<ol class="steps">')
                in_ol = True
            out.append(f"<li>{inline(re.sub(r'^\d+\.\s+', '', stripped))}</li>")
            i += 1
            continue

        if stripped == "":
            close_lists()
            i += 1
            continue

        close_lists()
        if stripped.startswith(">"):
            out.append(f'<div class="callout"><p>{inline(stripped.lstrip("> ").strip())}</p></div>')
        else:
            out.append(f"<p>{inline(stripped)}</p>")
        i += 1

    close_lists()
    close_table()
    return "\n".join(out)


def extract_title(md: str) -> tuple[str, str]:
    for line in md.splitlines():
        m = re.match(r"^#\s+(.+)$", line.strip())
        if m:
            raw = m.group(1)
            clean = re.sub(r"\*\*([^*]+)\*\*", r"\1", raw)
            clean = re.sub(r"`([^`]+)`", r"\1", clean)
            short = clean[:60] + ("…" if len(clean) > 60 else "")
            return clean, short
    return "Document", "Document"


def split_pages(content_html: str, max_chars: int = 5200) -> list[str]:
    parts = re.split(r"(?=<h2|<h3|<span class=\"section-num\")", content_html)
    pages: list[str] = []
    buf = ""
    for part in parts:
        if not part.strip():
            continue
        if len(buf) + len(part) > max_chars and buf:
            pages.append(buf)
            buf = part
        else:
            buf += part
    if buf.strip():
        pages.append(buf)
    return pages or [content_html]


def build_page_html(md_path: Path) -> str:
    md = md_path.read_text(encoding="utf-8")
    title, title_short = extract_title(md)
    css = css_href_for(md_path)
    body = md_to_html(md)
    rel_arevoir = md_path.relative_to(AREVOIR).as_posix()

    cover = f"""
<section class="page cover">
  <div class="cover-inner">
    <div class="cover-top">
      <div class="cover-logo"><div class="wordmark">Flow<em>Learn</em></div></div>
      <div class="cover-meta">
        <div>{esc(META['formation'])}</div>
        <div><strong>À revoir</strong></div>
        <div>{esc(META['date'])}</div>
      </div>
    </div>
    <div class="cover-middle">
      <div class="cover-eyebrow">3-a-revoir · <span class="tag tag-revoir">{esc(META['statut'])}</span></div>
      <h1 class="cover-title">{esc(title_short)}</h1>
      <p class="cover-deck mono" style="font-size:10pt;">{esc(rel_arevoir)}</p>
    </div>
    <div class="cover-bottom">
      <div class="cover-stat"><div class="label">Source MD</div><div class="value" style="font-size:12pt;">{esc(md_path.name)}</div></div>
      <div class="cover-stat"><div class="label">Version</div><div class="value" style="font-size:14pt;">{esc(META['version'])}</div></div>
    </div>
  </div>
</section>"""

    pages = [cover]
    for i, chunk in enumerate(split_pages(body), start=2):
        pages.append(f"""
<section class="page">
  <div class="running-header">
    <span class="brand-name">Flow<em>Learn</em></span>
    <span class="doc-tag">À revoir · {esc(md_path.stem)}</span>
  </div>
  {chunk}
  <div class="page-footer"><span>3</span><span class="pf-brand">FlowLearn — {esc(title_short)}</span><span>{i:02d}</span></div>
</section>""")

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>FlowLearn — {esc(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,600;1,9..144,400&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}">
</head>
<body>
{"".join(pages)}
</body>
</html>"""


def main():
    removed = []
    for old in [
        AREVOIR / "FlowLearn-PBS.html",
        AREVOIR / "FlowLearn-WBS.html",
        AREVOIR / "FlowLearn-DoD.html",
        AREVOIR / "FlowLearn-Index-A-Revoir.html",
    ]:
        if old.exists():
            old.unlink()
            removed.append(old.name)

    count = 0
    for md_path in sorted(AREVOIR.rglob("*.md")):
        html_path = md_path.with_suffix(".html")
        html_path.write_text(build_page_html(md_path), encoding="utf-8")
        print(f"Wrote {html_path.relative_to(ROOT)}")
        count += 1

    if removed:
        print(f"Removed consolidated: {', '.join(removed)}")
    print(f"Done — {count} HTML files next to their .md sources.")


if __name__ == "__main__":
    main()
