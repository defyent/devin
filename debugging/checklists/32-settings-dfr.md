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
| SDFR-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SDFR-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SDFR-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SDFR-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SDFR-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SDFR-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SDFR-001 | Enable Advanced Filtering > Save Changes | DFR shows advanced panel; disable hides it | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
