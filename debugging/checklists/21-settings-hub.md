# Settings and Tools hub

- **Checklist ID prefix:** `HUB`
- **Guide section:** §11.1
- **Where:** Administration > Settings and Tools
- **Permission:** System Settings = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| HUB-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| HUB-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| HUB-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| HUB-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| HUB-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| HUB-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| HUB-001 | Category cards and links | Operations, People, Forms, Safety, Configuration, Training, Logs, Notices, Maintenance — every link opens its page | TODO | | |
| HUB-002 | Arrow keys + Enter | Move between links and open | TODO | | |
| HUB-003 | Hub access without page permission | Linked page shows Access Denied | TODO | | |
| HUB-004 | Empty 'Notices' card | Card has no links on staging — log | TODO | | |
| HUB-005 | Missing from hub vs guide | WhatsApp, Maintenance, Location Planner, Chat not linked — confirm intended | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| UX-11 | Low | Open (external) | Settings hub "Notices" card has no links (see also seed HUB-004) |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
