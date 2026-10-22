# Settings – Activity Log

- **Checklist ID prefix:** `SLOG`
- **Guide section:** §12.19
- **Where:** Settings and Tools > Logs > Activity Log
- **Permission:** settings_activitylog = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SLOG-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Logs > Activity Log opens settings_activitylog (Activity Browser, pills Flights / SMS Reports / Personnel, 30 rows), with no console errors. |
| SLOG-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-SLOG-001 | There is no page Help (?) control. |
| SLOG-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | N/A |  | The page has no popups. Clicking a row opens nothing. |
| SLOG-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-SLOG-001 | Shows "22 Oct 2026, 02:51 am" / "21 Oct 2026, 10:35 pm" instead of DD/MM/YYYY 24-hour. The local time (Pacific/Auckland) is correct. |
| SLOG-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | 390 px: the pills become a dropdown and rows become cards. scrollWidth 375, nothing off-screen. |
| SLOG-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Settings and Tools shows Access Denied (System Settings). |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SLOG-001 | Pills Flights / SMS Reports / Personnel with search | Entries for this run's changes appear | PASS |  | The pills switch columns: Flights (Flight ID, Changes), SMS Reports (Report ID, Field, Description), Personnel (Person, Changes). This run's changes are all there: flight 42903 category/status edits and deletes of 42904-42908; SMS #2060 status, comment, document, action and personnel changes; #2061 created and "Investigator removed: Zoe Mason"; Personnel exam submit, signature and photo for BETA TEST ONLY Lowperm. Search filters each pill. |
| SLOG-002 | View-only | No edit controls | PASS |  | View-only: no buttons on the page, only the search box and the pills. No edit or delete controls in the rows. |
| SLOG-003 | Performance with large log | Acceptable | PASS |  | 30 rows load at first. Scrolling loads more (30 -> 180 rows in about 7.6 s, with 1.5 s waits between scrolls). Pills switch in under a second. No errors. |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| DATE-08 | Low | Open (external) | Activity Log uses lowercase "am" and 12-hour time even when 24-hour is set |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
