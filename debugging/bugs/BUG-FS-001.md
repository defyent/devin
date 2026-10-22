# BUG-FS-001: New flight defaults (and Planner 'today') follow the browser time zone instead of Settings > Time Zone

| Field | Value |
|---|---|
| Checklist row | `FS-011` in `checklists/06-flight-schedule.md` |
| Module | Flight Schedule > Flight Details (new) |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings > Time Zone is Pacific/Auckland (header shows UTC 08:25, Local 21:25)
2. Flight Schedule > Enable Live Edit > Add Flight
3. Look at Start Time, End Time and SAR TIME (LOCAL)

## Expected
Start defaults to local now (21:25), end +1h (22:25), SAR time in local time.

## Actual
Start 21/10/2026 08:25, End 09:25, SAR TIME (LOCAL) 09:25 - all UTC values. Near midnight the date would also be wrong. Also Cancel with no changes does nothing (only the back arrow leaves). Retest 22/10/2026 (v2.0.114, assets ?v=2.0.114): still failing. At local 18:09 (UTC 05:09) on 22/10/2026, Flight Schedule > Live Edit > Add Flight opens New Flight Details with Start 22/10/2026 05:10, End 06:10 and SAR TIME (LOCAL) 06:10, i.e. UTC, 13 h behind local. Header 'Time: 05:10' also UTC. Cancel with no changes still does nothing (URL stays action=flightdetails). Second retest 22/10/2026 (still v2.0.114, no new version deployed): at local 20:43 (UTC 07:43) Add Flight shows Start 07:45, End 08:45, SAR 08:45 and header Time 07:45, still UTC. Cancel with no changes still stays on action=flightdetails. Third retest 22/10/2026 (v2.0.115, flightdetails/index.js?v=2.0.115): unchanged. At local 20:49 (UTC 07:49) Add Flight shows Start 07:50, End 08:50, SAR 08:50, header Time 07:50 (UTC). Cancel with no changes still stays on action=flightdetails. Fourth retest 22/10/2026 (v2.0.117, flightdetails/index.js?v=2.0.117): unchanged. At local 21:00 (UTC 08:00) Add Flight shows Start 08:00, End 09:00, SAR 09:00, header Time 08:00 (UTC). Cancel with no changes still stays on action=flightdetails. Retest 22/10/2026 (v2.0.118): unchanged. At local 21:20 (UTC 08:20) Add Flight shows Start 08:20, End 09:20, SAR 09:20, header Time 08:20 (UTC). Cancel with no changes still stays on action=flightdetails. Retest 23/10/2026 (v2.0.119): Cancel is fixed: with no changes it returns to action=flightschedule, and after editing Notes it shows the Unsaved Changes popup (Stay on Page / Leave Page). Default times still wrong in a UTC browser: at local 09:20 on 23/10/2026 (UTC 20:20 on 22/10) Add Flight shows Start 22/10/2026 20:20, End 21:20, SAR 21:20 and header Date 22/10/2026 Time 20:20 (UTC, previous day). Cause narrowed: the same test with the browser time zone set to Pacific/Auckland shows Start 23/10/2026 09:25, End 10:25, SAR 10:25, so the defaults use the browser's own clock/time zone, not the server and not Settings > Time Zone. The Planner 'today' column has the same cause: in a UTC browser it highlights 22/10 while the org date is 23/10 (FullCalendar's today is correct, 23/10).

## Evidence
- Screenshot: `screenshots/BUG-FS-001-1.png`, `screenshots/BUG-FS-001-2.png`, `screenshots/BUG-FS-001-3.png`, `screenshots/BUG-FS-001-4.png`, `screenshots/BUG-FS-001-5.png`, `screenshots/BUG-FS-001-6.png`, `screenshots/BUG-FS-001-7.png`, `screenshots/BUG-FS-001-8.png`, `screenshots/BUG-FS-001-9.png`
- Console / network errors: none

## Suspected cause (optional)
Defaults are built with the browser's new Date() / local time zone. Correct for users whose computer is set to the org time zone (Pacific/Auckland); wrong for any other browser time zone (travelling users, UTC machines). Build 'now' in the org time zone instead. Planner today-column highlight uses the same browser date.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
