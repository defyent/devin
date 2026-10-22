# Cross-cutting: date/time formats and pickers

- **Checklist ID prefix:** `DATE`
- **Guide section:** §4, §12.3
- **Where:** Every date shown or entered
- **Permission:** settings_timezone = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| DATE-001 | For each date format: header clocks, Dashboard, Schedule, Flight Details, Active Flights, DFR, Personnel, Timesheets, Roster, F&D, Notices, Recency, SMS, Hazards, Reports, Activity Log, Access Manager hover | All use chosen format; no raw ISO or US dates leaking | FAIL | BUG-SLOG-001 | DD/MM/YYYY is used in the header, DFR, Flight Details, Notices and Personnel. Many places ignore it: Activity Log "22 Oct 2026", File Browser/Form Browser/Exams "Oct 22, 2026", Chat "Thursday, October 22, 2026", Roster Builder "Monday, October 5", ISO dates in F&D, Timesheets, Inspections, Resources, Google Calendar and Reports CSV (12 bugs with ISO dates, 56 bugs mention dates/times). |
| DATE-002 | For each time format (incl. 12-hour) | AM/PM parsed correctly on save | FAIL | BUG-STZ-003 | The three 12-hour time formats are greyed out in Time Zone settings, and the preview ignores the time format (BUG-STZ-003). With 24-hour set, many pages still show 12-hour or seconds: Chat "01:32 AM", Activity Log "02:51 am", Form Browser "10:24 PM", Timesheets "14:00:00". |
| DATE-003 | For each picker type | Every date/time input uses it and saves the right value | PASS |  | Each picker type (Type-In, Native, Scroll Wheel) is used everywhere once saved (checklist 33 STZ rows). The known Scroll Wheel issues (DATE-03, POP-07) are tracked. |
| DATE-004 | UTC vs Local | Local = org timezone; times saved and reloaded unchanged (no drift) | FAIL | BUG-STZ-001 | Header UTC and Local clocks are right. Several defaults and previews use UTC instead of local: Time Zone preview (BUG-STZ-001), Shift Type duty times (BUG-SST-002), Form Builder Date/Time widgets (BUG-FBLD-002), Safety Report event time (BUG-SMS-002), and 11 bugs in total. |
| DATE-005 | Day boundary: local date differs from UTC (staging NZ is UTC+13) | Flights/rosters on the right day | FAIL | BUG-FAD-005 | Staging is UTC+13, so local 22/10 is UTC 21/10 until 13:00. F&D View as Date (BUG-FAD-005), the Inspection date picker (BUG-SINS-003) and Safety Report Event Date (BUG-SMS-002) start on the UTC date, one day behind. |
| DATE-006 | DST transition dates | No off-by-one-hour | FAIL | date006_tw2 | BUG-DATE-001: flight #42911 set to 04/04/2027 01:00-05:00, across the NZ DST end at 03:00. The planned times save and show correctly (DFR, schedule month/day). A leg 01:00-05:00 gives 4.0 h, but the real time is 5.0 h. The leg was not saved. |
| DATE-007 | Restore original settings | Done | PASS |  | Time Zone settings were changed during checklist 33 and put back to Pacific/Auckland, DD/MM/YYYY, 24-hour (HH:mm), Type-In Fields. Checked again after a reload. |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| DATE-02 | High | Open (external) | Dates ignore the date setting: Dashboard, Flight Schedule, Resources, Activity Log, W&B Configs, Exam Builder |
| DATE-03 | Medium | Open (external) | Scroll Wheel picker fields always show "Oct 16, 2026 6:00 AM", whatever the format setting |
| DATE-04 | High | Open (external) | Empty date fields show today's date (Personnel Birth Date, SMS Review Date), in all picker modes |
| DATE-10 | Medium | Open (external) | Native mode: header and inputs show different formats; seconds dropped despite HH:mm:ss |
| DATE-11 | Low | Open (external) | Header UTC/Local clocks don't update until page reload |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
