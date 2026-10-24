# BUG-SLP-003: Add Lesson accepts negative hours (Solo Hours -1 is saved and shown as "Solo: -1h")

| Field | Value |
|---|---|
| Checklist row | `SLP-003` in `checklists/42-settings-lessonplans.md` |
| Module | Settings: Lesson Plans |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Lesson Plans > Lessons > Add Lesson.
2. Lesson Plan "BETA TEST ONLY LP2", Name "BETA TEST ONLY Lesson", Dual 1.5, Solo -1, Ground 1, then Save.

## Expected
Hours can't be negative. The save should be refused with a message.

## Actual
"Lesson saved successfully" (server replied Ok:65). The lesson card shows "Solo: -1h".

## Evidence
- Screenshot: `screenshots/BUG-SLP-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
The lesson-*hours inputs have no min="0", and neither saveLesson() nor settings_lessonplans_lessons_save checks the range.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
