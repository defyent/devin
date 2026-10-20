# Daily Flight Record

- **Checklist ID prefix:** `DFR`
- **Guide section:** §8.5
- **Where:** Flight Operations > Daily Flight Record
- **Permission:** DFR A/RG
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| DFR-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| DFR-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| DFR-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| DFR-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| DFR-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| DFR-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| DFR-001 | Default list | Completed flights only | TODO | | |
| DFR-002 | Manage Columns | Every column listed incl. active Extra Flight Info; choice persists | TODO | | |
| DFR-003 | Long text cell | Full Text popup | TODO | | |
| DFR-004 | Click row | Opens Flight Details | TODO | | |
| DFR-005 | Simple search multi-word | Each word must match across ID, rego, PIC, crew, customer, route, notes, activity, category | TODO | | |
| DFR-006 | Enable Advanced Filtering in Settings > DFR | Filter panel appears | TODO | | |
| DFR-007 | Status checkboxes | Completed + Complete Locked ticked by default; others filter correctly | TODO | | |
| DFR-008 | Date From/To, Flight ID, Rego, PIC, Customer, Search | Filter correctly; active-filter badge; clear works | TODO | | |
| DFR-009 | RG user | Only flights for people in their groups | TODO | | |
| DFR-010 | Performance with 9,400+ flights | Acceptable load time | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
