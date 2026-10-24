# BUG-RB-006: Roster Builder: at phone width the shift palette takes half the screen and the Draft Edit Mode banner covers the search box and palette

| Field | Value |
|---|---|
| Checklist row | `RB-S05` in `checklists/14-roster-builder.md` |
| Module | Roster Builder |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Roster Builder, select a draft
2. Resize the window to 390 px wide

## Expected
Grid usable, palette collapsible or below the grid, banner doesn't cover controls.

## Actual
The roster grid gets only about 175 px (names column plus no visible days) while the palette fills the right half. The orange Draft Edit Mode banner sits on top of the search box and the first palette items. The violations toggle and Enable Live Edit are hidden. No page-level sideways scroll.

## Evidence
- Screenshot: `screenshots/BUG-RB-006-1.png`
- Console / network errors: none

## Suspected cause (optional)
No narrow-screen layout for the builder: grid and palette stay side by side and the banner is absolutely positioned.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
