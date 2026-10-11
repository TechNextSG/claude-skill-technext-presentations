# -*- coding: utf-8 -*-
"""QA for the TechNext decks: build, static checks, then every slide played in real-time headless Chrome.

    python deck_check.py                      # build, then check every deck
    python deck_check.py odoo-crm portfolio   # only these decks
    python deck_check.py odoo-crm --shots     # also save each slide's end state + a contact sheet to look at
    options: --no-build  --wait 2.5 (seconds per slide)  --base http://127.0.0.1:3970/ (use a running server)
             --phone (also open each deck as a phone held upright: the deck must turn, no errors)

ERROR (exit 1): build failure, script errors, broken images, text pushed off the 1600x900 stage, a shared copy that
still leads to the launcher. WARN: missing speaker notes, text overlapping other text, text cut by its container, text truncated with an ellipsis,
text under 11px, README slide count out of date. Every WARN gets a look in the shot before it is waived.
Shots land in ~/ClaudeWork/qa/decks/<deck>/ (contact sheet: <deck>-sheet.jpg). LOOK at the sheet: the script
cannot judge design, balance or whether a slide reads at the back of a room."""
import argparse, json, pathlib, re, subprocess, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _cdp import REPO, serve, Chrome, decks  # noqa: E402

OUT = pathlib.Path.home() / "ClaudeWork/qa/decks"

AUDIT = r"""
(function (i) {
  var slide = Deck.slides[i], sb = slide.getBoundingClientRect(), k = Deck.scale || 1, out = {off: [], clip: [], trunc: [], overlap: [], small: [], img: []};
  function name(el) {
    var t = (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 40);
    return el.tagName.toLowerCase() + (el.classList[0] ? '.' + el.classList[0] : '') + ' "' + t + '"';
  }
  function deco(el) { return el.closest('[aria-hidden=true],.s-chrome,.s-foot,.notes,script,style,template,noscript'); }
  function opac(el) { var o = 1; for (var e = el; e && e !== slide.parentNode; e = e.parentElement) o *= +getComputedStyle(e).opacity; return o; }
  var moving = new Set(); document.getAnimations().forEach(function (a) {
    var t = a.effect && a.effect.target; if (t && a.playState === 'running' && (a.effect.getTiming().iterations === Infinity)) moving.add(t);
  });
  function isMoving(el) { for (var e = el; e && e !== slide; e = e.parentElement) if (moving.has(e)) return true; return false; }
  function clipper(el) {
    for (var e = el.parentElement; e && e !== slide; e = e.parentElement) { var s = getComputedStyle(e); if (s.overflowX !== 'visible' || s.overflowY !== 'visible') return e; }
    return null;
  }
  function rel(r) { return {x: (r.left - sb.left) / k, y: (r.top - sb.top) / k, r: (r.right - sb.left) / k, b: (r.bottom - sb.top) / k, w: r.width / k, h: r.height / k}; }
  var boxes = [];
  var walker = document.createTreeWalker(slide, NodeFilter.SHOW_TEXT);
  var seen = new Set();
  for (var n = walker.nextNode(); n; n = walker.nextNode()) {
    if (!n.nodeValue.trim()) continue;
    var el = n.parentElement; if (!el || deco(el)) continue;
    if (el.checkVisibility && !el.checkVisibility({opacityProperty: true, visibilityProperty: true})) continue;
    var o = opac(el); if (o < .5) continue;
    var rg = document.createRange(); rg.selectNodeContents(n);
    var rs = [].slice.call(rg.getClientRects()).map(rel).filter(function (r) { return r.w > 1 && r.h > 1; });
    if (!rs.length) continue;
    var mv = isMoving(el), c = clipper(el);
    if (!seen.has(el)) {
      seen.add(el);
      var fs = parseFloat(getComputedStyle(el).fontSize);
      if (fs < 11) out.small.push(name(el) + ' ' + fs + 'px');
      var cs = getComputedStyle(el);
      if (cs.textOverflow === 'ellipsis' && (el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1)) out.trunc.push(name(el) + ' (shows "...")');
    }
    var ell = getComputedStyle(el).textOverflow === 'ellipsis';
    rs.forEach(function (r) {
      if (!c && (r.x < -2 || r.y < -2 || r.r > 1602 || r.b > 902)) out.off.push(name(el) + ' at ' + Math.round(r.x) + ',' + Math.round(r.y) + ' to ' + Math.round(r.r) + ',' + Math.round(r.b));
      if (c && !mv && !ell) {
        var cb = rel(c.getBoundingClientRect());
        var cut = Math.max(cb.x - r.x, cb.y - r.y, r.r - cb.r, r.b - cb.b);
        // a scroll box or a long list made to fade out is fine; text sliced by a card edge is not
        if (cut > 3 && cut < Math.min(r.h, r.w) && c.scrollHeight <= c.clientHeight + 4 && c.scrollWidth <= c.clientWidth + 4) out.clip.push(name(el) + ' cut by ' + name(c).split(' ')[0] + ' (' + Math.round(cut) + 'px)');
      }
      if (!mv) boxes.push({el: el, r: r});
    });
  }
  for (var a = 0; a < boxes.length; a++) for (var b = a + 1; b < boxes.length; b++) {
    var A = boxes[a], B = boxes[b]; if (A.el === B.el || A.el.contains(B.el) || B.el.contains(A.el)) continue;
    var ix = Math.min(A.r.r, B.r.r) - Math.max(A.r.x, B.r.x), iy = Math.min(A.r.b, B.r.b) - Math.max(A.r.y, B.r.y);
    if (ix <= 2 || iy <= 2) continue;
    var small = Math.min(A.r.w * A.r.h, B.r.w * B.r.h);
    if (ix * iy > small * .25) out.overlap.push(name(A.el) + ' x ' + name(B.el));
  }
  [].slice.call(slide.querySelectorAll('img')).forEach(function (im) {
    if (im.getAttribute('src') && im.complete && !im.naturalWidth) out.img.push(im.getAttribute('src'));
  });
  out.notes = !!slide.querySelector('.notes');
  out.id = slide.id; out.title = slide.dataset.title || '';
  for (var key in out) if (Array.isArray(out[key])) out[key] = Array.from(new Set(out[key])).slice(0, 8);
  return out;
})(%d)
"""


