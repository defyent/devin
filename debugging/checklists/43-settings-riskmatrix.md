# Settings – Risk Matrix

- **Checklist ID prefix:** `SRM`
- **Guide section:** §12.13
- **Where:** Settings and Tools > Safety > Risk Matrix
- **Permission:** settings_riskmatrix = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SRM-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SRM-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SRM-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SRM-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SRM-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SRM-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SRM-001 | Create empty / from template | Works | TODO | | |
| SRM-002 | Likelihood / Consequence levels add/edit/delete/reorder | Grid updates | TODO | | |
| SRM-003 | Cell Risk Text + Color; reuse offered | Used on Safety Reports and Hazards | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
