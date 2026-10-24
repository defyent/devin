# Settings – Waypoint Locations

- **Checklist ID prefix:** `SWP`
- **Guide section:** §12.8
- **Where:** Settings and Tools > Configuration > Waypoint Locations
- **Permission:** settings_waypoints = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SWP-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Opened from Settings and Tools > Configuration > Waypoint Locations with no console errors. 11 waypoints (10 NZ airports plus the test waypoint ZZZQ). |
| SWP-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-SWP-001 | There is no Help (?). |
| SWP-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside Add Waypoint to outside it: it stays open. |
| SWP-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | N/A |  | There are no dates or times on this page. |
| SWP-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | FAIL | BUG-SWP-004 | At 390 px the table columns overlap and can't be read, and the header buttons are 420 px wide, so Add Waypoint is cut off and the page scrolls sideways. |
| SWP-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | BETA TEST ONLY Lowperm gets Access Denied for Settings and Tools. |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SWP-001 | Search name/lat/long; columns incl. Flights count | Correct | PASS |  | Search works by name ("Dunedin"), code ("NZWN"), latitude ("-43.48") and longitude ("168.73"). Columns: Name, Code, Latitude, Longitude, Flights (e.g. NZAA 5177), Actions. |
| SWP-002 | settings (threshold, coordinate format) | Saved; format applied | PASS |  | Coordinate Format (DD/DMS/DMM, each with an example) applies straight away: Wellington shows 41° 19' 38.00" S, 174° 48' 19.00" E in DMS, and the header shows "Coordinate Format: DMS". Put back to DD. The Similarity Threshold slider (80%) is used by Scan. |
| SWP-003 | find_replace duplicates > consolidate / Consolidate All | References moved | PASS |  | Scan at 80% found 1 group: the 3 BETA test waypoints. It suggested a parent (WP1 with code) and offered per-item remove, Consolidate and Consolidate All. Consolidate asked to confirm ("merge 2 duplicate waypoint(s) into BETA TEST ONLY WP1 (ID: 140)... references will be updated"), then: "Consolidated 3 waypoints into BETA TEST ONLY WP1". The duplicates were removed. They had 0 references, so I did not see references being moved. No real waypoints were consolidated. |
| SWP-004 | playlist_add bulk add; add single | Works | PASS |  | Bulk Add accepted 3 lines with comma, pipe and semicolon delimiters, including a DMS line converted to -36.85/174.76: "Successfully added 3 waypoint(s)". Code is optional. Single Add Waypoint (code, name, map with Auto-name, lat/long) gave "Waypoint added successfully" and the waypoint is there after a reload. |
| SWP-005 | Detail: map, Auto-name from location, Files, Forms, Save, Delete | Works | PASS | BUG-SWP-003 | Detail page: Leaflet map, Auto-name ("Porirua" for -41.0/174.76), Files tab (Browse/Upload), Forms tab (Add Form opens the template search), Save Changes (kept after a reload), Delete (gone after a reload), and Cancel with edits gives the Unsaved Changes prompt. These all work. The list is not refreshed after save or delete until you reopen the module (BUG-SWP-003). |
| SWP-006 | Large move | 'Significant Location Change' warning | FAIL | BUG-SWP-002 | Moved BETA TEST ONLY WP1 from -36.85 to -41.00 (about 250 nm) on the detail page. Save Changes saved it with no warning. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |

## Test data
- All "BETA TEST ONLY" waypoints (WP1, WP1x, DMS, Single) are deleted. Coordinate Format is back to DD. "ZZZQ" (made in 07, used on flight 42903) is still there and is on the main cleanup list.
