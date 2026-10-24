# BUG-RV-002: Roster Viewer: clicking a shift does not open Shift Details

| Field | Value |
|---|---|
| Checklist row | `RV-004` in `checklists/13-roster-viewer.md` |
| Module | Roster Viewer |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Personnel > Roster Viewer (October 2026)
2. Click the PM shift for Aisha Johnston on 5 Oct (centre of the badge)
3. Then click the small blue corner on the same badge

## Expected
Clicking a shift opens Shift Details (shift name, times, notes).

## Actual
Clicking the badge does nothing (no popup, no console error). Only the tiny blue corner opens a 'Note for Aisha Johnston' popup with the date and note text.

## Evidence
- Screenshot: `screenshots/BUG-RV-002-1.png`, `screenshots/BUG-RV-002-2.png`
- Console / network errors: none

## Suspected cause (optional)
Only the note-corner element has a click handler; .assigned-shift has none.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
