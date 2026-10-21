# BUG-RPT-001: Reports has no page Help (?), and Escape doesn't close New Report Template

| Field | Value |
|---|---|
| Checklist row | `RPT-S02` in `checklists/26-reports.md` |
| Module | Reports |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > Reports
2. Look for the Help (?) button
3. Click Add Report Template, press Escape

## Expected
A Help (?) button like other modules; Escape closes the popup.

## Actual
No Help button on the page. The New Report Template popup stays open on Escape.

## Evidence
- Screenshot: `screenshots/BUG-RPT-001-1.png`, `screenshots/BUG-RPT-001-2.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
