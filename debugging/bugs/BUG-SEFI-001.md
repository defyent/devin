# BUG-SEFI-001: Extra Flight Info Settings: no Help (?), and Escape does not close Add Field

| Field | Value |
|---|---|
| Checklist row | `SEFI-S02` in `checklists/36-settings-extraflightinfo.md` |
| Module | Settings: Extra Flight Info |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Configuration > Extra Flight Info.
2. Look for a Help (?).
3. Click Add New Field, then press Escape.

## Expected
A Help (?) is shown, and Escape closes the popup.

## Actual
There is no Help button, and Escape leaves Add New Field open.

## Evidence
- Screenshot: `screenshots/BUG-SEFI-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
No help modal, and no keydown handler on the modals.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
