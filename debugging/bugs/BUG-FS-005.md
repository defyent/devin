# BUG-FS-005: JS error on every Live Edit toggle: Cannot read properties of null (reading 'scrollTop')

| Field | Value |
|---|---|
| Checklist row | `FS-008` in `checklists/06-flight-schedule.md` |
| Module | Flight Schedule |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Schedule (Planner Only or Schedule view), DevTools console open
2. Click Enable Live Edit
3. Click Disable Live Edit

## Expected
No console errors.

## Actual
Each click logs uncaught TypeError "Cannot read properties of null (reading 'scrollTop')". The toggle still works, but later code in the same handler does not run. Retest 22/10/2026 (v2.0.114, assets ?v=2.0.114): fixed. Enable/Disable Live Edit as Service Account and betatest_grp logs no script errors.

## Evidence
- Screenshot: n/a
- Console / network errors: none

## Suspected cause (optional)
Edit-mode toggle handler saves/restores the scroll position of an element that does not exist in the current view mode (e.g. the time-grid scroller while the planner is shown); needs a null check.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
