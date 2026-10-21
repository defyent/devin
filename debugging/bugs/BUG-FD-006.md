# BUG-FD-006: Flight can be set to Complete with no times or destination on a leg; no 'Required Information' prompt

| Field | Value |
|---|---|
| Checklist row | `FD-031` in `checklists/07-flight-details.md` |
| Module | Flight Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open flight #42903 in Flight Details (leg 1 has no destination, start/end times).
2. Select status Complete.
3. Click Save Changes.

## Expected
A 'Required Information' popup lists the missing Start/End/destination fields and the flight is not completed.

## Actual
The flight saves as Complete with no prompt. The header badge shows 'Complete' and Delete is hidden. The attached QA Post-Flight Report also has empty required fields.

## Evidence
- Screenshot: `screenshots/BUG-FD-006-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
