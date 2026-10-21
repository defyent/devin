# BUG-FB-002: File Browser shows Date Uploaded as 'Oct 22, 2026' instead of DD/MM/YYYY

| Field | Value |
|---|---|
| Checklist row | `FB-S04` in `checklists/22-file-browser.md` |
| Module | File Browser |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > File Browser
2. Open SMS Reports > 2026 > October > SMS Report 2060, or search 'BETA_TEST_ONLY'
3. Look at Date Uploaded

## Expected
22/10/2026, as set in Settings > Time Zone.

## Actual
Oct 22, 2026

## Evidence
- Screenshot: `screenshots/BUG-FB-002-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
