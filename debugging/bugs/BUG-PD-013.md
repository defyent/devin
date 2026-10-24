# BUG-PD-013: Personnel Details: an empty Birth Date shows today's date

| Field | Value |
|---|---|
| Checklist row | `PD-004` in `checklists/12-personnel-details.md` |
| Module | Personnel Details |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. All Personnel > BETA TEST ONLY Lowperm (no birth date on file) > Personal Details
2. Look at Birth Date

## Expected
Birth Date is blank when none is recorded.

## Actual
The box shows 21/10/2026 (today), but the field has no value (data-has-value=false, initialValue empty). Users will think today's date is saved as the birth date.

## Evidence
- Screenshot: `screenshots/BUG-PD-013-1.png`
- Console / network errors: none

## Suspected cause (optional)
The date picker fills in today for empty values; may be linked to the picker load error in BUG-PD-001 (getPickerMod is not defined). Same pattern as the DFR date boxes in BUG-DFR-002.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
