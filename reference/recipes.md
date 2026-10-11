# Recipes: the common jobs

Every recipe ends with the pipeline's steps 3–10: build, ASSET_V, preview, `deck_check`, PDFs and thumbnails, ship, Drive, report and train.

## Change a fact, name, number or wording everywhere ("apply to all")
1. `grep -rn -i "<old>" _src assets README.md`. Also search close variants: plural, capitalised, with or without a hyphen, and the short form.
2. Change every source hit: deck HTML, notes, `*_data.py`, partials, JS strings, `DECKS` descriptions in build.py, and README tables or rules.
3. Build, then `grep -rn -i "<old>" *.html s-*.html`. It must return ZERO. Paste that proof in the report.
4. Reprint the PDFs of every deck that changed (`deck_pdf.py <decks> --look`). Reshoot thumbnails if a cover or hover slide shows the fact.
5. Add the fact to `content-rules.md`.

## Edit one slide
1. Find it: `grep -n 'id="<id>"' _src/decks/<deck>.html`. Its script is `Deck.on('<id>'` in `assets/<deck>.js`, and its styles use the slide's prefix in `assets/<deck>.css`.
2. Keep the grammar: a kicker → `.h-m` with one `.hl` → `.lead`, staggered `data-in`, and notes.
3. If the slide animates from JS, check that `settle` still paints the finished state. Test with `?print` and the overview `O`.
4. Preview at `/<deck>.html#<n>`, step through every build, then hold a phone upright (`resize_window` mobile).

## Add a slide
1. Copy the closest slide in the same deck (or another deck) and give it a new unique `id` and a `data-title`.
2. Add its hooks (`init`/`enter`/`step`/`settle`), using `ctx` for every timer and listener, and its styles with a fresh prefix (grep first).
3. Slide numbers shift. Update the README slide count and any "slide n" text (the tier decks compute theirs). Check the hover slide in `scripts/thumbs.py` `HOVER`.
4. Add a decorative infinite animation to deck.css's `.deck.is-tv` list.

## Remove a slide
1. Delete the `<section>`, its `Deck.on` hook, its styles (unless shared: the `proposal.css` kit keeps its chart styles for future proposals) and any build step only it used.
2. Re-sequence the entrance timings and numbering on neighbouring slides when they referred to it.
3. Update the README count, `decks.md`, and any `data-go` jump that pointed at it. Reprint the PDF and recheck the hover thumbnail.
4. Log the removal as a user decision in `lessons.md` and `decks.md`, so nobody brings it back.

## Add a new deck
1. Write `_src/decks/<slug>.html` from the closest deck (head, body `data-label` + `data-home="./"`, `{{og:<slug>}}`), plus `assets/<slug>.css|js`.
2. Add it to `DECKS` in `_src/build.py` (group, slug, title, mins, pdf, alt, desc). The build creates its share token in `_src/share.json`.
3. Mark any link to another deck `data-internal`.
4. Run `thumbs.py <slug> --hover N`, `deck_pdf.py <slug>`, bump ASSET_V and build.
5. Add it to the README deck table, update the launcher's description meta, and add it to `decks.md` and `thumbs.py` `HOVER`.
6. Run `deck_check.py <slug> --shots --phone`.

## A new client sales proposal
1. Read the client's requirements file and verify every public fact on the client's own sites (note the date). Keep internal research out.
2. Copy `hitachi-elevator-ph` as the frame: cover with a lockup, what we understand, pressure points (hypotheses), architecture, 4–7 workflow demos on labelled sample data, scope in the client's phases, roadmap, contact.
3. Add `data-cobrand` logos (`assets/img/clients/<client>.png` + `-white.png`, from the client's official files or the user's upload).
4. Use `proposal.css|js` (PX charts with validated palettes, `.px-gl` gridlines, `PX.svgAt` for SVG hover) and write `assets/<client>.js`, with a settle hook on every animated slide.
5. Add it to the "Client decks" group, then send the share link (never the launcher), after the user's sign-off.
6. Write a memory file for the proposal (phases, decisions, the share link).

