# BUG-POP-001: Error modal ('Failed to Create User') does not close with Esc

| Field | Value |
|---|---|
| Checklist row | `AM-S03` in `checklists/04-access-manager.md` |
| Module | Access Manager (shared errorModal) |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Access Manager > New User
2. Username 'root', fill the rest, Create User
3. Error modal 'Failed to Create User - That username is not allowed' opens; press Esc

## Expected
Esc closes it (as Help does on the same page).

## Actual
Modal stays open; only OK closes it. Same as the logout confirm (BUG-LOG-002). Retest 22/10/2026 (v2.0.113, accessmanager/index.js?v=2.0.113): fixed. Esc closes the 'Failed to Create User - That username is not allowed' error modal.

## Evidence
- Screenshot: `screenshots/BUG-POP-001-1.png`, `screenshots/BUG-POP-001-2.png`
- Console / network errors: none

## Suspected cause (optional)
#errorModal has no keydown Escape handler.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
