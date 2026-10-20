# Settings – Inspection Notifications

- **Checklist ID prefix:** `SINS`
- **Guide section:** §12.16
- **Where:** Settings and Tools > Maintenance > Inspection Notifications
- **Permission:** settings_inspections = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SINS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SINS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SINS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SINS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SINS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SINS-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SINS-001 | Search; Group by None/Name/Resource/Status | Works | TODO | | |
| SINS-002 | Add Inspection: Date trigger vs meter trigger | Field switches; overdue logic correct | TODO | | |
| SINS-003 | Schedule flight popup 'Aircraft Inspections' | Shows due/overdue | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
