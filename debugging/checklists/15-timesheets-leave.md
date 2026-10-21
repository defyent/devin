# Timesheets, Timesheet Details, Leave Requests

- **Checklist ID prefix:** `TS`
- **Guide section:** §9.5
- **Where:** Settings and Tools > People > Timesheets
- **Permission:** Timesheets A/WG/RG
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| TS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Administration > Settings and Tools > Timesheets opens 'Timesheet Approval' (October 2026, group pills All Personnel 110 / Administration 10 / Crew 40 / Engineers 20 / Pilots 40), no console errors |
| TS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-TS-001 | No Help on Timesheet Approval; Timesheet Details (?) does nothing |
| TS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Add Leave Type popup stays open after mousedown inside / release outside. F&D and Roster Violation popups close on outside click as designed |
| TS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-TS-004 | Details DATE column 'Oct 5', ROSTER times '14:00:00' with seconds |
| TS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS | BUG-PD-010 | At 390px Timesheet Approval, Timesheet Details and Leave Requests fit the screen; group and section pills become dropdowns; tables scroll sideways inside their card (no card view). The Performance panel covers rows (BUG-PD-010) |
| TS-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Settings and Tools gives Access Denied and its own Personnel Details has no Timesheets tab |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| TS-001 | Month ‹ ›, search, status filter (All/Unsigned/Pending/Approved/Rejected) | Filters correctly | FAIL | BUG-TS-002 | Month < > works (September 2026 / October 2026), search 'Aisha' leaves the 2 Aishas, group pills work (Pilots 40, All 110). Status filter: Unsigned shows 'No personnel found' though everyone has unsigned days; Pending/Approved/Rejected empty (no such data yet) |
| TS-002 | Columns totals | Rostered Days, Duty Hours, counts match details | FAIL | BUG-TS-003 | Aisha Johnston: list 13 days / 0.0h, details 19 Rostered Days / 180 Duty Hours. Every list row shows 0.0h. DS/NS shifts have no times so count 0 hours (check in 39) |
| TS-003 | Click person > Timesheet Details | Month view | PASS |  | Clicking a person opens Timesheet Details for that month (Aisha Johnston, October 2026) with Back, Help, month < >, Today, Approve Selected |
| TS-004 | Approve day / Bulk Approve / Unapprove | Works | PASS | ts004_unapproved | Timesheet Details for BETA TEST ONLY Second (19 and 20 Oct signed): ticked both > Approve Selected > "Approve Multiple Timesheets" lists both dates > Confirm. Both show Approved. Clicking 20 Oct "Approved - Click to unapprove" > Confirm ("change the status back to submitted") puts it back to Submitted, checked after a reload. The list counts went from 2 Pending to 1 Pending and 1 Approved. |
| TS-005 | Approve day with pending claim | Blocked until claim approved/rejected | PASS | ts005_blocked | BETA TEST ONLY Second signed 19 Oct with a pending Meal claim ($25). In Timesheet Details as Service Account, I ticked 19 Oct > Approve Selected. A "Pending Claims" popup appeared: "Cannot approve timesheets with pending claims ... Mon, Oct 19, 2026". The day stayed Submitted. The popup dates are in US format, same as BUG-TS-004. |
| TS-006 | Reject claim (reason required); move back to Pending | Works | FAIL | ts006_rejected | BUG-TS-007: View Claims > reject (×) asks for a reason. Leaving it empty gives "Rejection reason is required", but closing that error also closes the reject popup (script error). With the reason "BETA TEST ONLY reject reason", the claim shows Rejected plus the reason. "Move to Pending" (undo) brought it back to Pending, and approving it (✓) then showed Approved. |
| TS-007 | F&D / Roster Violation popups | Open | PASS | BUG-TS-005 | F&D shield opens 'Flight & Duty Analysis' (FRMS limits, predicted violations); roster warning triangle opens 'Roster Violation Analysis' (Shift Sequence rule). Both ignore Escape and use ISO dates (BUG-TS-005) |
| TS-008 | Leave Requests (beach icon) Pending Queue: search, filter, Approve/Reject | Approve toast reports roster shifts updated; roster changed | FAIL | ts008_roster_after | BUG-TS-008: Pending Queue search ("Second") and the leave-type filter (Sick Leave gives none) work. Approve and Reject (with a reason) work, and the counts update. But approving Annual Leave 26-27 Nov over rostered DS shifts left Roster Builder showing DS, with no roster-updated message. Reject with an empty reason does nothing and shows no message. |
| TS-009 | All Requests: filters; return decided to Pending | Works | PASS | ts009_returned | Leave Requests > All Requests: setting Status Approved plus Person BETA TEST ONLY Second and clicking Apply narrowed the list to 1 row (Annual Leave 5-6 Nov, Approved by Service Account). "Return to pending" > Confirm ("previous decision and comments will be cleared"): the counts changed from 0 Pending / 1 Approved to 1 Pending / 0 Approved. The list dates are US style ("Oct 22, 2026 10:28", "Thu, Nov 5, 2026"), same as BUG-TS-004. |
| TS-010 | Leave Types: Add (Name, hex Colour, Sort, Status); deactivate/reactivate | Works; invalid hex rejected | PASS | BUG-TS-006 | Added 'BETA TEST ONLY Leave' #AB12CD sort 70 (toast 'Leave type added'); invalid hex ZZZZZZ rejected; deactivate (confirm) shows Inactive, reactivate works. Validation error closes the popup and loses input, popup ignores Escape (BUG-TS-006) |
| TS-011 | Dashboard Unsigned Timesheets count after sign/approve | Updates | PASS | ts011_dash | As BETA TEST ONLY Second, the Dashboard Unsigned Timesheets badge showed 1 (21/10 Not signed). I signed 21 Oct (Sign Selected > password) and it showed Submitted. Back on the Dashboard the badge number was gone and the tab said "All timesheets are signed!". |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Leave type 'BETA TEST ONLY Leave' (#AB12CD, sort 70) | Leave Requests > Leave Types | Partly - deactivated (Inactive); the app has no delete for leave types |
