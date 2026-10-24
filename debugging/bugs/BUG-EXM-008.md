# BUG-EXM-008: Exam Builder: deleting an exam or exam group that has instances fails silently (error only in the console), and graded instances can't be removed

| Field | Value |
|---|---|
| Checklist row | `EXM-001` in `checklists/29-exams.md` |
| Module | Exams |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Assign an exam and let the person submit it.
2. Exam Builder > exam row > Delete > Confirm.
3. Group header > Delete Group > Confirm.

## Expected
A clear message saying why it can't be deleted, plus a way to archive the exam or remove its instances.

## Actual
The confirm closes, no toast or message, and the exam/group stay. Console only: 'Cannot delete exam: 1 exam instance(s) exist. Exams with instances cannot be deleted.' and the same for the group. Exam Instances only lets you delete unstarted instances, so a test exam that has been taken can never be removed.

## Evidence
- Screenshot: `screenshots/BUG-EXM-008-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
