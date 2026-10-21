# BUG-PD-014: Digital Signature: wrong password closes the popup and throws away the drawing; empty Save gives no message

| Field | Value |
|---|---|
| Checklist row | `PD-007` in `checklists/12-personnel-details.md` |
| Module | Personnel Details |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. All Personnel > BETA TEST ONLY Lowperm > Personal Details > Create Signature
2. Click Save Signature with nothing drawn and no password
3. Draw a signature, enter a wrong password, click Save Signature

## Expected
Empty drawing or password shows a message such as 'Please draw your signature' / 'Enter your password'. A wrong password shows the error and keeps the popup open with the drawing, so the user can retype the password.

## Actual
Save with nothing drawn or no password does nothing at all, with no message. A wrong password shows 'Save Failed - Incorrect password' and closes the Create Signature popup, so the drawing is lost and must be redrawn. The correct password saves ('Digital signature saved successfully').

## Evidence
- Screenshot: `screenshots/BUG-PD-014-1.png`, `screenshots/BUG-PD-014-2.png`
- Console / network errors: none

## Suspected cause (optional)
Save handler returns silently on empty input, and the error path closes the modal before showing the alert.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
