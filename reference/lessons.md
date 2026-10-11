# Lessons log

Add a dated entry after every presentation job, with the newest at the bottom and one bullet per lesson. Quote the user verbatim when they set a rule. When a lesson becomes a rule, add it to `content-rules.md`, `engine.md` or the SKILL.md Non-negotiables table.

## 2026-09-27/28 · First three decks and the launcher (f86021b)
- **User:** "create a powerpoint presentation html base on technext website branding… highly interactive and animated… different html file". The first decks were the company profile, the service showcase, and What is Odoo with a lead-to-cash walkthrough.
- **The engine was built once and shared:** a 1600x900 stage, builds, overview, notes, kiosk and print. Each deck has its own CSS and JS. Pages deploy via Actions, because the legacy Pages builder wedges.

## 2026-09-28 · Leaving a deck glitched (dda7122)
- Esc opened the overview, and in full screen the browser also uses Esc to exit, so the two fought. **Esc now only closes things.**
- Opening the overview, or going Home, flew every slide across the stage. **The stage now fades out, swaps, and fades back in** (`is-fading` + `no-anim`).
- Hover lifts on cards shook when the pointer rested on an edge. **No hover lifts.**

## 2026-09-28 · More decks: tiers, portfolio, showcase; phones; print (12bdd0f, cfe0f3e)
- **User:** "add more presentation". Added the ERP and Marketing tier lists, the Portfolio (from the Drive client folders, repos and sessions) and the Marketing Showcase (every live site and mockup).
- **User:** phones must auto-rotate. The whole deck turns 90° when held upright. Every position read had to go through `Deck.rect`/`Deck.point`, or drags and hovers missed by 90°.
- **User:** PDFs must show every slide finished. **Print never plays a slide**: `settleAll` paints every build and runs every `settle` hook. Six slides printed half-done until they got settle hooks: the engagement steps, the CRM board, the customisation answer, the integration counters, the tier finder and the plan builder. The overview reuses the same hooks.
- **Site captures:** keep the real viewport height and use `captureBeyondViewport`, because resizing to the page height stretched 100vh heroes. Skip intros, and seek paused poster-less videos.
- **Print ignores CSS `filter`,** so dark slides need the white logo PNG. `h0` dots vanish in PDF, so use `h.01`.

## 2026-09-28 · Share links and the launcher card row (79093a1, ff87a2a)
- **The need:** send one deck without the way to the others. Each deck builds as `s-<token>.html`: no Home button, `data-internal` links stripped, and the build exits if a leak remains.
- **User:** the card actions go on ONE row of small buttons (13px, 33px tall, nowrap). A size container hides the icons, then "loop", then padding as the card narrows.

## 2026-09-28 · Sales proposals: Hitachi Elevator Philippines (725c1fd, 017a416, 4ec5532)
- **User:** "create a sales proposal category base on client requirements… highly animated workflow, chart". It was built from the pre-discovery analysis, using only HEP's public facts. The pains are hypotheses and every demo is labelled sample data.
- **The user set the phases;** PH2 is "to confirm" because it depends on GERP. Inventory and AI were dropped. The Hitachi logo sits beside TechNext's (`data-cobrand`).
- **Chart gridlines drawn with `repeating-linear-gradient` printed as striped bars.** They are now real 1px elements (`.px-gl`).
- **SVG hover:** `Deck.lbox` is HTML-only and gives NaN on SVG, so use `PX.svgAt` (getScreenCTM).
- **The cover connector** started 70px below the labels and the Makati shaft touched the top edge. Measure after every layout change.

## 2026-09-28 · Odoo 20 everywhere (017a416)
- **User:** "technext presentation also need to be fully updated… mention about odoo 20". Added the "Odoo 20, in six changes" slide. The catalogue now says Field Service runs in Planning and VoIP is Phone, and the kickers say "odoo 20". Facts come only from the release notes.

