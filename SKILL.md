---
name: technext-presentations
description: Edit, add, fix, redesign or audit TechNext's interactive HTML presentations in the repo TechNextSG/technext-presentations (live, unlisted, at technextsg.github.io/technext-presentations). The decks are the company profile, portfolio, service showcase, marketing showcase, What is Odoo, the Odoo app series (Accounting, Sales, CRM), the ERP and marketing tier lists, client decks (Hitachi Elevator Philippines, JR-Tech Solution, BHD Asia · HummingBeing, HST Medical) and the launcher page. Covers the 1600x900 deck engine (builds, settle hooks for print, phone rotation, TV mode, presenter view), the Python build and its tokens, share links, PDFs, launcher thumbnails, the Drive mirror, TechNext's content and fact rules, and a QA gate. Use whenever the user asks to change, update, add, remove, check or reprint a TechNext presentation, deck, slide, proposal deck, PDF or the presentations launcher, including "edit all the presentations".
---

# TechNext presentations

TechNext presents from interactive HTML decks: every map, pipeline, Odoo screen and AI demo works when clicked. The decks are a fixed 1600 x 900 stage that scales to any screen. A Python build expands the sources into the HTML at the repo root. GitHub Pages serves them. They also exist as share links, PDFs and a Drive copy.

| What | Where |
|---|---|
| Live (unlisted, `noindex`) | https://technextsg.github.io/technext-presentations/ (the launcher lists every deck) |
| Repo | `TechNextSG/technext-presentations` (public, branch `main`; Pages deploys via Actions in about 30 s) |
| Local clone (work here) | `~/ClaudeWork/technext-presentations` |
| Preview | launch config `technext-decks`, port 3970 (serves the clone) |
| Drive copy for the team | `G:\Shared drives\Marketing\00. TechNext Folder\07. TechNext Presentations\HTML Presentations\` |
| Memory | `project_technext_html_presentations.md` (+ `project_hitachi_proposal.md` for the proposal) |
| Design context | `DESIGN.md` and `PRODUCT.md` in the clone (impeccable's design system notes; untracked, local only) |
| This skill's tools | `~/.claude/skills/technext-presentations/scripts/` (written `scripts/` below): `deck_check.py` (QA gate), `deck_pdf.py`, `thumbs.py`, `drive_sync.py`. Each serves the repo itself; `--base http://127.0.0.1:3970/` reuses the preview |

## Before anything else

