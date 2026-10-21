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
| SINS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Maintenance > Inspection Notifications opens settings_inspections (search, Group by, Add Inspection, Inspection Records table), with no console errors. |
| SINS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-SINS-001 | No page Help (?), and Escape does not close Add Inspection. |
| SINS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside Add Inspection to outside it: it stays open, because setupOverlayClickHandler only closes when both mousedown and click are on the overlay. |
| SINS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-SINS-003 | Trigger column shows "2026-10-01 (20 days overdue)" (should be 01/10/2026 and 21 days). Add Inspection date defaults to 21/10 (the UTC date) while it is 22/10 locally. The date input itself uses DD/MM/YYYY. |
| SINS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | 390 px: page scrollWidth 390. Search, Group by and Add Inspection fit on screen, and the table scrolls sideways inside its own box (scrollbar shown). |
| SINS-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Settings and Tools shows Access Denied (System Settings). |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SINS-001 | Search; Group by None/Name/Resource/Status | Works | PASS |  | 251 records, all COMPLETED. Search "R44-04" gives 14 rows, all R44-04. Group by Inspection Name gives 9 groups with counts (e.g. "100 Hour Inspection #2 (60)"), Resource gives 20 groups, Status gives "Completed (251)", and None gives the flat list again. Note: 108 COMPLETED rows still show text like "2100.0 / 447.0 (1653.0 overdue)". That is odd wording for a completed inspection, but it may just be how history rows are shown. |
| SINS-002 | Add Inspection: Date trigger vs meter trigger | Field switches; overdue logic correct | FAIL | BUG-SINS-002 | Trigger dropdown is filled after you choose a Resource (Date + that resource's meters). Date shows a DD/MM/YYYY date box, Flight Hours shows #inspectionMeter, and the fields switch correctly. Date trigger 01/10/2026 gives OVERDUE (correct). Meter trigger -5 is accepted and shows "(5.0 overdue)" but PENDING, because a current reading of 0 is treated as missing. |
| SINS-003 | Schedule flight popup 'Aircraft Inspections' | Shows due/overdue | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