## 2026-09-30 · Removals the user asked for (d5937c1, 65562c3, 3328e3a)
- **Portfolio:** the clients x services matrix is gone. Client lists are plain bullets with NO dates. The "Proposals, concepts and paused work" slide is gone.
- **Hitachi:** slide 3 lost the parts point and the Inventory and Purchase cards ("Five places…"). The parts slide and the "Five questions" slide were removed (16 → 14 slides).
- **After a removal:** re-sequence the entrance timings, reprint the PDF, recapture the hover thumbnail if its page number moved, and bump ASSET_V.

## 2026-09-30 · Office roles (4f6d41d)
- **Per Pia Cachola:** the Philippines (Taguig City) is the main development and consulting hub, and Vietnam (Ho Chi Minh City) is AI engineering. This touched the office cards, map labels, notes, the who-we-are lead, the engagement slide and the service showcase Build phase.
- **One fact, many places.** Grep every deck, note and README rule.

## 2026-09-30 · Tier decks to three tiers (afc611d)
- **User:** three tiers only. Starter folded into Essentials (ERP) and Launch (marketing). Enterprise and Brand are "customisation", and add-ons are the customisation layer.
- **Every price is TechNext's service fee.** Say so on the slide. The code follows the tier count.

## 2026-09-30 · Smooth on TVs, then a Display option (e7ed568, d5eed94)
- **At 4K the decks stuttered.** Causes: about 30 loops on hidden slides kept ticking; 90px blur glows; backdrop blur. Fixes: pause every animation off the current slide, use radial-gradient glows, drop backdrop blur, and promote scroll pictures to a GPU layer only on screen. The company profile at 4K with a 4x CPU throttle went from 63 to 121 fps.
- **The Display menu:** `T` cycles HDMI (full), Wi-Fi/casting (less motion) and Auto. **Any new decorative loop must join the `.is-tv` stop list.**

## 2026-10-02 · Present anywhere (7891853, c421adf)
- **An audit of real set-ups:** cable, casting, screen share, the TV's own browser, a Bluetooth clicker, no internet. It added:
  - the presenter view (`P`, BroadcastChannel sync);
  - clicker keys: B and `.` black, W and `,` white, F5 for full screen;
  - Wake Lock, and a hidden cursor;
  - `sw.js` offline copies (live https only);
  - self-hosted fonts;
  - `inset` spelled out for 2020–21 TV browsers.

