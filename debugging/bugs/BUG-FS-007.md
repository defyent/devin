# BUG-FS-007: Edit-mode idle timeout switches Live Edit off silently, throws 'calendarEl is not defined' and leaves the schedule blank

| Field | Value |
|---|---|
| Checklist row | `FS-025` in `checklists/06-flight-schedule.md` |
| Module | Flight Schedule |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Schedule > Planner Only (or any view) > Enable Live Edit
2. Do not touch the page for 20 minutes

## Expected
Edit mode turns off with the message 'Edit mode has been disabled due to inactivity.'

## Actual
At 20 min the button silently returns to 'Enable Live Edit'; no popup or toast, and the console shows uncaught ReferenceError 'calendarEl is not defined', so the rest of the timeout handler (probably the message and the calendar refresh) does not run. A user who comes back can think they are still editing. Afterwards the schedule is left blank (month view 'October 2026' with no flights) until the page is reloaded. Retest 22/10/2026 (v2.0.114, assets ?v=2.0.114): fixed. betatest_grp enabled Live Edit at 04:54:45 UTC and left the page idle: at 20.0 min Live Edit turned off with the toast 'Edit mode has been disabled due to inactivity.', no script errors, and week view still shows its flights (6 events) without a reload.

## Evidence
- Screenshot: `screenshots/BUG-FS-007-1.png`, `screenshots/BUG-FS-007-2.png`
- Console / network errors: none

## Suspected cause (optional)
Inactivity handler references a variable calendarEl that is not in scope (renamed or local to another function).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
