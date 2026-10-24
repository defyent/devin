# BUG-FBLD-004: Form Builder on a phone: page is wider than the screen and the Toolbox covers the form

| Field | Value |
|---|---|
| Checklist row | `FBLD-S05` in `checklists/23-form-builder.md` |
| Module | Form Builder |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open Settings and Tools > Form Builder on a 390px wide screen

## Expected
A usable layout, or a clear 'use a larger screen' message.

## Actual
The page is 644px wide in a 390px screen and scrolls sideways. The Toolbox panel opens over the form. The header, Form Template, Allow Confidential and Auto-Attach are cut off.

## Evidence
- Screenshot: `screenshots/BUG-FBLD-004-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
