# BUG-SST-001: Roster Shifts (Shift Type Editor): no Help (?), and Escape does not close popups

| Field | Value |
|---|---|
| Checklist row | `SST-S02` in `checklists/39-settings-shifttypes.md` |
| Module | Settings: Shift Types |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Roster Shifts.
2. Look for a Help (?).

## Expected
A Help (?) that explains groups, duty times, Show on Schedule and Deleted Items.

## Actual
There is no Help button on the page, and Escape leaves Create New Group open.

## Evidence
- Screenshot: `screenshots/BUG-SST-001-1.png`, `screenshots/BUG-SST-001-2.png`
- Console / network errors: none

## Suspected cause (optional)
The template has no help button or help modal.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
