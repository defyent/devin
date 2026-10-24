# BUG-RV-003: Roster Viewer shift note popup shows the date as 'October 5, 2026', not the configured DD/MM/YYYY

| Field | Value |
|---|---|
| Checklist row | `RV-S04` in `checklists/13-roster-viewer.md` |
| Module | Roster Viewer |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings > Time Zone is DD/MM/YYYY
2. Personnel > Roster Viewer, click the blue corner of Aisha Johnston's 5 Oct shift

## Expected
Date: 05/10/2026

## Actual
Date: October 5, 2026

## Evidence
- Screenshot: `screenshots/BUG-RV-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
Popup uses toLocaleDateString with a hard-coded long format instead of the shared date formatter.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