1. **Read** `reference/content-rules.md` (what may be said), then `reference/lessons.md` (what went wrong before: don't repeat it), then `reference/engine.md` (how a slide works) and `reference/build-and-ship.md` (the commands). For one deck, read its section in `reference/decks.md`. For a common job, follow `reference/recipes.md`.
2. **Sync:** `git -C ~/ClaudeWork/technext-presentations pull --ff-only`. Parallel chats edit this repo too (the Odoo app series came from one). Never reset or overwrite their work.
3. **Know the state:** run `python -B _src/build.py` once, check that `git status` is clean, and run `python scripts/deck_check.py <deck> --shots` on the decks you will touch. That is your before-picture.
4. **Facts come from the live sources.** The company facts come from technext.asia. Odoo facts come from the Odoo 20 release notes and the 20.0 docs. A client's facts come from the client's own public pages. Never invent a figure, a client or a price.

## The pipeline

1. **Plan the change.** Name the decks and slides it touches. Then find every other place the same fact or element lives: other decks, `_src/*_data.py`, the partials, the launcher `DECKS` list in `_src/build.py`, the README tables, speaker notes, PDFs and share copies. A change that applies to one deck usually applies to all of them ("apply every change to ALL pages"). `grep -rn "<old text>" _src assets README.md` is the start.
2. **Edit the sources only.** Edit `_src/decks/*.html`, `_src/partials/`, `_src/*_data.py`, `assets/*.css|js` and `_src/build.py`. The root `*.html` and `s-*.html` files are generated, so never edit them by hand. Follow the slide grammar in `reference/engine.md`. Copy the closest existing slide instead of starting blank.
3. **Build.** Run `python -B _src/build.py`. It fails on an unknown token, icon or Odoo icon, a missing site picture, or a share copy that still links to another deck. Fix the cause, never the check.
4. **Bump ASSET_V.** Raise `ASSET_V` in `_src/build.py` by one whenever any file under `assets/` changes (CSS, JS, pictures, thumbnails), then build again. Without the bump, browsers and offline copies keep the old file.
5. **Look in the preview.** Open `technext-decks` on port 3970 at the changed slide (`/<deck>.html#<n>`) and keep that tab in front for the user. Step through every build with the arrow key. Check the overview (`O`), the speaker notes (`N`), a phone held upright and `?print`.
6. **QA gate.** Run `python scripts/deck_check.py <decks> --shots`. Every ERROR must be fixed. Look at every WARN in the slide's shot, and either fix it or say why it is fine. Look at the contact sheet `~/ClaudeWork/qa/decks/<deck>-sheet.jpg`. The script cannot judge design, so you must. Then run `reference/qa-checklist.md`.
7. **Reprint and reshoot.** Run `python scripts/deck_pdf.py <decks> --look` after any visible change, and compare the PDF sheet with the live end states. Run `python scripts/thumbs.py <deck>` when the cover or the launcher's hover slide changed. A thumbnail change means another `ASSET_V` bump and build.
8. **Ship.** Commit only your files, push, and prove the change is live.
   - Stage the files explicitly. Never use `git add -A`: `.claude/`, `.impeccable/`, `DESIGN.md` and `PRODUCT.md` stay untracked.
   - Commit with the house style (`reference/build-and-ship.md`) and `git push`.
   - Wait for the Pages run, then check that the live deck returns 200 and contains the change.
   - Give the user `?v=<ASSET_V>` links, because Pages caches HTML for 10 minutes.
9. **Mirror to Drive.** Run `python scripts/drive_sync.py`, which copies and md5-verifies the files. Report any extra files in Drive, but don't delete them.
10. **Report and train.** Give a status table (deck, slides, what changed, PDF, live check). Then update this skill (see below). This step is not optional.

## Non-negotiables (the user's words where they set the rule)

| Rule | Source |
|---|---|
| Every deck is "highly interactive and animated" and in technext.asia branding. Demos run live on labelled sample data. No static screenshot slides, except the site pictures in the showcases. | first brief, 2026-09-27 |
| A test link comes first. The site stays `noindex` and unlisted, and nothing is linked from a public page without the user's sign-off. | feedback_test_link_before_publish |
| Website work is not done until it is pushed and the live URL is verified with a 200. | feedback_push_and_url |
| "Apply every change to ALL pages". A fact, name, price or style change goes to every deck, note, PDF and share copy. Prove with grep that zero old values remain. | feedback_apply_to_all_pages |
| Phones must auto-rotate: the deck turns 90° when the phone is held upright. Slide scripts read positions only through `Deck.rect(el)` and `Deck.point(e)`. | 2026-09-28 |
| "PDFs must show every slide finished". Print never plays a slide, so every slide whose finished state comes from JS needs a `settle` hook. | 2026-09-28 |
| Approved figures only: 10+ countries, 11+ enterprise clients, 4 AI disciplines, 3 offices. Always "Odoo Ready Partner", never "certified". NDA clients are counted, never named. | content rules |
| Office roles (Pia Cachola, 30 Sep 2026): Singapore is the HQ (sales, discovery, on-site work). The Philippines (Taguig City) is the main development and consulting hub. Vietnam (Ho Chi Minh City) is mainly AI engineering. Never call Vietnam "the development hub". | 4f6d41d |
| Tier decks have THREE tiers only. ERP: Essentials · Growth · Enterprise. Marketing: Launch · Growth · Brand. Every price is TechNext's service fee ("On quotation"), not the Odoo licence or ad spend. | afc611d |
| Portfolio: no clients x services matrix, no "proposals, concepts and paused work" slide, and no dates in client lists. Don't reintroduce them. | 2026-09-30 |
| Blue Moon Secret's Chamber and Tri-Comp Solutions are out of the Marketing Showcase. | 2026-10-02 |
| Proposals use only the client's own public facts. Pain points are hypotheses. Job ads, reviews and headcount guesses never go in the deck, notes included. Sample data is labelled. | Hitachi proposal |
| Launcher card actions (Present, Kiosk loop, PDF, Share) sit on ONE row of small buttons. | 2026-09-28 |
| A video in a deck zooms with the deck's own zoom and controls, never the browser's video full screen, and comes back into the slide with the deck still in full screen. | JR-Tech, 2026-10-06 |
| A client's discovery questions go "at the back": the last part before the closing slide, as tick buttons (answered / follow up) with a copyable follow-up list. | JR-Tech, 2026-10-06 |
| A client deck made from an internal "for team review" document is client-facing by default: keep the facts and open items, leave out what was said about the client, and offer a team-only version. | BHD Asia, 2026-10-06 |
| "Properly showcase the logo": the client's official lock-up large on the cover, a legible crop in the header, a white tile on dark slides; animate only the untouched file, never recolour it. | HST Medical, 2026-10-07 |

## Train the skill after every job (the loop)

1. **Log** a dated entry in `reference/lessons.md`: what changed, what went wrong, why, and the fix. Quote the user's feedback verbatim when it set a rule.
2. **Promote** each new rule. A content rule goes to `reference/content-rules.md`. A user rule also goes to the Non-negotiables table above. An engine or build change goes to `engine.md` or `build-and-ship.md`. A new or changed slide goes to its deck's section in `decks.md`. A repeatable job goes to `recipes.md`.
3. **Automate** a check that was missed twice, or that the user had to point out: extend `scripts/deck_check.py`, and prove it catches the bad case.
4. **Publish** the skill:
   - Run `python ~/ClaudeWork/technext-claude-skills/tools/build_skills.py --push` (pushes this skill's repo and the Claude Skills site).
   - Check that https://technextsg.github.io/technext-claude-skills/ returns 200.
5. **Remember:** update `project_technext_html_presentations.md` (the deck list, the last commit, `ASSET_V`, anything decided).

## Last step: update the repo (owner rule, 2026-10-11)
Every time this skill is used, and after any lesson or rule is added to it, finish with
`python ~/ClaudeWork/technext-claude-skills/tools/build_skills.py --push`. It mirrors this folder to its own public repo
https://github.com/TechNextSG/claude-skill-technext-presentations and rebuilds https://technextsg.github.io/technext-claude-skills/
(it only commits what changed). Report the repo commit in the status, or the error if the push failed.
