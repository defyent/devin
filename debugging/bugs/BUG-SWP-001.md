# BUG-SWP-001: Waypoints Settings: no Help (?), and Escape does not close popups

| Field | Value |
|---|---|
| Checklist row | `SWP-S02` in `checklists/38-settings-waypoints.md` |
| Module | Settings: Waypoints |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Configuration > Waypoint Locations.
2. Look for a Help (?).

## Expected
A Help (?) that explains duplicates, consolidation and coordinate formats.

## Actual
There is no Help button on the page, and Escape leaves the Coordinate Format, Scan for Duplicates and Bulk Add popups open.

## Evidence
- Screenshot: `screenshots/BUG-SWP-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
The template has no help button or help modal.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
