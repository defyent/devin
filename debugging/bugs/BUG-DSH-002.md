# BUG-DSH-002: Dashboard has no Help (?) button

| Field | Value |
|---|---|
| Checklist row | `DSH-S02` in `checklists/05-dashboard.md` |
| Module | Dashboard |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open Dashboard from the sidebar
2. Look at the page header (top right)

## Expected
Help (?) button top right like other modules (CON-001).

## Actual
Header shows only the 'Dashboard' title; no Help button.

## Evidence
- Screenshot: `screenshots/BUG-DSH-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
Dashboard header template lacks the shared help button.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
