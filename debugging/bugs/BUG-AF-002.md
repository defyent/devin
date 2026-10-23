# BUG-AF-002: Active Flights lists future flights that have no SAR time, and the stats cards don't count them

| Field | Value |
|---|---|
| Checklist row | `AF-001` in `checklists/08-active-flights.md` |
| Module | Active Flights |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Open (retested 23/10/2026 v2.0.122, not fixed) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Sidebar > Flight Operations > Active Flights
2. Look at the status column and the stats cards

## Expected
Only open flights whose start or SAR time has passed are listed, and Total = Active + Past + Overdue.

## Actual
6 FUTURE flights (#8853, #8854, #8855, #8857, #8858, #8860) are listed with Active Time 00h 00m and SAR Time '01/01/1970 00:00 NO SAR TIME SET'. Cards show Total 1377, Active 0, Past 1364, Overdue 7, so the 6 future flights are in Total but in no other card.

## Evidence
- Screenshot: `screenshots/BUG-AF-002-1.png`, `screenshots/BUG-AF-002-2.png`
- Console / network errors: none

## Suspected cause (optional)
An empty SAR time is stored/treated as 0 (1970), which counts as 'passed', so future flights pass the list filter.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
| 23/10/2026 | v2.0.122 | Not fixed | UTC browser: 6 future flights with no or later SAR still listed as FUTURE (#8878, #8874, #8873, #8879, #8865, #8876); cards Active 0 + Past 1375 + Overdue 7 = 1382 of Total 1388. In an NZ browser the same flights are counted (2 Active, 1379 Past), so this overlaps BUG-AF-004. |
