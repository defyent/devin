# BUG-EXM-004: Exam Builder has no way to link or unlink user groups on an exam group

| Field | Value |
|---|---|
| Checklist row | `EXM-003` in `checklists/29-exams.md` |
| Module | Exams |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Training > Exam Builder (Service Account, permission A)
2. Look at an exam group header (e.g. 'BETA TEST ONLY Exams' or 'Aviation Theory')

## Expected
'User Groups:' badges and an 'Add User Group' button on each exam group, with a remove x on each badge.

## Actual
The group header only has Add Exam and Delete Group. No User Groups row or Add User Group button is shown for any group.

## Evidence
- Screenshot: `screenshots/BUG-EXM-004-1.png`, `screenshots/BUG-EXM-004-2.png`
- Console / network errors: none

## Suspected cause (optional)
createUsergroupBadges() (exambuilder/index.js line 291) builds the User Groups row and Add User Group button but is never called.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
