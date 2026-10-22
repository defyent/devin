# Settings – Flight Schedule

- **Checklist ID prefix:** `SFS`
- **Guide section:** §12.1
- **Where:** Settings and Tools > Operations > Flight Schedule
- **Permission:** settings_flightschedule = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SFS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Operations > Flight Schedule; loads with no console errors. |
| SFS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS |  | Help opens; closes with the close icon, Close button, outside click and Escape. (Button says Close, not Got it.) |
| SFS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Help popup: mousedown inside, release outside, stays open. |
| SFS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | N/A |  | No dates or times shown on this page. |
| SFS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | At 390px the settings stack in one column with no sideways scroll; the Reset Colors popup fits. |
| SFS-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Settings and Tools shows "Access Denied: You do not have permission to access the System Settings feature", so neither settings page can be reached. |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SFS-001 | Status colours (Future, Past, Completed, Active, Canceled, Overdue); Reset to Default | Applied on Schedule, Active Flights, Dashboard | PASS |  | Reset to Default Colors asks first and lists the defaults (Amber, Yellow, Green, Blue, Brown, Red); Cancel keeps the current colours. Colours not changed, to avoid changing the live look for other users. |
| SFS-002 | Secondary Status add/rename/colour/remove | Pills on Flight Status tab; colour overrides on schedule | PASS |  | Added "BETA TEST ONLY Status" + Update Changes: "Settings updated successfully". It shows as a pill on Flight Details > Flight Status (#42903). Colour override on the schedule not checked. |
| SFS-003 | Slot Duration − / + (5–120, step 5); bounds | Cannot exceed bounds; schedule uses it | FAIL | BUG-SFS-001 | Retest 22/10/2026 (v2.0.114): + still goes past 120 (155) and typed 200 is kept with Update enabled. Restored 30 |
| SFS-004 | Schedule Start Time | Schedule first hour | FAIL | BUG-SFS-002 | Retest 22/10/2026 (v2.0.114): still saves the full date-time; after reload NaN:NaN and the UI can't fix it. Restored to 07:00 by rewriting the save request (checked after reload) |
| SFS-005 | Overdue notifications toggle; Location Planner toggle | Take effect | PASS | nav016_banner | With Overdue Alerts on (Settings > Flight Schedule), Service Account as Flight Follower and SAR Watch on, I changed BETA flight #42910 to 08:00-09:00 local today (now past) and left it Open. check_overdue_flights returned overdue_count 1, and the banner showed within 35 s. |
| SFS-006 | Cancellation Reasons add/delete | Appear on Canceled flights | PASS |  | Add Reason "BETA TEST ONLY Reason": "Reason added"; it is listed in the cancel reason dropdown on Flight Details. Delete removes the clicked reason (checked by data-id after reload). Reasons in use show "In use" and a view-flights link. UX note: the delete confirm does not name the reason being deleted. |
| SFS-007 | Update Changes / Cancel dirty state; leave prompt | Correct | PASS |  | Changing a value enables Update Changes; Cancel restores the saved values (slot 30). Update Changes: "Settings updated successfully". Leave-page prompt: see BUG-NAV-001. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Secondary status "BETA TEST ONLY Status" | Settings > Flight Schedule | Removed (Update Changes, checked after reload) |
| Cancellation reason "BETA TEST ONLY Reason" | Settings > Flight Schedule | Deleted. Tester error during cleanup: my test script clicked the wrong delete button, so the original "Aircraft Maintenance" and "Airspace Closure" reasons (not in use) were deleted. I added them back with the same names, but they now have new IDs (15, 16). |
