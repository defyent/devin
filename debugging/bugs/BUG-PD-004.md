# BUG-PD-004: Security tab 'Enabled on' date ignores Settings > Time Zone format

| Field | Value |
|---|---|
| Checklist row | `PD-S04` in `checklists/12-personnel-details.md` |
| Module | Personnel Details > Security |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings > Time Zone is DD/MM/YYYY, 24-hour HH:mm
2. Enable 2FA on an account, view My Account > Security

## Expected
'Enabled on: 21/10/2026 21:03'.

## Actual
'Enabled on: 2026-10-21 21:03:55' (raw database format).

## Evidence
- Screenshot: `screenshots/BUG-PD-004-1.png`
- Console / network errors: none

## Suspected cause (optional)
Value printed as-is; not passed through formatDateWithConfig/formatTimeWithConfig.

## Test data involved
none

## Related
DATE-01

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
