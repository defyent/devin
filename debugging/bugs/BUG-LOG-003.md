# BUG-LOG-003: 'Trust this device for 30 days' is lost on Logout (logout deletes the trusted-device cookie)

| Field | Value |
|---|---|
| Checklist row | `LOG-010` in `checklists/01-login-auth.md` |
| Module | Login / 2FA (main) |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Log in as a 2FA user, tick 'Trust this device for 30 days', enter a valid code
2. Check cookies: dhkey_trusted_<user> set, expires in 29-30 days
3. Click Logout > Log Out
4. Log in again with username + password

## Expected
2FA page skipped on this browser for 30 days.

## Actual
Logout deletes all cookies (dhkey_<user>, dhkey_trusted_<user>, dhkey_username); the next login asks for the 2FA code again. Trust only survives if the user never logs out. Retest 22/10/2026 (v2.0.112): fixed. After Logout only dhkey_trusted_betatest_low (30 days) is kept; the next login skips the 2FA page.

## Evidence
- Screenshot: `screenshots/BUG-LOG-003-1.png`, `screenshots/BUG-LOG-003-2.png`
- Console / network errors: none

## Suspected cause (optional)
Logout handler expires every dhkey_* cookie; should keep dhkey_trusted_*.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
