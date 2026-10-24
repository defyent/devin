# BUG-HAZ-003: Hazard Register has no way to create a hazard entry

| Field | Value |
|---|---|
| Checklist row | `HAZ-002` in `checklists/20-hazard-register.md` |
| Module | Hazard Register |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Safety > Hazard Register
2. Look for a New / Create button

## Expected
A Create New Hazard button that makes the hazard entry and its safety report (as the checklist describes).

## Actual
The only buttons are Help and the search clear. Hazards can only be added from a Safety Report's Final Report tab.

## Evidence
- Screenshot: `screenshots/BUG-HAZ-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
hazardregister/index.js still has handleAddReport() and wires #addReportBtn plus the New Report / Confidential / Anonymous popups (copied from Safety Reports), but the page has no #addReportBtn.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
