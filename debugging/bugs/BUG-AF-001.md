# BUG-AF-001: Active Flights shows SAR Time '01/01/1970 00:00' for flights with SAR watch disabled

| Field | Value |
|---|---|
| Checklist row | `AF-004` in `checklists/08-active-flights.md` |
| Module | Active Flights |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Sidebar > Flight Operations > Active Flights
2. Look at the SAR Time column for PAST flights (e.g. #8861, #8844)

## Expected
Flights without SAR watch show a dash or just 'SAR Watch Disabled' in the SAR Time column.

## Actual
SAR Time shows '01/01/1970 00:00' above 'SAR Watch Disabled' (Unix epoch shown for an empty SAR time).

## Evidence
- Screenshot: `screenshots/BUG-AF-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
Empty/0 SAR timestamp formatted as a date instead of being treated as no value.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
