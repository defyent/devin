# BUG-FB-007: File Browser on a phone: table is cut off, edit buttons are off-screen

| Field | Value |
|---|---|
| Checklist row | `FB-S05` in `checklists/22-file-browser.md` |
| Module | File Browser |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open Administration > File Browser on a 390px wide screen

## Expected
Cards (or a layout that fits), like Safety Reports and Hazard Register on a phone.

## Actual
The table stays 585px wide in a 390px screen. Revision, Uploader and the edit buttons are hidden; you have to scroll sideways to reach them.

## Evidence
- Screenshot: `screenshots/BUG-FB-007-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
