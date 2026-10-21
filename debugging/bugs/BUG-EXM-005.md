# BUG-EXM-005: Exam Builder on a phone: exam table columns and action icons overlap

| Field | Value |
|---|---|
| Checklist row | `EXM-S05` in `checklists/29-exams.md` |
| Module | Exams |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Training > Exam Builder
2. Resize to 390px wide

## Expected
Exams shown as cards or a readable table with tappable actions.

## Actual
The table is squeezed: Questions/Revision headers overlap, the MASTER/Rev pills sit under the action icons, and the icons overlap the Created date.

## Evidence
- Screenshot: `screenshots/BUG-EXM-005-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
