# BUG-RB-008: Roster Builder can only be opened from Settings and Tools, so a Roster Builder user without System Settings can't reach it

| Field | Value |
|---|---|
| Checklist row | `RB-015` in `checklists/14-roster-builder.md` |
| Module | Roster Builder |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. BETA TEST ONLY Grpuser has Roster Builder = WG and no System Settings permission.
2. Log in as betatest_grp and look through every sidebar section.
3. Open Settings and Tools.

## Expected
Roster Builder is in the Personnel menu (next to Roster Viewer), or Settings and Tools shows the pages the user is allowed to use, so a WG roster planner can edit their group's roster.

## Actual
The sidebar has no Roster Builder entry. Personnel only shows Roster Viewer, All Personnel and the groups. Settings and Tools is the only link to Roster Builder, but it needs System Settings. So the Roster Builder WG permission can't be used. Access Manager has the same problem (AM-018).

## Evidence
- Screenshot: `screenshots/BUG-RB-008-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
