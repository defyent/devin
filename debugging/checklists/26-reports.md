# Reports

- **Checklist ID prefix:** `RPT`
- **Guide section:** §11.6
- **Where:** Administration > Reports
- **Permission:** Reports = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| RPT-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Administration > Reports loads (Report Templates list with Last Run '16/10/2026 16:11'), no page errors |
| RPT-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-RPT-001 | No Help (?) on the page; Escape does not close New Report Template |
| RPT-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | New Report Template, Change Data Source, Unsaved Changes and Delete Report Result popups stay open after mousedown inside / release outside (Escape also does nothing - BUG-RPT-001) |
| RPT-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | PASS |  | Last Run / Run Date and report data show DD/MM/YYYY HH:MM (e.g. 22/10/2026 01:20, local time); filter summary '01/10/2026 00:00 and 31/10/2026 23:59'. CSV export is wrong - see RPT-009 |
| RPT-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | FAIL | BUG-RPT-003 | At 390px the Report Templates columns overlap each other and Actions need horizontal scroll |
| RPT-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low sees the Reports menu link but gets 'Error Access Denied: You do not have permission to access Reports' (menu link visibility tracked in BUG-PERM-001) |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| RPT-001 | Add Template wizard Name > Columns > Summarise > Date Range > Review | Navigates both ways | PASS |  | Add Report Template > Step-by-Step Wizard: Name > Columns > Summarise > Date Range > Review with Next, and Back returns a step (step bar ticks each completed step) |
| RPT-002 | Data Source: Flights / SMS Reports / People / Forms | Each offered only with matching permission; description text shown | BLOCKED |  | As Service Account the Data Source list offers Flights (includes leg information), SMS Reports, People, Forms with a description under it ('One row per flight ...'). Per-permission filtering needs users with partial permissions - retest in 90 |
| RPT-003 | Change data source with columns set | Confirm prompt; columns cleared | PASS |  | Changing Data Source Flights > SMS Reports in Edit asks 'Change Data Source? Changing the data source removes the selected columns, Group Sum By fields and filters ...' (Cancel/Continue). Back to Templates then asks 'Unsaved Changes ...'; template stays Flights |
| RPT-004 | Report Type All Data / Totals Only; Group By; Group Sum By | Correct output | PASS |  | Existing 'QA Totals Graph Test' result (Totals Only) shows Total Count grouped by Flight Type / Aircraft with summed Flight Time and Engine Time; BETA report (All Data) lists every row |
| RPT-005 | Display Format Table and each Graph type | Render | PASS |  | Table display (BETA report) and Graph display (QA Totals Graph Test, Bar) both render; other graph types not re-run |
| RPT-006 | Columns incl. Extra Flight Info, Meter, form fields; filters, filter groups | Correct | BLOCKED |  | Extra Flight Info, Meter and form-field columns plus filter groups need matching setup data (checklists 34/36). Retest in 99 |
| RPT-007 | Duplicate / save template | Works | PASS |  | Save Template via wizard 'Create Template' adds 'BETA TEST ONLY Report'; Duplicate in Edit adds a copy straight away (Last Run 'Never') |
| RPT-008 | Run with date range and presets | Report Data + Summary | PASS |  | Wizard date range with 'This Month' preset (01/10/2026-31/10/2026). Run (play button) goes to Report Results; opening it shows Report Summary (columns, filters) and Report Data (8795, 42903; Total: 2) |
| RPT-009 | Export CSV / Create PDF | Files correct, dates in org format | FAIL | BUG-RPT-002 | Create PDF downloads beta_test_only_report_report.pdf with dates 16/10/2026 06:00 and 'Generated: 22/10/2026 01:21' (correct). Export CSV downloads the rows but dates are '2026-10-16 06:00:00' |
| RPT-010 | Report Results: reopen / delete | Works; result access rules per §11.6 | PASS |  | Opening a result from Report Results shows its data; Back to Results returns. Delete asks 'Delete Report Result? ...' and removes it. Deleting a template asks and says results are kept. Result access rules for other users not checked (needs 90) |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| FORM-38 | Info | Info | Reports help text mentions renewals, but Form Browser has no Renewals folder |
| DATE-01 | High | Open (external) | Reports Last Run shows "16 10M 2026" with DD MMM YYYY; Reports time ignores 12-hour setting |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Report template 'BETA TEST ONLY Report', its copy and its result | Administration > Reports | Yes - all deleted |
