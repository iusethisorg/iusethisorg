#!/usr/bin/env python3
"""iusethis static builder.

Reads articles/*.md (front matter + a small text markup), renders
writeups/<slug>.html from templates/article.html, and emits articles.js
(the manifest the front-page ledger gallery reads).

No dependencies beyond Python 3 stdlib — runs identically on a laptop
and in the GitHub Pages action. `make build` is the only entry point
people should need.

Markup understood in the body (deliberately tiny — this is a text blog):
  ## Heading            -> numbered section heading (I., II., ...)
  ![caption](src)       -> numbered figure; src "placeholder:hint" renders
                           an empty slot labeled with the hint
  > text                -> pull quote
  1. item / 2. item     -> ordered list
  blank-line-separated  -> paragraphs
"""

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "articles"
TEMPLATE = ROOT / "templates" / "article.html"
OUT_DIR = ROOT / "writeups"

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

REQUIRED = ["title", "standfirst", "author", "status"]
REGISTER_FIELDS = [
    ("since", "in use since"),
    ("hours_logged", "hours logged"),
    ("hours_to_fluency", "hours to fluency"),
    ("expected_remaining", "expected remaining"),
    ("provenance", "provenance"),
    ("care_ritual", "care ritual"),
]


def parse_front_matter(text, path):
    if not text.startswith("---"):
        sys.exit(f"{path}: missing front matter (--- block)")
    _, fm, body = text.split("---", 2)
    meta = {}
    for line in fm.strip().splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            meta[key.strip()] = val.strip()
    for key in REQUIRED:
        if key not in meta:
            sys.exit(f"{path}: front matter missing required field '{key}'")
    if meta["status"] == "published":
        missing = [k for k, _ in REGISTER_FIELDS if k not in meta]
        if missing:
            sys.exit(f"{path}: published article missing Register fields: {missing}"
                     " (the Register block is a merge requirement)")
    return meta, body.strip()


def render_body(body, warnings, path):
    out, sections, figures = [], 0, 0
    paras = re.split(r"\n\s*\n", body)
    list_buf = []

    def flush_list():
        nonlocal list_buf
        if list_buf:
            items = "".join(f"<li>{html.escape(i)}</li>" for i in list_buf)
            out.append(f"<ol>{items}</ol>")
            list_buf = []

    for para in paras:
        para = para.strip()
        if not para:
            continue
        m = re.match(r"^##\s+(.*)$", para)
        if m:
            flush_list()
            num = ROMAN[sections] if sections < len(ROMAN) else str(sections + 1)
            sections += 1
            out.append(f'<h2 class="section"><span class="num">{num}.</span>'
                       f"{html.escape(m.group(1))}</h2>")
            continue
        m = re.match(r"^!\[(.*?)\]\((.*?)\)$", para)
        if m:
            flush_list()
            figures += 1
            caption, src = m.group(1), m.group(2)
            if src.startswith("placeholder:"):
                hint = html.escape(src[len("placeholder:"):])
                img = f'<div class="placeholder">image {figures} / 5 — {hint}</div>'
            else:
                img = f'<img src="{html.escape(src)}" alt="{html.escape(caption)}">'
            out.append(f'<figure>{img}<figcaption><span class="fig-no">FIG. '
                       f"{figures}</span> {html.escape(caption)}</figcaption></figure>")
            continue
        if para.startswith(">"):
            flush_list()
            quote = " ".join(l.lstrip("> ").strip() for l in para.splitlines())
            out.append(f'<blockquote class="pull">{html.escape(quote)}</blockquote>')
            continue
        if re.match(r"^\d+\.\s", para):
            for line in para.splitlines():
                list_buf.append(re.sub(r"^\d+\.\s+", "", line.strip()))
            continue
        flush_list()
        text = html.escape(" ".join(para.split()))
        out.append(f"<p>{text}</p>")

    flush_list()
    if figures != 5:
        warnings.append(f"{path}: {figures} figures (the ledger format wants 5)")
    return "\n".join(out)


def register_rows(meta):
    rows = []
    for key, label in REGISTER_FIELDS:
        if key in meta:
            rows.append(f"<dt>{html.escape(label)}</dt>"
                        f"<dd>{html.escape(meta[key])}</dd>")
    return "\n      ".join(rows)


def main():
    template = TEMPLATE.read_text()
    manifest, warnings = [], []
    OUT_DIR.mkdir(exist_ok=True)

    sources = sorted(ARTICLES.glob("*.md"))
    published_no = 0
    for path in sources:
        meta, body = parse_front_matter(path.read_text(), path)
        slug = path.stem
        entry = {
            "slug": slug,
            "title": meta["title"],
            "standfirst": meta["standfirst"],
            "author": meta["author"],
            "status": meta["status"],
            "object": meta.get("object", ""),
            "since": meta.get("since", ""),
        }
        if meta["status"] == "published":
            published_no += 1
            entry["url"] = f"writeups/{slug}.html"
            body_html = render_body(body, warnings, path)
            words = len(re.sub(r"<[^>]+>", " ", body_html).split())
            page = template
            for key, val in {
                "TITLE": html.escape(meta["title"]),
                "STANDFIRST": html.escape(meta["standfirst"]),
                "AUTHOR": html.escape(meta["author"]),
                "KICKER": html.escape(meta.get("kicker", "A love story of an object")),
                "PALETTE": meta.get("palette", "marble"),
                "NO": f"{published_no:03d}",
                "REGISTER_ROWS": register_rows(meta),
                "BODY": body_html,
                "WORDS": f"~{words:,} words",
            }.items():
                page = page.replace("{{" + key + "}}", val)
            leftover = re.findall(r"{{\w+}}", page)
            if leftover:
                sys.exit(f"{path}: template placeholders unfilled: {leftover}")
            (OUT_DIR / f"{slug}.html").write_text(page)
        manifest.append(entry)

    # published first (newest file order), then forthcoming
    manifest.sort(key=lambda e: (e["status"] != "published", e["slug"]))
    js = ("// Generated by tools/build.py — do not edit. Source: articles/*.md\n"
          f"window.ARTICLES = {json.dumps(manifest, indent=2)};\n")
    (ROOT / "articles.js").write_text(js)

    print(f"built {published_no} page(s), {len(manifest)} manifest entr(ies)")
    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)


if __name__ == "__main__":
    main()
