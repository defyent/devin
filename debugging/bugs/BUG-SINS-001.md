# BUG-SINS-001: Inspection Notifications Settings: no Help (?), and Escape does not close popups

| Field | Value |
|---|---|
| Checklist row | `SINS-S02` in `checklists/45-settings-inspections.md` |
| Module | Settings: Inspection Notifications |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Maintenance > Inspection Notifications.
2. Look for a Help (?) button.
3. Click Add Inspection, then press Escape.

## Expected
There is a page Help (?), and Escape closes the popup.

## Actual
There is no page Help (?), and Escape leaves Add Inspection open.

## Evidence
- Screenshot: `screenshots/BUG-SINS-001-1.png`, `screenshots/BUG-SINS-001-2.png`
- Console / network errors: none

## Suspected cause (optional)
No help modal. The modal is built in templates2/settings_inspections/index.js with only an overlay click handler (setupOverlayClickHandler) and no keydown/Escape handler.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
