# Build, share, print, ship

Everything runs from the clone at `~/ClaudeWork/technext-presentations`, with Python 3.12. The Python modules needed are `segno` (QR codes), `Pillow`, `pymupdf` and `websocket-client`. Chrome is at `C:\Program Files\Google\Chrome\Application\chrome.exe`. There is no Node on this PC.

## The build: `python -B _src/build.py [--prune]`

It turns every `_src/decks/*.html` into a root `*.html`, then writes each deck's share copy, then the launcher, which reads the built decks. These tokens are expanded:

| Token | Gives |
|---|---|
| `{{head}}` | the shared `<head>`: charset, viewport, `noindex,nofollow`, theme colour, favicons, font preloads, fonts.css and deck.css, all with `?v=` |
| `{{v}}` | `ASSET_V`; write `assets/x.css?v={{v}}` on every asset link |
| `{{og:slug}}` | Open Graph and Twitter tags from the page's own `<title>` and description. The image is `assets/img/thumbs/<slug>-og.jpg` |
| `{{icon:name}}` | an inline SVG from `_src/icons.json`. Unknown names fail the build |
| `{{odoo:module[:size]}}` | the official Odoo app icon `assets/img/odoo/<module>.svg` (default size 40) |
| `{{qr:key}}` | an inline QR SVG for `meet` (Odoo booking page), `whatsapp`, `site` or `odoo`. The links are in `QR` in build.py |
| `{{seamap:W:H}}` | the Southeast Asia dot map. `{{mapxy:sg\|ph\|vn:W:H}}` gives the office x,y for SVG; `{{mappx:…}}` gives `--x/--y` for HTML pins |
| `{{worldmap:W:H}}`, `{{worldxy:lon,lat:W:H}}` | the world dot map, from Europe to Japan and Australia (Portfolio) |
| `{{phmap:W:H}}`, `{{phxy:lon,lat:W:H}}`, `{{phpx:…}}` | the Philippines dot map (client proposals) |
| `{{apps_json}}` | `assets/apps.json`, the Odoo app catalogue (Odoo 20 names: Field Service in Planning, VoIP is "Phone") |
| `{{include:name}}` | `_src/partials/name.html`, up to 3 levels deep |
| `{{sc:*}}` | Marketing Showcase slides from `_src/showcase_data.py` + `_src/sites_meta.json` |
| `{{pf:*}}`, `{{scroll:slug:W:H[:m]}}`, `{{thumb:slug}}` | Portfolio pieces from `_src/portfolio_data.py`, and site pictures |
| `{{launcher}}`, `{{deck_count}}` | the launcher cards and the deck count in `index.html`. `WORDS` spells 1–10 ("Seven decks"); 11 or more prints as digits ("11 decks", live since the Odoo series) |

Any `{{…}}` left over fails the build. The build also appends `?v=ASSET_V` to every `assets/img/sites|thumbs/*.jpg`.

**`ASSET_V`** (in `_src/build.py`) is the cache version of every asset. Bump it by one whenever ANY file under `assets/` changes: CSS, JS, pictures, thumbnails, fonts or apps.json. It is 31 as of 2026-10-08 (78274bf). Client logos in `assets/img/clients/` are NOT auto-versioned: write `?v={{v}}` on their `src` and `data-cobrand` yourself. Mention the new value in the commit message.

## The launcher and the deck list

`DECKS` in `_src/build.py` is the launcher. It is a list of groups: "About TechNext", "What we build", "Odoo", "Client decks" and "Pricing". Each deck has `slug, tags, title, mins, pdf, alt, desc`: `tags` (odoo, ai, websites, marketing) drive the launcher's Topic chips, and each group needs a `GROUPS` entry (filter key + one-line blurb).

- A deck appears once its HTML is built.
- The slide count is read from the built file.
- The PDF button shows only when `pdf/<pdf>` exists.
- The hover picture shows only when `assets/img/thumbs/<slug>-2.jpg` exists.

The launcher source is `_src/decks/index.html`, with styles and script in `assets/index.css|js`. It includes the "Presenting tips" and "Presenting on a TV or projector" sections and "Save every deck for offline use". When the deck count or set changes, update the description `<meta>` in `index.html` and the README deck table (deck, file, slides).

## Share links

Each deck also builds as `s-<token>.html`. The tokens live in `_src/share.json`: the build creates a new deck's token and never changes an existing one. In the share copy, `data-home` becomes `data-shared`, so there is no Home button. Every `p`, `a`, `div` or `li` marked `data-internal` is removed, so there are no links to other decks.

- The build STOPS if a share copy still links to a deck or to the launcher. The fix is to mark that element `data-internal`.
- These URLs are in clients' hands (Hitachi: `s-vwagibj.html`). Never change a token unless the user asks to retire a link. Changing it deletes the old file.
- The site is public, so a share link hides the way to the other decks; it doesn't lock them.

## Site pictures (Marketing Showcase, Portfolio)

1. Capture full pages: `<slug>-d.jpg` at 1440 wide and `<slug>-m.jpg` at 390 wide.
   - Keep the viewport at its normal height and use `captureBeyondViewport` with a clip. Stretching the viewport to the page height blows up 100vh heroes.
   - Skip intros. Seek paused poster-less videos.
   - Force `dropdown-menu` / `sub-menu` hidden, because the capture can open a hover menu.
   - technext.asia needs a browser user agent.
