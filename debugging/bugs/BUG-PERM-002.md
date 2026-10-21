# BUG-PERM-002: User with no permissions cannot open their own My Account (no self-service password / 2FA)

| Field | Value |
|---|---|
| Checklist row | `PERM-007` in `checklists/90-permissions.md` |
| Module | Personnel Details / My Account |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Log in as a user with 0 permissions (BETA TEST ONLY Lowperm)
2. Click your name in the top bar

## Expected
Own My Account opens (at least Security and Customize tabs) so the user can change password and set up 2FA.

## Actual
'Access Denied: You do not have permission to access the Personnel Details' for person_id=276 (own record).

## Evidence
- Screenshot: `screenshots/BUG-PERM-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
Personnel Details access check does not allow self (person_id == logged-in person) when no Personnel permission row exists.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
