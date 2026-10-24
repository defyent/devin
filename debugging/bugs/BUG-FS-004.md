# BUG-FS-004: Planner Add Location replaces the New Booking popup - typed booking and location input is lost

| Field | Value |
|---|---|
| Checklist row | `FS-029` in `checklists/06-flight-schedule.md` |
| Module | Flight Schedule > Location Planner |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Schedule > Planner Only > Rows by Location > Enable Live Edit
2. Drag across empty days in a location row > New Booking opens; type a note
3. Click 'Add Location' in New Booking
4. Leave Name and Code empty, click Save, then OK on the Error popup

## Expected
Add Location opens on top of New Booking; after the error you are back in Add Location with your input; after saving you return to New Booking with the new location selected and your note kept.

## Actual
Add Location replaces New Booking (the note is gone). OK on 'Name and Code are required.' closes all popups, so the user has to start again. After a successful Save ('Location created') New Booking does not come back either. Retest 22/10/2026 (v2.0.114, assets ?v=2.0.114): fixed. Planner Only > Rows by Location > Live Edit > drag 26-28/10 on BETA TEST ONLY Loc > New Booking > typed a note > Add Location opens on top of New Booking. Empty Save shows 'Name and Code are required.' and OK returns to Add Location. Saving 'BETA TEST ONLY Loc2' / BT2 returns to New Booking with the new location in the list and the typed note kept. Booking was then cancelled. Minor: after Filter by Location > pick a location, the Locations popup stays open until Esc/Close.

## Evidence
- Screenshot: `screenshots/BUG-FS-004-1.png`, `screenshots/BUG-FS-004-2.png`, `screenshots/BUG-FS-004-3.png`, `screenshots/BUG-FS-004-4.png`
- Console / network errors: none

## Suspected cause (optional)
Planner popups use one shared modal slot: opening a modal closes the current one and closing the error closes everything instead of returning to the parent modal.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
