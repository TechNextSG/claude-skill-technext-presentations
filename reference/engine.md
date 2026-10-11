# The deck engine

`assets/deck.js` and `assets/deck.css` are shared by every deck. Change them with care: one edit reaches 11 decks, their share copies and every offline copy. After an engine change, run `scripts/deck_check.py` on ALL decks, not just one.

## A deck file (`_src/decks/<slug>.html`)

```html
<!doctype html><html lang="en"><head>
{{head}}                                   <!-- charset, viewport, noindex, theme colour, favicons, fonts, deck.css -->
<title>TechNext Company Profile</title>
<meta name="description" content="...">    <!-- og tags are built from title + description -->
{{og:company-profile}}
<link rel="stylesheet" href="assets/<deck>.css?v={{v}}">
</head>
<body data-label="Company profile" data-home="./">   <!-- label = chrome text top right; data-home = Home button (removed in share copies) -->
<main class="deck" aria-label="..."><div class="stage">
  <section class="slide ..." id="..."> ... </section>
</div></main>
<script src="assets/deck.js?v={{v}}"></script>
<script src="assets/<deck>.js?v={{v}}"></script>
</body></html>
```

Proposals add `data-cobrand="assets/img/clients/<client>.png"` and `data-cobrand-white="..."` to `<body>`. Their logo then sits beside TechNext's on every slide.

## A slide

```html
<!-- 3 · offices -->
<section class="slide" id="offices" data-steps="3" data-title="Three offices, one team">
  <div class="sec-head">
    <span class="kicker" data-in>where we are</span>
    <h2 class="h-m" data-in style="--d:80ms">Three offices, <span class="hl">one team.</span></h2>
    <p class="lead" data-in style="--d:160ms">...</p>
  </div>
  ... content ...
  <aside class="notes"><p>What the presenter says.</p></aside>
</section>
```

- **`id`** is required and must be unique. Hooks, `Deck.goId`, thumbnails and share links all use it.
- **`data-title`** names the slide in the overview, the presenter view and screen readers. Without it, the first h1/h2 is used.
- **Classes:**
  - `dark` gives a navy slide (covers, closes, the odd turn).
  - `cover` removes padding (use it with `.cv-copy`).
  - `plain` gives a white ground.
- **`data-chrome`:**
  - `none` hides the logo, label and footer (covers).
  - `foot` keeps only the footer (closing slides).
- **`data-transition="fade"`** fades the slide in place instead of gliding it (the What is Odoo walkthrough).
- **`data-group="live"`:** consecutive slides of one group CUT instead of fading, so a shared frame (the live Odoo window) holds still.
- **`data-steps="n"`** sets the number of builds when no `[data-step]` elements exist. A script then reads the step in `step()`.
- **`data-dur`** sets the milliseconds this slide stays up in `?kiosk`.
- **Padding:** 118px top, 120px sides, 96px bottom. The chrome (logo and label) sits in the top 92px and the footer at the bottom 34px. Don't put content there.
- **Speaker notes:** every slide has `<aside class="notes">`. `deck_check` warns on a missing one.

## Entrances and builds

| Markup | Effect |
|---|---|
| `data-in` | Animates in when the slide opens: rises 24px and fades over .7s. Stagger with `style="--d:120ms"`. |
| `data-fx="fade\|left\|right\|scale\|blur"` | A different entrance on a `data-in` or `data-step` element. Blur is dropped in TV mode. |
| `data-step="n"` | Appears on the n-th press of → (rises 18px). |
| `data-until="m"` | The element hides again after step m. |
| `data-dim` | The element stays after its step but dims to .38 once the next step arrives. |
| `.hl` | The marker stroke behind one key phrase per headline. It draws in once the slide opens. |
| `.draw` (SVG, `--len`) | A line draws itself in. `.flow` gives moving dashes. |

The rhythm: kicker 0ms, headline 80ms, lead 160ms, then content from about 200ms in steps of 60 to 120ms. Keep a whole slide's entrance under about 1.2s.

## Slide scripts: `Deck.on(id, hooks)`

```js
Deck.on('offices', {
  init: function (s) { /* once at start: wire clicks with s.addEventListener */ },
  enter: function (ctx, s) { /* the slide opened: start demos with ctx timers */ },
  step: function (n, ctx, s, first) { /* build n reached (first = arriving on the slide at step n) */ },
  leave: function (s) { },
  settle: function (s) { /* paint the FINISHED state with no animation: overview, print, PDF */ }
});
```

