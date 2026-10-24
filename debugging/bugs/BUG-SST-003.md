# BUG-SST-003: Roster Shifts: after Edit Group the selected group jumps back to Duty, so the next New Shift Type goes into the wrong group

| Field | Value |
|---|---|
| Checklist row | `SST-001` in `checklists/39-settings-shifttypes.md` |
| Module | Settings: Shift Types |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Roster Shifts, then click the "BETA TEST ONLY Grp2" tab.
2. Edit Group, rename it, then Update Group ("Group updated successfully").
3. Look at the selected tab, then click New Shift Type and save.

## Expected
The renamed group stays selected, and the new shift type goes into it.

## Actual
The selected tab and the section header go back to "Duty". "BETA TEST ONLY Shift" was created in Duty and not in the group I had been working on, with nothing to tell me.

## Evidence
- Screenshot: `screenshots/BUG-SST-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
The group list is reloaded after the update and the first group is selected again. The current group ID is not kept.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