def static_checks(slugs, problems):
    v = re.search(r'ASSET_V = "(\d+)"', (REPO / "_src/build.py").read_text(encoding="utf-8")).group(1)
    share = json.loads((REPO / "_src/share.json").read_text(encoding="utf-8"))
    readme = (REPO / "README.md").read_text(encoding="utf-8")
    launcher = (REPO / "index.html").read_text(encoding="utf-8")
    for slug in slugs:
        html = (REPO / f"{slug}.html").read_text(encoding="utf-8")
        n = len(re.findall(r'<section class="slide[ "]', html))
        if 'name="robots" content="noindex,nofollow"' not in html:
            problems.append(("ERROR", slug, "no noindex,nofollow meta"))
        stale = sorted(set(re.findall(r'assets/[a-z0-9-]+\.(?:css|js)\?v=(\d+)', html)) - {v})
        if stale:
            problems.append(("ERROR", slug, f"assets carry ?v={stale}, ASSET_V is {v}: rebuild"))
        if slug in share:
            s = REPO / f"s-{share[slug]}.html"
            if not s.exists():
                problems.append(("ERROR", slug, f"shared copy {s.name} missing: rebuild"))
            elif 'data-home=' in s.read_text(encoding="utf-8"):
                problems.append(("ERROR", slug, f"shared copy {s.name} still has the Home button"))
        else:
            problems.append(("WARN", slug, "no share token yet (the build makes one)"))
        if f'href="{slug}.html"' not in launcher:
            problems.append(("WARN", slug, "not on the launcher: add it to DECKS in _src/build.py"))
        m = re.search(r"`%s\.html`\s*\|\s*(\d+)" % re.escape(slug), readme)
        if m and int(m.group(1)) != n:
            problems.append(("WARN", slug, f"README says {m.group(1)} slides, the deck has {n}"))
        elif not m:
            problems.append(("WARN", slug, "missing from the README deck table"))


