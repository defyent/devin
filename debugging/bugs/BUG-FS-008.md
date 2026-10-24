# BUG-FS-008: Flight Schedule: a group-level user (G / WG) sees no flights, even on aircraft in their own group

| Field | Value |
|---|---|
| Checklist row | `FS-027` in `checklists/06-flight-schedule.md` |
| Module | Flight Schedule |
| Severity | High |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Aircraft ZK-BTO (BETA TEST ONLY R) has User Group Assignments = BETA TEST ONLY Group.
2. BETA TEST ONLY Grpuser is a member of BETA TEST ONLY Group (On Roster) and has Flight Schedule = G on the first card and WG on the second (BUG-AM-005).
3. Flights #42909 (PIC Grpuser, 22/10 10:00-11:00) and #42910 (22/10 08:00-09:00) are on ZK-BTO.
4. Log in as betatest_grp > Flight Schedule > week of 19-25 Oct, then list view, then Group By = BETA TEST ONLY Group.

## Expected
ZK-BTO and its flights #42909 and #42910 are shown, including the user's own PIC flight.

## Actual
Week view shows no aircraft rows or events. List view says 'No events to display', even with Group By = BETA TEST ONLY Group ('Showing only aircraft and personnel in the "BETA TEST ONLY Group" group'). Daily Flight Record (RG) lists #42909 for the same user, so the data is there. Group memberships in Access Manager only have an 'On Roster' flag, with no read/write flag (§14 caveat). Retest 22/10/2026 (v2.0.114, assets ?v=2.0.114): fixed. betatest_grp (Flight Schedule #209=WG, member of BETA TEST ONLY Group) now sees ZK-BTO with #42909 and #42910 in week view, list view and Group By = BETA TEST ONLY Group. No script errors.

## Evidence
- Screenshot: `screenshots/BUG-FS-008-1.png`, `screenshots/BUG-FS-008-2.png`, `screenshots/BUG-FS-008-3.png`, `screenshots/BUG-FS-008-4.png`, `screenshots/BUG-FS-008-5.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
