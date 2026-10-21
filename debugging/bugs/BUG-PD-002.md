# BUG-PD-002: Personnel Details modals (Enable 2FA, Setup Error alert): title right-aligned, away from its icon

| Field | Value |
|---|---|
| Checklist row | `PD-027` in `checklists/12-personnel-details.md` |
| Module | Personnel Details > Security |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. My Account > Security
2. Click Enable 2FA

## Expected
Header like other modals: icon then title, left-aligned (e.g. 'Activate Login Access').

## Actual
Lock icon on the far left, 'Enable 2FA' title pushed to the far right of the header. Same on the shared #alert-modal ('Setup Error / Invalid password').

## Evidence
- Screenshot: `screenshots/BUG-PD-002-1.png`, `screenshots/BUG-PD-002-2.png`
- Console / network errors: none

## Suspected cause (optional)
Header uses justify-content: space-between without the title wrapper used by other modals.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
