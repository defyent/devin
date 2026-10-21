# BUG-DFR-003: Daily Flight Record: changing filters quickly appends results instead of replacing them, showing duplicate and wrong-status rows

| Field | Value |
|---|---|
| Checklist row | `DFR-008` in `checklists/09-daily-flight-record.md` |
| Module | Daily Flight Record |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Sidebar > Flight Operations > Daily Flight Record > expand Advanced Filters
2. Click the Open status pill twice quickly (on, then off)
3. Look at the list: only Completed + Complete Locked are ticked
4. Or: with only Cancelled ticked, quickly click Completed, Complete Locked and Cancelled to get back to the defaults

## Expected
The list always matches the current filters, each flight once (30 Completed rows).

## Actual
Open on/off quickly: 60 rows, 30 Open flights plus 30 Completed, although Open is unticked. Three quick clicks back to the defaults: 90 rows of which 60 are duplicate IDs. Changing one filter at a time (4 s apart) is correct. Seen earlier too: Flight ID 42903 listed twice followed by unfiltered flights.

## Evidence
- Screenshot: `screenshots/BUG-DFR-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
Each filter change starts a new load, and every response is appended to the table; earlier, slower requests are not cancelled or ignored, and the table is not cleared per request.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
