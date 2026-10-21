# BUG-FD-005: Leg with two unknown waypoints: only the first is offered for adding, the second is silently dropped on save

| Field | Value |
|---|---|
| Checklist row | `FD-022` in `checklists/07-flight-details.md` |
| Module | Flight Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open flight #42903 > Times and Weights > Add Leg
2. Departure 'ZZZQ', Destination 'NZWN' (neither in Settings > Waypoints)
3. Save Changes > 'Add New Waypoint' for ZZZQ > Add Waypoint
4. Back, reopen the flight > Times and Weights

## Expected
You are asked about each unknown waypoint (ZZZQ, then NZWN) before the flight is saved; nothing you typed is lost.

## Actual
Only ZZZQ is prompted ('Waypoint "ZZZQ" added successfully'), then the flight saves straight away and the leg Destination is stored empty - NZWN is lost without a warning. Typing NZWN again and saving does prompt for it.

## Evidence
- Screenshot: `screenshots/BUG-FD-005-1.png`, `screenshots/BUG-FD-005-2.png`
- Console / network errors: none

## Suspected cause (optional)
After 'Add Waypoint' the save continues without re-validating the remaining unknown waypoints, and unknown codes are blanked instead of blocking the save.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
