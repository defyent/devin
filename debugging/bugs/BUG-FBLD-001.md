# BUG-FBLD-001: Form Builder: popups ignore Escape and outside clicks (Help, Create New Form Template, Edit Options)

| Field | Value |
|---|---|
| Checklist row | `FBLD-S02` in `checklists/23-form-builder.md` |
| Module | Form Builder |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Form Builder
2. Click Help (?)
3. Press Escape, then click outside the popup

## Expected
The popup closes, as on Settings and Tools, Safety Reports and Hazard Register.

## Actual
Help, Create New Form Template and Edit Dropdown Options stay open on Escape and outside clicks. Only x, Close or Cancel close them. Same as earlier FORM-20.

## Evidence
- Screenshot: `screenshots/BUG-FBLD-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
formbuilder/index.js has no Escape handler and no overlay click handler; closeModal() only runs on [data-close] buttons.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
