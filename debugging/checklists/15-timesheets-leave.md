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
| TS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| TS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| TS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| TS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| TS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| TS-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| TS-001 | Month ‹ ›, search, status filter (All/Unsigned/Pending/Approved/Rejected) | Filters correctly | TODO | | |
| TS-002 | Columns totals | Rostered Days, Duty Hours, counts match details | TODO | | |
| TS-003 | Click person > Timesheet Details | Month view | TODO | | |
| TS-004 | Approve day / Bulk Approve / Unapprove | Works | TODO | | |
| TS-005 | Approve day with pending claim | Blocked until claim approved/rejected | TODO | | |
| TS-006 | Reject claim (reason required); move back to Pending | Works | TODO | | |
| TS-007 | F&D / Roster Violation popups | Open | TODO | | |
| TS-008 | Leave Requests (beach icon) Pending Queue: search, filter, Approve/Reject | Approve toast reports roster shifts updated; roster changed | TODO | | |
| TS-009 | All Requests: filters; return decided to Pending | Works | TODO | | |
| TS-010 | Leave Types: Add (Name, hex Colour, Sort, Status); deactivate/reactivate | Works; invalid hex rejected | TODO | | |
| TS-011 | Dashboard Unsigned Timesheets count after sign/approve | Updates | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
