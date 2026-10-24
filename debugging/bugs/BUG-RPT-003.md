# BUG-RPT-003: Reports tables overlap on a phone: column text is drawn on top of other columns

| Field | Value |
|---|---|
| Checklist row | `RPT-S05` in `checklists/26-reports.md` |
| Module | Reports |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open Administration > Reports at 390px wide (phone)
2. Look at the Report Templates list

## Expected
Readable rows (card layout or stacked columns), no overlapping text.

## Actual
Template Name, Data Source, Columns, Filters, Last Run and Run By text run into each other (e.g. 'QA SMS Filter 107SMS Reports' over '16/10/2026 16:07'); Actions are cut off and need horizontal scroll.

## Evidence
- Screenshot: `screenshots/BUG-RPT-003-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
