# BUG-EXM-011: Taking an exam: "N of 10 questions answered" and the navigator tick only update after moving to another question

| Field | Value |
|---|---|
| Checklist row | `EXM-010` in `checklists/29-exams.md` |
| Module | Personnel Details > Exams (personneldetails) |
| Severity | Low |
| DataHangar version | v2.0.121 |
| Account / permission level | betatest_grp (BETA TEST ONLY Grpuser, group level) / betatest_low |
| Browser / width | Chrome desktop (UTC time zone), 1600 px |
| Status | Fixed (verified 23/10/2026 v2.0.122) |
| Found / session | 23/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open an assigned exam
2. Tick an answer on question 1 and look at the counter under the navigator

## Expected
"1 of 10 questions answered" and the Q1 tick appear straight away; unticking decrements straight away.

## Actual
Found 23/10/2026 on v2.0.121: stayed "0 of 10" until Next/Previous redrew the navigator. Retest 23/10/2026 (v2.0.122): fixed. Ticking BETA 0 shows "1 of 10" at once, unticking "0 of 10", ticking by text "1 of 10", and the Multiple Choice pick on Q2 "2 of 10". True/False, sequence, matching, hotspot etc. not tested live (code calls the update for them too).

## Evidence
- Screenshot: `screenshots/BUG-EXM-011-1.png`
- Console / network errors: none

## Suspected cause (optional)
Answer change handlers saved progress but did not call updateQuestionNavigator(); v2.0.122 calls it after every answer change.

## Test data involved
BETA TEST ONLY Exam instances 6167 (Grpuser) and 6164/6166

## Related
BUG-EXM-006

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
| 23/10/2026 | v2.0.122 | Fixed | See Actual |
