# BUG-FD-003: Times and Meters: no link to the previous flight next to 'Previous' meter readings

| Field | Value |
|---|---|
| Checklist row | `FD-019` in `checklists/07-flight-details.md` |
| Module | Flight Details |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open flight #42903 (ZK-SIM) > Times and Weights
2. Look at Meters (Engine Hours, Flight Hours)

## Expected
Each meter shows the previous reading and a link to the flight it came from (guide).

## Actual
'Previous: 2450.3 (+0.0)' is shown but there is no link; the only link in the panel is an info icon (href '#'). The user cannot check which flight set the previous reading.

## Evidence
- Screenshot: `screenshots/BUG-FD-003-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
