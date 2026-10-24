# Daily Flight Record

- **Checklist ID prefix:** `DFR`
- **Guide section:** §8.5
- **Where:** Flight Operations > Daily Flight Record
- **Permission:** DFR A/RG
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| DFR-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Sidebar > Flight Operations > Daily Flight Record loads (action=dailyflightrecord), no console errors (shot dfr_open) |
| DFR-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-DFR-001 | No Help (?) button anywhere on the page |
| DFR-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS | BUG-DFR-001 | Manage Columns: drag-out keeps it open; x, Done and outside click close it. Escape does not (BUG-DFR-001) |
| DFR-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | PASS |  | Start/End times DD/MM/YYYY HH:MM; date filters DD/MM/YYYY as set in Settings > Time Zone |
| DFR-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | 390 px: no horizontal scroll (375 <= 390), table becomes cards (rego, status, times, PIC, crew, flight time, activity); filters collapse into an Advanced Filters bar (shot dfr_mobile). The Performance timing panel again floats over the cards until closed |
| DFR-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low (no DFR right): link shown, page says 'Access Denied: You do not have permission to access the daily flight record', no rows (shot dfr_low) |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| DFR-001 | Default list | Completed flights only | PASS |  | Default list shows only Completed flights (newest first: #42903, #8795, #7435...) |
| DFR-002 | Manage Columns | Every column listed incl. active Extra Flight Info; choice persists | PASS |  | Manage Columns lists ID, Status, Start/End Time, Rego, PIC, Secondary Flight Crew, Customer, Flight Time, Engine Time, Flight Activity, Flight Category, Notes, Route, Debrief and Flight Meters (Cycles, Engine Hours, Flight Hours). Ticking Notes persisted after leaving to Dashboard and coming back; restored afterwards. No Extra Flight Info fields are set up on stresstest, so none listed |
| DFR-003 | Long text cell | Full Text popup | PASS |  | Clicking a Notes cell opens a 'Notes' Full Text popup with the whole text (shot dfr_fulltext) |
| DFR-004 | Click row | Opens Flight Details | PASS |  | Clicking row #8795 opens Flight Details for flight 8795 (shot dfr_row) |
| DFR-005 | Simple search multi-word | Each word must match across ID, rego, PIC, crew, customer, route, notes, activity, category | PASS |  | 'ZK-RVN Fisher' -> 1 row (#8795), so words are ANDed across rego and PIC; 'BETA zzznomatch' -> 0 rows. 'Aaron Charter' and 'Charter Aaron' give the same rows (word order ignored) |
| DFR-006 | Enable Advanced Filtering in Settings > DFR | Filter panel appears | PASS |  | Tested in 32 (SDFR-001): Settings > Daily Flight Record, Enable Advanced Filtering Off + Save hides the panel; On + Save brings back the Advanced Filters panel (status, date from/to, flight ID, rego, PIC, customer). Left On. |
| DFR-007 | Status checkboxes | Completed + Complete Locked ticked by default; others filter correctly | PASS |  | Status pills on a fresh load: Completed and Complete Locked ticked, Open/Cancelled/Deleted unticked; active-filter badge 2 |
| DFR-008 | Date From/To, Flight ID, Rego, PIC, Customer, Search | Filter correctly; active-filter badge; clear works | FAIL | BUG-DFR-002, BUG-DFR-003 | Flight ID 42903 -> 1 row, badge 1; Rego ZK-SIM -> only ZK-SIM rows, badge 3; Date 01/05-08/05/2026 -> rows dated 06/05-08/05 only. Clear Filters unticks every status and shows Open/Deleted flights; date fields show today when unused (BUG-DFR-002). Quick filter changes append duplicate / wrong-status rows (BUG-DFR-003) |
| DFR-009 | RG user | Only flights for people in their groups | PASS | dfr009_grp | BETA TEST ONLY Grpuser (Daily Flight Record = RG, member of BETA TEST ONLY Group only) sees just 42909 (PIC Grpuser) and 42903 (PIC Lowperm, also in the group). No other people's flights are listed. |
| DFR-010 | Performance with 9,400+ flights | Acceptable load time | PASS |  | Menu click to rows visible 1.4 s; dailyflightrecord_json 0.26-0.28 s for 30 rows. Scrolling the table loads 30 more each time (30 > 60 > 90), each page about 0.1 s server time |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`STATUS.md`](../STATUS.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| DATE-05 | Medium | Open (external) | DFR filter dates are lost in Scroll Wheel and Native modes |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
