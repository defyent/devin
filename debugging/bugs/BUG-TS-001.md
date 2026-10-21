# BUG-TS-001: Timesheet Approval has no page Help (?)

| Field | Value |
|---|---|
| Checklist row | `TS-S02` in `checklists/15-timesheets-leave.md` |
| Module | Timesheets |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > Settings and Tools > Timesheets
2. Look for the Help (?) button in the page header

## Expected
Standard Help (?) button opening the page help popup.

## Actual
No Help button anywhere on the page.

## Evidence
- Screenshot: `screenshots/BUG-TS-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
Timesheets template has no page-help block.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
