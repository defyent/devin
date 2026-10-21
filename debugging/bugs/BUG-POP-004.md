# BUG-POP-004: Flight Schedule 'View Details' popup does not close with Esc

| Field | Value |
|---|---|
| Checklist row | `FS-013` in `checklists/06-flight-schedule.md` |
| Module | Flight Schedule |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Schedule (week view), click a flight to select it
2. Click its note / View Details icon
3. Press Esc

## Expected
Popup closes (CON-015).

## Actual
Popup stays open; only OK, x or a click outside closes it.

## Evidence
- Screenshot: `screenshots/BUG-POP-004-1.png`
- Console / network errors: none

## Suspected cause (optional)
#flight-details-modal has no keydown Escape handler (same pattern as BUG-POP-001).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
