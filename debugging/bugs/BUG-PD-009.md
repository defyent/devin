# BUG-PD-009: Personnel Details > Renewal edit: the Today and Calculate links can't be clicked because the date fields cover them

| Field | Value |
|---|---|
| Checklist row | `PD-022` in `checklists/12-personnel-details.md` |
| Module | Personnel Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. All Personnel > Ethan Abbott > Recency and Renewals > edit (pencil) on Dangerous Goods Training
2. Click 'Today' next to Last Conducted
3. Click 'Calculate' next to Expires

## Expected
Today sets Last Conducted to today; Calculate sets Expires to Last Conducted + frequency.

## Actual
The date boxes are squeezed and overlap the links. A real click on 'Calculate' lands on the Renewal Notes textarea and a click on 'Today' lands on the Scheduled field's container, so nothing happens. When the link is triggered from code, Calculate works: Expires 20/10/2028 and toast 'Expiry date set to 20/10/2028 (730 days from Last Conducted)', which is correct and in the org date format.

## Evidence
- Screenshot: `screenshots/BUG-PD-009-1.png`
- Console / network errors: none

## Suspected cause (optional)
Layout of .input-with-button-container: the date inputs are too narrow and the link sits under the next field.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
