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
| DFR-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Sidebar > Flight Operations > Daily Flight Record loads (action=dailyflightrecord), no console errors (shot dfr_open) |
| DFR-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-DFR-001 | No Help (?) button anywhere on the page |
| DFR-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS | BUG-DFR-001 | Manage Columns: drag-out keeps it open; x, Done and outside click close it. Escape does not (BUG-DFR-001) |
| DFR-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | PASS |  | Start/End times DD/MM/YYYY HH:MM; date filters DD/MM/YYYY as set in Settings > Time Zone |
| DFR-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| DFR-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| DFR-001 | Default list | Completed flights only | PASS |  | Default list shows only Completed flights (newest first: #42903, #8795, #7435...) |
| DFR-002 | Manage Columns | Every column listed incl. active Extra Flight Info; choice persists | PASS |  | Manage Columns lists ID, Status, Start/End Time, Rego, PIC, Secondary Flight Crew, Customer, Flight Time, Engine Time, Flight Activity, Flight Category, Notes, Route, Debrief and Flight Meters (Cycles, Engine Hours, Flight Hours). Ticking Notes persisted after leaving to Dashboard and coming back; restored afterwards. No Extra Flight Info fields are set up on stresstest, so none listed |
| DFR-003 | Long text cell | Full Text popup | PASS |  | Clicking a Notes cell opens a 'Notes' Full Text popup with the whole text (shot dfr_fulltext) |
| DFR-004 | Click row | Opens Flight Details | PASS |  | Clicking row #8795 opens Flight Details for flight 8795 (shot dfr_row) |
| DFR-005 | Simple search multi-word | Each word must match across ID, rego, PIC, crew, customer, route, notes, activity, category | PASS |  | 'ZK-RVN Fisher' -> 1 row (#8795), so words are ANDed across rego and PIC; 'BETA zzznomatch' -> 0 rows. 'Aaron Charter' and 'Charter Aaron' give the same rows (word order ignored) |
| DFR-006 | Enable Advanced Filtering in Settings > DFR | Filter panel appears | TODO | | |
| DFR-007 | Status checkboxes | Completed + Complete Locked ticked by default; others filter correctly | PASS |  | Status pills on a fresh load: Completed and Complete Locked ticked, Open/Cancelled/Deleted unticked; active-filter badge 2 |
| DFR-008 | Date From/To, Flight ID, Rego, PIC, Customer, Search | Filter correctly; active-filter badge; clear works | FAIL | BUG-DFR-002 | Flight ID 42903 -> 1 row, badge 1; Rego ZK-SIM -> only ZK-SIM rows, badge 3; Date 01/05-08/05/2026 -> rows dated 06/05-08/05 only. Clear Filters unticks every status and shows Open/Deleted flights; date fields show today when unused (BUG-DFR-002) |
| DFR-009 | RG user | Only flights for people in their groups | TODO | | |
| DFR-010 | Performance with 9,400+ flights | Acceptable load time | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| DATE-05 | Medium | Open (external) | DFR filter dates are lost in Scroll Wheel and Native modes |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
