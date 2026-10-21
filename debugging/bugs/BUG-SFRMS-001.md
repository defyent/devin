# BUG-SFRMS-001: FRMS Settings: no Help (?), and Escape does not close popups

| Field | Value |
|---|---|
| Checklist row | `SFRMS-S02` in `checklists/40-settings-frms.md` |
| Module | Settings: FRMS |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Fatigue Risk Management Settings.
2. Look for a Help (?) button.
3. Click + Add Flight Time Limit Rule, then press Escape.

## Expected
There is a page Help (?), and Escape closes the popup.

## Actual
There is no page Help (?). Escape leaves Add Flight Time Limit Rule open. Only the small field (?) tips are there.

## Evidence
- Screenshot: `screenshots/BUG-SFRMS-001-1.png`, `screenshots/BUG-SFRMS-001-2.png`
- Console / network errors: none

## Suspected cause (optional)
The page has no help modal, and there is no keydown Escape handler on its modals.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
