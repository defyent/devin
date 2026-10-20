# Settings – Flight Schedule

- **Checklist ID prefix:** `SFS`
- **Guide section:** §12.1
- **Where:** Settings and Tools > Operations > Flight Schedule
- **Permission:** settings_flightschedule = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SFS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SFS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SFS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SFS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SFS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SFS-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SFS-001 | Status colours (Future, Past, Completed, Active, Canceled, Overdue); Reset to Default | Applied on Schedule, Active Flights, Dashboard | TODO | | |
| SFS-002 | Secondary Status add/rename/colour/remove | Pills on Flight Status tab; colour overrides on schedule | TODO | | |
| SFS-003 | Slot Duration − / + (5–120, step 5); bounds | Cannot exceed bounds; schedule uses it | TODO | | |
| SFS-004 | Schedule Start Time | Schedule first hour | TODO | | |
| SFS-005 | Overdue notifications toggle; Location Planner toggle | Take effect | TODO | | |
| SFS-006 | Cancellation Reasons add/delete | Appear on Canceled flights | TODO | | |
| SFS-007 | Update Changes / Cancel dirty state; leave prompt | Correct | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
