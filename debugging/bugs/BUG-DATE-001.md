# BUG-DATE-001: Flight time across a DST change is out by an hour (01:00-05:00 on 04/04/2027 gives 4.0 instead of 5.0)

| Field | Value |
|---|---|
| Checklist row | `DATE-006` in `checklists/92-xc-dates-timezones.md` |
| Module | Flight Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight #42911 (ZK-BTO): set Start 04/04/2027 01:00 and End 04/04/2027 05:00, then Save Changes. NZ daylight saving ends at 03:00 that morning, when clocks go back to 02:00.
2. Times and Weights > Add Leg > Takeoff 01:00, Landing 05:00.

## Expected
Leg and flight total = 5.0 h, because 01:00 NZDT is 12:00 UTC and 05:00 NZST is 17:00 UTC. The schedule should also allow for the repeated 02:00-03:00 hour.

## Actual
Leg total and Total Flight Time both show 4.0. The flight saves and shows as 01:00-05:00 in the Daily Flight Record and the schedule (day view block is 4 hours tall), so the time is worked out from the clock times and the DST shift is ignored. This affects recorded hours, FRMS and timesheets for any flight that night (and the spring-forward night the other way round).

Retest v2.0.119: #42911 Add Leg, engine and flight 2027-04-04 01:00 > 05:00: leg 4.0/4.0, flight total 4.0/4.0 (should be 5.0). Not saved. Still fails.

## Evidence
- Screenshot: `screenshots/BUG-DATE-001-1.png`, `screenshots/BUG-DATE-001-2.png`, `screenshots/BUG-DATE-001-3.png`
- Console / network errors: none

## Suspected cause (optional)
calculateTimeDifference(start,end) (index.js ~L2310) only gets HH:MM and uses new Date(0,0,0,h,m), so the date and DST are ignored.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
