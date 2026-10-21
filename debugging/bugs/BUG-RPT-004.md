# BUG-RPT-004: Reports: the Flight Hours meter column shows the aircraft's current meter on every flight, and Total adds them up

| Field | Value |
|---|---|
| Checklist row | `RPT-006` in `checklists/26-reports.md` |
| Module | Reports |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Aircraft ZK-BTO has Flight Hours 'Last: 100.0 (2026-10-22)' in Resources (Aircraft).
2. Flights #42909 (Complete), #42910 and #42911 (Open) are on ZK-BTO. None of them has a meter reading entered.
3. Reports > Add Report Template > Custom Report > Flights, tick Meters > Flight Hours, filter Aircraft/Resource = ZK-BTO, run it and open the result.

## Expected
Each row shows that flight's own meter reading (or is empty when none was entered). Total is only shown when adding the values makes sense.

## Actual
All three flights show Flight Hours 100, including the two Open flights with no reading, and Total shows 300.

## Evidence
- Screenshot: `screenshots/BUG-RPT-004-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
