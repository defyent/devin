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
4. Give the user the first "Notices" card at WO and Save, then log in as that user and open Notices.

## Expected
Each permission type shows once, or the cards are named or grouped clearly enough to tell them apart.

## Actual
16 names are shown more than once, with no heading or hint to tell them apart: Flight Schedule (ids 2, 209), Dashboard (3, 208), Personnel List (4, 215), Daily Flight Record (5, 213), Personnel Details (6, 216), Roster Viewer (7, 217), Roster Builder (8, 223), File Browser (9, 225), Flight and Duty (10, 31, 218), Notices (11, 219), Safety Reports (13, 30, 221), Hazard Register (14, 222), System Settings (15, 211), Form Builder (16, 224), Exam Builder (18, 232), Access Manager (34, 210). The copies offer different levels: Flight Schedule id 2 offers RA/WA/G, id 209 offers A/RA/WG/RG. An admin can easily give the wrong one. This has a real effect: giving Lowperm the first "Notices" card (id 11) at WO still gives "Access Denied: You do not have permission to access Notices", so the module checks the other Notices card. The first "Flight Schedule" card (id 2) is the one that works for the schedule, so you cannot tell from the name which copy each page uses. Also, BETA TEST ONLY Second with Access Manager WA on one card and A on the other still gets 'You need All Access permission to access the access manager' (AM-018). Retest 22/10/2026 (v2.0.113, accessmanager/index.js?v=2.0.113): part fixed. Each card now shows its module key and id plus a 'Duplicate name' tag (e.g. 'accessmanager · #34 · Duplicate name' and 'accessmanager · #210 · Duplicate name'). But the same 16 names are still duplicated, and both copies show the same module key, so you still can't tell which one the module checks. AM-018 still fails: betatest_two has Access Manager #34=WA and #210=A and still gets 'Access Denied: You need All Access permission to access the access manager'. Retest 2 22/10/2026 (v2.0.113): fixed. The permissions editor now has 47 cards (was 76), with no duplicate names or module keys; the 29 old ids (2-11, 13-28, 30, 31, 34) are gone and each module has one card (e.g. accessmanager #210, notices #219, flightschedule #209). AM-018 now passes: betatest_two (Access Manager #210=A) opens Access Manager, and in Roles the Admin checkbox is disabled ('Only admins can grant admin access'). betatest_grp still opens Flight Schedule, Notices, Roster Viewer and Daily Flight Record after the cleanup.

## Evidence
- Screenshot: `screenshots/BUG-AM-005-1.png`, `screenshots/BUG-AM-005-2.png`, `screenshots/BUG-AM-005-3.png`, `screenshots/BUG-AM-005-4.png`, `screenshots/BUG-AM-005-5.png`, `screenshots/BUG-AM-005-6.png`
- Console / network errors: none

## Suspected cause (optional)
The permission types table has more than one row with the same display name (probably a second set added for a newer module version). The editor lists every row by name only, with no grouping or description.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
