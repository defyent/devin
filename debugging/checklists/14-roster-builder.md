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
| RB-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| RB-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| RB-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| RB-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| RB-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| RB-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| RB-001 | « ‹ › » navigation, This Month, Search | Double arrows move half a month | TODO | | |
| RB-002 | Select Roster View: Live / Draft | Switches | TODO | | |
| RB-003 | Bulk: New Draft (BETA TEST ONLY), Rename, Copy Live to Draft (Merge / Clear then Copy), Delete Draft | Each works with confirmation | TODO | | |
| RB-004 | Drag shift from palette to cell | Shift placed | TODO | | |
| RB-005 | Drag shift to delete zone | Removed | TODO | | |
| RB-006 | Copy/paste with violations ON | Not allowed (documented) | TODO | | |
| RB-007 | Violations OFF: click, Shift+click range, Ctrl+C/X/V, Esc | Blue/red borders; preview; earliest shift pasted | TODO | | |
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
| | | |
