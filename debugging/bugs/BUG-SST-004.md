# BUG-SST-004: Roster Shifts on a phone: the table scrolls the page sideways and the group tabs are hidden

| Field | Value |
|---|---|
| Checklist row | `SST-S05` in `checklists/39-settings-shifttypes.md` |
| Module | Settings: Shift Types |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open Settings and Tools > Roster Shifts at a 390 px width.

## Expected
Group tabs (or a dropdown) to switch groups, and rows that fit or scroll inside their own box.

## Actual
The table is 513 px wide, so the whole page scrolls sideways and "On Schedule" and Actions (edit/delete) are off-screen. The Duty/Leave/Training/... group tabs are not shown, so you can't switch groups.

## Evidence
- Screenshot: `screenshots/BUG-SST-004-1.png`
- Console / network errors: none

## Suspected cause (optional)
The table has no overflow-x wrapper or card layout, and the pill nav is hidden at narrow widths with no dropdown shown instead.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
