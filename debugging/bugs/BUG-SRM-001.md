# BUG-SRM-001: Risk Matrix Settings: no Help (?), and Escape does not close popups

| Field | Value |
|---|---|
| Checklist row | `SRM-S02` in `checklists/43-settings-riskmatrix.md` |
| Module | Settings: Risk Matrix |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Risk Matrix.
2. Look for a Help (?) button.
3. Click Add New Matrix, then press Escape.

## Expected
There is a page Help (?), and Escape closes the popup.

## Actual
There is no page Help (?), and Escape leaves Add New Matrix open.

## Evidence
- Screenshot: `screenshots/BUG-SRM-001-1.png`, `screenshots/BUG-SRM-001-2.png`
- Console / network errors: none

## Suspected cause (optional)
The page has no help modal, and there is no Escape key handler on its modals.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
