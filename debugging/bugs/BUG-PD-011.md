# BUG-PD-011: Personnel Details > Security: Change Password always fails with 'Invalid Action: change_password'

| Field | Value |
|---|---|
| Checklist row | `PD-026` in `checklists/12-personnel-details.md` |
| Module | Personnel Details |
| Severity | High |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. As Service Account: All Personnel > BETA TEST ONLY Lowperm > Security tab
2. Enter the correct current password, a new 14-character password twice
3. Click Change Password

## Expected
'Password changed' and the new password works; a wrong current password gives a clear 'Current password is incorrect' message.

## Actual
Both with the correct and with a wrong current password: 'Password Change Failed - Invalid Action: change_password'. The password is not changed. The client-side checks work: empty fields 'Please fill in all password fields', short 'New password must be at least 8 characters long', mismatch 'New passwords do not match'. Same result when betatest_low changes its own password from My Account (header name > own Personnel Details > Security).

## Evidence
- Screenshot: `screenshots/BUG-PD-011-1.png`, `screenshots/BUG-PD-011-2.png`, `screenshots/BUG-PD-011-3.png`
- Console / network errors: none

## Suspected cause (optional)
The page posts action=change_password, which the server doesn't recognise (missing or renamed handler).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
