# BUG-FBLD-003: Form Builder: table conditions do nothing in View Form

| Field | Value |
|---|---|
| Checklist row | `FBLD-005` in `checklists/23-form-builder.md` |
| Module | Form Builder |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Form Builder, template with a Dropdown (BETA A/B/C) in Table 1
2. Add Table 2, click its C (Conditions)
3. IF 'Choose an option' is 'BETA A' THEN show this table > Add > Save Conditions > Save Form Template
4. View Form, pick BETA B, then BETA A

## Expected
Table 2 is hidden until BETA A is picked.

## Actual
Table 2 is always shown (with nothing picked, with BETA A and with BETA B). No console errors.

## Evidence
- Screenshot: `screenshots/BUG-FBLD-003-1.png`, `screenshots/BUG-FBLD-003-2.png`
- Console / network errors: none

## Suspected cause (optional)
formbuilder/index.js render script looks up formContainer.querySelector('[data-table-id=...]') and [data-widget-id=...], but the rendered preview has no elements with data-table-id or data-widget-id, so every condition returns early. Related to FORM-17/FORM-18.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
