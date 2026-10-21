# Roster Viewer

- **Checklist ID prefix:** `RV`
- **Guide section:** §9.3
- **Where:** Personnel > Roster Viewer
- **Permission:** Roster Viewer A/RG/RO
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| RV-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Personnel > Roster Viewer opens 'Staff Roster LIVE' October 2026 grid, no console errors |
| RV-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-RV-001 | No Help (?) button on Roster Viewer |
| RV-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag-out (mousedown inside, release outside) keeps Group Visibility and Full Shift Legend open |
| RV-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-RV-003 | Header month and day numbers fine; shift note popup shows 'October 5, 2026' instead of 05/10/2026. Legend times 24-hour |
| RV-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | 390 px: page itself doesn't scroll sideways; the grid scrolls inside its box with the Employee column fixed; month arrows, search, font and group buttons fit. 'This Month' link is hidden at this width |
| RV-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| RV-001 | Month grid, < > This Month | Published (live) roster shown | PASS |  | Grid shows 'Staff Roster LIVE' for October 2026; < goes to September, > to November, This Month back to October; today (21) highlighted |
| RV-002 | Groups shown | Only Show Group in Roster; people only On Roster | TODO | | |
| RV-003 | Search staff… | Filters | PASS |  | Typing 'Aisha' in Search staff highlights the matching rows (Aisha Johnston, Aisha Pearce) in yellow; other rows stay visible (highlight, not hide). × clears it |
| RV-004 | Click shift | Shift Details | FAIL | BUG-RV-002 | Clicking a shift badge does nothing. Only the small blue corner opens 'Note for <name>' (date + note). Note, legend closes with Esc and ×; Full Shift Legend lists codes, times and 'Counts as Duty Time' |
| RV-005 | Group Visibility > Apply | Hides/shows groups | PASS |  | Group Visibility lists BETA TEST ONLY Group, Crew, Engineers, Pilots (Your Group). Ticking Engineers > Apply adds the Engineers block; unticking > Apply removes it; choice kept after reload. Restored to Pilots only |
| RV-006 | RG / RO | Only own groups / self | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| VIS-20 | Low | Open (external) | Text "< >" arrows used in Roster Viewer, Roster Builder and date picker; "today" vs "Today" |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
