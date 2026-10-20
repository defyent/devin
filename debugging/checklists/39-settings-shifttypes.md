# Settings – Roster Shifts

- **Checklist ID prefix:** `SST`
- **Guide section:** §12.9
- **Where:** Settings and Tools > People > Roster Shifts
- **Permission:** settings_shifttypes = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SST-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SST-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SST-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SST-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SST-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SST-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SST-001 | Groups add/edit/delete | Works | TODO | | |
| SST-002 | Add Shift: Short Name > 5 chars, colour, duty times, Show on Schedule | Validation; palette + schedule row update | TODO | | |
| SST-003 | Deleted Items restore | Restored | TODO | | |
| SST-004 | Overnight shift (e.g. 14:00–02:00) | Duty hours computed correctly | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
