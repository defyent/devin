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
| TS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| TS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-TS-004 | Details DATE column 'Oct 5', ROSTER times '14:00:00' with seconds |
| TS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| TS-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Settings and Tools gives Access Denied and its own Personnel Details has no Timesheets tab |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| TS-001 | Month ‹ ›, search, status filter (All/Unsigned/Pending/Approved/Rejected) | Filters correctly | FAIL | BUG-TS-002 | Month < > works (September 2026 / October 2026), search 'Aisha' leaves the 2 Aishas, group pills work (Pilots 40, All 110). Status filter: Unsigned shows 'No personnel found' though everyone has unsigned days; Pending/Approved/Rejected empty (no such data yet) |
| TS-002 | Columns totals | Rostered Days, Duty Hours, counts match details | FAIL | BUG-TS-003 | Aisha Johnston: list 13 days / 0.0h, details 19 Rostered Days / 180 Duty Hours. Every list row shows 0.0h. DS/NS shifts have no times so count 0 hours (check in 39) |
| TS-003 | Click person > Timesheet Details | Month view | PASS |  | Clicking a person opens Timesheet Details for that month (Aisha Johnston, October 2026) with Back, Help, month < >, Today, Approve Selected |
| TS-004 | Approve day / Bulk Approve / Unapprove | Works | BLOCKED |  | No submitted timesheets on stresstest: approve checkboxes only enable for status 'submitted' and every day is Draft/unsigned. Needs a user with Timesheets Own to sign days first. Retest in 90 |
| TS-005 | Approve day with pending claim | Blocked until claim approved/rejected | BLOCKED |  | Needs a submitted day with a pending claim; Add Claim does nothing (BUG-PD-016). Retest in 90 |
| TS-006 | Reject claim (reason required); move back to Pending | Works | BLOCKED |  | No claims exist (Claims 0) and Add Claim does nothing (BUG-PD-016). Retest in 90 |
| TS-007 | F&D / Roster Violation popups | Open | PASS | BUG-TS-005 | F&D shield opens 'Flight & Duty Analysis' (FRMS limits, predicted violations); roster warning triangle opens 'Roster Violation Analysis' (Shift Sequence rule). Both ignore Escape and use ISO dates (BUG-TS-005) |
| TS-008 | Leave Requests (beach icon) Pending Queue: search, filter, Approve/Reject | Approve toast reports roster shifts updated; roster changed | TODO | | |
| TS-009 | All Requests: filters; return decided to Pending | Works | TODO | | |
| TS-010 | Leave Types: Add (Name, hex Colour, Sort, Status); deactivate/reactivate | Works; invalid hex rejected | TODO | | |
| TS-011 | Dashboard Unsigned Timesheets count after sign/approve | Updates | BLOCKED |  | Needs sign/approve (TS-004). Retest in 90 |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
