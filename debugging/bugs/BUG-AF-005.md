# BUG-AF-005: Active Flights: a Read Only Group (RG) user sees every company flight, not only their group's

| Field | Value |
|---|---|
| Checklist row | `FS-027` in `checklists/08-active-flights.md` |
| Module | Active Flights |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Open (retested 23/10/2026 v2.0.122, not fixed) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. BETA TEST ONLY Grpuser has Active Flights = RG and is only in BETA TEST ONLY Group.
2. Log in as betatest_grp > Active Flights.

## Expected
Only flights on the group's aircraft or crew are listed (the same as Daily Flight Record RG, which shows 2 flights).

## Actual
All 1,381 flights are counted and listed, including #42892 (Unknown aircraft) and #42893 (R44-01, Aaron Fisher, not in the group), with their SAR times and notes.

## Evidence
- Screenshot: `screenshots/BUG-AF-005-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
| 23/10/2026 | v2.0.122 | Not fixed | betatest_grp (Active Flights RG): activeflights_json still returns all 1388 flights, including #42893 (ZK-HEL, Aaron Fisher, not in the group) and #42892. Screenshot `screenshots/BUG-AF-005-rt122-1.png`. |
