# BUG-EXM-009: Exams: a hotspot question with no image shows a developer debug message to the person taking the exam

| Field | Value |
|---|---|
| Checklist row | `PD-017` in `checklists/12-personnel-details.md` |
| Module | Exams |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Exam 'BETA TEST ONLY Exam' has hotspot question 'BETA TEST ONLY hotspot question' (Question ID 67) with no image saved.
2. Assign it to BETA TEST ONLY Second.
3. Log in as betatest_two > Dashboard > Exams > open the exam > go to question 10.

## Expected
The builder refuses to publish a hotspot question without an image, or the exam shows a plain message. No debug text is shown to users.

## Actual
Question 10 shows 'No image available for this hotspot question Debug: BACKEND_UPDATED: No image_data found in database row Question ID: 67'. The question can't be answered.

## Evidence
- Screenshot: `screenshots/BUG-EXM-009-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
