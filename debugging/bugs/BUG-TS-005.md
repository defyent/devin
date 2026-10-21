# BUG-TS-005: Timesheet Details: F&D and Roster Violation popups ignore Escape and show ISO dates in the title

| Field | Value |
|---|---|
| Checklist row | `TS-007` in `checklists/15-timesheets-leave.md` |
| Module | Timesheets |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Timesheets > Aisha Johnston (October 2026)
2. Click the F&D shield on Oct 5, press Escape
3. Click outside to close, then click the warning triangle on the Oct 7 roster shift, press Escape

## Expected
Escape closes the popups; title date in DD/MM/YYYY.

## Actual
Both popups stay open on Escape (outside click closes them). Titles read 'Flight & Duty Analysis for 2026-10-05' and 'Roster Violation Analysis for 2026-10-07'.

## Evidence
- Screenshot: `screenshots/BUG-TS-005-1.png`, `screenshots/BUG-TS-005-2.png`
- Console / network errors: none

## Suspected cause (optional)
timesheetdetails.js has no Escape handler for .active dialogs and puts the raw YYYY-MM-DD date into the title (same as BUG-PD-015).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
