# BUG-DSH-005: Dashboard Project Tasks: clicking a task opens an empty project list instead of the project

| Field | Value |
|---|---|
| Checklist row | `DSH-011` in `checklists/05-dashboard.md` |
| Module | Dashboard |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Project 'BETA TEST ONLY TT DSH' (#14) has user group BETA TEST ONLY Group, with task 'BETA TEST ONLY Task for Second' in component/feature.
2. Assign the task to BETA TEST ONLY Grpuser (Task Tracker = WG, member of BETA TEST ONLY Group).
3. Log in as betatest_grp > Dashboard > Project Tasks tab > click the task.

## Expected
The project opens with the task visible, as it is for an admin.

## Actual
The URL goes to ?action=tasktracker&project_id=14 but the page shows 'Projects ... No projects yet', so the user can't see the project their task is in. With BETA TEST ONLY Second (no Task Tracker permission) the same click gives Access Denied, even though tasks can be assigned to them.

## Evidence
- Screenshot: `screenshots/BUG-DSH-005-1.png`, `screenshots/BUG-DSH-005-2.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
