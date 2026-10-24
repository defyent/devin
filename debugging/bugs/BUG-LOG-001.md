# BUG-LOG-001: Login Message popup reappears on every browser reload

| Field | Value |
|---|---|
| Checklist row | `LOG-013` in `checklists/01-login-auth.md` |
| Module | Shell (main) |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Log in and close the Login Message with OK
2. Press F5 / reload on any page

## Expected
Guide: Login Message is shown after login (once per login).

## Actual
The Login Message opens again after every reload. Guide or app? Retest 22/10/2026 (v2.0.112): fixed. The Login Message shows after login, and doesn't come back after two reloads.

## Evidence
- Screenshot: `screenshots/BUG-LOG-001-1.png`, `screenshots/BUG-LOG-001-2.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
