# Cross-cutting: performance, console and network

- **Checklist ID prefix:** `PERF`
- **Guide section:** Login message
- **Where:** Every page
- **Permission:** n/a
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| PERF-001 | Performance panel timings | Server < 500 ms (orange values flagged) | FAIL | BUG-SWAB-003 | The developer "Performance" timings panel shows to users on Active Flights, W&B Settings and Access Manager (Total Time 7.0 ms on Access Manager), and on a phone it covers content. Page timings are low (Access Manager 7 ms server time). |
| PERF-002 | Console | No JS errors / uncaught promise rejections | FAIL | BUG-RB-005 | Opening 11 modules (Flight Schedule, DFR, Active Flights, All Personnel, Roster Viewer, Safety Reports, Hazard Register, File Browser, Reports, Support, Task Tracker) logs no console errors. Some actions do throw errors: Roster Builder openErrorModal (BUG-RB-005), and deleting a used exam logs the error only (BUG-EXM-008). |
| PERF-003 | Network | No 4xx/5xx; no duplicate repeated calls | FAIL | BUG-SDFR-001 | The same 11 modules give no 4xx/5xx responses. DFR settings asks for colorpicker.js, which returns 404 (BUG-SDFR-001). Folder delete and change password return "Invalid Action" (BUG-FB-006, BUG-PD-011). |
| PERF-004 | Badge polling (60 s / chat 20 s) | No runaway requests | PASS |  | Idle for 70 s on Task Tracker: check_overdue_flights, get_chat_badge_count and get_chat_new_messages ran 3 times each (about every 20 to 25 s). Notices and support badge counts ran once (60 s). There were no duplicate bursts. |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| INFO-01 | Info | Info | Version tag (?v=) missing on about half the modules (see section 5). Seen in the POP-01 retest: without ?v= the browser kept serving old JS, so the drag-out fixes only appeared after clearing the cache. Users may not get fixes until their cache expires |
| INFO-02 | Info | Info | Performance popup shows on 9 modules and covers content (see section 6) |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
