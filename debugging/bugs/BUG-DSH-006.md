# BUG-DSH-006: Dashboard My Flights shows a canceled flight's status as 'Unknown'

| Field | Value |
|---|---|
| Checklist row | `DSH-005` in `checklists/05-dashboard.md` |
| Module | Dashboard |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight #42910 (ZK-BTO, PIC BETA TEST ONLY Second, 22/10/2026 08:00-09:00) is set to Canceled.
2. Log in as betatest_two > Dashboard > My Flights for Thu 22/10/2026.

## Expected
The status badge says 'Canceled' (as in Flight Details / Flight Schedule).

## Actual
The badge says 'Unknown'.

## Evidence
- Screenshot: `screenshots/BUG-DSH-006-1.png`
- Console / network errors: none

## Suspected cause (optional)
dashboard/index.js shows flight.status as sent by the server, so the Dashboard flights JSON has no mapping for the Canceled status.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
