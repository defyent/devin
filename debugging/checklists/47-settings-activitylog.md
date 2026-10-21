# Settings – Activity Log

- **Checklist ID prefix:** `SLOG`
- **Guide section:** §12.19
- **Where:** Settings and Tools > Logs > Activity Log
- **Permission:** settings_activitylog = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SLOG-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SLOG-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SLOG-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SLOG-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SLOG-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SLOG-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SLOG-001 | Pills Flights / SMS Reports / Personnel with search | Entries for this run's changes appear | TODO | | |
| SLOG-002 | View-only | No edit controls | TODO | | |
| SLOG-003 | Performance with large log | Acceptable | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| DATE-08 | Low | Open (external) | Activity Log uses lowercase "am" and 12-hour time even when 24-hour is set |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
