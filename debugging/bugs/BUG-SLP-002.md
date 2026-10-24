# BUG-SLP-002: Lesson Plan Settings: Exercises are never saved; add/edit/delete only change the page and are lost when you leave

| Field | Value |
|---|---|
| Checklist row | `SLP-001` in `checklists/42-settings-lessonplans.md` |
| Module | Settings: Lesson Plans |
| Severity | High |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Lesson Plans > Exercises > Add Exercise.
2. Name "BETA TEST ONLY Ex", then Save. It shows in the list.
3. Click edit on it, change the name to "BETA TEST ONLY Ex2", then Save.
4. Go to Settings and Tools, then back to Lesson Plans > Exercises.

## Expected
The exercise is saved to the server, edit renames it, and it's still there when you come back.

## Actual
No request goes to the server on Save (none seen in the network log), and no success message shows. Edit adds a second row ("BETA TEST ONLY Ex" and "BETA TEST ONLY Ex2") instead of renaming. When you come back, the list says "No exercises configured". So exercises can never be set up, and the Exercise Configuration on lessons can't be used. Lesson Plans on the same page do save (POST settings_lessonplans_save, "Ok:14").

## Evidence
- Screenshot: `screenshots/BUG-SLP-002-1.png`, `screenshots/BUG-SLP-002-2.png`
- Console / network errors: none

## Suspected cause (optional)
templates2/settings_lessonplans/index.js saveExercise() and deleteExercise() only change the in-memory exercises array ("// TODO: Implement API integration"), and loadExercises() only re-renders that array. The edit form doesn't carry the id, so data.id is empty and edit takes the "Add new" branch.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
