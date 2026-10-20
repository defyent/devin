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
| SFT-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SFT-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SFT-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SFT-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SFT-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SFT-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SFT-001 | Categories / Activities: search, add, edit, delete (confirm) | Reflected in Flight Details, FRMS, Form auto-attach, Reports | TODO | | |
| SFT-002 | Delete type in use | Check behaviour; log if silently orphaned | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
