# BUG-SWP-002: Waypoints: moving a waypoint about 250 nm saves with no "Significant Location Change" warning

| Field | Value |
|---|---|
| Checklist row | `SWP-006` in `checklists/38-settings-waypoints.md` |
| Module | Settings: Waypoints |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Waypoint Locations, then open waypoint "BETA TEST ONLY WP1" (-36.85, 174.76).
2. Change Latitude to -41.000000.
3. Click Save Changes.

## Expected
A "Significant Location Change" confirmation, since the move is over 1 nm. The code has this check.

## Actual
Saved straight away with "Waypoint saved successfully" and no warning. That move is about 250 nm.

## Evidence
- Screenshot: `screenshots/BUG-SWP-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
In settings_waypoints/index.js the >1 nm check (calculateDistanceNM, then the "Significant Location Change" showModal) is only in the old edit-modal save handler. The detail-page Save Changes path does not call it.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
