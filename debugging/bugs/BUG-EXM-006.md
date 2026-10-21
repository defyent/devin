# BUG-EXM-006: Taking an exam: Multi-Response checkboxes toggle twice, so clicking the box does nothing and the saved answer can differ from what is ticked

| Field | Value |
|---|---|
| Checklist row | `EXM-010` in `checklists/29-exams.md` |
| Module | Exams |
| Severity | High |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Assign an exam with a Multi-Response question to a user.
2. Log in as that user > My Account > Exams > click the exam.
3. On the Multi-Response question click directly on a checkbox, then on an option's text.

## Expected
Each click ticks or unticks the option once, and the answer saved is what is ticked on screen.

## Actual
Clicking the checkbox square leaves it unchanged. renderMultiResponse() in personneldetails/index.js adds a click handler on the option row that flips checkbox.checked and the answers list, so a click on the box (native toggle + row handler) cancels out, and a click on the label fires the row handler twice. In my run the review showed 'Your Answer: BETA 1' while BETA 0 was the one I had just ticked, and the question was marked Incorrect.

## Evidence
- Screenshot: `screenshots/BUG-EXM-006-1.png`, `screenshots/BUG-EXM-006-2.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
