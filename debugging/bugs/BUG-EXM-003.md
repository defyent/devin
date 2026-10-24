# BUG-EXM-003: Exam viewer 'Read Only' still shows Add Question, Add Group and Save Question

| Field | Value |
|---|---|
| Checklist row | `EXM-004` in `checklists/29-exams.md` |
| Module | Exams |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Training > Exam Builder
2. On a MASTER exam click View (Read Only)
3. Open any question

## Expected
Read-only view hides or disables Add Question, Add Group, Save Question and the option editors.

## Actual
Banner says 'Viewing Master exam (Rev 2) - Read Only' but Add Question, Add Group and each question's Save Question / Add Image / Add Option are shown (external FUNC-05 still present).

## Evidence
- Screenshot: `screenshots/BUG-EXM-003-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
