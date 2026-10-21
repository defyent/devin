# Cross-cutting: date/time formats and pickers

- **Checklist ID prefix:** `DATE`
- **Guide section:** §4, §12.3
- **Where:** Every date shown or entered
- **Permission:** settings_timezone = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| DATE-001 | For each date format: header clocks, Dashboard, Schedule, Flight Details, Active Flights, DFR, Personnel, Timesheets, Roster, F&D, Notices, Recency, SMS, Hazards, Reports, Activity Log, Access Manager hover | All use chosen format; no raw ISO or US dates leaking | TODO | | |
| DATE-002 | For each time format (incl. 12-hour) | AM/PM parsed correctly on save | TODO | | |
| DATE-003 | For each picker type | Every date/time input uses it and saves the right value | TODO | | |
| DATE-004 | UTC vs Local | Local = org timezone; times saved and reloaded unchanged (no drift) | TODO | | |
| DATE-005 | Day boundary: local date differs from UTC (staging NZ is UTC+13) | Flights/rosters on the right day | TODO | | |
| DATE-006 | DST transition dates | No off-by-one-hour | TODO | | |
| DATE-007 | Restore original settings | Done | TODO | | |

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
