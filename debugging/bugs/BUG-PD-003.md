# BUG-PD-003: 2FA setup: one wrong verification code closes the setup dialog and issues a new secret

| Field | Value |
|---|---|
| Checklist row | `PD-027` in `checklists/12-personnel-details.md` |
| Module | Personnel Details > Security |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. My Account > Security > Enable 2FA, enter password, Confirm
2. Scan the QR code / note the key
3. Enter a wrong 6-digit code, click Verify and Enable
4. Click OK on '2FA Setup Failed - Error: Invalid verification code'

## Expected
Setup dialog stays open with the same QR/key so the user can retry the code.

## Actual
Setup dialog closes. Clicking Enable 2FA again generates a new key and new backup codes, so the entry already added to the authenticator app is useless and must be deleted and re-scanned.

## Evidence
- Screenshot: `screenshots/BUG-PD-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
Verify failure handler closes #2fa-setup-modal and discards the pending secret.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
