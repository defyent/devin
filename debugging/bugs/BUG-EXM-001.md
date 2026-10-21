# BUG-EXM-001: Exam Builder/Editor have no page Help (?); Escape doesn't close Add Group, Add Exam or Choose Question Type

| Field | Value |
|---|---|
| Checklist row | `EXM-S02` in `checklists/29-exams.md` |
| Module | Exams |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Training > Exam Builder
2. Look for a Help (?) button
3. Click Add Group, press Escape

## Expected
Help (?) like other modules; Escape closes the popup.

## Actual
No page Help (the help_outline icons on each exam row have no title or action). Add Group / Add Exam stay open on Escape; only outside click, x or Cancel close them. Escape is only handled in the confirm popups. In the Exam Editor, Escape also doesn't close Choose Question Type.

## Evidence
- Screenshot: `screenshots/BUG-EXM-001-1.png`, `screenshots/BUG-EXM-001-2.png`
- Console / network errors: none

## Suspected cause (optional)
Only showConfirm/showAlert add an Escape listener; the global keydown handles Enter only.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