## 2026-10-02 · Showcase refresh; the Odoo app series (9987823, 428c0c8)
- **Showcase:** five sites were recaptured after their redesigns. **User:** remove Blue Moon and Tri-Comp. The wall picks a column count so every row is full. Pictures carry `?v=`, so offline copies refresh. `sites_images.py` now merges, so a partial recapture keeps the rest.
- **A parallel session** built the Accounting, Sales and CRM decks with the impeccable and web-design-engineer skills. The structure is one live Odoo window held across seven cut slides (`data-group`). One sample company, Kestrel & Pine, runs through all three. Labels follow the 20.0 docs. DESIGN.md and PRODUCT.md came from that work.
- **A capture can open a hover menu** (HummingBeing's Services). Force dropdowns hidden while capturing.

## 2026-10-03 · TRE in Singapore's live domain (c428d9f)
- The Showcase and the Portfolio still showed the old test address after the site moved to `tre-in-singapore.com`. **When a client site changes its domain, grep the decks.**

## 2026-10-04 · This skill
- **User:** "check the skils in the presentation https://technextsg.github.io/technext-presentations/, later on i will edit all the presentation. make sure the capture the skills for this".
- **The skill captures** the engine, the build, the 11 decks, the content rules, the design system (condensed from the untracked DESIGN.md) and this history. Four tools came with it: `deck_check.py` (QA gate), `deck_pdf.py`, `thumbs.py` and `drive_sync.py`. The thumbnail and Drive scripts used to live only in an old scratchpad.
- **Baseline QA:** 0 errors and 16 warnings across 11 decks. The list is in `decks.md` ("Baseline QA"). `deck_check` first called an ellipsis a "cut", so it now reports `text-overflow: ellipsis` as "text truncated" by name. The checker was proven on planted defects (off-stage text, overlap, tiny text, a broken image), and `thumbs.py` reproduced the committed thumbnails (mean pixel difference under 1).
- **The gap to close in the next edit:** technext.asia added a fourth practice, Technology (IoT · Apps · Networks), on 2026-10-03. The decks still show three practices and "fourteen services".

## 2026-10-06 · JR-Tech Solution client deck (5d80e2e)
- **User:** "create Presentation JR Tech https://technextsg.github.io/technext-presentations/ use this material, question at the back", then attached `JRTech-Accounting-and-Billing-Questions.pdf`: "add this", "at the end of presentation". So "question at the back" meant the client's discovery questions as the last part of the deck, before the close. When a short instruction is ambiguous, wait a moment for the rest; this user often sends the material in a second message.
- **A 100 MB PDF** can't be read by the Read tool (limit 100 MB): extract text with `pymupdf` (`page.get_text()`) and render 48 dpi contact sheets of four pages to look at the design.
- **Make the material work, don't transcribe it:** each static slide got one interaction that proves its point (drag the cut-off into mid-month and it turns red; the migration lines travel the way they really move; a go / no-go gate that only goes green with five checks; the questions as live tick buttons with counters on the part-04 tiles and a copyable follow-up list).
- **`data-step` is the engine's build attribute.** A jump button marked `data-step="1"` would have become a hidden build. Jumps to a build use `data-go` + `data-at` (handled in `jrtech.js`).
- **Text beside a `<b>` inside a flex button splits into two columns** (the text node becomes its own flex item). Wrap the label in one `<span>`; caught on the contact sheet, not by `deck_check`.
- **Per-card vignettes align only if everything under them has a fixed height** (the benefit pill went to 52px). Check the bottoms of a card row on the sheet.
- **Hidden preview panes throttle requestAnimationFrame:** a `ctx.tween` or `ctx.count` checked from `javascript_tool` while the pane is hidden can read mid-way. Read the value again later, or rely on `deck_check` (headless, visible).
- **Clipboard:** `navigator.clipboard` can be refused (no focus, file:// Drive copies). Fall back to `execCommand('copy')`, then to a visible textarea with the text selected.
- **Build after printing:** the launcher's PDF button only appears if `pdf/<name>` exists at build time, so build once more after `deck_pdf.py`.

## 2026-10-06 · A video in the JR-Tech deck (9b93fbd)
- **User:** "add this video after page 15" (a WhatsApp MP4, 3:21, narrated: part 3 of TechNext's Odoo 20 accounting video series for JR-Tech). Page 15 was the risk register in both the source PDF and the deck, so it became slide 16.
- **Read the video before placing it:** `ffprobe` (size, codec), a 14-frame contact sheet, `faster-whisper` on 40 s to learn it is narrated (so it plays with sound), and caption-badge crops at 1 fps to find the chapter times.
- **The engine's offline copies could not seek video:** `sw.js` cached everything and had no answer for `Range` requests. It now cuts 206 slices from the saved file. Tested live: offline, with the network cut, chapters jump and play.
- **Local tests mislead for video:** SimpleHTTP ignores ranges (seeks snap to 0), and a hidden preview pane or a background CDP tab defers playback. Test on the live site, each page in its own window.
- **Presenter view needed its own sync** for media: the deck's BroadcastChannel only moves slides.

## 2026-10-06 · The video zooms and comes back (d2a0ab2, afec470)
- **User:** "make the video can zoom properly and exit seemless bck to presentation". The browser's video full screen was the problem: leaving it also left the deck's full screen.
- **Built:** the deck's own zoom (FLIP from the slide to the whole stage; document full screen only if needed; Esc held by the Keyboard Lock API so it only shrinks the video) and a TechNext control bar, because `controlslist="nofullscreen"` still drew a greyed full-screen button that did nothing.
- **Tested with real input events** in headless Chrome (`Input.dispatchMouseEvent` / `dispatchKeyEvent`, so full screen counts as a user gesture): zoom by button, Z and double-click; back by Esc, Z, double-click and the Back button; deck already in full screen stays there; PageDown comes back and moves on; presenter view mirrors the zoom. Click a faded control without moving the mouse first and the click goes to the video: move the mouse in tests.
- **A real bug the zoom work surfaced:** chapter jumps failed with a media error once the offline copy had saved the video (pieces from the network and from the cache in one stream). `sw.js` is now network-first for ranges, and the player reloads and resumes after any media error. Test chapter jumps both before and after the background save.
- **The Bash tool halves backslashes** inside heredocs: a `split('\n')` in a JS string broke a test. Write such scripts with the Write tool.

## 2026-10-06 · Faster-hiding video controls (f12a5b9)
- **User:** "when not active, hide floating ui in the video much faster". Idle 2.6 s -> 1.1 s, fade out 0.2 s, instant on mouseleave; kept while hovered, seeking or paused; 2.6 s after a touch tap. Measured with real mouse events (`qa/jrtech-deck/idle_test.py`) locally and live.

## 2026-10-06 · Chapters that land properly; question 1.2 (34ba43a)
- **User (screenshot of the chapter list):** "some of this not properly jump to selected video, fix this". Cause 1: the chapter times came from the caption badge changing, but the narration starts 1-3 s earlier (Reminders: first word 112.6 s, chapter was 114 s, so it opened mid-sentence). Fixed from word timestamps. Cause 2: the media-error recovery resumed at the position before the click; it now resumes at the jump's target. Cause 3 (likely in the user's browser): an older offline worker still mixing sources; deck.js now asks for the newest `sw.js` on every visit.
- **Proof:** `qa/jrtech-deck/live_chapters.py` clicks every chapter in a mixed order before and after the offline save, checks time, playing and the lit row, then fakes a media error mid-jump: 0 failures.
- **User:** question 1.2 reworded ("How many companies or databases do you keep in SQL Account today, and should they run as separate companies or as branches of one company in Odoo?"). Engine change → `deck_check` on all 12 decks: 0 errors, the 16 known baseline warnings.

## 2026-10-06 · BHD Asia · HummingBeing implementation scope (ea36df5)
- **User:** "create a technext presentation here's the scope." with `BHDAsia-Implementation-Scope.pdf`, an internal "for team review" document. Built an 18-slide client-facing deck (share `s-4sg4p5j`, ASSET_V 24) and left the internal remarks out (who asked how often, who resents what, a staff name, a dormant entity, a price rise). Reported what was left out and offered a team-only version.
- **The Read tool returned no PDF content** (no pdftoppm): `pypdf` text works, but print with `PYTHONIOENCODING=utf-8` or the console codepage crashes on the minus sign.
- **Port 3970 was held by another chat's preview**: added `technext-decks-2` on 3988 to the Marketing launch.json rather than stopping theirs.
- **`.illus` overlapped the slide number** on every workflow slide (deck.css puts it at bottom 30). `deck_check` passed with 0 warnings; caught on the shots. Lift it to bottom 66–70.
- **6- and 7-step slides left the lower third empty** next to a 9-step slide: fixed-height body + `space-between` steps + the scene card stretched with its content centred.
- **TRE™ applies to speaker notes too**: a regex `\bTRE(?!™)\b` sweep found three bare "TRE" in notes.
- **Bash heredocs broke a Python patch** (quotes and backslashes): write patch scripts with the Write tool and run them.
- **Every control verified by script in the preview** (toggle, Play, slot, Approve, joins, accountant view, module light-up, switches, currency lock, open-item marks, copy fallback panel, slider) and the "contraindication" path by real clicks; `deck_check --shots` and `--phone`: 0 errors, 0 warnings.

## 2026-10-06 · BHD Asia scope, revision 2 (a3815b7)
- **User:** "update the scope", with the same PDF re-exported (20.5 KB, 16:56). Diffed it against the first version's text: three changes (workflow 2 rebuilt as "screened once, then frictionless" with a "why before payment" paragraph; currency settled on SGD; back-office access decided as full admin). The rest was identical, and the report says so.
- **The "why" became its own slide** (07 frontdoor) rather than a crowded callout: two lanes, the order we avoid (pay, wait, decline, refund) and the one we build.
- **Settled decisions move, they don't vanish:** the currency slide changed from a choose-and-lock demo to "settled" with a pricelist switch; the open list went from 8 to 7 plus a "Settled on 6 October" card; the decided slide got a sixth card.
- **Chips in a 590px column wrap at 13.5px:** a returning-client chain of four chips only fitted after shortening the long label and moving the full question into the caption.
- **Still kept the back-office person unnamed** in the deck (the PDF names him); his access decision is in the notes for the presenter.

## 2026-10-06 · BHD Asia logo fix (748451e, b105345)
- **User:** "fix the logo." The BHD mark has navy H-bars and transparent gaps between its letters: on navy slides both vanished and it read as "1D". It was also 19px tall in the slide header (deck.css `.s-co` is sized for wide wordmarks such as Hitachi's).
- **Fix:** dark slides get the official mark untouched on a white rounded tile (`bhdasia-white.png`); never recolour a client's logo. The header uses `.s-co{height:34px}` (40px for the tile) in the deck's own CSS. The closing lockup needed `.hx-lock--sm .ec-bhd--sm` to beat proposal.css's `.hx-lock--sm .hx-co{height:28px}`.
- **`assets/img/clients/*.png` is not versioned by the build** (only sites and thumbs get `?v=`): when a client logo changes under the same name, add `?v={{v}}` to its `src` and to `data-cobrand`, or browsers and offline copies keep the old file.
- **Check every client logo on BOTH a light and a dark slide** at its real size before shipping; the QA sheet is too small to show it, so crop the chrome and lockups at 2x.

## 2026-10-06 · BHD Asia workflow 3 questionnaire (9b00cb4)
- **User:** "there's no survey between 4 and 5?", then a screenshot of the WORKFLOW 2 slide with "fix this part: 4. review and approve 5. questionnaire (survey module) 6. meeting lands on you[r calendar]". The wording was workflow 3's (its steps 4 and 5), and putting it on workflow 2 would have removed payment and contradicted the "front door" slide. Asked with two previewed options; the user chose workflow 3. When a screenshot and the words point at different slides, ask with previews rather than guess.
- **The deck now differs from the scope PDF on purpose** (the questionnaire step in workflow 3 is the user's addition). Note such edits in decks.md so a later "update the scope" doesn't silently undo them.

## 2026-10-07 · HST Medical website review deck (66b8e24)
- **User:** "in technext presentation, create deck for hst. we already have website, webook, research and stuff. add this as reference. build a good presentation. properly showcase the logo", with a screenshot of Pia's agenda (1 website & product catalogue: review feedback, discuss revisions; 2 AI for the website) and her question to Sky: "for our initial scope for HST (purely website), okay to do 1500-3000 USD pricing?". "webook" = the flip-book.
- **Find the client's material first:** `00. Client Folder\28. HST Medical Website (prototype)`, `30. … Product Sheets (flipbook)`, `31. … Brand Strategy`, plus `~/ClaudeWork/hst-wp` (the WordPress build with the performance report, Theme Check and editor guide) and `Downloads\hstwebRFP.docx` (the RFP). An Explore agent summarised the three Drive folders while the engine docs were read.
- **"Properly showcase the logo":** the official colour lock-up (with "Kowa Subsidiary") on a big white card on the cover that builds itself (four clip-path layers of ONE image: the roundel spins in, HST and MEDICAL wipe, the Kowa line rises, a masked sheen); a no-tagline crop for the 36px header (the Kowa line sat right of the roundel, so it was cleared by region, nothing recoloured); the same on a white tile for dark slides. Header crops checked on light and dark.
- **Real product answers, not invented ones:** the Ask HST slides use the prototype's actual replies, probed in headless Chrome through `window.HSTChat.reply()` (scratchpad `chatprobe.py`). The probe also found the gaps the AI slide shows (a Chinese question falls back to the help menu; a blood-thinner question shows the caution AND the product to buy). The "With AI" side is labelled illustrative and quotes only label statements.
- **Catalogue fixes marked on the real pages:** the flip-book repo's `book/words/NNN.json` holds word boxes in 1/10000 of the page, so each print issue (CATALOGUE-QA.md) is boxed exactly; a lens zooms on it.
- **Facts checked live on 7 Oct:** "HST = Higher, Stronger, Together", 1930 Heng Say Tong, 1994, Kowa from 29 May 2026 (hstmedical.com/about and the Kowa announcement). The live site uses ® on HST Medical, Heritage and Rheuma-Salve, not on Zoo-Vite. Awards wording and the 5.0 rating are unconfirmed by HST, so they stay off the brand slide.
- **The first shots caught:** a 3-line cover headline (h-xl + `text-wrap:balance` in a 720px column: keep cover headlines to about 20 characters a line), a seg pressed state with magenta text on blue (unreadable), a product card under the slide number, a 7-item list running into the footer, a price overflowing its card at 50px.
- **A shared preview pane is shared:** during scripted tests the deck jumped slides and question marks changed by themselves; event logging on a re-run showed nothing from the deck. Someone was clicking in the pane. Re-run a test before "fixing" such a bug.
- **Price on a public page:** the USD 1,500–3,000 range comes from Pia's question to Sky, not answered in the screenshot. It is on one slide (14) and its notes, and flagged in the report.

## 2026-10-07 · HST Medical deck, revision 2 (b3d77a7)
- **User:** "Redo last slides, change to explain why TechNext is the best company to implement: 1. We move fast, really really fast, we recognise time as money... 2. TechNext have an ERP implementation division... data migration, APIs, connectors and implementing an integrated solution 3. AI competency very high. Implementating futureproof technologies. ensure light theme only. Slide 5: we could build your brief, slide 6 we could propose ideas after understanding your direction (AI enabled, e-commerce store that converts, support branding strategy). Remove any mention of pricing in the any part of the slides. How we get there? We do and show rather than traditional way of wireframing. Garunteed satisfaction".
- **"Light theme only":** the cover, the AI-search slide and the close lost `.dark`. On a light cover/close the lockup needs the colour logos and a `var(--line)` divider, the agenda/piece buttons need light styles, and deck.css `.ct-links a` is white (built for navy): override it, or the email and site links vanish (caught on the shots).
- **"Remove any mention of pricing" was taken literally:** the price slide, quotation wording, "running cost", "quoted separately", AND HST's own product prices in the Ask HST / rules-vs-AI demos and the JSON-LD excerpt. The "add 2 balms" conversation (all prices) was swapped for Ask HST's real store-finder answer. A regex sweep (`S\$\d|USD|quot(e|ation)|pric(e|ing)|fee|cost`) over the deck HTML + JS proved zero left, and the live share copy was grepped too.
- **Speed proven with the client's own timeline:** git first commits gave the dates (prototype 2 Oct, flip-book 5 Oct, brand pack 6 Oct; the WordPress build's report 2–3 Oct). The usual-vs-ours route shows no durations, only where the launch lands, so nothing is invented.
- **Why-TechNext slides use only approved company facts:** Odoo Ready Partner, 11+ enterprise clients, 10+ countries, four AI disciplines (the company profile's own names), HCMC = AI engineering. A 01/02/03 switcher (`.ky-nav`, `data-go`) ties the three reasons together.
- **"Satisfaction guaranteed"** is the user's own promise; worded as "we refine on the live test link until you are happy; nothing launches without your sign-off", no number of rounds.
- **The preview server from the morning had stopped** (new session): `deck_check --base http://127.0.0.1:3970/` failed with "Deck is not defined". Without `--base` the scripts serve the repo themselves.


## 2026-10-07 · Presenter scripts page (`presenter-guide.html`)
- User: "create another webpage and push online, webpage should be an internal sales guide for presenter. It should show exactly what to say for each slides. It should also contain additional add on jokes to entertain" (JR-Tech + HST Medical).
- Built as a HAND-WRITTEN root file (`presenter-guide.html`, not under `_src/decks`, not in `DECKS`, so the launcher doesn't list it; `noindex`). The build never touches it (it only writes `_src/decks/*` and retires `s-*.html`). Data lives in the `DECKS` object in its own script: per slide `t, who, min, say[], do[], watch?, joke, next`. Slide order must match the deck: a new or moved slide in either deck means updating this page too.
- Scripts are rewritten from each slide's speaker notes in spoken first person; "Never say" panels repeat the content rules (HST: no pricing at all, AI answers illustrative/sample; JR: SST+MyInvois inside Accounting, sample data). Jokes are clean, self-deprecating, never about the client's staff, money or anyone's health; HST slide 10 (the 995 emergency answer) carries a "no jokes after this click" warning.
- Rehearse mode loads the live deck in an iframe and moves it by setting the iframe's `location.hash` (deck.js listens to `hashchange`); timer per slide against `min`.
- Totals: JR-Tech 51 min, HST 42 min of scripted time.
- `git push` and the contents API both returned HTTP 500 for a while on 7 Oct (githubstatus said all operational): retried in a background loop rather than changing anything.

## 2026-10-08 · JR-Tech: Maintenance is not for customers' units (51898f4)
- **User:** "removal of this. Maintenance is not for external clients. It is for maintaining your own equipment that you use." Slide 04 (big idea) dropped the "Service maintains it / Preventive visits planned" step; the combi oven now goes through four apps (Sales, Inventory, Field Service, Accounting). Odoo Maintenance stays where it is about JR-Tech's own hire fleet (phase 2 card, the AI slide's rental units).

## 2026-10-08 · JR-Tech: no presenter names on the part dividers (78274bf)
- **User:** "remove the presentor name apply to related pages" then "this is jr tech only". The "Presents Jett & Phillip / AJ / Sky" chips came off slides 03, 09 and 18. The part-04 chip (`jd-who`, "28 questions · 0 answered") reuses the same class: a regex on `jd-who` removed it too and it had to be restored; match on the content, not the class. The team chips on the close and the speaker notes still name the team (not asked).

## 2026-10-11 · Launcher redesign: find a deck (3c22368, ASSET_V 32)
- User: "revise the design of this. make this the design will be properly arrange all additional presentation / filtering." The launcher had grown to 14 decks in five stacked groups with a big hero and no way to filter.
- Built: a sticky find bar (search, group tabs with counts, Topic and Length chips, Sort, grid/list), filter state in the hash, a compact hero with totals, and a folded "How to present" section. "Sales proposals" became "Client decks" (it holds the HST review too).
- **Arrangement:** groups of 2 in a 3-column grid left an empty column on every small group. Now groups flow on a 4-column grid, each spanning its deck count, so small groups pair up. A new deck needs `tags=` and a group that exists in `GROUPS`, or the build fails with a KeyError.
- Headless Chrome `--window-size=390` doesn't give a real 390px viewport (the page looked clipped). Check phone width in the browser pane with the mobile preset and measure `scrollWidth` instead.
- The in-app pane screenshot timed out while the window was in the background. Use headless shots (`~/ClaudeWork/qa/ix-shots.py`, which deletes its profile) to check the layout.
- **Follow-up (6c584fe, ASSET_V 33):** user: "make it smoother, it's glitching when selecting a deck". Cause: the card description un-clamped on hover, so the card grew and the whole grid row jumped; the thumbnail also zoomed and the lazy hover slide popped in late. Fix: no size change on hover (rule: **a hover must never change a card's size**), no zoom, preload `.ix-thumb-2` after load, and filter/sort/view changes run inside `document.startViewTransition` (each card has `view-transition-name: ix-c<i>`; the bar is `ix-bar`; reduced motion = instant).
- **Follow-up (7c22c25, ASSET_V 34):** user: "make this html smoother, its having a framedrop". Measured with `~/ClaudeWork/tn-perf-tools/ixperf.py` (rAF intervals during scroll, a hover sweep and 9 filter clicks; `CPU=4` throttles; named CSS ablations). The View Transitions added in 6c584fe cost a 50-83 ms frame per filter click (it snapshots every card); big 50-60px-blur shadows added scroll/hover blips. Fix: FLIP with WAAPI on on-screen cards only (transform/opacity), small shadows, hover changes the border only, `.ix-thumb-2` on its own layer, `content-visibility:auto` on the guide. Result at 4x CPU: filter 0% dropped (was 3.6%, max 83 ms). **Rules: no View Transitions on the launcher; no animated or 50px+ shadows; never `decoding="async"` on the visible thumbnail (it painted blank first).**
