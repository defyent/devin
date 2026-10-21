# BUG-TS-006: Leave Types: a validation error closes the Add Leave Type popup and throws away what you typed; the popup ignores Escape

| Field | Value |
|---|---|
| Checklist row | `TS-010` in `checklists/15-timesheets-leave.md` |
| Module | Leave Requests |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Timesheets > Leave Requests (beach icon) > Leave Types > Add Leave Type
2. Type a name, set Colour to ZZZZZZ, click Save
3. Click OK on the error

## Expected
Error is shown with the form still open and the entered values kept; Escape closes the popup.

## Actual
The Add Leave Type popup closes, then 'Colour must be a 6 character hex value, e.g. #3B82F6.' is shown. After OK the form is gone and must be reopened and retyped. Same for an empty name. Escape does nothing on the Add Leave Type popup.

## Evidence
- Screenshot: `screenshots/BUG-TS-006-1.png`
- Console / network errors: none

## Suspected cause (optional)
saveLeaveType() in timesheets/leaverequests.js calls hideTypeModal() before showErrorModal() for both validation errors.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