## A client deck from TechNext's own presentation material (JR-Tech, 2026-10-06)
1. Extract the PDF: `pymupdf` text per page and 48 dpi contact sheets (the Read tool refuses PDFs over 100 MB). List every slide's claims.
2. Map one source slide to one deck slide; give each one interaction that proves its point. Keep the source's wording; fix template leftovers and the house rules (contact, partnership).
3. Client logo: the official file (the client's site repo) for dark slides; the light variant the source deck uses for white slides. Crop to the bounding box, 80px tall.
4. Questions or a checklist from the client: the last part before the close, as tick buttons kept in `sessionStorage`, with counters and a copyable follow-up list (see `jrtech.js`).
5. Prefix every class with one letter not used by deck.css or proposal.css (`grep -ho "\.j[a-z]-" assets/deck.css assets/proposal.css`).
6. Then the "Add a new deck" steps: `DECKS` (Client decks group), README row, `thumbs.py` HOVER, PDF, build again, `deck_check --shots --phone`.

## A client deck from an internal scope document (BHD Asia, 2026-10-06)
1. The Read tool can't render PDFs on this PC (no pdftoppm): extract text with `pypdf` and `PYTHONIOENCODING=utf-8` (the console codepage chokes on the minus sign, ™ and arrows).
2. Decide the audience: client-facing by default; strip the internal remarks (content-rules). Turn "open items" into the questions-at-the-back slide with owner chips.
3. One slide per workflow on the shared `flow()` engine; one interaction each (a toggle that changes the path, a button that performs the step).
4. Logos: look in the client's production folders (`00. Client Folder\08. BHDasia (production)`, `09. HummingBeing (production)\Website\images`) and crop to the bounding box; drop a tagline the deck can't read at 40px.
5. Then "Add a new deck" (DECKS in the Client decks group, README row, launcher meta description, thumbs HOVER, PDF, build again).

## The client sends a revised source document ("update the scope")
1. Extract the new text (`pypdf`, `PYTHONIOENCODING=utf-8`), save it to the scratchpad, and compare it section by section with the text the deck was built from. List what changed before editing; say in the report that the rest was word-for-word the same.
2. A rewritten workflow: rebuild its slide on the `flow()` engine; when the source adds a "why" paragraph, give it its own slide instead of cramming it into the scene.
3. A decision that was open and is now settled: change its slide from "decide" to "settled" (with the date), take it off the open list and show it as settled on the open-items slide and the decided slide. Update counters, the copy text, the jump links and the workflow map.
4. Renumber the `<!-- n · -->` comments, update the README count, decks.md, the DECKS description; bump ASSET_V, reprint the PDF (the page count must match), build again.

## Add or recapture a site (Marketing Showcase / Portfolio)
1. Add or edit the entry in `_src/showcase_data.py` (LIVE / CONCEPTS / MORE / PITCH) and/or `_src/portfolio_data.py`. Every URL must return 200.
2. Capture `<slug>-d.jpg` (1440 wide) and `<slug>-m.jpg` (390 wide). See the capture rules in build-and-ship.
3. Run `python -B _src/sites_images.py <capture dir>`, then `python -B _src/build.py --prune`, then bump ASSET_V.
4. Check the gallery wall: its columns are chosen so every row is full (`mz_layout`).

## Change the tiers
1. Edit BOTH `erp-tiers.html` and `marketing-tiers.html`: the cards, explorer, finder `min` indexes, add-ons and the cover lines.
2. If the tier count changes, the finder's `min` values and the explorer data must follow. `tiers.js` reads the count from the cards.
3. Prices stay "On quotation" and service fee. Keep the note under the cards.

## Retire a share link (only when the user asks)
Change that deck's token in `_src/share.json` and build. The old `s-*.html` is deleted. Tell the user that the old link is now dead for everyone who has it.

## Edit all the presentations (a sweep)
1. List the change per deck in a table first (deck, slides, change). Agree it with the user if it is a content call.
2. Work deck by deck, building after each. Run `deck_check.py` on all decks at the end, plus `deck_pdf.py --all --look`.
3. One commit per logical change (not per deck), so each can be reverted alone.
4. Thumbnails for every changed cover or hover slide, and a single ASSET_V bump at the end is enough if nothing shipped in between.
5. Report a status table for all 11 decks, even the untouched ones ("no change").

## A client deck for a website project (HST Medical, 2026-10-07)
1. Collect what TechNext built: the client's numbered folders under `00. Client Folder` (site, flip-book, research), local repos in `~/ClaudeWork/<client>-*`, and any RFP or brief in Downloads. Delegate the folder survey to an Explore agent and read the engine docs meanwhile.
2. Verify the client's facts on its own live site (date them); keep TechNext's internal research out.
3. Capture the live test links (1440 desktop, 390 phone, reveals forced visible, intros skipped) and run `_src/sites_images.py`; show them as tabbed browser + phone scroll frames (`showcase.css|js`).
4. Probe any on-site assistant for its real answers (headless Chrome, its own JS API) instead of writing them.
5. Logo: the official file large on the cover, a legible crop in the header, a white tile on dark (content-rules).
6. Agenda items become parts; "review feedback" becomes a live capture board; questions at the back with a copy list that also carries the feedback.
7. Then "Add a new deck" (DECKS, README, launcher meta, thumbs HOVER, PDF, build again, `--prune`).

