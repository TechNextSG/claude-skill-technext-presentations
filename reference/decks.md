# The decks, one by one (state on 2026-10-07, ASSET_V 29, last commit b3d77a7)

Slide maps are `number · id · title`. **dark** marks a navy slide. Each deck lists its sources, data and special rules. When a deck changes, update its section here.

Every deck shares the same shape:
- **Cover** (`cover`): dark, `data-chrome="none"`, with a logo, a kicker, a `.h-xl` headline with one `.hl`, a lead, tags and a hint saying "→ or click to begin · O all slides".
- **Closing slide** (`contact` or `next`): dark, `data-chrome="foot"`, the booking CTA with `{{qr:meet}}`.

## About TechNext

### Company profile: `company-profile` (11 slides, about 10 min, share `s-4zprjc7`)
Files: `_src/decks/company-profile.html`, `assets/company-profile.css|js`, `ai-demos.*`, `fx.js`, `{{include:ai-templates}}`, `window.APPS`.

01 cover (plane and orbit art) · 02 who (who we are, stats) · 03 offices (SEA dot map and office cards, `data-steps="3"`) · 04 practices (ERP, AI and marketing) · 05 partner **dark** (Odoo Ready Partner orbit) · 06 engagement (five steps, `data-steps="4"`) · 07 ai (four disciplines, live AI demos) · 08 industries · 09 rules **dark** (a few rules we keep) · 10 details (company record, click to copy) · 11 contact **dark**

- Office cards and map labels carry the office roles (see content-rules).
- The `practices` slide lists three practices. Technology (IoT · Apps · Networks) is pending (see content-rules).

### Portfolio: `portfolio` (10 slides, share `s-77yjkef`)
Files: `_src/decks/portfolio.html`, `assets/showcase.css`, `showcase.js`, `portfolio.js`, and data in `_src/portfolio_data.py` (CLIENTS, SERVICES, STATUS, PINS with label side r/l/t/b).

01 cover (client-name marquee) · 02 map (world dot map, pins) · 03 clients (directory: filter and detail panel, cycles until clicked) · 04 story-casa · 05 story-tre · 06 story-niv · 07 story-jrt · 08 story-imc · 09 enterprise **dark** (NDA work as counts) · 10 contact **dark**

- Stories are plain bullets (`.st-list`), with no dates anywhere.
- The matrix slide and the proposals/paused slide are removed for good.

## What we build

### Service showcase: `service-showcase` (15 slides, share `s-pamt7t8`)
Files: `_src/decks/service-showcase.html`, `assets/service-showcase.css|js`, `ai-demos.*`, `fx.js`.

01 cover · 02 map (the service map) · 03 erp (Odoo 20 implementation plan, a Gantt you can drag: `.gt-body[data-drag]`) · 04 crm (live pipeline board, add a lead, assignment rules) · 05 group (multi-company) · 06 custom (customisation Q&A) · 07 integrate (integrations with outages, counters, MCP line) · 08 care (training and support) · 09 ai · 10 rag · 11 aiodoo · 12 agents · 13 marketing (websites, social, brand) · 14 pricing (how engagements are priced; Light User line, no figures) · 15 contact **dark**

- "All fourteen services". When a service is added (the Technology practice), the map, the count, the launcher description and a slide all change.

### Marketing showcase: `marketing-showcase` (15 slides, share `s-p98b5ej`)
Files: `_src/decks/marketing-showcase.html` (mostly `{{sc:*}}` tokens), `assets/showcase.css|js`, and data in `_src/showcase_data.py` (LIVE 7, CONCEPTS 3 featured, MORE, PITCH 10, five to a row) + `_src/sites_meta.json` + `assets/img/sites/`.

