# BUG-AF-003: Active Flights has no page Help (?), and its popups (About Live Tracking, Adjust SAR, Add Note) don't close with Escape

| Field | Value |
|---|---|
| Checklist row | `AF-S02` in `checklists/08-active-flights.md` |
| Module | Active Flights |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Sidebar > Flight Operations > Active Flights
2. Look for the Help (?) button in the page header
3. Click the help icon in the Live Tracking box ('About Live Tracking')
4. Press Escape; look for an x button
5. Click Adjust SAR or Add Note on an OVERDUE row, press Escape

## Expected
Like other modules, a page Help (?) button that opens help; every help popup closes with Got it, x, clicking outside and Escape.

## Actual
No page-level Help (?) button exists (the only help is 'About Live Tracking'). That popup has only 'Got it', no x, and Escape does not close it. Adjust SAR and Add Note popups also stay open on Escape (Add Note with typed text and no prompt). Got it / Cancel and clicking outside do close them.

## Evidence
- Screenshot: `screenshots/BUG-AF-003-1.png`, `screenshots/BUG-AF-003-2.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
