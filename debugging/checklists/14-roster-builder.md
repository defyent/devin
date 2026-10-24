# Roster Builder

- **Checklist ID prefix:** `RB`
- **Guide section:** §9.4
- **Where:** Settings and Tools > People > Roster Builder
- **Permission:** Roster Builder A/WG
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| RB-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > People > Roster Builder opens 'Staff Roster Live' (Oct 2026), no console errors |
| RB-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-RB-001 | No page Help (?). Copy/Paste Instructions popup: × and Close work, Escape and outside click don't |
| RB-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Copy/Paste Instructions, Rename Draft and Copy Live to Draft popups stay open after mousedown inside / release outside |
| RB-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-RB-004 | Month header/day columns fine; Rule Violations popup says 'Monday, October 5' (US format, no year) |
| RB-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | FAIL | BUG-RB-006 | 390 px: no page sideways scroll and month/draft/bulk/search controls visible, but grid squeezed to about 175 px beside the palette, Draft Edit Mode banner covers search and palette, violations toggle and Live Edit hidden |
| RB-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Administration > Settings and Tools shows 'Access Denied: You do not have permission to access the System Settings feature', so Roster Builder can't be reached (menu link still visible, see BUG-PERM-001) |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| RB-001 | « ‹ › » navigation, This Month, Search | Double arrows move half a month | PASS |  | » moves forward 2 weeks (Oct 18 - Nov 14), again to Nov 1-30; « back to Oct 18 - Nov 14; < / > whole months; This Month back to Oct 1-31. Search 'Aisha' highlights the 2 matching rows |
| RB-002 | Select Roster View: Live / Draft | Switches | PASS |  | Select Roster View lists Live Roster and the drafts; picking a draft switches the grid, the badge shows the draft name and an orange 'Draft Edit Mode - Changes are saved to this draft only' banner appears |
| RB-003 | Bulk: New Draft (BETA TEST ONLY), Rename, Copy Live to Draft (Merge / Clear then Copy), Delete Draft | Each works with confirmation | FAIL | BUG-RB-002 | New Draft (no name prompt) and Rename work; empty rename silently ignored. Copy Live to Draft Clear then Copy works but took about 6 min for 1690 shifts. Delete or Clear Draft popup: 'Delete entire draft permanently' gives 'Draft ... deleted successfully' and the draft leaves the list |
| RB-004 | Drag shift from palette to cell | Shift placed | PASS |  | BETA TEST ONLY Draft: dragged 'Office Hours' from the palette onto Aisha Johnston 1 Oct (empty) - cell shows OH, 'Shift added successfully' |
| RB-005 | Drag shift to delete zone | Removed | PASS |  | Dragged the OH shift from Aisha Johnston 1 Oct onto the bin (delete zone) - 'Shift deleted successfully', cell empty |
| RB-006 | Copy/paste with violations ON | Not allowed (documented) | FAIL | BUG-RB-003 | Violations ON: Ctrl+C 'Copied 1 cell(s)', Ctrl+V 'Successfully pasted 1 shift(s)' - not blocked |
| RB-007 | Violations OFF: click, Shift+click range, Ctrl+C/X/V, Esc | Blue/red borders; preview; earliest shift pasted | PASS |  | Violations off (CHECKING DISABLED), draft: click selects 1 cell, Shift+click selects range 5-7 Oct (3), Ctrl+C 'Copied 3 cell(s)', click 1 Oct shows 3-cell paste preview, Ctrl+V 'Successfully pasted 3 shift(s)' (PM NT AM on 1-3 Oct), Esc clears selection |
| RB-008 | Person name > Shift Summary; Apply Shift Pattern; Clear Month | Counts and hours correct | FAIL | BUG-RB-005 | Name click opens Shift Summary: counts match the row (DS 7, NS 1, AM 5, PM 9, NT 5 = 27). Apply Shift Pattern DS+NS, 1 day off from 01/10/2026: 'Applied pattern: 6 shifts added' (fills empty days only), summary DS 10 / NS 4 = 33, but Total Duty Hours stays 228.00 (check shift durations in 39). Clear October 2026 asks to confirm, then 'Cleared all shifts for Aisha Johnston', row empty. Empty pattern Apply: popup closes with no message + JS error. Escape ignored on Shift Summary (BUG-RB-001) |
| RB-009 | Reorder people; Reset Order | Works | PASS |  | Pilots > Reorder: handles appear, dragged Aisha Pearce above Aisha Johnston, Save Order 'Order saved for Pilots', Reset Order button appears; Reset Order asks to confirm, 'Order reset for Pilots', alphabetical order back and Reset button gone. Confirm ignores Escape (BUG-RB-001) |
| RB-010 | Cell notes add/edit/delete | Works | PASS |  | Hover a shift cell > corner note button > 'Note for Aisha Johnston': add 'BETA TEST ONLY note', reopen shows it, edit saves, Delete Note clears it (marker gone). Empty cells open the popup with the textarea disabled ('A shift must be assigned to add a note.'). Escape doesn't close it (BUG-RB-001); date in US format (BUG-RB-004) |
| RB-011 | Violations toggle | Rule Violations from FRMS rostered shift rules | PASS |  | Toggle ON: badge VIOLATIONS FOUND, flagged shifts get red border + warning triangle (628 cells, about 0.5 s to compute). Triangle opens 'Rule Violations' - 'Max 8.0 Duty Time hours in any 24 hours period, Applies to: Pilots' (FRMS rostered shift rule). Toggle OFF restores CHECKING DISABLED. Triangle is mostly covered by the shift badge; only its top-left corner is clickable |
| RB-012 | Export PDF | Generated | PASS |  | Bulk actions > Export to PDF downloads 'Roster_October_2026_Draft___BETA_TEST_ONLY_Draft.pdf' (3 pages): title 'Roster for October 2026 - Draft - BETA TEST ONLY Draft', per-day totals per shift type and per-person rows; totals for 1-3 Oct match the grid (AM 18/0/20, PM 20/19/0, NT 0/20/20, OH 19/19/0) |
| RB-013 | Publish Month: Merge / Clear then Publish (on draft only) | Live roster updated; Viewer, Dashboard, Schedule roster row, Timesheets reflect it | FAIL | BUG-RB-007 | Tested on December 2027 (empty in live). Publish Month popup offers Clear then Publish / Publish Only (Merge). Merge with 1 BETA TEST ONLY OH shift: 'Draft "BETA TEST ONLY Draft" published to live roster successfully', shift appears in Live. Clear then Publish with the draft emptied: native confirm, then no message and the live shift stays. Test shift removed from live via Live Edit; live December 2027 empty again |
| RB-014 | Enable Live Edit > Confirm & Edit | Live roster editable | PASS |  | Live Roster view is read-only (0 draggable shifts). Enable Live Edit > 'Confirm Live Roster Edit' (20 minute access warning) > Confirm & Edit: button becomes Finish Editing, all 1690 shifts draggable. Finish Editing turns it off. No live data changed. Confirm popup ignores Escape (BUG-RB-001) |
| RB-015 | WG user | Can only edit own groups | FAIL | rb015_wg | BUG-RB-008: Grpuser (Roster Builder WG) has no menu path to Roster Builder. It isn't in the sidebar, and Settings and Tools needs System Settings. So I couldn't check whether WG can only edit its own groups. |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`STATUS.md`](../STATUS.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| VIS-24 | Low | Open (external) | Roster Builder: only orange primary button; dashed-border trash button |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Draft rosters 'New Draft 1' and 'New Draft 2' (renamed 'BETA TEST ONLY Draft', live October 2026 copied in, pattern/notes/paste tests) | Roster Builder drafts | Yes - both deleted with Delete entire draft permanently |
| Aisha Johnston October 2026 shifts cleared (Clear Month test) | BETA TEST ONLY Draft only | Yes - draft deleted, live untouched |
| Pilots custom order (Aisha Pearce first) | Roster Builder Pilots group | Yes - Reset Order, alphabetical again |
| One Office Hours shift for Aisha Pearce on 01/12/2027 published to live | Live roster December 2027 | Yes - removed with Live Edit, December 2027 empty |
