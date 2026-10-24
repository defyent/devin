# BUG-TS-004: Timesheet Details shows dates as 'Oct 5' and times with seconds (14:00:00)

| Field | Value |
|---|---|
| Checklist row | `TS-S04` in `checklists/15-timesheets-leave.md` |
| Module | Timesheets |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Timesheets > click a person > Timesheet Details
2. Look at the DATE and ROSTER columns

## Expected
Dates in the configured DD/MM/YYYY (05/10/2026 or 05/10), times as HH:MM.

## Actual
Dates show 'Oct 5' (US month-day, no year) and roster times '14:00:00 02:00:00' with seconds.

## Evidence
- Screenshot: `screenshots/BUG-TS-004-1.png`
- Console / network errors: none

## Suspected cause (optional)
Hard-coded month-day formatting in the timesheetdetails template instead of the Time Zone setting.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
