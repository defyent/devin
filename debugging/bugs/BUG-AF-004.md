# BUG-AF-004: Active Flights overdue and active times are 13 h out: local SAR/start times are compared with UTC 'now'

| Field | Value |
|---|---|
| Checklist row | `AF-004` in `checklists/08-active-flights.md` |
| Module | Active Flights |
| Severity | High |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open flight #42903 (Start 21/10/2026 08:30, SAR TIME (LOCAL) 21/10/2026 09:30 in Flight Details) and set Flight Status to Open, Save
2. At 22:33 local / 09:33 UTC open Sidebar > Flight Operations > Active Flights
3. Look at row #42903

## Expected
SAR 09:30 local passed 13 hours ago: 'OVERDUE by 13h 03m', Active Time 14h 03m.

## Actual
Row shows SAR '21/10/2026 09:30 OVERDUE by 3m' and Active Time '01h 03m' - the countdown uses UTC now (09:33) against the local time, so an overdue flight looks only just overdue for 13 hours. For a search-and-rescue watch this delays the alarm. Confirmed with Adjust SAR: setting SAR to 21/10/2026 23:30 at 22:34 local shows '13h 55m remaining' instead of about 56m.

## Evidence
- Screenshot: `screenshots/BUG-AF-004-1.png`, `screenshots/BUG-AF-004-2.png`
- Console / network errors: none

## Suspected cause (optional)
Active Flights compares the stored local SAR/start time with the UTC clock (or Flight Details labels UTC times as local). Related to BUG-FS-001 (Add Flight defaults to UTC).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