- **`ctx`** lives for one visit. Everything made through it stops when the slide closes:
  - timers: `ctx.after(ms, fn)`, `ctx.every(ms, fn)`, `await ctx.wait(ms)`;
  - listeners: `ctx.on(el, ev, fn)`;
  - frame loops: `ctx.frame(fn(elapsed))` (return `false` to stop);
  - animation: `await ctx.tween(ms, fn(p), 'out'|'io'|'lin')`, `ctx.count(el, to, {from, dur, dec, pre, suf})` and `ctx.type(el, text, speed)`.

  Never use a bare `setTimeout` or `setInterval` on a slide. A bare timer keeps running after the slide has gone.
- **`settle` is mandatory** for any slide whose finished state comes from JS. Print (`?print`) never runs `enter` or `step`. It shows every build, adds `.is-in`, then runs every `settle`. The overview settles every slide except the current one. A missing settle hook shows up as a half-built page in the PDF.
- **Positions:** use `Deck.rect(el)` and `Deck.point(event)`, never a raw `getBoundingClientRect` or `clientX`. They stay right when a phone turns the deck 90°. Other helpers:
  - `Deck.lbox(el, ref)` gives the layout box in stage pixels, ignoring transforms. It works on HTML only, not SVG (it returns NaN there).
  - `Deck.vbox(el, ref)` gives the visual box, divided by the scale.
  - `Deck.scale` is the current scale.
  - On SVG, map the pointer with `PX.svgAt(e, svg)` (proposal kit) or `getScreenCTM`.
- **Draggable elements:** mark them `data-drag`. The CSS sets `touch-action:none`, so a swipe on them doesn't change slides. Clicks on `a, button, [role=button], [tabindex], [data-i]` never advance the deck. Add `data-i` to a clickable div.
- **Other API:**
  - navigation: `Deck.go(i, step)` (step `-1` means all builds), `Deck.goId(id)`, `Deck.next()`, `Deck.prev()`;
  - state: `Deck.index`, `Deck.step`, `Deck.slides`, `Deck.tv`, `Deck.reduce` (reduced motion), `Deck.print`, `Deck.presenter`;
  - helpers: `Deck.money(n, 'S$')`, `Deck.$`, `Deck.$$`, `Deck.clamp`, `Deck.ease`;
  - the event `deck:slide` (with `detail.index`) fires on the `.deck` element.
