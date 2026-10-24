# BUG-PD-006: Personnel Details > Recency and Renewals: action buttons are hidden (Add Item, Table/Card view, renewal Save / Complete Renewal / Cancel) and Group by / Order by are disabled

| Field | Value |
|---|---|
| Checklist row | `PD-019` in `checklists/12-personnel-details.md` |
| Module | Personnel Details |
| Severity | High |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. All Personnel > Ethan Abbott > Recency and Renewals tab
2. Try to change Group by to Status, or Order by to Expiry Date
3. Look for the Table / Card view buttons
4. Click the pencil on Dangerous Goods Training and look for Save / Complete Renewal

## Expected
Add Item opens the add renewal/recency search; Group by and Order by change the list; Table and Card buttons switch the layout.

## Actual
Both dropdowns are disabled (greyed out, can't be changed). #add-recency-btn (Add Item), #view-table-btn and #view-card-btn exist in the page but are hidden (display:none), so you can't add a renewal/recency item or switch to card view. On the renewal edit page (pencil on Dangerous Goods Training) there is no Save, Complete Renewal or Cancel: #save-recency-btn, #complete-renewal-btn and #renewal-cancel-btn have display:none, so a renewal can't be saved or completed from Personnel Details. Renewal edit page has only the Go Back arrow, which discards changes without asking.

## Evidence
- Screenshot: `screenshots/BUG-PD-006-1.png`, `screenshots/BUG-PD-006-2.png`
- Console / network errors: none

## Suspected cause (optional)
Possibly the page script stops at the 'getPickerMod is not defined' error (BUG-PD-001) before it enables these controls.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
