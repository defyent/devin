# BUG-FD-005: Leg with two unknown waypoints: only the first is offered for adding, the second is silently dropped on save

| Field | Value |
|---|---|
| Checklist row | `FD-022` in `checklists/07-flight-details.md` |
| Module | Flight Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 23/10/2026 v2.0.120) |
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

Retest v2.0.119 (23/10/2026, #42903): leg 1 Departure BTQA + Destination BTQB (both unknown) > Save > only 'Add New Waypoint "BTQA"' is asked (cancel button still says 'Stay on Page') > Add Waypoint > saves immediately; after reload Destination is empty, BTQB lost. Still fails.

## Evidence
- Screenshot: `screenshots/BUG-FD-005-1.png`, `screenshots/BUG-FD-005-2.png`, `screenshots/BUG-FD-005-3.png`, `screenshots/BUG-FD-005-4.png`
- Console / network errors: none

## Suspected cause (optional)
After 'Add Waypoint' the save continues without re-validating the remaining unknown waypoints, and unknown codes are blanked instead of blocking the save.

index.js submit handler (~L7929-7948) returns at the first unknown waypoint; its onSuccess sets skipWaypointValidation=true and calls form.requestSubmit(), so every remaining waypoint check is skipped. Server stores an unmatched dest as empty instead of rejecting.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
| 23/10/2026 | v2.0.120 | Fixed | Leg BTQC > BTQD: one popup per unknown waypoint; Cancel on the second clears only that field and nothing is saved. Server refusal by direct request not tested. |
