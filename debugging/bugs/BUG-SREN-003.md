# BUG-SREN-003: Add Renewal Type accepts negative Days to Notify and a Frequency of 0 days

| Field | Value |
|---|---|
| Checklist row | `SREN-002` in `checklists/41-settings-renewals.md` |
| Module | Settings: Recency and Renewals |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Recency and Renewals > Renewals > Add Renewal.
2. Name "BETA TEST ONLY Ren", Days to Notify -10, Frequency (Days) 0, then Save.

## Expected
Both must be positive numbers (Frequency at least 1 day). The save should be refused with a message.

## Actual
"Renewal type added successfully". The row shows Days to Notify -10 and Frequency 0. A 0-day renewal would be due again straight away, and a negative notify window means no notice ever comes before expiry.

## Evidence
- Screenshot: `screenshots/BUG-SREN-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
The number inputs have no min attribute, and the server doesn't check the range.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
