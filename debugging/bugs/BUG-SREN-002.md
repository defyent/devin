# BUG-SREN-002: Add Recency accepts negative Days, and a Caution value higher than Warning

| Field | Value |
|---|---|
| Checklist row | `SREN-001` in `checklists/41-settings-renewals.md` |
| Module | Settings: Recency and Renewals |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Recency and Renewals > Recencies > Add Recency.
2. Name "BETA TEST ONLY Rec", Days -5, Warning Value 10, Caution Value 20, then Save.

## Expected
Days must be a positive number. Caution should not be above Warning, since the existing items use Warning 30 / Caution 15 and Warning 50 / Caution 25.

## Actual
"Recency added successfully". The row shows Days -5, Warning 10, Caution 20. A negative period would make every recency check meaningless, and the warning levels are inverted.

## Evidence
- Screenshot: `screenshots/BUG-SREN-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
input_days and the value inputs have no min attribute, and the save doesn't check the values on either side.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
