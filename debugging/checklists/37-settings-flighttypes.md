# Settings – Flight Types

- **Checklist ID prefix:** `SFT`
- **Guide section:** §12.7
- **Where:** Settings and Tools > Configuration > Flight Types
- **Permission:** settings_flighttypes = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

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
| SFT-001 | Categories / Activities: search, add, edit, delete (confirm) | Reflected in Flight Details, FRMS, Form auto-attach, Reports | FAIL | BUG-SFT-002 | Categories/Activities pills, search ("BETA" filters to one row), add (empty name refused: "Flight category name is required."), edit, and delete (confirm names the item) all work. "BETA TEST ONLY Cat2" and "BETA TEST ONLY Act" show on flight 42903 in the flight-category, flight-activity and leg category dropdowns. FAIL: a duplicate "PIC" was accepted (ID 15, since deleted). I did not check FRMS, Form auto-attach or Reports. |
| SFT-002 | Delete type in use | Check behaviour; log if silently orphaned | PASS |  | I set flight 42903 to "BETA TEST ONLY Cat2" and "BETA TEST ONLY Act". Deleting either is refused: "Cannot delete this flight category/activity because 1 flight references it. Please update or remove those flights first." Nothing is orphaned. The message shows in a warning popup titled "API Error", which is not the clearest title. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |

## Test data
- "BETA TEST ONLY Cat"/"Cat2", "BETA TEST ONLY Act" and the duplicate "PIC" (ID 15) are deleted. Flight 42903 is set back to no category and no activity.
