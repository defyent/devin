# BUG-SST-002: New Shift Type: Duty Start/End Time default to the current UTC time

| Field | Value |
|---|---|
| Checklist row | `SST-002` in `checklists/39-settings-shifttypes.md` |
| Module | Settings: Shift Types |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Roster Shifts > pick a group > New Shift Type.
2. Look at Duty Start Time and Duty End Time.

## Expected
Empty duty times (most shifts here have none), or the local time if a default is wanted.

## Actual
Both show 14:02, which is the UTC time. Local time was 03:02 (Pacific/Auckland). If you save without changing them you get a 0-hour duty at a UTC time.

## Evidence
- Screenshot: `screenshots/BUG-SST-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
The DateTimePicker is given new Date() in UTC (same pattern as BUG-FS-001, SMS-002 and FBLD-002), and the duty times are not left empty when unset.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
