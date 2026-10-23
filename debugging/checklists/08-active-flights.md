# Active Flights and Live Tracking

- **Checklist ID prefix:** `AF`
- **Guide section:** §8.4
- **Where:** Flight Operations > Active Flights
- **Permission:** Active Flights A/RA/WG/RG; Live Tracking
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| AF-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Sidebar > Flight Operations > Active Flights loads (action=activeflights), no console errors (shot af_open) |
| AF-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-AF-003 | No page Help (?) button on Active Flights. 'About Live Tracking' popup: Got it closes, clicking outside closes, no x button, Escape does nothing (BUG-AF-003) |
| AF-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Mouse down inside Contact Details, Adjust SAR and Add Note popups, release outside: all stay open. (Escape does not close them - BUG-AF-003) |
| AF-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | PASS | BUG-AF-004 | Dates shown DD/MM/YYYY HH:MM as set in Settings > Time Zone; note timestamps local ([22:34]). The overdue / remaining countdown uses the wrong zone - see BUG-AF-004 |
| AF-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | 390 px: no horizontal scroll (375 <= 390), list shows cards only (table and table/card toggle hidden), map full width (shot af_mobile). Note: the 'Performance' timing panel (Active Flights API 295 ms) floats over the cards and hides Add Note until closed with x |
| AF-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low (no Active Flights right): menu link shown, opening it gives 'Access Denied: You do not have permission to access the Active Flights feature. Please contact your administrator.' No data, no Adjust SAR, no map (shot af_low) |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| AF-001 | List content | Only open flights whose start or SAR time has passed | FAIL | BUG-AF-002 | 1,377 rows: 1,364 PAST, 7 OVERDUE and 6 FUTURE. The FUTURE flights (#8853-#8860) have not started and have no SAR time ('01/01/1970 00:00 NO SAR TIME SET') but are still listed (BUG-AF-002) (shot af_future) |
| AF-002 | Stats cards: Total, Active, Past, Overdue | Match list | FAIL | BUG-AF-002 | Cards: Total 1377, Active 0, Past 1364, Overdue 7. Past and Overdue match the list, but the 6 FUTURE rows are counted in Total and in no other card (BUG-AF-002) |
| AF-003 | Table / card view; sort by SAR / Start Time | Works; mobile shows cards only | PASS |  | Table / card view toggle (table_rows / grid_view) works; Sort by SAR Time / Start Time re-orders the list. Mobile check in AF-S05 |
| AF-004 | SAR countdown / overdue timer | Counts correctly; status colours from Settings > Flight Schedule | FAIL | BUG-AF-001, BUG-AF-004 | #42903 (SAR 09:30 local per Flight Details) shows 'OVERDUE by 3m' and Active Time 01h 03m at 22:33 local / 09:33 UTC - 13 h out (BUG-AF-004, shot af_overdue_tz). Also 1,365 rows with SAR watch disabled show SAR Time '01/01/1970 00:00' (BUG-AF-001) |
| AF-005 | Click row/card | Opens Flight Details | PASS |  | Click row #42903 > opens Flight Details flight_id=42903; Back returns to Active Flights |
| AF-006 | Click PIC | Contact details popup | PASS |  | Click PIC 'Graham Clarke' > popup 'Graham Clarke - Contact Details' with Mobile 021-555-0096, Email graham.clarke96@datahangar.net, Close (shot af_pic) |
| AF-007 | Notes | Readable | PASS |  | Notes column readable (e.g. 'Maintenance test flight post 100hr', 'No notes' when empty) |
| AF-008 | Adjust SAR (A/WG) | Picker + Disable/Enable SAR Watch + Save; hidden for RA/RG | PASS | BUG-AF-004 | Adjust SAR on #42903: picker prefilled 21/10/2026 09:30, changed to 23:30 > Save > row turns ACTIVE with SAR '21/10/2026 23:30'. Remaining time wrong ('13h 55m remaining' at 22:34 local) - BUG-AF-004. Hidden for RA/RG not checked (no RA user) |
| AF-009 | Add Note (A/WG) | Appended to flight | PASS |  | Add Note on #42903 > 'BETA TEST ONLY AF note' > Save > Notes column shows '[22:34] BETA TEST ONLY AF note' before the existing notes (timestamp in local time) |
| AF-010 | Auto-refresh | Refreshes; pauses while editing | PASS |  | activeflights_json re-requested every 20 s (live-tracking JSON separately). While Add Note was open with typed text the refresh kept running, but the popup and text were kept; no data lost |
| AF-011 | Complete a flight | Disappears from Active Flights | PASS |  | #42903 set to Complete in Flight Details > Save > Back > no longer listed; cards back to Total 1377 / Active 0 / Past 1364 / Overdue 7 |
| AF-012 | Live Tracking map (with permission) | Live (last 10 min) / Historical with date; ADS-B toggle; re-centre; collapse; About | PASS |  | Live Tracking card (starts collapsed; expand_more/less toggles 67 px <> 560 px map). Live / Historical toggle (Historical shows date field 21/10/2026); ADS-B button toggles on (11 markers); About (?) opens info. No separate re-centre control found (shots af_map_live, af_map_hist, af_map_adsb2) |
| AF-013 | Without Live Tracking permission | Map hidden | PASS | af013_two | BETA TEST ONLY Second has Active Flights = A. There is no Live Tracking card in Access Manager, so Second has no live tracking. Active Flights shows the table/grid with Adjust SAR and Add Note, and no map or map button. |

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
| Flight #42903 set to Open, SAR moved to 23:30, then Complete again (AF-011) | Flight #42903 | No (delete with the flight) |
| Note 'BETA TEST ONLY AF note' | Flight #42903 notes | No |

### Retest v2.0.122 (23/10/2026, Service Account in UTC and Pacific/Auckland browsers; betatest_grp)
All 5 Active Flights bugs still fail; the Active Flights script is unchanged from v2.0.121 and `activeflights_json` still sends no `siteTimeZone`/`serverNow`, so the fix does not appear to be deployed.
- BUG-AF-004: UTC browser 13 h short (#42898 OVERDUE by 151h 22m vs 164h 22m in NZ / server); Active card 0 vs 2.
- BUG-AF-001: "01/01/1970 00:00" still shown when there is no SAR time.
- BUG-AF-002: 6 future flights listed and not in any card (UTC browser).
- BUG-AF-003: no page Help; Escape doesn't close About Live Tracking, Adjust SAR or Add Note; no x.
- BUG-AF-005: RG user still gets all 1388 flights.
No data changed (Adjust SAR and Add Note were cancelled).
