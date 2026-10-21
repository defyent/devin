# BUG-PD-016: Personnel Details > Timesheets: Add Claim button does nothing

| Field | Value |
|---|---|
| Checklist row | `PD-010` in `checklists/12-personnel-details.md` |
| Module | Personnel Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. All Personnel > Ethan Abbott > Timesheets (October 2026)
2. On 01 Thu (Draft) click Add Claim

## Expected
A claim form opens (or the day's Timesheet Details opens) so a claim can be added.

## Actual
Nothing happens: no popup, no page change, no network request, no console error. Add Claim is enabled on past days and disabled on future days, so it looks usable.

## Evidence
- Screenshot: `screenshots/BUG-PD-016-1.png`
- Console / network errors: none

## Suspected cause (optional)
Click handler for .timesheet-claim-btn is probably not bound, possibly because the page script stops early (BUG-PD-001, getPickerMod is not defined).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
