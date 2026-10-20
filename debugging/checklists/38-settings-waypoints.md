# Settings – Waypoint Locations

- **Checklist ID prefix:** `SWP`
- **Guide section:** §12.8
- **Where:** Settings and Tools > Configuration > Waypoint Locations
- **Permission:** settings_waypoints = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SWP-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SWP-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SWP-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SWP-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SWP-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SWP-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SWP-001 | Search name/lat/long; columns incl. Flights count | Correct | TODO | | |
| SWP-002 | settings (threshold, coordinate format) | Saved; format applied | TODO | | |
| SWP-003 | find_replace duplicates > consolidate / Consolidate All | References moved | TODO | | |
| SWP-004 | playlist_add bulk add; add single | Works | TODO | | |
| SWP-005 | Detail: map, Auto-name from location, Files, Forms, Save, Delete | Works | TODO | | |
| SWP-006 | Large move | 'Significant Location Change' warning | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
