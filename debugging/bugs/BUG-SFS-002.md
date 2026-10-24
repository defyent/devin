# BUG-SFS-002: Changing Schedule Start Time saves a full date-time, and the setting then shows NaN:NaN

| Field | Value |
|---|---|
| Checklist row | `SFS-004` in `checklists/31-settings-flightschedule.md` |
| Module | Settings: Flight Schedule |
| Severity | High |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Operations > Flight Schedule.
2. In Schedule Start Time, type 06:00 and press Tab.
3. Click Update Changes ("Settings updated successfully").
4. Reload the page.

## Expected
Start time is saved as 06:00 and still shows 06:00 after reload.

## Actual
The page saves the picker's full value ("2026-10-22 06:00:00"). On reload it splits that on ":" to get the hours, gets NaN, and the box shows "NaN:NaN". The server then stores "NaN-NaN-NaN NaN:NaN:NaN". After that, typing a new time does not enable Update Changes, so a user can't fix it from the UI. Retest 22/10/2026 (v2.0.114, assets ?v=2.0.114): still failing. Typing 06:00 in Schedule Start Time and saving sent scheduleStartTime='2026-10-22 06:00:00'; after reload the box shows NaN:NaN (hidden value 'NaN-NaN-NaN NaN:NaN:NaN') and typing a time does not enable Update Changes. The save still posts the full date-time. Repaired for the test site by rewriting the save request to scheduleStartTime=07:00; reload then shows 07:00. Second retest 22/10/2026 (v2.0.114): unchanged; the save request still sends scheduleStartTime=2026-10-22 06:00:00, reload shows NaN:NaN, and typing 07:00 and saving leaves it NaN:NaN. Restored to 07:00 again by rewriting the save request. Third retest 22/10/2026 (v2.0.115): unchanged; the save still sends scheduleStartTime=2026-10-22 06:00:00, the reload shows NaN:NaN, and the UI can't fix it. Restored to 07:00 again by rewriting the save request. Fourth retest 22/10/2026 (v2.0.117): fixed. Typing 06:00 and saving sends scheduleStartTime=06:00; reload shows 06:00; setting it back to 07:00 through the UI works (checked after reload). Server-side validation of bad values not tested. Server check 22/10/2026 (v2.0.117): save requests rewritten to scheduleStartTime=NaN:NaN and 25:99 are rejected ('Schedule Start Time must be a valid time (HH:MM)') and the stored value stays 07:00.

## Evidence
- Screenshot: `screenshots/BUG-SFS-002-1.png`, `screenshots/BUG-SFS-002-2.png`, `screenshots/BUG-SFS-002-3.png`, `screenshots/BUG-SFS-002-4.png`, `screenshots/BUG-SFS-002-5.png`
- Console / network errors: none

## Suspected cause (optional)
templates2/settings_flightschedule/index.js: the change listener does state.scheduleStartTime = e.target.value, but datetimepicker.js writes "YYYY-MM-DD HH:MM:SS" to .dtp-hidden-input. init then does state.scheduleStartTime.split(":").map(Number). Fix: keep only HH:MM (e.g. value.slice(11,16)) and check it is valid before saving.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
