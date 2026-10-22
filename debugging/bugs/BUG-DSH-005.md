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
The URL goes to ?action=tasktracker&project_id=14 but the page shows 'Projects ... No projects yet', so the user can't see the project their task is in. With BETA TEST ONLY Second (no Task Tracker permission) the same click gives Access Denied, even though tasks can be assigned to them. Retest 22/10/2026 (v2.0.111): unchanged. With new project #15 the click now goes to ?action=tasktracker&project_id=15&task_id=468 and still shows 'No projects yet'. Second still gets Access Denied. Even an admin opening that URL lands on the project list, not the project. Retest 2 22/10/2026 after the Task Tracker update: fixed. Grpuser and Second both open the project from the Dashboard with their task highlighted.

## Evidence
- Screenshot: `screenshots/BUG-DSH-005-1.png`, `screenshots/BUG-DSH-005-2.png`, `screenshots/BUG-DSH-005-3.png`, `screenshots/BUG-DSH-005-4.png`, `screenshots/BUG-DSH-005-5.png`, `screenshots/BUG-DSH-005-6.png`, `screenshots/BUG-DSH-005-7.png`
- Console / network errors: none

## Suspected cause (optional)
For betatest_grp (Task Tracker WG, member of group 103 which is on project #15), ?action=tasktracker_json returns userPermission 'read' and projects []. The server isn't reading the group-level permission or the project's usergroup_ids. Task Tracker also doesn't read project_id/task_id from the URL to open the project.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
