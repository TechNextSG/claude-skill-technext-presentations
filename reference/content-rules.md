# Content rules: what a deck may say

Every word in a deck is something a client may quote back. When unsure, leave it out and ask.

## Company facts (re-verified on technext.asia 2026-10-02)

- **Name:** TechNext Pte. Ltd., UEN 202699888G, 261 Waterloo Street #03-36, Singapore 180261. The company details slide carries these. Never add a founding year or a project count.
- **Approved figures only:** clients in 10+ countries, 11+ enterprise clients, 4 core AI disciplines, 3 offices. Never add other numbers (team size, projects, revenue, years) unless the user gives them.
- **Partnership:** always "Odoo Ready Partner", never "certified", "Gold" or "Silver". Use the badge `assets/img/odoo-ready-partner.png`. Licences come from Odoo, per user per month. TechNext quotes the implementation.
- **Offices and roles** (Pia Cachola, 30 Sep 2026):
  - Singapore is the headquarters: sales, discovery and on-site work.
  - The Philippines office in Taguig City (Metro Manila) is the main development and consulting hub.
  - The Vietnam office in Ho Chi Minh City is mainly AI engineering.
  - Never call Vietnam "the development hub".
  - TechNext has no Malaysia office. Clients in Malaysia (JR-Tech, Penang) are fine as clients.
- **Practices:**
  - The decks show three: Odoo ERP, Enterprise AI, and websites/social/brand (marketing).
  - On 2026-10-03 technext.asia added a fourth, **Technology (IoT · Apps · Networks)**, LIVE via website PR #42. The decks do not show it yet. When the user edits the decks, bring it in everywhere the practices are listed (company profile `practices`, service showcase `map` and services, the launcher description), after confirming with the user.
  - **Never add Cyber Security.** The ACRA codes exclude cybersecurity, and penetration testing and SOC monitoring need a CSA licence (user rule, 2026-10-03).
- **ISO 27001:** not certified. Never claim it.
- **Contact:**
  - booking page `https://technext.odoo.com/book/c82cf8a9` (`{{qr:meet}}`);
  - WhatsApp +65 8839 6998;
  - sales@technext.asia;
  - technext.asia.
- **Live site wins:** if a fact here conflicts with technext.asia, the live site wins. Update this file, and tell the user.

## Odoo facts

- **Current release: Odoo 20.** Facts come only from the Odoo 20 release notes and the 20.0 documentation. Field Service runs inside Planning from Odoo 20. VoIP is called "Phone". `assets/apps.json` mirrors the technext.asia app catalogue.
- **What is Odoo** has the slide "Odoo 20, in six changes": AI agents, MCP, offline mode, Field Service into Planning, accounting, payroll, and a strip of changes for SG, PH and VN.
- **Screen labels** follow the 20.0 docs and code: Fetch Transactions, Bank Matching, Create Payment, Tax Returns (Review, Submit, Pay; Validate posts the closing entry), Send (not "Send by Email"), Generate › Lead Sourcing, Assign Leads, Convert to Opportunity.
- **Statuses:** a payment goes Draft → Paid → Reconciled. An invoice shows In Payment, then Paid once reconciled.
- **Do not claim:**
  - InvoiceNow or Peppol for Singapore (Odoo only says it is preparing for future InvoiceNow compliance);
  - a GST F5 or IRAS e-filing report;
  - bank feeds for banks that are not on Odoo's list;
  - Accounting, bank sync, digitisation, the marketplace connectors or Commissions in Community;
  - credit-free Lead Sourcing, enrichment, digitisation or AI.
- **Logo:** the plain Odoo logo where Odoo is meant; the partner badge only for the partnership.
- **Look:** every Odoo screen is a simplified, illustrative view, labelled as such (a "Sample" chip or the `.illus` foot note).

## Prices

- **Tier decks:** prices are "On quotation". Every price is TechNext's SERVICE FEE: not the Odoo licence (ERP), not ad spend, and not third-party subscriptions (marketing). Say so on the tiers slide.
- **Three tiers only:**
  - ERP: Essentials (took in Starter) · Growth (most popular) · Enterprise (customisation, custom quotation).
  - Marketing: Launch (took in Starter) · Growth · Brand (customisation).
  - Add-ons are the customisation layer.
  - The Starter tiers were our invention, so flag the tier names before external use.
- **Elsewhere:** no prices beyond Odoo's own published structure (per user per month). The service showcase `pricing` slide explains how engagements are priced, never a figure. "Light User" may be mentioned, never priced.

## Clients and work shown

- **Portfolio** = clients with delivered work or work under way (10 clients in `_src/portfolio_data.py`).
  - Stories are plain bullets (`.st-list`). Directory `did` lists carry NO dates.
  - The clients x services matrix and the "Proposals, concepts and paused work" slide were removed (30 Sep 2026). Never bring them back.
- **Marketing Showcase** = live sites, concepts and pitch microsites (`_src/showcase_data.py`; every URL checked 200).
  - Blue Moon Secret's Chamber and Tri-Comp Solutions are removed (2 Oct 2026). Keep them out.
  - TRE in Singapore shows and links `tre-in-singapore.com`, not the old github.io test address.
