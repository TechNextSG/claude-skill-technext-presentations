# -*- coding: utf-8 -*-
"""Launcher thumbnails for a deck (the repo has no generator of its own):

  assets/img/thumbs/<deck>.jpg      960x540   the cover, finished
  assets/img/thumbs/<deck>-og.jpg   1200x630  share image (cover at 1200x675, crop y 22..652)
  assets/img/thumbs/<deck>-2.jpg    960x540   the launcher's hover picture: one slide, finished

    python thumbs.py odoo-crm                 # cover + og + the deck's usual hover slide (HOVER below)
    python thumbs.py odoo-crm --hover 9       # hover = slide 9 (1-based), all builds shown
    python thumbs.py odoo-crm --hover 0       # cover and og only
    options: --wait 6 (seconds the hover slide plays before the shot; a long demo needs more, e.g. Hitachi 05 = 14)

Re-shoot whenever a cover or the hover slide changes, then bump ASSET_V in _src/build.py and rebuild.
LOOK at the three files before committing."""
import argparse, pathlib, sys, tempfile, time

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _cdp import REPO, serve, Chrome  # noqa: E402
from PIL import Image  # noqa: E402

# the hover slide each deck used on 2026-10-04 (1-based); keep it unless the user asks for another
HOVER = {"company-profile": 3, "portfolio": 2, "service-showcase": 4, "marketing-showcase": 2, "what-is-odoo": 9,
         "odoo-accounting": 4, "odoo-sales": 6, "odoo-crm": 9, "hitachi-elevator-ph": 5, "erp-tiers": 2, "marketing-tiers": 2,
         "jrtech-odoo-erp": 2,
         "bhdasia-odoo-scope": 5, "hst-medical-website": 4}
WAIT = {"hitachi-elevator-ph": 14}
Q = dict(quality=86, optimize=True, progressive=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("--hover", type=int)
    ap.add_argument("--wait", type=float)
    ap.add_argument("--base")
    a = ap.parse_args()
    th = REPO / "assets/img/thumbs"
    hover = HOVER.get(a.deck, 2) if a.hover is None else a.hover
    wait = a.wait or WAIT.get(a.deck, 6)
    tmp = pathlib.Path(tempfile.mkdtemp())
    with serve(base=a.base) as base, Chrome(1600, 900) as c:
        c.call("Network.enable"); c.call("Network.setCacheDisabled", cacheDisabled=True)
        c.open(base + f"{a.deck}.html?cb={int(time.time())}", settle=3.2)
        c.images_loaded()
        cover = c.shot(tmp / "cover.png")
        if hover:
            c.ev(f"Deck.go({hover - 1}, -1)")
            c.sleep(wait)
            c.images_loaded(f"Deck.slides[{hover - 1}]")
            c.ev("document.querySelector('.ui').classList.add('is-idle')")
            second = c.shot(tmp / "hover.png")
        if c.errors:
            print("script errors while shooting:", *sorted(set(c.errors)), sep="\n  ")
    im = Image.open(cover).convert("RGB")
    im.resize((960, 540), Image.LANCZOS).save(th / f"{a.deck}.jpg", **Q)
    im.resize((1200, 675), Image.LANCZOS).crop((0, 22, 1200, 652)).save(th / f"{a.deck}-og.jpg", **Q)
    out = [f"{a.deck}.jpg", f"{a.deck}-og.jpg"]
    if hover:
        Image.open(second).convert("RGB").resize((960, 540), Image.LANCZOS).save(th / f"{a.deck}-2.jpg", **Q)
        out.append(f"{a.deck}-2.jpg")
    for n in out:
        p = th / n
        print(f"  {p}  {Image.open(p).size}  {p.stat().st_size // 1024} KB")
    print("Now: LOOK at them, bump ASSET_V in _src/build.py, python -B _src/build.py")


if __name__ == "__main__":
    main()
