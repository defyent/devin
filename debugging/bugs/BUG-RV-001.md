# BUG-RV-001: Roster Viewer: no page Help (?) and Group Visibility popup ignores Escape

| Field | Value |
|---|---|
| Checklist row | `RV-S02` in `checklists/13-roster-viewer.md` |
| Module | Roster Viewer |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Personnel > Roster Viewer
2. Look for the Help (?) button in the page header
3. Click the Group Visibility (people) icon, press Escape

## Expected
A Help (?) button like other modules; Escape closes the Group Visibility popup.

## Actual
No Help button on the page. Group Visibility stays open on Escape; only × or a click outside closes it.

## Evidence
- Screenshot: `screenshots/BUG-RV-001-1.png`, `screenshots/BUG-RV-001-2.png`
- Console / network errors: none

## Suspected cause (optional)
Roster Viewer header has no help-button include and the modal has no keydown Escape handler.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
