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
| HUB-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Administration > Settings and Tools loads with no page errors |
| HUB-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS |  | Help opens; closes with x, Close (there is no 'Got it' button), a click outside and Esc |
| HUB-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag-out (mousedown in the Help content, release outside) keeps Help open. Ctrl+K search popup also opens, finds 'time' (Timesheets, Time Zone) and closes with Esc |
| HUB-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | PASS |  | Hub shows no dates/times; header clock shows UTC and Local in DD/MM/YYYY |
| HUB-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | At 390px the cards stack in one column, links 310px wide, document width 375px |
| HUB-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low still sees the menu link; the hub shows 'Access Denied: You do not have permission to access the System Settings feature' |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| HUB-001 | Category cards and links | Operations, People, Forms, Safety, Configuration, Training, Logs, Notices, Maintenance — every link opens its page | PASS |  | 9 cards: Operations, People, Forms, Safety, Configuration, Training, Logs, Notices, Maintenance. All 23 links open the right page (Flight Schedule settings ... Inspection Notifications). Settings DFR asks for templates2/settings_dfr/colorpicker.js and gets a 404 (see checklist 32) |
| HUB-002 | Arrow keys + Enter | Move between links and open | PASS |  | Focus Flight Schedule, then ArrowDown/ArrowRight/ArrowUp move focus link by link (ended on Access Manager); Enter opens Access Manager settings |
| HUB-003 | Hub access without page permission | Linked page shows Access Denied | PASS | hub003_denied | Second (System Settings A) opens Settings and Tools. Clicking Flight Schedule (settings), which Second has no permission for, shows "Access Denied: You do not have permission to access the Flight Schedule Settings". |
| HUB-004 | Empty 'Notices' card | Card has no links on staging — log | FAIL | BUG-NOT-003 | Notices card shows its title and description but no links (same as BUG-NOT-003 / UX-11) |
| HUB-005 | Missing from hub vs guide | WhatsApp, Maintenance, Location Planner, Chat not linked — confirm intended | PASS |  | Confirmed not linked from the hub: WhatsApp, Maintenance (only Inspection Notifications under Maintenance), Location Planner, Chat. Asking Jon if that is intended |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| UX-11 | Low | Open (external) | Settings hub "Notices" card has no links (see also seed HUB-004) |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
