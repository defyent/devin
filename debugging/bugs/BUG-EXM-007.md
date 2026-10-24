# BUG-EXM-007: Exam Instances batch: deleting a person's instance shows success but the row stays until the page is reloaded

| Field | Value |
|---|---|
| Checklist row | `EXM-009` in `checklists/29-exams.md` |
| Module | Exams |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Exam Instances > Browse Batches > open a batch.
2. Add a person (row appears).
3. Click the bin on that person > OK.

## Expected
The row is removed and the batch totals update.

## Actual
Toast 'Exam instance deleted successfully' but the row and the totals (2 TOTAL, 50% complete) stay. After leaving and reopening Exam Instances the row is gone. Adding a person does refresh the list.

## Evidence
- Screenshot: `screenshots/BUG-EXM-007-1.png`, `screenshots/BUG-EXM-007-2.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
