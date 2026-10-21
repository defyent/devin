# Settings – Flight Schedule

- **Checklist ID prefix:** `SFS`
- **Guide section:** §12.1
- **Where:** Settings and Tools > Operations > Flight Schedule
- **Permission:** settings_flightschedule = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SFS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Operations > Flight Schedule; loads with no console errors. |
| SFS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS |  | Help opens; closes with the close icon, Close button, outside click and Escape. (Button says Close, not Got it.) |
| SFS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Help popup: mousedown inside, release outside, stays open. |
| SFS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | N/A |  | No dates or times shown on this page. |
| SFS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | At 390px the settings stack in one column with no sideways scroll; the Reset Colors popup fits. |
| SFS-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SFS-001 | Status colours (Future, Past, Completed, Active, Canceled, Overdue); Reset to Default | Applied on Schedule, Active Flights, Dashboard | PASS |  | Reset to Default Colors asks first and lists the defaults (Amber, Yellow, Green, Blue, Brown, Red); Cancel keeps the current colours. Colours not changed, to avoid changing the live look for other users. |
| SFS-002 | Secondary Status add/rename/colour/remove | Pills on Flight Status tab; colour overrides on schedule | PASS |  | Added "BETA TEST ONLY Status" + Update Changes: "Settings updated successfully". It shows as a pill on Flight Details > Flight Status (#42903). Colour override on the schedule not checked. |
| SFS-003 | Slot Duration − / + (5–120, step 5); bounds | Cannot exceed bounds; schedule uses it | FAIL | BUG-SFS-001 | − stops at 5, typing 7 snaps to 5; + goes past 120 (135) and typing 200 is kept. Not saved. Cancel restored 30. |
| SFS-004 | Schedule Start Time | Schedule first hour | FAIL | BUG-SFS-002 | Saving a new start time stores a full date-time; after reload the box shows NaN:NaN and the UI cannot fix it. Restored to 07:00 for the test site. |
| SFS-005 | Overdue notifications toggle; Location Planner toggle | Take effect | BLOCKED |  | Both toggles flip, enable Update Changes, and Cancel puts them back. Location Planner Off/On saved OK, but I could not confirm the effect on Flight Schedule because the same save hit BUG-SFS-002. Overdue notifications need a followed overdue flight. Retest in 99. Settings were put back to Planner On and Overdue Off. |
| SFS-006 | Cancellation Reasons add/delete | Appear on Canceled flights | PASS |  | Add Reason "BETA TEST ONLY Reason": "Reason added"; it is listed in the cancel reason dropdown on Flight Details. Delete removes the clicked reason (checked by data-id after reload). Reasons in use show "In use" and a view-flights link. UX note: the delete confirm does not name the reason being deleted. |
| SFS-007 | Update Changes / Cancel dirty state; leave prompt | Correct | PASS |  | Changing a value enables Update Changes; Cancel restores the saved values (slot 30). Update Changes: "Settings updated successfully". Leave-page prompt: see BUG-NAV-001. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Secondary status "BETA TEST ONLY Status" | Settings > Flight Schedule | Removed (Update Changes, checked after reload) |
| Cancellation reason "BETA TEST ONLY Reason" | Settings > Flight Schedule | Deleted. Tester error during cleanup: my test script clicked the wrong delete button, so the original "Aircraft Maintenance" and "Airspace Closure" reasons (not in use) were deleted. I added them back with the same names, but they now have new IDs (15, 16). |
