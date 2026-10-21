# BUG-FBR-003: Form Browser on a phone: table is cut off, Created and Created By are off-screen

| Field | Value |
|---|---|
| Checklist row | `FBR-S05` in `checklists/24-form-browser.md` |
| Module | Form Browser |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open Administration > Form Browser on a 390px wide screen
2. Search 'QA Post'

## Expected
Cards (or a layout that fits), like Safety Reports on a phone.

## Actual
The table keeps its desktop width and scrolls sideways. Created and Created By are hidden off to the right.

## Evidence
- Screenshot: `screenshots/BUG-FBR-003-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
