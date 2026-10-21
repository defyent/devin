# BUG-SUP-004: Support: the only permission level is All Access, so regular staff can't raise or see their own tickets

| Field | Value |
|---|---|
| Checklist row | `SUP-008` in `checklists/27-support.md` |
| Module | Support / Access Manager |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Access Manager > any user > Permissions > Support Tickets: the only level offered is A.
2. Log in as BETA TEST ONLY Grpuser (no Support permission) > Administration > Support.
3. Compare with BETA TEST ONLY Second (Support Tickets = A).

## Expected
A regular user can open Support, raise tickets and see only their own. An admin sees all tickets.

## Actual
Grpuser gets 'Access Denied: You do not have permission to access the Support feature', although Support is in their sidebar and the header headset icon. The only way to let staff raise a ticket is All Access, which shows every ticket. There's no 'own tickets' level.

## Evidence
- Screenshot: `screenshots/BUG-SUP-004-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
