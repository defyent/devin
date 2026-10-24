# BUG-SWAB-004: Weight & Balance Configs: on a phone the page is wider than the screen

| Field | Value |
|---|---|
| Checklist row | `SWAB-S05` in `checklists/35-settings-wab.md` |
| Module | Settings: Weight and Balance |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open Weight and Balance Configs at 390 px wide.
2. Scroll sideways.

## Expected
The page fits the screen; the revision table scrolls in its own box or becomes cards.

## Actual
The document is 651 px wide on a 390 px screen. The 615 px revision table is not in a scroll box (overflow-x: visible), so the whole page scrolls sideways.

## Evidence
- Screenshot: `screenshots/BUG-SWAB-004-1.png`
- Console / network errors: none

## Suspected cause (optional)
The table wrapper has no overflow-x:auto and there is no responsive rule.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
