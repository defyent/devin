# BUG-FBLD-002: Form Builder View Form: Date and Time widgets default to UTC, not local time

| Field | Value |
|---|---|
| Checklist row | `FBLD-S04` in `checklists/23-form-builder.md` |
| Module | Form Builder |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Form Builder, open a template with Date and Time widgets
2. Click View Form
3. Compare Date/Time with the header Local clock

## Expected
Local date and time: 22/10/2026 01:07.

## Actual
21/10/2026 and 12:07, which is the UTC date and time. Same as earlier FORM-06.

## Evidence
- Screenshot: `screenshots/BUG-FBLD-002-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
