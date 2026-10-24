# BUG-SWAB-002: Weight & Balance Configs: dates show as "14 Oct 2026" / "29 Sept 2026" instead of DD/MM/YYYY

| Field | Value |
|---|---|
| Checklist row | `SWAB-S04` in `checklists/35-settings-wab.md` |
| Module | Settings: Weight and Balance |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings > Time Zone date format is DD/MM/YYYY.
2. Open Weight and Balance Configs.
3. Look at the Active Master card and the Date / Approved columns in Revision History.

## Expected
14/10/2026, 29/09/2026

## Actual
"Approved 14 Oct 2026", "29 Sept 2026" (a browser-locale format).

## Evidence
- Screenshot: `screenshots/BUG-SWAB-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
Uses toLocaleDateString instead of the shared date formatter.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
