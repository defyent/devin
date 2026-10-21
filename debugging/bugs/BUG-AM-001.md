# BUG-AM-001: New User accepts a 6-character password (placeholder and Change Credentials require 10)

| Field | Value |
|---|---|
| Checklist row | `AM-010` in `checklists/04-access-manager.md` |
| Module | Access Manager |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Access Manager > New User
2. Fill all fields, Password and Confirm = a 6-character value (e.g. 'short1')
3. Click Create User

## Expected
Rejected: 'Password must be at least 10 characters' (placeholder says 'Minimum 10 characters'; Change Credentials needs 10).

## Actual
Toast 'User BETA TEST ONLY Lowperm created successfully'; account created with the 6-char password.

## Evidence
- Screenshot: `screenshots/BUG-AM-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
No min-length check in the New User handler (client and server) for create; only Change Credentials enforces 10.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
