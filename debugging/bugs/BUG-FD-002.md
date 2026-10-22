# BUG-FD-002: Flight Details History misses edits saved in Flight Details and shows a false 'Aircraft: ZK-SIM > Unassigned' on schedule moves

| Field | Value |
|---|---|
| Checklist row | `FD-037` in `checklists/07-flight-details.md` |
| Module | Flight Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Schedule > Enable Live Edit > move/resize flight #42903 (ZK-SIM)
2. Double-click it > Flight Details > add a custom passenger and a comment > Save Changes
3. Click History

## Expected
History shows every change including the Flight Details save (passenger added, comment added), and only fields that really changed.

## Actual
The Flight Details save at 10:17 pm is not listed; newest entry is the 09:31 pm schedule move. Each schedule move/resize entry lists 'Aircraft: ZK-SIM > Unassigned' (the aircraft stayed ZK-SIM) and 'Source: (blank) > Flight Schedule'. Values are shown as raw '2026-10-21 09:30:00' instead of DD/MM/YYYY HH:MM.

Retest v2.0.119: a schedule resize of #42903 (flightschedule_updateflight without resource_id) logs 'Aircraft: ZK-SIM > Unassigned' (aircraft really still ZK-SIM) and 'Source: > Flight Schedule', and also overwrote SAR Time 21/10 23:30 > 09:45 (real change). A Flight Details save of leg 1 depart/dest/PIC added no history entry (main fields like Status/Notes are logged). Modal shows dates as '23 Oct 2026', not DD/MM/YYYY. Still fails.

## Evidence
- Screenshot: `screenshots/BUG-FD-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
Schedule drag/resize audit compares against a payload without aircraft (null > 'Unassigned'); Flight Details save path either does not write to the audit log or only logs main-table fields (passengers/comments not tracked).

fs_new.js eventResize (~L1536-1570) omits resource_id (eventDrop sends it); server diffs the missing value as Unassigned, always logs Source and resets SAR to the end time. Flight Details save doesn't diff legs/manifest/comments. History modal uses toLocaleDateString('en-NZ',{month:'short'}).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