def sheet(shots, path, cols=4):
    from PIL import Image, ImageDraw
    W, H, L = 400, 225, 22
    rows = (len(shots) + cols - 1) // cols
    im = Image.new("RGB", (cols * W + (cols + 1) * 8, rows * (H + L) + (rows + 1) * 8), "#e9ebf2")
    d = ImageDraw.Draw(im)
    for i, (label, p, bad) in enumerate(shots):
        x, y = 8 + (i % cols) * (W + 8), 8 + (i // cols) * (H + L + 8)
        im.paste(Image.open(p).convert("RGB").resize((W, H), Image.LANCZOS), (x, y + L))
        d.text((x + 2, y + 4), label, fill="#b4372b" if bad else "#1f1f3d")
        if bad:
            d.rectangle((x - 2, y + L - 2, x + W + 1, y + L + H + 1), outline="#b4372b", width=3)
    im.save(path, quality=82)
    return path


def check_deck(c, base, slug, a, problems):
    c.errors.clear()
    c.open(base + f"{slug}.html", settle=1.0)
    n = c.ev("Deck.slides.length")
    shots, d = [], OUT / slug
    if a.shots:
        d.mkdir(parents=True, exist_ok=True)
    for i in range(n):
        c.ev(f"Deck.go({i}, -1)")
        c.sleep(a.wait)
        c.images_loaded(f"Deck.slides[{i}]")
        r = c.ev(AUDIT % i)
        tag = f"{i + 1:02d} {r['id']}"
        bad = False
        for kind, level, label in (("off", "ERROR", "text off the stage"), ("img", "ERROR", "broken image"),
                                   ("overlap", "WARN", "text overlaps"), ("clip", "WARN", "text cut"), ("trunc", "WARN", "text truncated"), ("small", "WARN", "text under 11px")):
            for x in r[kind]:
                problems.append((level, slug, f"{tag}: {label}: {x}"))
                bad = bad or level == "ERROR" or kind in ("overlap", "clip", "trunc")
        if not r["notes"]:
            problems.append(("WARN", slug, f"{tag}: no speaker notes"))
        if a.shots:
            shots.append((f"{tag} {r['title'][:44]}", c.shot(d / f"{i + 1:02d}-{r['id']}.png"), bad))
    for e in sorted(set(c.errors)):
        problems.append(("ERROR", slug, e))
    # print mode: nothing plays, every slide settles; it must not throw
    c.errors.clear()
    c.open(base + f"{slug}.html?print", settle=1.5)
    for e in sorted(set(c.errors)):
        problems.append(("ERROR", slug, "?print: " + e))
    if a.shots and shots:
        print("  sheet:", sheet(shots, OUT / f"{slug}-sheet.jpg"))
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("decks", nargs="*")
    ap.add_argument("--no-build", action="store_true")
    ap.add_argument("--shots", action="store_true")
    ap.add_argument("--phone", action="store_true")
    ap.add_argument("--wait", type=float, default=2.5)
    ap.add_argument("--base")
    a = ap.parse_args()
    problems = []
    if not a.no_build:
        b = subprocess.run([sys.executable, "-B", "_src/build.py"], cwd=REPO, capture_output=True, text=True)
        if b.returncode:
            print("BUILD FAILED\n" + b.stdout + b.stderr)
            sys.exit(1)
    allslugs = [p.stem for p in sorted((REPO / "_src/decks").glob("*.html")) if p.stem != "index"]
    slugs = a.decks or allslugs
    unknown = [s for s in slugs if s not in allslugs]
    if unknown:
        sys.exit(f"unknown deck(s): {unknown}; decks: {allslugs}")
    static_checks(slugs, problems)
    with serve(base=a.base) as base:
        with Chrome(1600, 900) as c:
            for slug in slugs:
                n = check_deck(c, base, slug, a, problems)
                print(f"  {slug:22s} {n:2d} slides checked")
        if a.phone:
            with Chrome(390, 844, mobile=True, touch=True) as c:
                for slug in slugs:
                    c.errors.clear()
                    c.open(base + f"{slug}.html", settle=1.5)
                    if not c.ev("document.querySelector('.deck').classList.contains('is-rotated')"):
                        problems.append(("ERROR", slug, "phone held upright: the deck did not turn"))
                    for i in range(c.ev("Deck.slides.length")):
                        c.ev(f"Deck.go({i}, -1)")
                        c.sleep(.6)
                    for e in sorted(set(c.errors)):
                        problems.append(("ERROR", slug, "phone: " + e))
    errs = [p for p in problems if p[0] == "ERROR"]
    for p in sorted(problems, key=lambda p: (p[0] != "ERROR", p[1])):
        print(f"{p[0]:5s} {p[1]}: {p[2]}")
    print(f"\n{len(slugs)} deck(s): {len(errs)} error(s), {len(problems) - len(errs)} warning(s)" + (" -> FAIL" if errs else " -> PASS (look at the warnings and the sheets)"))
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
