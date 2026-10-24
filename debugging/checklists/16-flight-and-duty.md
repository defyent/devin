# Flight and Duty

- **Checklist ID prefix:** `FAD`
- **Guide section:** §10.1
- **Where:** Flight Safety > Flight and Duty
- **Permission:** Flight and Duty A/RG/RO
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FAD-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Flight Safety > Flight and Duty loads, no console errors |
| FAD-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-FAD-001 | No Help (?) on the page. Popups also ignore Escape (BUG-FAD-002) |
| FAD-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Flight Details popup stays open after mousedown inside / release outside |
| FAD-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-FAD-003 | View as Date box uses DD/MM/YYYY, but popups show '16 Oct 2026'. View as Date defaults to the UTC date (BUG-FAD-005) |
| FAD-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS | BUG-PD-010 | At 390px the page fits (375px); each group table scrolls sideways inside its 303px card (Pilots table 1200px). Performance panel covers rows (BUG-PD-010) |
| FAD-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: menu link shows, page says 'Access Denied: You do not have permission to access Flight and Duty' |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FAD-001 | Rows | One per person in groups with Show Group in Flight and Duty | PASS |  | Sections BETA TEST ONLY Group (1), Crew (41), Pilots (83); Administration and Engineers not shown. Show Group setting itself not checked here (04/34) |
| FAD-002 | Columns | One per FRMS flight-time and duty-time rule period; OK/Caution/Warning colours vs thresholds | PASS | BUG-FAD-004 | Pilots: 4 flight-time + 3 duty-time columns with limits in brackets, Crew: 2 duty-time columns. All seeded values under the soft limit (green), so Caution/Warning colours not seen. Ambiguous headers (BUG-FAD-004) |
| FAD-003 | View Date | Figures recalculated as at date | PASS | BUG-FAD-005 | View as Date 15/10/2026 shows 'Viewing as: 15/10/2026 x' and Aisha Johnston 7 Days drops to 0.0h; 17/10/2026 shows 11.0h again (flight #8795 on 16/10). Default date is UTC (BUG-FAD-005) |
| FAD-004 | Search / Filter by Group | Work | PASS |  | Search 'Aisha' leaves Aisha Johnston and Aisha Pearce; Filter by Group Crew shows only Crew (41) |
| FAD-005 | Click flight time value | Contributing flights list with all columns | PASS |  | Aisha Johnston 7 Days 11.0h opens Flight Details: soft 38h / hard 40h, flight #8795 with ID, Date, Aircraft, Route, Type, Category, Role, Hours |
| FAD-006 | Click duty value | Duty Time Details | PASS |  | Duty value opens Duty Time Details (soft 13h / hard 14h, 'No timesheets found for this period') |
| FAD-007 | Seeded violations | Resolutions Required / Roster Violations shown | PASS |  | Roster error icon opens Roster Violations (9 Shift Sequence warnings); Resolution icon opens Resolutions Required with roster resolution |
| FAD-008 | Performance (150 staff, FRMS calc) | < 500 ms server time | PASS |  | Performance panel Total Time 440.1 ms for 125 people (Process People 436 ms); TTFB 173 ms |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
