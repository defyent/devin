# BUG-FD-007: New flight defaults its leg date/time to UTC instead of local time

| Field | Value |
|---|---|
| Checklist row | `DATE-005` in `checklists/92-xc-dates-timezones.md` |
| Module | Flight Details |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings > Time Zone is Pacific/Auckland (UTC+13).
2. At local 09:42 on 22/10/2026 (UTC 20:42 on 21/10), open Flight Schedule > Live Edit > Add Flight.
3. Look at the leg start/end date and time fields.

## Expected
Start defaults to the local date/time: 22/10/2026 09:40.

## Actual
Start defaults to 21/10/2026 20:40 and end to 21/10/2026 21:40, which is UTC. A user who doesn't notice saves the flight on the previous day, 13 hours early. The SAR Watch time has the same problem: on flight #42910 (planned 22/10 13:00-14:00) SAR defaulted to 21/10/2026 21:55, which is the UTC time and is before the flight starts. Retest 22/10/2026 (v2.0.114, assets ?v=2.0.114): still failing: new flight Start/End/SAR default to the UTC time (05:10 at local 18:09), see BUG-FS-001. Second retest 22/10/2026 (v2.0.114): unchanged; at local 20:43 the new flight defaults to 07:45 (UTC). Third retest 22/10/2026 (v2.0.115): unchanged; at local 20:49 the new flight defaults to 07:50 (UTC). Fourth retest 22/10/2026 (v2.0.117): unchanged; at local 21:00 the new flight defaults to 08:00 (UTC). Retest 22/10/2026 (v2.0.118): unchanged; at local 21:20 the new flight defaults to 08:20 (UTC). Retest 23/10/2026 (v2.0.119): still failing in a UTC browser (local 09:20 23/10 -> Start 22/10/2026 20:20). Correct when the browser time zone is Pacific/Auckland (09:25 23/10), so the default uses the browser time zone. See BUG-FS-001.

Retest v2.0.119: allFlightData (new and existing flights) has no siteTimeZone or serverNow key, and config has no time zone, so siteNow() falls back to the browser clock. Still fails in a UTC browser.

## Evidence
- Screenshot: `screenshots/BUG-FD-007-1.png`, `screenshots/BUG-FD-007-2.png`, `screenshots/BUG-FD-007-3.png`, `screenshots/BUG-FD-007-4.png`, `screenshots/BUG-FD-007-5.png`, `screenshots/BUG-FD-007-6.png`, `screenshots/BUG-FD-007-7.png`
- Console / network errors: none

## Suspected cause (optional)
Uses the browser time zone, not Settings > Time Zone (see BUG-FS-001).

Front end siteNow() (index.js L1546-1561) is ready but the flightdetails JSON doesn't send siteTimeZone/serverNow.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
