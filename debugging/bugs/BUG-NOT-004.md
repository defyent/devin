# BUG-NOT-004: Notices: a Write Group (WG) user gets 'An error occurred' when clicking New Notice

| Field | Value |
|---|---|
| Checklist row | `NOT-004` in `checklists/17-notices.md` |
| Module | Notices |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. BETA TEST ONLY Grpuser has Notices = WG and is a member of BETA TEST ONLY Group.
2. Log in as betatest_grp > Notices > New Notice.

## Expected
New Notice opens, and only the user's own groups (BETA TEST ONLY Group) can be picked.

## Actual
An 'Error: An error occurred.' popup appears and no form opens, so a WG user can't create a notice. The list itself works and shows notice #1189.

## Evidence
- Screenshot: `screenshots/BUG-NOT-004-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
