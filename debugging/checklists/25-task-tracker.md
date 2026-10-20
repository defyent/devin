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
| TT-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| TT-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| TT-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| TT-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| TT-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| TT-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| TT-001 | Add Project (Group, Name, Description, Due) | Created; link/unlink groups | TODO | | |
| TT-002 | Add Component > Feature > Task; copy tasks from feature | Works | TODO | | |
| TT-003 | Assign task, due date, complete, drag reorder | Works; shows on assignee Dashboard Project Tasks | TODO | | |
| TT-004 | Comments > Post Comment | Works | TODO | | |
| TT-005 | Table / Card view; search | Works | TODO | | |
| TT-006 | RA / RG / WG | Read-only / scoped correctly | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
