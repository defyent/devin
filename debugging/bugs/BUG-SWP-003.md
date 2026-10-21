# BUG-SWP-003: Waypoints: the list is not refreshed after you save or delete on the detail page

| Field | Value |
|---|---|
| Checklist row | `SWP-005` in `checklists/38-settings-waypoints.md` |
| Module | Settings: Waypoints |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Waypoint Locations, then open a test waypoint.
2. Change Latitude and click Save Changes ("Waypoint saved successfully"), then go back to the list. It shows the old latitude.
3. Open it again, click delete, then Delete ("Waypoint deleted successfully"). It is still in the list.

## Expected
The list shows the new values straight away, and a deleted waypoint is gone from it.

## Actual
The list keeps the old latitude (-36.85 instead of -41.00), and keeps the deleted waypoint, until you leave Waypoints and come back. Someone may think the save or delete failed and do it again. The detail-page delete popup also uses "Stay on Page / Delete" buttons and does not name the waypoint, while the list delete names it and uses Cancel/Confirm.

## Evidence
- Screenshot: `screenshots/BUG-SWP-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
The detail-page save and delete handlers do not reload or update the cached waypoint list.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
