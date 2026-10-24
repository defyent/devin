# BUG-SWP-004: Waypoints on a phone: table columns overlap and Add Waypoint is off-screen

| Field | Value |
|---|---|
| Checklist row | `SWP-S05` in `checklists/38-settings-waypoints.md` |
| Module | Settings: Waypoints |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open Settings and Tools > Waypoint Locations at a 390 px width.

## Expected
Readable rows (cards or a table that scrolls), with every header button on screen.

## Actual
Code, Latitude, Longitude and Flights are squeezed into a 303 px table, so their text overlaps and can't be read (e.g. "NZAA-37.008056174.791667"). The header button row is 420 px wide, so "Add Waypoint" is cut off at the right edge and the page scrolls sideways.

## Evidence
- Screenshot: `screenshots/BUG-SWP-004-1.png`
- Console / network errors: none

## Suspected cause (optional)
There is no responsive rule for the table cells (no wrap or min-width) or for the header button row (no flex-wrap).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
