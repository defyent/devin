# BUG-SFS-002: Changing Schedule Start Time saves a full date-time, and the setting then shows NaN:NaN

| Field | Value |
|---|---|
| Checklist row | `SFS-004` in `checklists/31-settings-flightschedule.md` |
| Module | Settings: Flight Schedule |
| Severity | High |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Operations > Flight Schedule.
2. In Schedule Start Time, type 06:00 and press Tab.
3. Click Update Changes ("Settings updated successfully").
4. Reload the page.

## Expected
Start time is saved as 06:00 and still shows 06:00 after reload.

## Actual
The page saves the picker's full value ("2026-10-22 06:00:00"). On reload it splits that on ":" to get the hours, gets NaN, and the box shows "NaN:NaN". The server then stores "NaN-NaN-NaN NaN:NaN:NaN". After that, typing a new time does not enable Update Changes, so a user can't fix it from the UI.

## Evidence
- Screenshot: `screenshots/BUG-SFS-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
templates2/settings_flightschedule/index.js: the change listener does state.scheduleStartTime = e.target.value, but datetimepicker.js writes "YYYY-MM-DD HH:MM:SS" to .dtp-hidden-input. init then does state.scheduleStartTime.split(":").map(Number). Fix: keep only HH:MM (e.g. value.slice(11,16)) and check it is valid before saving.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
