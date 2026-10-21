# Active Flights and Live Tracking

- **Checklist ID prefix:** `AF`
- **Guide section:** §8.4
- **Where:** Flight Operations > Active Flights
- **Permission:** Active Flights A/RA/WG/RG; Live Tracking
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| AF-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Sidebar > Flight Operations > Active Flights loads (action=activeflights), no console errors (shot af_open) |
| AF-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-AF-003 | No page Help (?) button on Active Flights. 'About Live Tracking' popup: Got it closes, clicking outside closes, no x button, Escape does nothing (BUG-AF-003) |
| AF-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Mouse down inside Contact Details, Adjust SAR and Add Note popups, release outside: all stay open. (Escape does not close them - BUG-AF-003) |
| AF-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| AF-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| AF-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| AF-001 | List content | Only open flights whose start or SAR time has passed | FAIL | BUG-AF-002 | 1,377 rows: 1,364 PAST, 7 OVERDUE and 6 FUTURE. The FUTURE flights (#8853-#8860) have not started and have no SAR time ('01/01/1970 00:00 NO SAR TIME SET') but are still listed (BUG-AF-002) (shot af_future) |
| AF-002 | Stats cards: Total, Active, Past, Overdue | Match list | FAIL | BUG-AF-002 | Cards: Total 1377, Active 0, Past 1364, Overdue 7. Past and Overdue match the list, but the 6 FUTURE rows are counted in Total and in no other card (BUG-AF-002) |
| AF-003 | Table / card view; sort by SAR / Start Time | Works; mobile shows cards only | PASS |  | Table / card view toggle (table_rows / grid_view) works; Sort by SAR Time / Start Time re-orders the list. Mobile check in AF-S05 |
| AF-004 | SAR countdown / overdue timer | Counts correctly; status colours from Settings > Flight Schedule | FAIL | BUG-AF-001 | Overdue rows show 'OVERDUE by 2784h 23m' etc. 1,365 rows with SAR watch disabled show SAR Time '01/01/1970 00:00' above 'SAR Watch Disabled' (BUG-AF-001). Status colours not compared to settings yet |
| AF-005 | Click row/card | Opens Flight Details | TODO | | |
| AF-006 | Click PIC | Contact details popup | PASS |  | Click PIC 'Graham Clarke' > popup 'Graham Clarke - Contact Details' with Mobile 021-555-0096, Email graham.clarke96@datahangar.net, Close (shot af_pic) |
| AF-007 | Notes | Readable | PASS |  | Notes column readable (e.g. 'Maintenance test flight post 100hr', 'No notes' when empty) |
| AF-008 | Adjust SAR (A/WG) | Picker + Disable/Enable SAR Watch + Save; hidden for RA/RG | TODO | | |
| AF-009 | Add Note (A/WG) | Appended to flight | TODO | | |
| AF-010 | Auto-refresh | Refreshes; pauses while editing | TODO | | |
| AF-011 | Complete a flight | Disappears from Active Flights | TODO | | |
| AF-012 | Live Tracking map (with permission) | Live (last 10 min) / Historical with date; ADS-B toggle; re-centre; collapse; About | TODO | | |
| AF-013 | Without Live Tracking permission | Map hidden | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| DATE-06 | Medium | Open (external) | Active Flights falls back to DD/MM/YYYY for text-month formats |
| DATE-07 | Medium | Open (external) | Active Flights shows 01/01/1970 for an empty SAR time |
| DATE-14 | Info | Info | Flight #8795 SAR time is before the booking start (may be expected) |
| DATA-01 | Low | Open (external) | Active Flights overdue rows: follower "Unknown", empty route |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
