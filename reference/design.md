# Design system: "The Working Presentation"

This is condensed from `DESIGN.md` in the clone, which has the full token list (impeccable format, written 2026-10-02 and untracked). Read the full file for a redesign or a new kind of slide. For design critique and polish, the `impeccable` and `web-design-engineer` skills work with it: the Odoo app series was built and reviewed that way.

## The idea

Every deck is a fixed 1600 x 900 stage that behaves like the thing it sells. Maps answer a click, pipelines move, and Odoo screens do the work in front of the room. The stage scales whole to the screen and NEVER reflows: there are no breakpoints inside a deck.

- **Density for presenting:** one idea per slide, 44px titles, 22px body. It must read on a projector, a TV and a phone held sideways.
- **Light slides:** a lilac-white paper (#FAF9FB), a faint blue dot grid (34px pitch, 13% blue) and two slow glows. Text is deep ink (#1F1F3D).
- **Dark slides** (navy #0F2350 → #1E4691 → #2D5DB8 at 140°) open and close a deck. An incumbent deck may use one more dark slide at a turn; the Odoo series uses exactly two.
- **Brand blue (#3167CA) points:** one marker-stroked phrase per headline, the pressed control, the progress rule.

## Named rules (keep them)

- **One Marker:** every headline has exactly one `.hl` phrase (blue over an 18% blue marker band that draws in). On dark slides it is white over 60% sky blue.
- **Two Palettes:** inside a live Odoo window, plum (#714B67) is the only action colour and teal (#017E84) the only link colour, and blue appears only as an avatar fill. Outside the window, blue leads, and plum marks only what belongs to Odoo (the Odoo tag, the press cue, Odoo's own app names).
- **Paper Ground:** light slides sit on the paper and dot grid. Don't put a flat white or colour field behind a whole slide (use `.plain` only when needed).
- **Product Voice:** inside the window, type drops to product sizes (11–18px Inter). Deck-scale type never enters the window.
- **Lifted Window:** on a move slide the window is the one lifted object. Inside it everything is flat, split by 1px hairlines. Only a dialog, a PDF page or a phone casts its own shadow.
- **Held Frame:** consecutive slides that share the window carry one `data-group` and cut, so the frame never moves.
- **One Ready Control:** each move readies exactly one control (a plum ring breathing over 2.4s). Pressing → or clicking it performs the move, after which it greys out.
- **Toast Lane:** keep a 64px lane at the window's foot for the move's toast.
- **Rings, not shadows, signal state:** a plum ring is the control to press, a blue ring the current step or the selected place.

## Type

| Role | Font, weight, size, line height | Class |
|---|---|---|
| Display (cover, close) | Plus Jakarta Sans 800, 92px, 1.02, -0.025em (84px beside the series cover window) | `.h-xl` |
| Headline | 800, 64px, 1.06 (incumbent decks only) | `.h-l` |
| Title (the workhorse) | 750 (renders 800), 44px, 1.12, balanced | `.h-m` |
| Card title | 750, 27–28px | `.h-s` |
| Lead | Inter 400, 26px, 1.5, 760px measure | `.lead` |
| Body | Inter 400, 22px, 1.5 (19px in cards) | body |
| Small | 17px | `.small` |
| Hand kicker | Caveat 600, 38px, tilted -1.5°, lowercase, blue (ice blue #A9C8FF on dark) | `.kicker` |
| Label | Plus Jakarta Sans 600, 15px, tracked .14em, uppercase | `.s-label`, `.eyebrow` |

Both faces ship as four static weights each (Jakarta 500–800, Inter 400–700), so 650 renders as 700 and 750 as 800. Secondary text under 18px uses #6C6C80 (5.1:1 contrast). `deck_check` warns under 11px.

## Colour roles

- **Blue:** `--blue` #3167CA does the pointing. Hover is navy #1E4691; ends of the progress rule and focus are sky #6FA0F5; quiet borders #A9C4F5 and #DDE7F8; tag and icon-tile fills are the wash #EAF0FB.
- **Text and lines:** ink #1F1F3D, body #4C4C63, chrome grey #8888A0 (only for the engine's 14–16px chrome), hairline #E7E4E9.
- **Signals:**
  - deck set: green #137A4A / #E8F5EE, amber #A96B00 / #FFF4DF, red #B4372B / #FBEDEB;
  - window badges: #14703F on #E3F4EA, #016A70 on #E1F1F2, #8A5A00 on #FFF1D6, #A6312A on #FBE6E3;
  - "Reconciled" green #1E7E34 for PAID and WON stamps.
- **Proposal charts:** branches #3167CA / #EB6834 / #1BAF7A; ordinal #86b6ef → #104281. Use the `dataviz` skill to validate any new palette.

## Space, shape, depth

- **Frame:** 118 top, 120 sides, 96 bottom. The chrome band is the top 92px; the footer is 34px up; a 5px progress rule runs along the foot.
- **Rhythm:** a section head 40px above content; vertical steps 16 / 32 / 52; a 24px gap in a row; split columns 72px apart.
- **Corners:** 14 for buttons and segments, 16 for icon tiles and the window, 20 for cards, 28 for the QR card. Inside the window: 8 for sheets, 6 for buttons and inputs, 4 for facets, 10 for dialogs. Tags are pills.
- **Shadows** are ink-tinted and wide (`--sh-1` rest, `--sh-2` lift, `--sh-blue` primary button). Dark slides use no card shadows.
- **Dashed lines** mean work done by hand or not yet finished.

## Motion

- **Curves:** one ease-out `cubic-bezier(.2,.8,.2,1)` for everything; the in-out `cubic-bezier(.65,0,.35,1)` only for loops and drawn lines.
- **Moves:** slides glide 56px and cross-fade; entrances rise 24px in short staggers; builds rise 18px.
- **Loops:** anything off screen pauses. Decorative loops must be listed under `.deck.is-tv` so TV and casting mode stops them.
- **Banned:** never animate `filter: blur` or use big blurred layers (the 4K TV stutter of 2026-09-30). Use radial gradients for glows, and no `backdrop-filter` on things that move.
- **Reduced motion:** fade only. Every demo must still land in its final state.
- **No hover lifts** on cards and buttons. They shook when the pointer rested on an edge (2026-09-28).

## The craft floor (what the user praised and asked for)

- **Interactive, not illustrated:** something on most slides answers a click, a drag, a filter or a press of →.
- **Real-looking product screens,** simplified but true to the product's own labels, on labelled sample data.
- **One idea per slide,** with the headline making the point. Copy short enough to read from the back of a room.
- **Finished in print:** every slide's end state is designed, because the PDF and the overview show it.
- **The series thesis** ("no feature grids, icon bullets or static screenshots") belongs to the Odoo app series. The incumbent decks may use cards and icon badges.
