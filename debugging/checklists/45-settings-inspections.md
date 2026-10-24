# Settings – Inspection Notifications

- **Checklist ID prefix:** `SINS`
- **Guide section:** §12.16
- **Where:** Settings and Tools > Maintenance > Inspection Notifications
- **Permission:** settings_inspections = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

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
| SINS-002 | Add Inspection: Date trigger vs meter trigger | Field switches; overdue logic correct | FAIL | BUG-SINS-002 | Trigger dropdown is filled after you choose a Resource (Date + that resource's meters). Date shows a DD/MM/YYYY date box, Flight Hours shows #inspectionMeter, and the fields switch correctly. Date trigger 01/10/2026 gives OVERDUE (correct). Meter trigger -5 is accepted and shows "(5.0 overdue)" but PENDING, because a current reading of 0 is treated as missing. Edit opens with the saved values (date 01/10/2026). Changing it to 31/12/2026 saved ("2026-12-31 (70 days)", PENDING). |
| SINS-003 | Schedule flight popup 'Aircraft Inspections' | Shows due/overdue | PASS | sins_bto_popup | New BETA flight #42909 on ZK-BTO > note icon popup lists "Aircraft Inspections": date inspection "Due: 2026-12-31 ✓ 71 days" and meter inspection "Overdue 5.0 hours". The due date is in YYYY-MM-DD and the day count comes from the UTC date (71 instead of 70 locally), as in BUG-SINS-003. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Two BETA TEST ONLY inspections (date trigger and meter trigger) | Settings > Inspections, aircraft ZK-BTO | No - kept with test aircraft ZK-BTO; delete with it |
