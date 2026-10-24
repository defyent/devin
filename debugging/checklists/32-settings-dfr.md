# Settings – Daily Flight Record

- **Checklist ID prefix:** `SDFR`
- **Guide section:** §12.2
- **Where:** Settings and Tools > Operations > Daily Flight Record
- **Permission:** settings_dfr = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SDFR-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | FAIL | BUG-SDFR-001 | Opens from Settings and Tools > Operations > Daily Flight Record, but the console shows a 404 for templates2/settings_dfr/colorpicker.js. |
| SDFR-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS |  | Help opens. It closes with ×, the Close button, a click outside and Escape. There is no Got it button, Close does the same job. |
| SDFR-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside the Help popup to outside it: the popup stays open. |
| SDFR-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | N/A |  | The page has no dates or times, only the Enable Advanced Filtering toggle. |
| SDFR-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | At 390px there is no sideways scroll, and the toggle and Save Changes are visible and usable. |
| SDFR-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Settings and Tools shows "Access Denied: You do not have permission to access the System Settings feature". |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SDFR-001 | Enable Advanced Filtering > Save Changes | DFR shows advanced panel; disable hides it | PASS |  | Off + Save: Daily Flight Record shows only Columns and search. On + Save: the Advanced Filters panel is back (status, date from/to, flight ID, rego, PIC, customer). Left On. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
