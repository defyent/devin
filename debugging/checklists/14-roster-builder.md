# Roster Builder

- **Checklist ID prefix:** `RB`
- **Guide section:** §9.4
- **Where:** Settings and Tools > People > Roster Builder
- **Permission:** Roster Builder A/WG
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| RB-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > People > Roster Builder opens 'Staff Roster Live' (Oct 2026), no console errors |
| RB-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-RB-001 | No page Help (?). Copy/Paste Instructions popup: × and Close work, Escape and outside click don't |
| RB-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| RB-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| RB-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| RB-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| RB-001 | « ‹ › » navigation, This Month, Search | Double arrows move half a month | PASS |  | » moves forward 2 weeks (Oct 18 - Nov 14), again to Nov 1-30; « back to Oct 18 - Nov 14; < / > whole months; This Month back to Oct 1-31. Search 'Aisha' highlights the 2 matching rows |
| RB-002 | Select Roster View: Live / Draft | Switches | PASS |  | Select Roster View lists Live Roster and the drafts; picking a draft switches the grid, the badge shows the draft name and an orange 'Draft Edit Mode - Changes are saved to this draft only' banner appears |
| RB-003 | Bulk: New Draft (BETA TEST ONLY), Rename, Copy Live to Draft (Merge / Clear then Copy), Delete Draft | Each works with confirmation | FAIL | BUG-RB-002 | New Draft creates 'New Draft 1/2' straight away (no name prompt or message). Rename: empty name silently ignored; 'BETA TEST ONLY Draft' saves ('Draft renamed to ...'). Copy Live to Draft offers Clear then Copy / Copy Only (Merge); Clear then Copy works ('Live roster copied ... successfully', rows match live) but takes about 6 min for 1690 shifts. Delete Draft: see end of checklist |
| RB-004 | Drag shift from palette to cell | Shift placed | PASS |  | BETA TEST ONLY Draft: dragged 'Office Hours' from the palette onto Aisha Johnston 1 Oct (empty) - cell shows OH, 'Shift added successfully' |
| RB-005 | Drag shift to delete zone | Removed | PASS |  | Dragged the OH shift from Aisha Johnston 1 Oct onto the bin (delete zone) - 'Shift deleted successfully', cell empty |
| RB-006 | Copy/paste with violations ON | Not allowed (documented) | TODO | | |
| RB-007 | Violations OFF: click, Shift+click range, Ctrl+C/X/V, Esc | Blue/red borders; preview; earliest shift pasted | PASS |  | Violations off (CHECKING DISABLED), draft: click selects 1 cell, Shift+click selects range 5-7 Oct (3), Ctrl+C 'Copied 3 cell(s)', click 1 Oct shows 3-cell paste preview, Ctrl+V 'Successfully pasted 3 shift(s)' (PM NT AM on 1-3 Oct), Esc clears selection |
| RB-008 | Person name > Shift Summary; Apply Shift Pattern; Clear Month | Counts and hours correct | TODO | | |
| RB-009 | Reorder people; Reset Order | Works | TODO | | |
| RB-010 | Cell notes add/edit/delete | Works | TODO | | |
| RB-011 | Violations toggle | Rule Violations from FRMS rostered shift rules | TODO | | |
| RB-012 | Export PDF | Generated | TODO | | |
| RB-013 | Publish Month: Merge / Clear then Publish (on draft only) | Live roster updated; Viewer, Dashboard, Schedule roster row, Timesheets reflect it | TODO | | |
| RB-014 | Enable Live Edit > Confirm & Edit | Live roster editable | TODO | | |
| RB-015 | WG user | Can only edit own groups | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| VIS-24 | Low | Open (external) | Roster Builder: only orange primary button; dashed-border trash button |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Draft roster 'New Draft 1' created by Bulk > New Draft in RB-003 (no name prompt) | Roster Builder drafts | No - to delete in RB-003 |
| Draft roster 'New Draft 2' created in RB-003, renamed 'BETA TEST ONLY Draft' | Roster Builder drafts | No - to delete at end of 14 |

| Draft roster 'New Draft 1' created by Bulk > New Draft in RB-003 (no name prompt) | Roster Builder drafts | No - to delete in RB-003 |
| Draft roster 'New Draft 2' created in RB-003, renamed 'BETA TEST ONLY Draft' | Roster Builder drafts | No - to delete at end of 14 |