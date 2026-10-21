# BUG-AM-005: Access Manager: 16 permission types appear twice with the same name (e.g. two "Flight Schedule" cards with different levels)

| Field | Value |
|---|---|
| Checklist row | `PERM-001` in `checklists/90-xc-permissions.md` |
| Module | Access Manager |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Access Manager > User Permissions.
2. Click the Permissions badge on BETA TEST ONLY Lowperm.
3. Scroll through the permission cards.

## Expected
Each permission type shows once, or the cards are named or grouped clearly enough to tell them apart.

## Actual
16 names are shown more than once, with no heading or hint to tell them apart: Flight Schedule (ids 2, 209), Dashboard (3, 208), Personnel List (4, 215), Daily Flight Record (5, 213), Personnel Details (6, 216), Roster Viewer (7, 217), Roster Builder (8, 223), File Browser (9, 225), Flight and Duty (10, 31, 218), Notices (11, 219), Safety Reports (13, 30, 221), Hazard Register (14, 222), System Settings (15, 211), Form Builder (16, 224), Exam Builder (18, 232), Access Manager (34, 210). The copies offer different levels: Flight Schedule id 2 offers RA/WA/G, id 209 offers A/RA/WG/RG. An admin can easily give the wrong one.

## Evidence
- Screenshot: `screenshots/BUG-AM-005-1.png`
- Console / network errors: none

## Suspected cause (optional)
The permission types table has more than one row with the same display name (probably a second set added for a newer module version). The editor lists every row by name only, with no grouping or description.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
