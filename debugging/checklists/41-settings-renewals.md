# Settings – Recency and Renewals

- **Checklist ID prefix:** `SREN`
- **Guide section:** §12.11
- **Where:** Settings and Tools > Safety > Recency and Renewals
- **Permission:** settings_renewals = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SREN-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Recency and Renewals opens settings_renewals (tabs: Recencies, Renewals, Alert Groups, User Group Templates), with no console errors. |
| SREN-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-SREN-001 | No page Help (?), and Escape does not close Add Recency. |
| SREN-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside Add Recency to outside it: it stays open. |
| SREN-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | N/A |  | No dates or times on this page, only day counts. |
| SREN-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | FAIL | BUG-SREN-004 | 390 px: no page overflow (scrollWidth 390) and the tabs become a dropdown, but the table columns overlap (Days on top of Name, headers overlap, edit icon over the Alert Group pill). |
| SREN-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Settings and Tools shows Access Denied (System Settings), same as 31-33. |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SREN-001 | Recencies CRUD (Name*, Days, Warning, Caution, Alert Group) | Saved | FAIL | BUG-SREN-002 | Add/edit/search/delete work: Name is required (native), the edit form loads the saved values, Alert Group can be set, and delete asks first and names the item. But Days -5 and Caution 20 > Warning 10 are accepted (BUG-SREN-002). Test recency deleted. |
| SREN-002 | Renewals CRUD (Days to Notify, Frequency, Notify) | Saved | FAIL | BUG-SREN-003 | Add/edit/delete work: Name is required, the edit form loads the saved values, and Notify Yes -> No is saved and shown. But Days to Notify -10 and Frequency 0 are accepted (BUG-SREN-003). Test renewal type deleted. |
| SREN-003 | Alert Groups CRUD | Saved | PASS |  | Alert Groups: add (Name only, required), and the new group shows in the Add Recency Alert Group dropdown. Rename works, and delete asks first and names the group. Test group deleted. |
| SREN-004 | User Group Templates > Edit Templates | Members receive items automatically | PASS |  | User Group Templates: cards show Users/Renewals/Recencies counts. In Edit Templates for BETA TEST ONLY Group I turned on Flight Review + Day Landings: "Templates updated successfully", card shows Renewals 1 Recencies 1. The member BETA TEST ONLY Lowperm then has a Day Landings recency (Crew has 0 recencies, so it came from the BETA template) and Flight Review in Recency and Renewals. Both templates were then turned off again. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |


**Cleanup (41):** test recency, renewal type and alert group (all "BETA TEST ONLY ...") deleted. The BETA TEST ONLY Group template was set back to 0 renewals / 0 recencies, and BETA TEST ONLY Lowperm's Day Landings recency was removed with it (checked in Personnel Details). Existing items were not changed.
