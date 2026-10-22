# BUG-SFS-001: Flight Schedule settings: Slot Duration + goes past 120 and typed values over 120 are accepted

| Field | Value |
|---|---|
| Checklist row | `SFS-003` in `checklists/31-settings-flightschedule.md` |
| Module | Settings: Flight Schedule |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Operations > Flight Schedule
2. Click + on Schedule Slot Duration repeatedly
3. Type 200 in the box

## Expected
Value stays between 5 and 120 (the input has min 5, max 120, step 5), and + is disabled at 120.

## Actual
+ keeps going (135 after 26 clicks from 5) and 200 typed in stays 200. − stops at 5 correctly and typing 7 snaps to 5. handleUpdate() sends the value without checking it, so an out-of-range slot size can be saved. Retest 22/10/2026 (v2.0.114, assets ?v=2.0.114): still failing. + still goes past 120 (25 clicks reach 155, + never disables) and typed 200 is kept with Update Changes enabled.

## Evidence
- Screenshot: `screenshots/BUG-SFS-001-1.png`, `screenshots/BUG-SFS-001-2.png`
- Console / network errors: none

## Suspected cause (optional)
handleNumberInput() caps the decrement with Math.max(5, ...) but has no Math.min(120, ...) on increment; handleUpdate() does parseInt only.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
