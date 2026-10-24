# iPad: Configuration: Personnel and Waypoints

- **Checklist ID prefix:** `IPPER`
- **Guide section:** `ipad/IPAD_AUDIT_PLAN.md`
- **Where:** Config > Personnel / Waypoints
- **Frontend cross-reference:** 11/12 personnel, 38-settings-waypoints
- **Viewport:** P 820x1180 and L 1180x820 unless stated
- **Tester:**  
- **Date / app build / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID. Sync rows: put the frontend record checked in Notes.

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPPER-001 | Personnel list = frontend crew list (count, names, sort) | Same set | TODO |  |  |
| IPPER-002 | Personnel weights match frontend Personnel Details weight | Same weights (currently all 0.0 kg) | TODO |  |  |
| IPPER-003 | Linked personnel are read-only (buttons disabled) and say why | Clear | TODO |  |  |
| IPPER-004 | Waypoints list = frontend Settings > Waypoints (count, ident, name, coords) | Same set (NZAA appears twice) | TODO |  |  |
| IPPER-005 | Edit Waypoint: lat/lon validation, coordinate format | Validated | TODO |  |  |
| IPPER-006 | Name Waypoint from flight ('Name this Waypoint') creates waypoint on frontend (flightdetails_addwaypoint) | Created on frontend, BETA TEST ONLY name | TODO |  |  |
| IPPER-007 | Search/filter in pickers ('No results found') | Works | TODO |  |  |

## Test data created

| Record | Where | Cleaned up |
|---|---|---|
