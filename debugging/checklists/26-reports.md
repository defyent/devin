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
| RPT-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| RPT-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| RPT-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| RPT-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| RPT-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| RPT-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| RPT-001 | Add Template wizard Name > Columns > Summarise > Date Range > Review | Navigates both ways | TODO | | |
| RPT-002 | Data Source: Flights / SMS Reports / People / Forms | Each offered only with matching permission; description text shown | TODO | | |
| RPT-003 | Change data source with columns set | Confirm prompt; columns cleared | TODO | | |
| RPT-004 | Report Type All Data / Totals Only; Group By; Group Sum By | Correct output | TODO | | |
| RPT-005 | Display Format Table and each Graph type | Render | TODO | | |
| RPT-006 | Columns incl. Extra Flight Info, Meter, form fields; filters, filter groups | Correct | TODO | | |
| RPT-007 | Duplicate / save template | Works | TODO | | |
| RPT-008 | Run with date range and presets | Report Data + Summary | TODO | | |
| RPT-009 | Export CSV / Create PDF | Files correct, dates in org format | TODO | | |
| RPT-010 | Report Results: reopen / delete | Works; result access rules per §11.6 | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