01 cover (scrolling site wall) · 02 gallery (the wall of 29 tiles, filter All/Live/Concepts/Pitch; columns chosen so every row is full) · 03–09 one slide per LIVE site (Casa Escondida, BHD Asia, HummingBeing, nivellipso, JR-Tech, TRE in Singapore, technext.asia) · 10–12 featured concepts (Immaculate Connections, Auntie Gaik Lean's, TRE Worldwide Conference) · 13 more (more concepts) · 14 pitch (pitch microsites) · 15 contact **dark**

- A site slide (`sc_feature` in build.py) has the copy on the left, and a browser frame plus a phone on the right, each scrolling the full page.
- Adding a site: an entry in `showcase_data.py`, a capture, `sites_images.py`, `build.py --prune` (see recipes).
- Blue Moon and Tri-Comp are removed. The last recapture was 2026-10-02 (BHD, HummingBeing, TRE SG, technext.asia, Immaculate Connections).

## Odoo

### What is Odoo: `what-is-odoo` (17 slides, share `s-4xgby3f`)
Files: `_src/decks/what-is-odoo.html`, `assets/what-is-odoo.css|js`, `fx.js`, `{{include:walkthrough}}` (the walkthrough screens in `_src/partials/walkthrough.html`).

01 cover · 02 problem (`data-steps="1"`) · 03 what · 04 new20 ("Odoo 20, in six changes", filter All/New/Check before upgrading) · 05 apps (catalogue from `{{apps_json}}`) · 06 onedb **dark** (one database) · 07 walk (index of the walkthrough, `data-go` jumps) · 08–13 w1–w6 (CRM, Sales, Inventory, Invoicing, Accounting, Reporting; `data-transition="fade"`, one build each, a stepper on top) · 14 editions (Community and Enterprise) · 15 hosting (where Odoo runs) · 16 implement (how TechNext implements Odoo) · 17 contact **dark**

- The walkthrough follows one order (S00042, Lumen Trading Pte Ltd, office chairs) from lead to cash. Keep its figures consistent across w1–w6.

### The Odoo app series: `odoo-accounting`, `odoo-sales`, `odoo-crm` (13 slides each; shares `s-myi79wm`, `s-tig4yfh`, `s-njrgnhn`)
Built 2026-10-02 by a parallel session with the impeccable and web-design-engineer skills. The user chose the structure "one live Odoo screen". It is reviewed against `DESIGN.md`.

01 cover **dark** (`oa-cover`, an Odoo window already working) · 02 replaces (what it replaces, one build: a counter and a meter) · 03–09 mv1–mv7 (the seven moves: `class="oa-mv"`, `data-group="live"`, `data-steps="1"`) · 10 new20 (each item has a "seen in Move n" jump) · 11 local (Singapore, the Philippines and Vietnam side by side, beside a dot map; a pin only highlights its column, so print carries all three) · 12 setup (phases light in turn) · 13 contact **dark**

- **Shared layer:** `assets/odoo-app.css|js` (`OA`): the window `.lw`, the move column, the session log `.mv-log`, and the replaces, new20, local and setup slides. Each deck adds its views in `assets/odoo-<app>.css|js` and its navbar in `_src/partials/<acc|sale|crm>-nav.html` (Sales also uses `pico-chair` and `pico-desk`).
- **A move script:**
  ```js
  OA.start({ cover: fn, coverSettle: fn, moves: [
    { id: 'mv1', name: 'Bank feed', result: '14 transactions in',
      reset(s),                       // back to the start, no transitions (wrapped in snap)
      intro(ctx, s, ready, quick),    // set the scene; call ready() to light the Odoo button
      act(ctx, s, done),              // perform the task; call done() to tick the log
      final(s),                       // the finished state, for print and the overview
      init(s) /* optional */ }, ... ] });
  ```
  Step 0 readies the highlighted `[data-act]` Odoo button. Step 1, or a click on that button, performs the move. Inside the window, keep Odoo's grammar: a plum primary button, teal links, a chevron status bar, the official app icons. Outside it, TechNext blue leads ("Two Palettes Rule", DESIGN.md).
- **The sample company:** Kestrel & Pine Pte Ltd (Singapore). Every window carries a "Sample" chip. The figures must agree:
  - **CRM:** two leads merged, Lead Sourcing (10 companies found), assignment by rotation, a planned next step, predictive scoring (41.2% → 63.0%; prorated S$7,416 → S$11,340), the Sunbird Clinics quotation, then Won (S$18,000 expected; October forecast S$55,840 → S$62,500).
  - **Sales:** S00057 for Sunbird Clinics: S$18,220.44 with installation at a 30% margin, S$18,318.54 at 35%, a S$5,000.00 deposit, S$13,318.54 still due. Then Shopee, Lazada and TikTok Shop orders, and commissions on paid sales.
  - **Accounting:** the bank feed (14 transactions; GL S$110,382.30 → S$130,407.90), 13 matched by rule plus Lumen Trading by suggestion, a bill read from its PDF, reminders, a batch payment, the GST return (Review, Submit, Pay, Validate), the month locked.
- **Odoo 20 claim limits:** see content-rules ("Do not claim").

## Client decks (sales proposals)

### Hitachi Elevator Philippines: `hitachi-elevator-ph` (14 slides, share `s-vwagibj`, which is WITH THE CLIENT; never change the token)
Files: `_src/decks/hitachi-elevator-ph.html`, `assets/proposal.css|js` (the shared kit), `assets/hitachi.js`, `fx.js`; body `data-cobrand="assets/img/clients/hitachi.png"` (+ `-white`).

01 cover **dark** (TechNext | Hitachi lockup `.hx-lock`; connector and service desk right under the branch labels) · 02 understand (PH dot map, NSCR stations) · 03 pressure ("Five places where Odoo takes the load") · 04 arch **dark** (a service layer beside GERP) · 05 breakdown (a call from ring to signed report: 3 scenarios, 3 branches, SLA clock, route; it takes about 14 s to finish) · 06 dispatch · 07 worksheet · 08 contract (handover to renewal) · 09 radar (contracts ending this year) · 10 projects (NSCR-scale installs) · 11 dashboard (the 24/7 promise, with a number) · 12 scope (the client's phases) · 13 roadmap (pilot first) · 14 contact **dark**

- **Phases (user):**
  - PH1: Helpdesk, Planning (field service), Sign, Documents, Project.
  - PH2: Subscriptions, Sales, CRM, Purchase, marked TO CONFIRM (it depends on what GERP covers).
  - PH3: Dashboards.
  - No Inventory and no AI tile.
- **Removed (don't bring back):** the parts pressure point, the Inventory and Purchase cards on slide 3, the "Parts confirmed before the van leaves" slide and the "Five questions" slide.
- **Public facts used** (hitachi-elevator.com.ph and hitachi.com):
  - 1971 Hi-Eles; a subsidiary since 2011;
  - Makati, Cebu (Mandaue) and Cagayan de Oro;
  - 24/7 service with "readily available maintenance parts";
  - NSCR 67 units (21 elevators and 46 escalators) across 7 stations, contracts CP01 Taisei-DMCI and CP02 Sumitomo Mitsui;
  - body cams and QR codes (22 Nov 2025).
- **Odoo's place:** the service layer beside GERP, never a replacement.

### JR-Tech Solution: `jrtech-odoo-erp` (25 slides, about 50 min, share `s-mm4jk7b`)
Built 2026-10-06 from two PDFs the user supplied: `Downloads\JRTech-Odoo-ERP-Presentation.pptx (1).pdf` (19 pages, TechNext's own presentation to JR-Tech) and `Downloads\JRTech-Accounting-and-Billing-Questions.pdf` (28 discovery questions + "please bring or send ahead"). User: "use this material", "question at the back", "at the end of presentation".
Files: `_src/decks/jrtech-odoo-erp.html`, `assets/jrtech.css|js` (every class starts with `j`), `proposal.css|js` for the lockup and `PX` chart helpers; body `data-cobrand="assets/img/clients/jrtech.png"` (the light logo JR-Tech's own deck uses on white) + `jrtech-white.png` (the official `JR-Tech-Logo_Final-white.png` from the client site repo, cropped).

01 cover **dark** (agenda buttons jump to the four parts; "one database, eleven applications" ring with numbered phase badges) · 02 solution (Migration → P1 → P2 → P3 → Go-live → Support, AI Blueprint band, "runs through every phase" strip; click a stage, "Go to it") · 03 s1 **dark** (part 01, Jett & Phillip; "in this part" jump list) · 04 bigidea (one combi oven record written by five apps, 5 builds) · 05 roadmap (11 apps, phase filter, counter) · 06 phase1 · 07 phase2 (five cards each, 5 builds; every card has a live vignette that resets, plays, or shows its end) · 08 phase3 (margin drop → six jobs; AI agent proposes a bill, Confirm/Discard; 2 builds) · 09 s2 **dark** (part 02, AJ) · 10 worries (4 builds) · 11 cutoff (drag the cut-off; mid-month turns red, "Cut at the close" snaps; plays once on arrival) · 12 scope (11 lines travel SQL Account → Odoo the way they move; tax codes re-configured, prior-year stays archived) · 13 process (7 builds, step caption with when it happens) · 14 runway (6 builds, system-of-record and e-Invoice-sender bars) · 15 risks (6 risks + go / no-go gate, auto-runs once) · 16 video-ar (the narrated video "Getting paid, with less chasing", Odoo 20 Accounting part 3 of 4, 3:21, user: "add this video after page 15"; poster = its title card, chapter list 0:00/0:15/0:45/1:20/1:52/2:25/3:04, each just before its first spoken word: data-t 0, 15, 45.4, 80.6, 112, 145, 184) · 17 needs (12-item checklist, ring) · 18 s3 **dark** (part 03, Sky; jumps to builds of 19 via `data-at`) · 19 aftergolive (drag the day, 3 builds) · 20 s4 **dark** (part 04: six question groups as tiles with live answered counters) · 21 q-books (01 + 02 KEY) · 22 q-billing (03 + 04 KEY) · 23 q-cash (05 + 06) · 24 prep (8 files to send, meeting tally, "Copy the follow-up list") · 25 contact **dark** ("Let's set the cut-over date", team chips, booking QR)

- **The video** (`assets/video/jrtech-getting-paid.mp4`, 12.8 MB, remuxed with `-movflags +faststart`, + `.jpg` poster): `preload="none"`, plays with sound on click, pauses on leave. Own control bar (play, time, seek track with chapter marks, sound, Zoom/Back; fades while playing); click = play/pause, double-click or Z = zoom to the whole stage (and the screen), Esc/Z/Back = back into the slide; recovers from a media error at the same point. Presenter view: a BroadcastChannel (`jrtech-odoo-erp-video`) keeps play, pause and seek in step; the presenter window is muted. Other parts of the series (1 supplier bills, 2 bank & reconciliation, 4 MyInvois, set-up & AI) exist as videos but were not given.
- **Question 1.2 is the user's wording** (2026-10-06): "How many companies or databases do you keep in SQL Account today, and should they run as separate companies or as branches of one company in Odoo?" (the Penang fabrication plant line is gone).
- **Questions at the back:** the 28 questions are buttons: one click answered, two follow up, three clear. Marks live in `sessionStorage` (`jrtech-odoo-erp:q|files|needs`), so a reload or moving between slides keeps them; "Clear all marks" needs two clicks. The copy button writes follow-ups, not-asked questions, missing files and open checklist items; if the clipboard is refused, the text opens in a panel to copy by hand. Print shows everything unticked.
- **Fixes to the source, on purpose:** cover footer said "Casa Escondida × TechNext · Phase 1" (template leftover); close said hello@technext.asia and "Odoo Implementation Partner" → sales@technext.asia and "Odoo Ready Partner"; date set to October 2026 (the questions sheet says the presentation is October 2026). The cover agenda listed "03 AI Blueprint" but the source had no AI Blueprint slides: it stays as the band on slide 2 and a phase-3 note, and Sky's chip reads "AI blueprint & support".
- **Facts checked:** SST-02 reports and the MyInvois intermediary (Odoo S.A. on MyTax, pre-production and production) are in Odoo's Malaysia localisation docs. "SST + MyInvois" is the localisation inside Accounting, so the deck lists it but does not count it among the eleven apps. Field Service is labelled as running in Planning (Odoo 20).
- **Sample data:** deal, quote, serials, jobs, bill, units, codes, month labels: all labelled "Sample" on the slide or in its foot note.
- **Open with the user:** Jett & Phillip (part 01 chip) vs "Migui & Jett · Odoo modules" (close) both come from the source; the AI Blueprint has no slide of its own.

### BHD Asia · HummingBeing: `bhdasia-odoo-scope` (19 slides, about 30 min, share `s-4sg4p5j`)
Built 2026-10-06 from `Downloads\BHDAsia-Implementation-Scope.pdf` (5 pages, TechNext's internal "for team review" scope: workflows and modules, consolidated from the 20 Aug and 18 Sep meetings, the client's lawyer's 6 Oct questions and five demo databases). User: "create a technext presentation here's the scope." Built as a CLIENT-FACING deck to walk Isabelle through the scope; the source's internal remarks were left out (see content-rules, "Client decks from an internal document").
Files: `_src/decks/bhdasia-odoo-scope.html`, `assets/bhdasia.css|js` (every class starts with `e`), `proposal.css|js` for the lockup; body `data-cobrand="assets/img/clients/bhdasia.png"` (= `-white`: the BHD mark cropped from `09. HummingBeing (production)\01. Images\09. Event Image\ALL LOGO\4.png` without its tagline; the mark works on navy too) + `hummingbeing-white.png` (from the HB site's `logo-dark.webp`) in the cover and close lockups.

01 cover **dark** (TechNext | BHD | HummingBeing lockup; agenda jumps to scope / flows / modules / decided; "one client record" hub with seven streams, `.flow` lines, bobbing chips in the `.is-tv` stop list) · 02 scope (layer stack: custom modules / third-party apps / code crossed out, configuration + Odoo Online; click a layer; recurring / one-off / code-upkeep ledger; Zoom capture out of scope) · 03 carry (seven kinds of work, cycles every 4.6 s until clicked; "how it's sold" badge, workflow jump buttons, modules, a record-chip row) · 04 flows (six workflows x nine modules dot grid built from `data-u`; click a module to light its rows; rows jump to w1–w6) · 05 w1 ticket (9 steps) · 06 w2 paid 1:1 session, "Screened once, then frictionless." (6 steps for a new client: the site's one "Book a session" button opens the questionnaire, scored against red-flag criteria, an automation rule emails the paid link on a pass or the free Discovery Call on a fail, pick a time, pay, invoice + calendar + reminder; switch No red flags / A red flag; pick a slot; an "every booking after that" card under the steps) · 07 frontdoor (`data-steps="2"`: two lanes, "pay to book, then approve" ending in a refund vs "questionnaire first"; the lawyer's timestamped record; the paid link never on the website) · 08 w3 free booking (7: link, intake question, request, you approve, the questionnaire in Surveys (user, 2026-10-06; not in the scope PDF), meeting on your calendar, no payment/no invoice; type switch, Approve at step 3) · 09 w4 screened sale (7, All clear / A contraindication: fail strikes steps 4–7 and shows "Stops here") · 10 gate (`data-steps="1"`: the shop search types "screened service", No results) · 11 w5 waitlist (4, seats fill 9 to 12, "Someone joins") · 12 w6 money and books (4, statuses In payment / Not paid then Paid, accountant Exports / Limited login) · 13 modules (carries / replaces switch) · 14 phase2 (five switches light dashed slots, 9 to 14) · 15 decided (six cards, 3 + 3, incl. "Books in SGD"; screening jumps to workflows 2 and 4; "booking links are public once published") · 16 currency ("Books in SGD, prices in any currency.": settled 6 Oct, Singapore chart; pricelist switch SGD/USD/EUR/GBP/JPY changes the sample quote; "Try to change the company currency" is refused) · 17 bundle **dark** (provider network slider, 25 by default; "not in this scope: to discuss") · 18 open (seven open items as tick buttons with owners + a "Settled on 6 October" card: books in SGD, back-office access full admin; counters, copy list, clear) · 19 contact **dark** ("Next, the quotation, in writing.")

- **The workflow engine** (`flow(id, opt)` in `bhdasia.js`): `data-steps` = number of steps; the arrow key, a step click or Play move the build; scene parts `data-on="n"` light from step n (ghosted before), `data-t="0:text|n:text"` swaps wording; `opt.paint` adds per-slide state; settle paints the last step. Reuse it for any "process played step by step" slide.
- **Open items** keep their marks in `sessionStorage` (`bhdasia-odoo-scope:q`): one click settled, two follow up, three clear. Print shows them unmarked.
- **Revision 2 (user: "update the scope", same PDF re-exported 16:56):** workflow 2 rebuilt (screened once, then frictionless) + the "why before payment" slide; currency settled 6 Oct (SGD, Singapore chart, pricelists USD/EUR/GBP/JPY); open item 5 became the back-office access paperwork (full admin decided 6 Oct, because Odoo has no standard group that publishes events while hiding registration answers). Everything else in the PDF was word-for-word the same.
- **Facts kept from the source:** six workflows and their steps, nine modules and what each replaces, phase two list, decisions, seven open items + what was settled on 6 Oct, the provider bundle (about 25 students, TRE™ Singapore membership benefit, shared service). TRE™ everywhere, notes included (client trademark rule).
- **Left out on purpose:** that she "asked three times", the cost she "resents", the back-office person's name, the dormant Japan entity, the Simba price rise, the "internal / confidential" labels. Multi-company being on Odoo's Custom plan is in the notes only, as a presenter check.
- **Open with the user:** whether a team-only (internal) version is also wanted. The card surcharge and bank sync are the source's tested claims (bank sync is footnoted "where your bank is on Odoo's list").

### HST Medical: `hst-medical-website` (19 slides, about 40 min, share `s-9d7xqqb`)
Built 2026-10-07 from the HST material on Drive (website prototype `28.`, product-sheet flip-book `30.`, brand strategy `31.`), `~/ClaudeWork/hst-wp` (WordPress build: performance report of 3 Oct, Theme Check, editor guide) and `Downloads\hstwebRFP.docx`, to Pia's agenda (website and catalogue feedback; AI for the website). User: "properly showcase the logo". Revision 2 the same day (b3d77a7): **light theme only, no pricing anywhere**, slide 5 "we can build your brief", slide 6 "your direction", the close rebuilt as why TechNext + how we build.
Files: `_src/decks/hst-medical-website.html`, `assets/hst.css|js` (every class starts with `k`), `proposal.css` (lockup), `showcase.css|js` (browser and phone frames, lazy site pictures). Body `data-cobrand="assets/img/clients/hst-mark.png?v="` (colour, no Kowa line; `hst-white.png` is unused now that every slide is light). `assets/img/clients/hst.png` is the full official lock-up. Packshots `assets/img/hst/pNN.webp`, catalogue pages `cat-NNN.jpg` / `fix-NNN.jpg`, site pictures `assets/img/sites/hst-{home,shop,pdp,where,about,cat,bs}-*`.

01 cover (light; colour lockup; a white logo card that builds itself, "Higher · Stronger · Together"; agenda 01 website & catalogue / 02 feedback / 03 AI for the site / 04 why TechNext) · 02 brand (1930 / 1994 / 2026; four brands with packshots) · 03 built (three live test links, hover pans) · 04 site (five page tabs, desktop + phone) · 05 brief ("We can build your brief, line by line": RFP 2.1–2.6 with evidence from the staging build; 2.4 carries a mini main-paint chart) · 06 direction ("Tell us your direction, we'll bring the ideas": AI-enabled / a store that converts / brand strategy support; click a column to pick it, the others dim; picks stored in `hst-medical-website:dir` and added to the follow-up list) · 07 book (CSS 3D page turn, product card with item codes) · 08 fixes (seven print fixes boxed on the pages) · 09 feedback (live board, `hst-medical-website:fb`) · 10 askhst (four real Ask HST conversations, no prices: stiff shoulders, kid's cough, the Watsons-near-Tampines store finder, the 995 emergency) · 11 ainext (rules vs AI, illustrative AI side, no prices) · 12 aimap (five AI opportunities; no cost row) · 13 geo (light; sample AI answer; real llms.txt, a JSON-LD excerpt without prices, the HTML) · 14 fast (why TechNext 01: "We move fast. Really fast."; HST's own timeline 2 Oct prototype, 3 Oct staging build, 5 Oct flip-book, 6 Oct brand pack, today; usual vs TechNext route, launch flag and "more time selling", no durations) · 15 erp (02: "An ERP division behind your website": integration map ERP / payments / couriers / channels / email & CRM / analytics, auto-cycles until clicked; data migration, APIs, connectors; "already moved on our staging build") · 16 ai (03: "Strong in AI, built for what's next": the four AI disciplines with what each means for HST and jumps back; future-proof list) · 17 how ("We build it and show you, not wireframes": usual vs TechNext lanes, "Another round" counter, Satisfaction guaranteed seal) · 18 questions (ten; Q3 delivery and GST without amounts; copy list = questions + directions + revisions) · 19 contact (light)

- **No pricing anywhere** (user, 7 Oct): no figures, no quotation wording, no product prices in the demos. Don't bring the scope/price slide back unless asked.
- **Facts used** (hstmedical.com, checked 7 Oct 2026): HST = Higher, Stronger, Together; Heng Say Tong 1930; incorporated 1994; Kowa Pharmaceutical Asia from 29 May 2026; 51 products, 11 ranges, 58 item codes; 30 stores. ® on HST Medical, Heritage, Rheuma-Salve (as the live site), none on Zoo-Vite; Alievaid™ (pack).
- **Left out on purpose:** the brand strategy's market figures and the internal research files; the 5.0 rating and award wording (unconfirmed, question 5).

**A new proposal:** copy this deck's structure, reuse `proposal.css|js`, write `assets/<client>.js`, and add it to the "Client decks" group in `DECKS`. Content rules apply in full.

## Pricing

### ERP tier list: `erp-tiers` and Marketing tier list: `marketing-tiers` (7 slides each; shares `s-w37eiqr`, `s-f3657x2`)
Files: `_src/decks/<x>-tiers.html` (tier cards and add-ons as static HTML with data attributes; `window.TIERS` = name, subject, viz, meter, finder questions, explorer data), and the shared `assets/tiers.css|js`.

01 cover **dark** · 02 tiers (three cards; Growth is "most popular"; the last one is marked customisation) · 03 explore (what each tier covers) · 04 finder (which tier fits; the answers set a minimum tier, and `why` explains it) · 05 addons (eight customisation add-ons) · 06 plan (tier + add-ons → an email, WhatsApp or clipboard quotation request) · 07 next **dark**

- Three tiers only. The prices are TechNext's service fee and "On quotation".
- The code follows the tier count (`NAMES.length`, `--last`), so the two decks must stay in step: change both together.

## Presenter scripts: `presenter-guide.html` (internal, hand-written)
Word-for-word scripts for the JR-Tech (25) and HST Medical (19) decks: say / do / watch out / bridge / optional joke per slide, deck tabs, search, jokes and script-only toggles, rehearse mode (live slide in an iframe + timer). Not generated by the build and not in the launcher. **When a slide is added, moved or reworded in either deck, update this page's `DECKS` data too.** Adding another deck = another key in `DECKS` with `url`, `parts` and `slides`.

## The launcher: `index.html`
Source `_src/decks/index.html` with `{{launcher}}` from `DECKS`, `assets/index.css|js`, and `sw.js`.

- **Hero:** "12 decks, made to be clicked" (12 since the JR-Tech deck).
- **Groups:** About TechNext · What we build · Odoo · Client decks · Pricing (each with a `GROUPS` key + blurb).
- **Find bar (2026-10-11, 3c22368):** sticky bar with search (`/` focuses it), group tabs with counts, Topic chips (from each deck's `tags`, AND), Length chips (≤10 · 15–25 · 30+ min), Sort, grid / list view (remembered in localStorage). No filter + "By group" = grouped; anything else = one flat sorted grid (`.ix-flat`), with the group name shown on each card. State is in the hash (`#g=odoo&t=ai&q=crm`) so a filtered view can be sent; `#guide` is left alone. Groups flow on a 4-column grid, each spanning as many columns as it has decks (`--n`), so two 2-deck groups share a row (2 cols ≤1100px, 1 col ≤680px). Hero shows decks / slides / hours (`{{slide_count}}`, `{{hours}}`); shortcuts, tips and TV set-ups sit in a folded "How to present" section (`#guide`).
- **Cards:** a thumbnail with a hover picture, then slides and minutes, the title and description, and one row of actions: Present, Kiosk loop, PDF, Share.
- **Card sizes:** `.ix-body` is a size container. At 315px or less the link icons hide; at 281px or less "Kiosk" stays without "loop"; at 254px or less the padding tightens. It was verified from 320 to 1440px.
- **Sections:** "Presenting tips" and "Presenting on a TV or projector", plus "Save every deck for offline use".
- **PRODUCT.md** describes a planned living dashboard: a team-only address, a registry, owners and statuses, freshness flags and GoatCounter views. It is NOT built: the launcher is still the site root. Don't treat it as done. Ask before building it.

## Baseline QA, 2026-10-04 (`deck_check.py` on all 11 decks, `--phone` included)

0 errors and 16 warnings. Every deck turns on a phone, and none throws in play or in `?print`. These warnings are the to-fix list for the coming edit. Each one is a call for the user: fix it, or record it as intended.

- **Text cut with "…":**
  - Hitachi 06 dispatch: the job card shows "#HD-2431 · Mand…" and "lift stopped, brake pa…". The card is too narrow; widen it or shorten the text.
  - Odoo CRM 03 mv1: the list cells "Orchard Pilates Studio" and "Tiong Bahru Bakehouse". Odoo truncates list columns the same way, so this may stay.
  - Odoo Sales 08 mv6: "Monitor riser: 46 on hand, sent…".
  - Service showcase 12 agents: "an email arrives, the order changes, a p…".
- **Text under 11px:**
  - avatar initials: service showcase 04 crm (10px) and What is Odoo 08 w1 (9.5px);
  - chips: Hitachi "phase 2" and "In progress" (10.5px), Portfolio status "Live" (10.5px);
  - What is Odoo 10 w3: "Reorder rule" (10.8px).
  - These are acceptable as captions inside a product window. On a 1080p screen they render at about 12–13px.
- **Not caught by the script, from reading the decks:** the decks show three practices and "fourteen services", while technext.asia now has a fourth practice, Technology (IoT · Apps · Networks).
