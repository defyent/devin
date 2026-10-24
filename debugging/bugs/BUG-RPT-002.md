# BUG-RPT-002: Reports Export CSV writes dates as '2026-10-16 06:00:00' instead of the org date format

| Field | Value |
|---|---|
| Checklist row | `RPT-009` in `checklists/26-reports.md` |
| Module | Reports |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > Reports > Report Results
2. Open 'BETA TEST ONLY Report' (Flights, Scheduled Start Time column)
3. Click Export CSV and open the file

## Expected
Dates as on screen and in Settings > Time Zone: 16/10/2026 06:00.

## Actual
CSV has '2026-10-16 06:00:00' (ISO with seconds). The screen shows 16/10/2026 06:00.

## Evidence
- Screenshot: `screenshots/BUG-RPT-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
exportReportCSV() writes the raw value instead of the formatted one.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
