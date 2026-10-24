# BUG-FS-003: Flight Schedule header overlaps when Live Edit is on - title covered, location pill cut off and its 'Show All' button cannot be clicked

| Field | Value |
|---|---|
| Checklist row | `FS-008` in `checklists/06-flight-schedule.md` |
| Module | Flight Schedule |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Schedule at 1568 px wide
2. Pick a location in Locations (pill 'Viewing location: Auckland Base')
3. Go to a past week and click Enable Live Edit

## Expected
Title, Live Edit banner, past-date banner and location pill all readable (wrap to a second line if needed).

## Actual
'Live Edit Mode' banner is drawn over the 'Flight Schedule' title and subtitle; 'Viewing location: Auckland Base' is cut to 'Viewing' and hidden behind the view buttons. The pill's 'Show All' button sits under the view-mode buttons, so a click lands on 'Schedule & Planner' instead (the location filter can only be cleared after turning Live Edit off or via Locations > All Locations). Retest 22/10/2026 (v2.0.114, assets ?v=2.0.114): fixed. At 1568 px with location Auckland Base picked, a past week shown and Live Edit on, the Live Edit, past-date and 'Viewing location: Auckland Base / Show All' banners sit on their own row under the title with no overlap. Show All is the top element at its centre and clicking it clears the location filter.

## Evidence
- Screenshot: `screenshots/BUG-FS-003-1.png`, `screenshots/BUG-FS-003-2.png`
- Console / network errors: none

## Suspected cause (optional)
Header banners are absolutely positioned / flex row with no wrap; no room left when 3 banners show.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
