# Settings – Daily Flight Record

- **Checklist ID prefix:** `SDFR`
- **Guide section:** §12.2
- **Where:** Settings and Tools > Operations > Daily Flight Record
- **Permission:** settings_dfr = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SDFR-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | FAIL | BUG-SDFR-001 | Opens from Settings and Tools > Operations > Daily Flight Record, but the console shows a 404 for templates2/settings_dfr/colorpicker.js. |
| SDFR-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SDFR-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SDFR-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | N/A |  | The page has no dates or times, only the Enable Advanced Filtering toggle. |
| SDFR-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SDFR-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Settings and Tools shows "Access Denied: You do not have permission to access the System Settings feature". |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SDFR-001 | Enable Advanced Filtering > Save Changes | DFR shows advanced panel; disable hides it | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
