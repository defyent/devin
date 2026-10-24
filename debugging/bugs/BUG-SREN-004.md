# BUG-SREN-004: Recency & Renewals Settings on a phone: table columns overlap each other

| Field | Value |
|---|---|
| Checklist row | `SREN-S05` in `checklists/41-settings-renewals.md` |
| Module | Settings: Recency and Renewals |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Recency and Renewals > Recencies.
2. Make the window 390 px wide.

## Expected
The table scrolls inside its card or switches to a card layout, and the text stays readable.

## Actual
The page doesn't scroll sideways and the tabs become a dropdown, which is good. But the columns are squeezed together: Days numbers sit on top of the names ("Landings90", "Approaches180"), the Warning Value / Caution Value headers run into each other, and the edit pencil covers the "Pilot Licenses" pill.

## Evidence
- Screenshot: `screenshots/BUG-SREN-004-1.png`
- Console / network errors: none

## Suspected cause (optional)
The table keeps 6 columns at narrow widths, with no overflow wrapper or card layout below 768 px.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