2. Run `python -B _src/sites_images.py <capture folder>`. It writes every size to `assets/img/sites/` and merges them into `_src/sites_meta.json`, so a partial recapture keeps the other sites.
3. Run `python -B _src/build.py --prune` to delete the sizes no deck uses. A normal build fails on a missing picture.
4. Bump `ASSET_V`.

Print uses small top-only crops (`-dp`, `-mp`, `-wp`) through `data-psrc`.

## PDFs: `python scripts/deck_pdf.py <decks|--all> [--look]`

The script opens `<deck>.html?print` in headless Chrome, waits for every image (lazy ones too) and the fonts, then runs `Page.printToPDF` with `preferCSSPageSize`. It writes `pdf/<name from DECKS>` and checks that the page count equals the slide count.

- With `--look`, it renders the pages into `~/ClaudeWork/qa/decks/<deck>-pdf.jpg`. Compare that sheet with the live end states.
- A half-built page means a missing `settle` hook.
- Known print gotchas:
  - Chrome's PDF output ignores CSS `filter`, so dark slides use the white logo PNG.
  - `repeating-linear-gradient` gridlines print as striped bars, so use real 1px elements (`.px-gl`).
  - `h0` dots vanish, so use `h.01`.
- Reprint every deck whose visible content changed, including when a shared fact changed.
- The older tool `~/ClaudeWork/qa/deck_pdf.py <url> <out.pdf>` does the same for one URL.

## Thumbnails: `python scripts/thumbs.py <deck> [--hover N] [--wait S]`

| File | Size | What |
|---|---|---|
| `assets/img/thumbs/<slug>.jpg` | 960x540 | the cover, finished (3.2 s after load) |
| `assets/img/thumbs/<slug>-og.jpg` | 1200x630 | the share image: the cover at 1200x675, cropped to y 22..652 |
| `assets/img/thumbs/<slug>-2.jpg` | 960x540 | the launcher's hover picture: one finished slide |

The hover slides as of 2026-10-04 are in the table below. The script uses them by default.

| Deck | Hover slide |
|---|---|
| company-profile | 3 (offices) |
| portfolio | 2 (map) |
| service-showcase | 4 (crm) |
| marketing-showcase | 2 (gallery) |
| what-is-odoo | 9 (w2) |
| odoo-accounting | 4 (mv2) |
| odoo-sales | 6 (mv4) |
| odoo-crm | 9 (mv7) |
| hitachi-elevator-ph | 5 (breakdown, `--wait 14`) |
| erp-tiers | 2 (tiers) |
| marketing-tiers | 2 (tiers) |
| jrtech-odoo-erp | 2 (solution) |
| bhdasia-odoo-scope | 5 (w1, the client record filled) |
| hst-medical-website | 4 (site: the website page by page) |

Reshoot when a cover or a hover slide changes, then bump `ASSET_V` and rebuild. LOOK at all three files.

## Ship

```bash
cd ~/ClaudeWork/technext-presentations
git status --short                      # only your files; .claude/ .impeccable/ DESIGN.md PRODUCT.md stay untracked
git add _src/... assets/... <root html> s-*.html pdf/... README.md    # explicit paths, never -A
git commit -m "<Deck>: <what changed, in plain words>" -m "<why / details; ASSET_V n; PDFs reprinted>" -m "Co-Authored-By: ..."
git push
```

- **Commit style:** the subject is a plain sentence naming the deck and the change (for example "Office roles: the Philippines is the main development and consulting hub, Vietnam is AI engineering"). The body says what moved, which PDFs and thumbnails were redone, and the new `ASSET_V`.
- **Commit identity:** the clone is set to `TechNext Marketing <hello@technext.asia>` and pushes to `https://github.com/TechNextSG/technext-presentations.git`. If a push is rejected, run `git pull --rebase`, rebuild, and push again. Never force-push.
- **Pages:** `.github/workflows/pages.yml` deploys `main` in about 30 s. Check with `gh run list -R TechNextSG/technext-presentations -L 1`, then `curl -s -o /dev/null -w "%{http_code}" https://technextsg.github.io/technext-presentations/<deck>.html`, and grep the live HTML for the change.
- **Build after the PDF:** the launcher's PDF button appears only when `pdf/<name>` exists at build time.
- **Cache:** Pages caches HTML for 10 minutes. Give the user `…/<deck>.html?v=<ASSET_V>#<slide>` links, or tell them to hard-refresh.
- **Drive:** run `python scripts/drive_sync.py` (it copies and md5-verifies; `--check` only verifies). It lists Drive files the repo no longer has and never deletes them.

## Local preview

- **Port 3970 can be held by another chat's `technext-decks` server**, which this session's browser can't reach and must not stop. Use `technext-decks-2` (port 3988, same clone) from the Marketing `.claude/launch.json` (the file has a UTF-8 BOM: read it with `utf-8-sig`, keep the BOM when writing). The scripts take `--base http://127.0.0.1:3988/`.

- Start it with `preview_start {name: "technext-decks"}`, which serves the clone at http://localhost:3970/. Keep the changed slide fronted for the user (`/<deck>.html#<n>`).
- Never start servers with Bash. The scripts serve the repo themselves on a free port.
- `sw.js` never registers on localhost, so a local preview is always fresh. Still, reload after every build (a cached tab can show the old slide count: add `?nc=` to the URL).
- **The local servers (preview and the scripts) are Python SimpleHTTP: no byte ranges.** A video plays locally but cannot seek. Test seeking, chapters and the offline copy on the live site in headless Chrome (`qa/jrtech-deck/live_video_test.py`, `sync_test.py`: open the presenter page with `Target.createTarget(..., newWindow=True)`, or Chrome defers media in the background tab).
