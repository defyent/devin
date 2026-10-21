# BUG-RB-001: Roster Builder: no page Help (?); Copy/Paste Instructions popup ignores Escape and outside click

| Field | Value |
|---|---|
| Checklist row | `RB-S02` in `checklists/14-roster-builder.md` |
| Module | Roster Builder |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Roster Builder
2. Look for the Help (?) button
3. Click the copy/paste instructions (?) icon, press Escape, then click outside the popup

## Expected
Standard page Help (?) like other modules; Escape and outside click close popups.

## Actual
Only a 'View copy/paste instructions' icon; no page Help. The Copy/Paste Instructions popup stays open on Escape and outside click; only × or Close work. The cell Note popup ('Note for <name>') also ignores Escape (outside click and x work). Shift Summary popup also ignores Escape (outside click works). Reset Custom Order confirm also ignores Escape. Confirm Live Roster Edit popup also ignores Escape.

## Evidence
- Screenshot: `screenshots/BUG-RB-001-1.png`, `screenshots/BUG-RB-001-2.png`
- Console / network errors: none

## Suspected cause (optional)
Page has no help include; modal lacks Escape/outside-click handlers.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
