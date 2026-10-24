# BUG-TT-004: Task Tracker: a Write Group (WG) user is treated as read-only and can't add a project

| Field | Value |
|---|---|
| Checklist row | `TT-006` in `checklists/25-task-tracker.md` |
| Module | Task Tracker |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. BETA TEST ONLY Grpuser has Task Tracker = WG and is in BETA TEST ONLY Group.
2. Log in as betatest_grp > Administration > Task Tracker.
3. Hover over or click Add Project.

## Expected
A WG user can create and edit projects for their own groups. Only RA/RG users are read-only.

## Actual
Add Project is disabled with the tooltip 'You have read-only access'. The list says 'No projects yet', so a WG user can't use Task Tracker at all.

## Evidence
- Screenshot: `screenshots/BUG-TT-004-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
