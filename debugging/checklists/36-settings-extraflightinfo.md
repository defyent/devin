# Settings – Extra Flight Info

- **Checklist ID prefix:** `SEFI`
- **Guide section:** §12.6
- **Where:** Settings and Tools > Configuration > Extra Flight Info
- **Permission:** settings_extraflightinfo = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SEFI-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Opened from Settings and Tools > Configuration > Extra Flight Info with no console errors. Both tabs were empty before the test. |
| SEFI-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-SEFI-001 | There is no Help (?), and Escape does not close Add New Field. |
| SEFI-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside Add New Field to outside it: it stays open. |
| SEFI-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | N/A |  | There are no dates or times on this page. |
| SEFI-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | At 390 px the page is 390 px wide, with no sideways scroll. |
| SEFI-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | BETA TEST ONLY Lowperm gets Access Denied for Settings and Tools. |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SEFI-001 | Pills F / C; Add Field (Name*, Type, Display Tab, Active) | Appears in matching Flight Details tab, DFR column, Reports | TODO | | |
| SEFI-002 | Edit, delete, drag reorder | Order reflected on Flight Details | TODO | | |
| SEFI-003 | 'Legacy' label in menu | Check naming consistency | PASS |  | The Settings and Tools card says "Extra Flight Info", with no "Legacy" label; this matches the page title "Extra Flight Info Settings". |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
