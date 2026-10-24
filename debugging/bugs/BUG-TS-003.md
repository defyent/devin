# BUG-TS-003: Timesheet Approval list totals don't match Timesheet Details (Rostered Days and Duty Hours)

| Field | Value |
|---|---|
| Checklist row | `TS-002` in `checklists/15-timesheets-leave.md` |
| Module | Timesheets |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > Settings and Tools > Timesheets (October 2026)
2. Read Aisha Johnston's row
3. Click Aisha Johnston to open Timesheet Details

## Expected
Rostered Days and Duty Hours in the list match the details page.

## Actual
List: 13 Rostered Days, 0.0h Duty Hours, 13 Unsigned. Details: 19 Rostered Days, 180 Duty Hours. Every person in the list shows 0.0h. The list's 13 seems to count only days up to today (21 Oct).

## Evidence
- Screenshot: `screenshots/BUG-TS-003-1.png`, `screenshots/BUG-TS-003-2.png`
- Console / network errors: none

## Suspected cause (optional)
List and details compute totals differently: the list appears to count rostered days up to today and duty hours only from saved timesheets.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
