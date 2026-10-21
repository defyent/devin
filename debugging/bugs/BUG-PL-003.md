# BUG-PL-003: All Personnel: a Read Only Group (RG) user can't open the details of anyone in their group

| Field | Value |
|---|---|
| Checklist row | `PD-029` in `checklists/12-personnel-details.md` |
| Module | Personnel List / Personnel Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. BETA TEST ONLY Grpuser has Personnel List = RG and Personnel Details = RG, and is in BETA TEST ONLY Group.
2. Log in as betatest_grp > Personnel > All Personnel.
3. Click BETA TEST ONLY Lowperm or BETA TEST ONLY Second.

## Expected
The person's details open read-only, because they are in the same group.

## Actual
The rows use cursor: default and clicking does nothing. The list shows the 3 group members, but the RG user can't see any of their details. Their own My Account (header name) opens read-only with no Save button, which is right for RG.

## Evidence
- Screenshot: `screenshots/BUG-PL-003-1.png`, `screenshots/BUG-PL-003-2.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
