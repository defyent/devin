# Settings – Flight Types

- **Checklist ID prefix:** `SFT`
- **Guide section:** §12.7
- **Where:** Settings and Tools > Configuration > Flight Types
- **Permission:** settings_flighttypes = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SFT-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Opened from Settings and Tools > Configuration > Flight Types with no console errors. 4 categories (Dual, PIC, PICUS, Solo) and 10 activities. |
| SFT-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-SFT-001 | There is no Help (?). |
| SFT-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside Add Flight Category to outside it: it stays open. |
| SFT-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | N/A |  | There are no dates or times on this page. |
| SFT-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | At 390 px the page is 378 px wide inside a 390 px screen, with no sideways scroll. |
| SFT-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | BETA TEST ONLY Lowperm gets Access Denied for Settings and Tools. |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SFT-001 | Categories / Activities: search, add, edit, delete (confirm) | Reflected in Flight Details, FRMS, Form auto-attach, Reports | TODO | | |
| SFT-002 | Delete type in use | Check behaviour; log if silently orphaned | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
