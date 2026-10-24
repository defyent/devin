# BUG-FAD-002: Flight and Duty popups (Flight Details, Duty Time Details, Roster Violations, Resolutions Required) ignore Escape

| Field | Value |
|---|---|
| Checklist row | `FAD-S02` in `checklists/16-flight-and-duty.md` |
| Module | Flight and Duty |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Safety > Flight and Duty
2. Click Aisha Johnston's 11.0h flight time value
3. Press Escape

## Expected
Escape closes the popup.

## Actual
The popup stays open. Outside click and Close/Ok work; drag-out keeps it open (correct).

## Evidence
- Screenshot: `screenshots/BUG-FAD-002-1.png`, `screenshots/BUG-FAD-002-2.png`
- Console / network errors: none

## Suspected cause (optional)
flightandduty/index.js has no keydown handler for #customModal; only the overlay click and Close button call closeModal().

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