- **Jump links (a deck's own script):** `data-go="<slide id>"` plus `data-at="<build>"` for a build. Never put `data-step` on a link: the engine treats it as a build and hides it. JR-Tech's `jrtech.js` and the What is Odoo walkthrough handle `data-go` with one delegated click on `.stage`.
- **Video on a slide** (JR-Tech 16): `<video preload="none" playsinline tabindex="0" poster>` with a `<source ...?v={{v}}>`, a big play button that starts it with sound, chapters that seek (set `currentTime` after `loadedmetadata` when `readyState` is 0), `leave` pauses it. `tabindex` stops Space from also turning the slide. Print and the overview show the poster. For presenter view, sync play/pause/seek over a BroadcastChannel and mute the presenter window. Remux with `ffmpeg -c copy -movflags +faststart` so it streams at once.
- **Video chapters start on the first spoken word**, not on the on-screen label: take word timestamps (`faster-whisper` small, `word_timestamps=True`; music under the voice defeats `silencedetect`) and set `data-t` 0.3-0.6 s before the first word. A jump remembers its target (`at()`), so a media error mid-jump resumes at the chapter, and a jump that lands elsewhere is put right once after 1.8 s.
- **deck.js calls `reg.update()` after registering `sw.js`**, so a fix to the offline worker reaches every browser on its next visit.
- **`sw.js` and video:** a request with a `Range` header goes to the network while there is one, and only offline is it cut from the saved copy as a 206 slice (`ranged()`). Never answer some ranges from the cache and others from the network: Chrome raises a media error on a stream with two sources (it happened once the page had saved the video a few seconds after opening). `poster=` files are saved with the page.
- **Zoom, never the browser's video full screen** (user, 2026-10-06: "make the video can zoom properly and exit seamless back to presentation"): leaving native full screen also drops the deck out of full screen. A video gets the deck's own controls (`jf-ctl`: play, time, seek track with chapter marks, sound, Zoom/Back) and a zoom that grows the frame (FLIP transform from its placeholder box) to the whole 1600 x 900 stage, requests document full screen only if the deck isn't already, holds Esc with `navigator.keyboard.lock(['Escape'])` while zoomed, and shrinks back on Esc / Z / double-click / Back / `ended`. Keys while zoomed are taken in the capture phase on `document`; a clicker's PageDown comes back first, then moves the deck. Hide `.ui`, notes and progress with `.deck.is-vzoom`. The floating controls go after 1.1 s of stillness while playing (0.2 s fade), at once on `mouseleave`, never while hovered, seeking or paused (user, 2026-10-06: "hide floating ui in the video much faster").
- **Tick lists that must survive the meeting** (JR-Tech questions): keep the marks in `sessionStorage` with try/catch, repaint in `settle` without resetting, and never let `settle` wipe what the presenter ticked.
- **The sample-data note** `.illus` sits at `bottom:30px` in deck.css, on top of the slide number. Lift it (`bottom:66–70px`, as What is Odoo and BHD Asia do) on any slide with a footer. `deck_check` does not catch this overlap: look at the bottom-right of every shot.
- **A process played step by step** (BHD Asia `flow()`): steps on the left, a scene card on the right with `data-on` / `data-t`; a Play button runs `ctx.every` with a token so a second click or leaving the slide stops it; step buttons call `Deck.go(Deck.index, n)`. Give `.ew-body` a fixed height and let the step list `space-between`, so 6-step and 9-step slides fill the same frame.
- **Errors:** hook errors are caught and logged, and a broken hook leaves the slide half-built. `deck_check` reports console errors as ERROR.

## Shared libraries

| File | Global | Use |
|---|---|---|
| `fx.js` | `FX` | `FX.orbit(items, {cx,cy,rx,ry,speed,min,fade})` returns tick(t); `FX.along(path, el, p)` follows a path; `FX.fracAtX`; `FX.pointer(ctx, area)` (smoothed parallax); `FX.arc(a, b, bow)`; `FX.svg(tag, attrs, parent)`; `FX.PLANE` (the logo's plane). |
| `ai-demos.js` + `.css` | `AIDemo` | AI vignettes `rag`, `odoo`, `auto`, `chat`. `AIDemo.play(host, kind, ctx, opts)` animates one run; `AIDemo.render(host, kind, opts)` draws the finished state (use it in `settle`). The templates are in `_src/partials/ai-templates.html` (`{{include:ai-templates}}`). Used by the company profile and the service showcase. |
| `proposal.js` + `.css` | `PX` | Sales proposal kit: SVG chart marks (`PX.col`, `hbar`, `rect`, `line`, `area`, `gridY`, `lin`, `lerp`, `morph`), a tooltip `PX.tip(host)`, and pointer mapping `PX.at`/`PX.svgAt`. Marks: bars at most 24px with a 4px rounded data end, 2px lines, end dots of at least 8px, and hairline grids as real elements (`.px-gl`). Palettes: branches #3167CA / #EB6834 / #1BAF7A; ordinal #86b6ef to #104281; status good/warn/crit. |
| `odoo-app.js` + `.css` | `OA` | The Odoo app series' live window and session (see `decks.md`, "Odoo app series"). |
| `tiers.js` + `.css` | (reads `window.TIERS`) | The tier decks: cards, explorer, finder, add-ons and a plan that becomes an email, a WhatsApp message or clipboard text. The tier count comes from the cards (`NAMES.length`, `--last`). |
| `showcase.js` + `.css` | none | Marketing Showcase and Portfolio. Site pictures lazy-load near their slide, the wall filters, and `data-psrc` swaps in the print crops. |

## The CSS kit (`deck.css`)

- **Tokens:**
  - blue: `--blue #3167CA`, `--blue-700 #1E4691`, `--blue-300 #6FA0F5`, `--blue-200`, `--blue-100`, `--blue-050`;
  - text and lines: `--ink #1F1F3D`, `--body #4C4C63`, `--muted #8888A0`, `--line #E7E4E9`, `--alt #FAF9FB`;
  - signals: `--ok`, `--amber`, `--red` (each with a `-050` wash);
  - Odoo: `--odoo #714B67`, `--odoo-050`, `--odoo-teal`;
  - shape and motion: radii `--r 14px`, `--r-lg 20px`, `--r-xl 28px`; shadows `--sh-1`, `--sh-2`, `--sh-blue`; easings `--ease cubic-bezier(.2,.8,.2,1)` and `--ease-io`.
- **Type:**
  - `.h-xl` 92px (covers), `.h-l` 64px, `.h-m` 44px (section titles, the workhorse), `.h-s` 28px;
  - `.lead` 26px (760px measure), body 22px, `.small` 17px;
  - `.kicker` is the Caveat handwritten line (38px, tilted -1.5°); `.eyebrow` is tracked capitals.
  - Fonts: Plus Jakarta Sans (display) and Inter (body), self-hosted in `assets/fonts`. There are no Google Fonts requests.
- **Layout:** `.sec-head` (`--row`), `.split` (`--wide`, `--narrow`), `.row`, `.col`, `.grow`, `.fill`, `.mt-s/m/l`.
- **Components:**
  - `.card`, `.ibadge` (icon tile), `.stat` (`.stat-n` / `.stat-l`);
  - buttons: `.btn` + `-primary`, `-light`, `-ghost`, `-line`;
  - `.seg` (segmented control with `aria-pressed`), `.tag` (`--odoo`, `--ok`, `--line`, `--badge`);
  - `.hint` with `kbd`, `.win` (`.win-bar`, `.win-url`) for an app window;
  - `.illus` (the "illustrative · sample data" foot note);
  - covers: `.cv-copy`, `.cv-logo`, `.cv-tags`, `.cv-hint`; closes: `.ct-h`, `.ct-actions`, `.ct-links`, `.ct-qr` / `.ct-qr-card`.
- **Icons:** `{{icon:name}}` from `_src/icons.json` (the technext.asia set) and `{{odoo:module[:size]}}` (official app icons in `assets/img/odoo/`). The build fails on an unknown name.
- **Class prefixes are per deck** (for example `of-` offices, `lw-` live window, `bk-` breakdown). Before inventing one, grep every stylesheet the deck loads (deck.css + shared + deck css). Prefixes already repeat across decks that never load together (`rm-`, `kb-`, `mk-`, `nw-`, `pm-`, `cv-`).

## Presenting modes (all in deck.js)

- **Keys:**
  - → Space PgDn: next build or slide; ← PgUp: back; Home / End: first or last slide;
  - `O` overview, `F` or `F5` full screen, `N` notes, `P` presenter view (a second window, synced over BroadcastChannel);
  - `B` or `.` black screen, `W` or `,` white;
  - `T` cycles the display mode: auto, HDMI `full`, or Wi-Fi `cast`;
  - a number then Enter jumps to that slide; `?` shows the shortcuts.
- **Mouse and touch:** a click on empty space advances; a swipe changes slides.
- **URL:**
  - `#5` opens slide 5;
  - `?kiosk` or `?kiosk=12` loops on its own (12 s a slide);
  - `?print` prints every slide finished;
  - `?display=full|cast|auto` (the old `?tv` still works);
  - `?presenter` opens the presenter view.
- **TV mode (`.deck.is-tv`):** slides fade in place with no transforms or blur, and the decorative loops stop. It turns on by itself for TV browsers, 4K outputs, machines with 4 cores or fewer, and `?kiosk`. A NEW decorative infinite loop must be added to the `.deck.is-tv … {animation:none}` list in deck.css. Hidden slides already pause their animations. Never animate blur filters. The background glows are radial gradients for this reason.
- **Phones:** a phone (coarse pointer, short side up to 600px) held upright gets `.deck.is-rotated`. The whole deck turns 90°, and the controls live inside `.deck`. A deck under 520px tall gets the smaller `.is-compact` bar.
- **Offline:** on the live https site only, `sw.js` keeps every deck opened once. Pages are network-first. `?v=` files are cache-first, so `ASSET_V` is what refreshes them. Other files are stale-while-revalidate. The cache name is `tn-decks-1`.
- **Reduced motion:** slides only fade, `ctx.after` is clamped to 60ms and tweens to 120ms. Anything you add must still end in its final state.
- **Old TV browsers:** write `inset` as top/right/bottom/left (2020–21 TV browsers lack `inset`). Flex `gap` needs Chromium 84 or later.
