# Location Planner (stand-alone)

- **Checklist ID prefix:** `LP`
- **Guide section:** §8.6
- **Where:** Only reachable via admin-added link — record if no UI path
- **Permission:** Location Planner = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| LP-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| LP-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| LP-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| LP-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| LP-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| LP-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| LP-001 | Find a UI path to the stand-alone planner | If none, mark BLOCKED (do not use ?action=) | TODO | | |
| LP-002 | Rows by groups / people / aircraft; Day/Week/Month | Render correctly | TODO | | |
| LP-003 | Filter by Location, Add Location, New Booking, Booking Details > Delete | Same behaviour as embedded planner | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
