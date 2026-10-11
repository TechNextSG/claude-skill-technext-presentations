# QA checklist (before every push)

The script checks what it can. You check the rest by looking. Report what you checked, and never say "verified" for something you did not open.

## Automatic: `python scripts/deck_check.py <decks> --shots [--phone]`

- [ ] The build passes: no unknown token, icon or Odoo icon, no missing site picture, and no share copy leading to another deck.
- [ ] No script errors while every slide plays to its last build, and none in `?print`.
- [ ] No broken images. No text pushed off the 1600 x 900 stage.
- [ ] Every page is `noindex,nofollow`. Asset links carry the current `ASSET_V`.
- [ ] Each share copy exists and has no Home button. The deck is on the launcher and in the README table, with the right slide count.
- [ ] Each WARN was looked at in its shot. Overlaps and cut text are fixed, or explained in the report (for example "the label sits over the map by design").
- [ ] `--phone`: the deck turns when the phone is held upright, with no errors.

## By eye, on the contact sheet and in the preview

- [ ] **Each changed slide** at its first and last build: hierarchy, one `.hl` per headline, nothing crowded, nothing orphaned, balanced left and right, nothing in the chrome band or footer zone.
- [ ] **The whole deck's sheet:** rhythm across slides, dark slides only at the open, the close and a deliberate turn, and no two adjacent slides looking the same.
- [ ] **Overview (`O`):** every slide shows its finished state.
- [ ] **`?print` / PDF sheet** (`deck_pdf.py --look`): every page finished, nothing half-drawn, no striped gridlines, logos visible on dark pages.
- [ ] **Interactions:** click every control on the changed slides. Clicks must not advance the slide by accident. A drag works with a mouse and with touch.
- [ ] **Keys:** → through every build, ← back through them, `N` notes make sense, `T` cast mode still looks right (loops stop, nothing stuck invisible).
- [ ] **Phone upright** (`resize_window` mobile, reload): the deck turns, positions in demos still hit their targets (`Deck.rect`/`Deck.point`), and swipes change slides.
- [ ] **Text:** spelling (British), names, figures, "Odoo Ready Partner", office roles, and no forbidden claim (content-rules). `grep` proves that zero old values remain after a rename.
- [ ] **Sample data** is labelled wherever a demo shows a company or figures.
- [ ] **Launcher:** the card's slide count, description, thumbnails (cover and hover) and buttons work: Present, Kiosk loop, PDF, Share.

## After the push

- [ ] The Pages run succeeded. The live deck returns 200 and contains the change (grep the live HTML).
- [ ] The share copy `s-<token>.html` is live and contains the change.
- [ ] The PDF on the live site is the new one (check its size or bytes).
- [ ] `drive_sync.py` reports 0 failed.
- [ ] The user has `?v=<ASSET_V>` links. Their own browser may hold the old page for 10 minutes.
