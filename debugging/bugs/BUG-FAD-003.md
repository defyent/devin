# BUG-FAD-003: Flight and Duty popups show dates as '16 Oct 2026' instead of the configured DD/MM/YYYY

| Field | Value |
|---|---|
| Checklist row | `FAD-S04` in `checklists/16-flight-and-duty.md` |
| Module | Flight and Duty |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Safety > Flight and Duty
2. Click Aisha Johnston's 11.0h flight time value (flight #8795)
3. Click the Roster error icon on Aisha Johnston

## Expected
Dates as 16/10/2026 (Settings > Time Zone format, as used by the View as Date box).

## Actual
Flight Details shows '16 Oct 2026'; Roster Violations shows '23 Oct 2026', '31 Oct 2026' and so on.

## Evidence
- Screenshot: `screenshots/BUG-FAD-003-1.png`, `screenshots/BUG-FAD-003-2.png`
- Console / network errors: none

## Suspected cause (optional)
Hard-coded toLocaleDateString('en-NZ', {day:'2-digit', month:'short', year:'numeric'}) in flightandduty/index.js instead of the Time Zone date format.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
