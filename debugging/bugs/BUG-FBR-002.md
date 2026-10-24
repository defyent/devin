# BUG-FBR-002: Form Browser and Form Viewer dates ignore the date setting ('Oct 21, 2026', '10:24 PM')

| Field | Value |
|---|---|
| Checklist row | `FBR-S04` in `checklists/24-form-browser.md` |
| Module | Form Browser |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > Form Browser
2. Open Flights > 2026 > October > Flight 42903 - 2026-10-21
3. Look at Created

## Expected
21/10/2026, as set in Settings > Time Zone.

## Actual
List: 'Oct 21, 2026'. Form Viewer header: 'Oct 21, 2026 10:24 PM' (12-hour clock). Same as earlier FORM-08.

## Evidence
- Screenshot: `screenshots/BUG-FBR-002-1.png`, `screenshots/BUG-FBR-002-2.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
