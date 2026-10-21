# BUG-PD-010: Personnel Details: the 'Performance' timing panel is shown to users and covers buttons

| Field | Value |
|---|---|
| Checklist row | `PD-024` in `checklists/12-personnel-details.md` |
| Module | Personnel Details |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open any person in Personnel Details
2. Look at the bottom right corner
3. Forms tab > archive a form > open Archived Forms and click Unarchive

## Expected
Debug timing info is hidden from normal users, or at least doesn't cover page controls.

## Actual
A 'Performance' panel (Permission Check, Load Person & Groups ... Total Time) is shown at the bottom right on every load. It sits on top of the Archived Forms Unarchive button, so the click goes to the panel until you close it with its x.

## Evidence
- Screenshot: `screenshots/BUG-PD-010-1.png`, `screenshots/BUG-PD-010-2.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
