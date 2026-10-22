# BUG-POP-004: Flight Schedule popups (View Details, Double Booking alert, note modals) do not close with Esc

| Field | Value |
|---|---|
| Checklist row | `FS-013` in `checklists/06-flight-schedule.md` |
| Module | Flight Schedule |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Schedule (week view), click a flight to select it
2. Click its note / View Details icon
3. Press Esc

## Expected
Popup closes (CON-015).

## Actual
Popup stays open on Esc; only OK, x or a click outside closes it. Same for #fad-modal 'Double Booking Detected' and the Add/Edit Note modals. Retest 22/10/2026 (v2.0.114, assets ?v=2.0.114): fixed for the popups tested. View Details on #8834 opens the flight popup and Esc closes it; Add Note popup closes with Esc; Help closes with Esc and outside click. The Double Booking alert (#fad-modal) was not triggered in this retest. Retest 22/10/2026 (v2.0.117): Double Booking popup (#fad-modal) verified. Flight #8852's alert icon opens 'Flight Alerts' (F&D plus double booking), and Esc closes it. The 'Flight & Duty Limit Exceeded' version also closes with Esc. All flightschedule popups listed now close with Esc.

## Evidence
- Screenshot: `screenshots/BUG-POP-004-1.png`, `screenshots/BUG-POP-004-2.png`
- Console / network errors: none

## Suspected cause (optional)
#flight-details-modal has no keydown Escape handler (same pattern as BUG-POP-001).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
