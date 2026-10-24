# Location Planner (stand-alone)

- **Checklist ID prefix:** `LP`
- **Guide section:** §8.6
- **Where:** Only reachable via admin-added link — record if no UI path
- **Permission:** Location Planner = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| LP-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | BLOCKED |  | No menu path (LP-001) |
| LP-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | BLOCKED |  | No menu path (LP-001) |
| LP-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | BLOCKED |  | No menu path (LP-001) |
| LP-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | BLOCKED |  | No menu path (LP-001) |
| LP-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | BLOCKED |  | No menu path (LP-001) |
| LP-S06 | Low-permission account | Access Denied or read-only as per permission | BLOCKED |  | No menu path (LP-001) |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| LP-001 | Find a UI path to the stand-alone planner | If none, mark BLOCKED (do not use ?action=) | BLOCKED |  | No UI path: sidebar has no Location Planner item (Flight Operations: Dashboard, Flight Schedule, Active Flights, Daily Flight Record) and Settings and Tools has only 'Waypoint Locations' (shot lp_hub). Embedded planner tested in 06 |
| LP-002 | Rows by groups / people / aircraft; Day/Week/Month | Render correctly | BLOCKED |  | No menu path (LP-001); embedded planner views passed in 06 |
| LP-003 | Filter by Location, Add Location, New Booking, Booking Details > Delete | Same behaviour as embedded planner | BLOCKED |  | No menu path (LP-001); embedded planner filter/booking tested in 06 (BUG-FS-004) |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
