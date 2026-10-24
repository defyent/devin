# BUG-EXM-010: Taking an exam as a read-only (group-level) user: saves and submit return Access Denied, and Previous/Close/Submit are hidden

| Field | Value |
|---|---|
| Checklist row | `EXM-010` in `checklists/29-exams.md` |
| Module | Personnel Details > Exams (personneldetails) |
| Severity | Medium |
| DataHangar version | v2.0.121 |
| Account / permission level | betatest_grp (BETA TEST ONLY Grpuser, group level) / betatest_low |
| Browser / width | Chrome desktop (UTC time zone), 1600 px |
| Status | Fixed (verified 23/10/2026 v2.0.122) |
| Found / session | 23/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings > Exam Instances > Assign Exam: BETA TEST ONLY Exam, All Questions, Individual, BETA TEST ONLY Grpuser
2. Log in as betatest_grp; Dashboard > Exams > click the exam, then click its row on Personnel Details > Exams
3. Tick an answer, click Next, try Previous / Close / Submit

## Expected
A user can answer, go back, close, reopen and submit an exam assigned to themselves whatever their Personnel Details level; another user's exam is refused.

## Actual
Found 23/10/2026 on v2.0.121: every personneldetails_saveexamprogress returned "Access Denied" and nothing was kept on reopen; Previous, Close (X) and Submit were hidden (page in read-only-mode); Submit on Q10 gave "Failed to Submit Exam: Access Denied" and the attempt stayed Assigned. Retest 23/10/2026 (v2.0.122): fixed. Previous/Next/Close show, saves return Ok, close + reopen resumed with 2 of 10 answered, Submit returned Ok and the Review matches (Q1 BETA 0 correct, Q2 BETA A). Submitting another user's instance (6164) is refused: "Access Denied: You can only submit your own exams". Not tested: progress save on another user's unstarted attempt (none available). Open question: Grpuser can read answers and score of instances 6166/6164 (not his) via personneldetails_getexaminstance; fine if group-level read covers group members' results.

## Evidence
- Screenshot: `screenshots/BUG-EXM-010-1.png`, `screenshots/BUG-EXM-010-2.png`
- Console / network errors: none

## Suspected cause (optional)
applyReadOnlyMode() hid every button not on its skip list, including the exam modal buttons, and the save/submit endpoints checked Personnel Details write access instead of exam ownership. v2.0.122 skips anything inside #exam-modal.

## Test data involved
BETA TEST ONLY Exam instances 6167 (Grpuser) and 6164/6166

## Related
BUG-EXM-006

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
| 23/10/2026 | v2.0.122 | Fixed | See Actual |
