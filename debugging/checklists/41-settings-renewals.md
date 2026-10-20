# Settings – Recency and Renewals

- **Checklist ID prefix:** `SREN`
- **Guide section:** §12.11
- **Where:** Settings and Tools > Safety > Recency and Renewals
- **Permission:** settings_renewals = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SREN-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SREN-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SREN-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SREN-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SREN-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SREN-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SREN-001 | Recencies CRUD (Name*, Days, Warning, Caution, Alert Group) | Saved | TODO | | |
| SREN-002 | Renewals CRUD (Days to Notify, Frequency, Notify) | Saved | TODO | | |
| SREN-003 | Alert Groups CRUD | Saved | TODO | | |
| SREN-004 | User Group Templates > Edit Templates | Members receive items automatically | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
