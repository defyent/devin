# Settings – Roster Shifts

- **Checklist ID prefix:** `SST`
- **Guide section:** §12.9
- **Where:** Settings and Tools > People > Roster Shifts
- **Permission:** settings_shifttypes = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SST-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Opened from Settings and Tools > Roster Shifts (Shift Type Editor) with no console errors. Groups: Duty, Leave, Training. 7 Duty shift types. |
| SST-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-SST-001 | There is no Help (?). |
| SST-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside Create New Group to outside it: it stays open. |
| SST-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | PASS |  | Duty times show in 24-hour HH:mm (e.g. 06:00 - 18:00), as set in Time Zone. |
| SST-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | FAIL | BUG-SST-004 | At 390 px the table is 513 px wide, so the page scrolls sideways with Actions off-screen, and there are no group tabs. |
| SST-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | BETA TEST ONLY Lowperm gets Access Denied for Settings and Tools. |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SST-001 | Groups add/edit/delete | Works | PASS | BUG-SST-003 | Groups: Create (empty name gives "Group name is required"), Edit/rename ("Group updated successfully") and Delete all work. Deleting a group with a shift type warns: "The 1 shift type(s) will appear in Unassigned until you restore this group", and the shift moves to an "Unassigned" tab. After Edit Group, the selected tab jumps back to Duty (BUG-SST-003). |
| SST-002 | Add Shift: Short Name > 5 chars, colour, duty times, Show on Schedule | Validation; palette + schedule row update | TODO | | |
| SST-003 | Deleted Items restore | Restored | PASS |  | View Deleted lists Deleted Groups. Restoring "BETA TEST ONLY Grp3" asked to confirm, then: "Group restored successfully". The tab came back and its shift type BETAT went back into it from Unassigned. |
| SST-004 | Overnight shift (e.g. 14:00–02:00) | Duty hours computed correctly | PASS |  | The existing "PM Afternoon Shift" 14:00 - 02:00 shows 12h, and "NT" 18:00 - 06:00 shows 12h. My new "BETA TEST ONLY Shift" 22:00 - 06:00 saved and shows 8h. Overnight duration is right. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
