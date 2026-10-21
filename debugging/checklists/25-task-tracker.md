# Task Tracker

- **Checklist ID prefix:** `TT`
- **Guide section:** §11.5
- **Where:** Administration > Task Tracker
- **Permission:** Task Tracker A/RA/WG/RG
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| TT-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Administration > Task Tracker loads ('No projects yet'), no page errors |
| TT-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-TT-001 | Help (unlabeled ? icon, aria-label Help) opens; Got it!, x and outside click close it; Escape does not (also Add Project) |
| TT-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Help and Add Project stay open after mousedown inside / release outside; typed name kept |
| TT-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-TT-002 | Due Date 'Dec 31', Created '2026-10-21' (UTC date) |
| TT-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | FAIL | BUG-TT-003 | At 390px header, groups, Table/Card and search fit, but feature cards are pushed right and cut off |
| TT-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low still sees the menu link; page shows 'Access Denied: You do not have permission to access the TaskTracker feature. Please contact your administrator.' |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| TT-001 | Add Project (Group, Name, Description, Due) | Created; link/unlink groups | PASS |  | Add Project (Name, Description, Due Date) creates 'BETA TEST ONLY Project' with toast. No Group field in Add Project; groups are linked in the project via Add User Group (link toast) and unlinked with x (confirm 'Are you sure you want to remove ...', toast). Author column is blank for the new project; toasts show twice |
| TT-002 | Add Component > Feature > Task; copy tasks from feature | Works | PASS |  | Add Component 'BETA TEST ONLY Component' > Add Feature > two tasks via 'Add a new task...' all save with toasts. Copy tasks (Card view only - no copy button in Table view) from Feature to 'BETA TEST ONLY Feature 2' with Merge Tasks: 'Copied 2 tasks successfully!' |
| TT-003 | Assign task, due date, complete, drag reorder | Works; shows on assignee Dashboard Project Tasks | BLOCKED |  | Assign (only people in the project's user groups are offered; assigned to BETA TEST ONLY Lowperm), due date ('Due date set to Oct 25!'), complete (progress 50%) and drag reorder (persists after re-render) all work. Dashboard Project Tasks not checked: the only assignable test user has no Dashboard permission. Retest in 90 |
| TT-004 | Comments > Post Comment | Works | PASS |  | Comments icon on the component opens 'Comments: BETA TEST ONLY Component'; Post Comment adds 'BETA TEST ONLY comment' by Service Account. The page-level Post Comment button sits off-screen until a comments panel is opened (UX-07) |
| TT-005 | Table / Card view; search | Works | PASS |  | Table and Card views both render the project; search 'Feature 2' filters to that feature, 'zzqq' shows 'No results found' |
| TT-006 | RA / RG / WG | Read-only / scoped correctly | FAIL | tt006_wg | BUG-TT-004: Grpuser (Task Tracker WG) sees Add Project disabled with "You have read-only access", so WG behaves like RG. RA was not set up. |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| VIS-28 | Low | Open (external) | Task Tracker header card narrower than other pages |
| UX-07 | Low | Open (external) | Task Tracker icon button with no label/tooltip; Post Comment shown with no projects |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Project 'BETA TEST ONLY Project' (component, 2 features, 4 tasks, comment) | Administration > Task Tracker | Yes - project deleted ('Project deleted successfully!') |
