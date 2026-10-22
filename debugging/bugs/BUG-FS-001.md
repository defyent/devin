# BUG-FS-001: New flight defaults to the current UTC time instead of local time (SAR TIME labelled LOCAL shows UTC+1h)

| Field | Value |
|---|---|
| Checklist row | `FS-011` in `checklists/06-flight-schedule.md` |
| Module | Flight Schedule > Flight Details (new) |
| Severity | Medium |
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
Start 21/10/2026 08:25, End 09:25, SAR TIME (LOCAL) 09:25 - all UTC values. Near midnight the date would also be wrong. Also Cancel with no changes does nothing (only the back arrow leaves). Retest 22/10/2026 (v2.0.114, assets ?v=2.0.114): still failing. At local 18:09 (UTC 05:09) on 22/10/2026, Flight Schedule > Live Edit > Add Flight opens New Flight Details with Start 22/10/2026 05:10, End 06:10 and SAR TIME (LOCAL) 06:10, i.e. UTC, 13 h behind local. Header 'Time: 05:10' also UTC. Cancel with no changes still does nothing (URL stays action=flightdetails). Second retest 22/10/2026 (still v2.0.114, no new version deployed): at local 20:43 (UTC 07:43) Add Flight shows Start 07:45, End 08:45, SAR 08:45 and header Time 07:45, still UTC. Cancel with no changes still stays on action=flightdetails.

## Evidence
- Screenshot: `screenshots/BUG-FS-001-1.png`, `screenshots/BUG-FS-001-2.png`, `screenshots/BUG-FS-001-3.png`
- Console / network errors: none

## Suspected cause (optional)
New-flight defaults built from server/UTC now() rather than the org time zone. Confirm whether flights are stored in UTC and shown in local everywhere else (see 92-xc-dates).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