- **Prospects:** Convotherm, Move with Ease and others appear in the decks. Confirm with the user before any of it goes outside the team.
- **NDA:** enterprise work under NDA is never named, only counted ("Enterprise work under NDA" slide).
- **SmartPOS** is excluded.
- **No results or metrics** for a client (traffic, revenue, rankings) unless the user supplies them and the client agreed.

## Sample data

- All demos use fictional companies, labelled as samples.
- **Odoo app series:** one sample company runs through all three decks: **Kestrel & Pine Pte Ltd**, with the Sunbird Clinics deal (details and figures in `decks.md`). Keep the figures agreeing across moves and decks.
- **Never use a real company as a sample.** The client's own name in its proposal is the exception.

## Client proposals (Client decks group)

- **Built from the client's requirements** (for Hitachi: the pre-discovery analysis `Downloads\Hitachi - Jett's 2c.md`).
- **Only the client's own public facts**, verified on the client's sites, with the date checked.
- **Pain points are hypotheses** to confirm in discovery, phrased as such.
- **Internal research stays out of the deck, the notes included:** job ads, employee reviews, headcount guesses.
- **Demo data:** every demo is labelled sample data. Response targets come from the client's own contracts.
- **The client's logo** goes beside TechNext's (`data-cobrand`). The lockup on the cover and close uses the client's official logo files only. A logo that breaks on navy (dark parts, transparent gaps) goes on a white rounded tile for dark slides; never recolour it. Near-square marks need about 34px in the header, not the 19px wordmark size.
- **Scope follows the client's own phases.** Anything undecided is marked "to confirm".
- **Send it with its share link,** never the launcher.
- **Client decks from TechNext's own material** (JR-Tech, 2026-10-06): the user's PDF is the source; keep its claims and wording, fix template leftovers (another client's name in a footer), and bring contact lines and the partnership into the house rules (sales@technext.asia, "Odoo Ready Partner"). Check any Odoo claim against the docs; say what was changed in the report.
- **Client decks from an internal document** (BHD Asia, 2026-10-06): when the source is marked internal / for team review, the deck is still for the client unless the user says "internal". Keep the facts, the workflows, the decisions and the open items with their owners; leave out everything said ABOUT the client (frustrations, how often they asked, who resents what), third parties' names that aren't needed, unannounced plans (price rises, dormant entities) and the "confidential" labels. Say in the report what was left out and offer a team-only version.
- **BHD Asia / HummingBeing:** TRE™ in all visible text, speaker notes included (client rule). Isabelle Claus Teixeira is the client; owner chips say "Isabelle".
- **HST Medical (Kowa Subsidiary):** light theme only, and no pricing of any kind in the deck: no figures, no quotation wording, no product prices in demos (user, 7 Oct 2026). The logo is the official colour lock-up with "Kowa Subsidiary"; never recolour it. ® on HST Medical®, Heritage® and Rheuma-Salve® as the live site does; Zoo-Vite without. Product claims only in the label's words, with "Always read the label". The awards wording and the Google rating are unconfirmed by HST: keep them off slides until confirmed.
- **A client logo "properly showcased"** (HST, 2026-10-07): the full official lock-up large on the cover (a white card on navy), a legible no-tagline crop in the slide header, a white tile on dark slides. Build any logo animation from the untouched file (clip-path layers of one image), never from a redrawn or recoloured copy.
- **Odoo Maintenance** is for a company's OWN equipment (e.g. a hire fleet, machines it uses), never for servicing customers' units; customer service visits are Field Service (user, 2026-10-08, JR-Tech).
- **Discovery questions go at the back** (user, 2026-10-06: "question at the back", "at the end of presentation"): a last part before the close, with the questions as tick buttons (answered / follow up) and a copyable follow-up list. Print shows them unticked.
- **Malaysia (JR-Tech):** SST + MyInvois is Odoo's Malaysian localisation inside Accounting (SST-02 reports; Odoo S.A. authorised as MyInvois intermediary on MyTax; pre-production and production modes). List it, never count it as an app. LHDN = Lembaga Hasil Dalam Negeri, Malaysia's tax authority. Money in Malaysia is written "RM 4,820.00".
- **Hitachi specifics** are in `decks.md` and in the memory file `project_hitachi_proposal.md`. Expect the Microsoft Dynamics question (sister company Hitachi Solutions PH sells it).

## Words

- **House voice:** plain, concrete, active. One idea per slide. A headline says the point, and its `.hl` marks the phrase that matters.
- **Spelling:** British (customisation, organise, centre), following technext.asia. Write "Odoo", never "ODOO". Money looks like "S$18,220.44".
- **Kickers** are short, lowercase, in Caveat: "where we are", "how an engagement runs".
- **Speaker notes** say what the presenter says or must know (sources, what's illustrative). They are not a repeat of the slide.
- **The closing slide** is the booking CTA: a 30-minute discovery call, `{{qr:meet}}`, WhatsApp and email.
