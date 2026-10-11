# -*- coding: utf-8 -*-
"""Print deck PDFs the way the README describes: headless Chrome, <deck>.html?print, Page.printToPDF with
preferCSSPageSize, after every image (lazy ones too) and the fonts have loaded. One slide per page, each finished
(print never plays a slide: every build shows and every settle hook runs).

    python deck_pdf.py odoo-crm portfolio     # writes pdf/<the deck's pdf name from DECKS in _src/build.py>
    python deck_pdf.py --all
    options: --look  (render the PDF pages to ~/ClaudeWork/qa/decks/<deck>-pdf.jpg to compare with the live end states)
             --base http://127.0.0.1:3970/  (use a running server)

Checks: page count == slide count. LOOK at the --look sheet: a half-built slide means a missing settle hook."""
import argparse, pathlib, re, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _cdp import REPO, serve, Chrome, decks  # noqa: E402

OUT = pathlib.Path.home() / "ClaudeWork/qa/decks"


def look(pdf, slug):
    import pymupdf
    from PIL import Image
    doc = pymupdf.open(pdf)
    W, H, cols = 400, 225, 4
    rows = (len(doc) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * W + (cols + 1) * 8, rows * H + (rows + 1) * 8), "#e9ebf2")
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=40)
        im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).resize((W, H), Image.LANCZOS)
        sheet.paste(im, (8 + (i % cols) * (W + 8), 8 + (i // cols) * (H + 8)))
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / f"{slug}-pdf.jpg"
    sheet.save(p, quality=82)
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("decks", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--look", action="store_true")
    ap.add_argument("--base")
    a = ap.parse_args()
    table = {d["slug"]: d for _, d in decks()}
    slugs = list(table) if a.all else a.decks
    if not slugs:
        sys.exit("name the decks, or --all")
    bad = [s for s in slugs if s not in table]
    if bad:
        sys.exit(f"not in DECKS (_src/build.py): {bad}")
    fails = 0
    with serve(base=a.base) as base, Chrome(1600, 900) as c:
        for slug in slugs:
            c.errors.clear()
            c.open(base + f"{slug}.html?print", settle=.5)
            c.ev("Promise.all([...document.images].map(i=>{i.loading='eager';return i.complete?1:new Promise(r=>{i.onload=i.onerror=r;})}).concat([document.fonts.ready])).then(()=>1)")
            c.sleep(2.5)
            c.images_loaded()
            out = REPO / "pdf" / table[slug]["pdf"]
            c.pdf(out)
            n = len(re.findall(r'<section class="slide[ "]', (REPO / f"{slug}.html").read_text(encoding="utf-8")))
            import pymupdf
            pages = len(pymupdf.open(out))
            ok = pages == n and not c.errors
            fails += not ok
            print(f"  {'ok ' if ok else 'BAD'} {out.name:44s} {pages} pages / {n} slides  {out.stat().st_size // 1024} KB" + (f"  errors: {sorted(set(c.errors))}" if c.errors else ""))
            if a.look:
                print("      look:", look(out, slug))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
