# BUG-RB-004: Roster Builder: Rule Violations popup shows 'Monday, October 5' instead of the configured DD/MM/YYYY date

| Field | Value |
|---|---|
| Checklist row | `RB-S04` in `checklists/14-roster-builder.md` |
| Module | Roster Builder |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Roster Builder, select a draft
2. Turn the violations toggle ON
3. Click the warning triangle on a flagged shift (Aisha Johnston, 5 Oct)

## Expected
Date shown in the Time Zone setting format, e.g. Monday 05/10/2026.

## Actual
'For Aisha Johnston on Monday, October 5:' - US long format, no year. Same issue as BUG-RV-003 in Roster Viewer.

## Evidence
- Screenshot: `screenshots/BUG-RB-004-1.png`
- Console / network errors: none

## Suspected cause (optional)
Popup builds the date with toLocaleDateString('en-US', ...) instead of the shared date formatter.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
