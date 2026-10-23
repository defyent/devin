# BUG-FD-010: Required Information check skipped on unlock saves: a flight was saved Complete with no departure, destination or PIC

| Field | Value |
|---|---|
| Checklist row | `FD-030` in `checklists/07-flight-details.md` |
| Module | Flight Details |
| Severity | Medium |
| DataHangar version | v2.0.120 |
| Account / permission level | Service Account (datahangar), Flight Details A and temporary WL |
| Browser / width | Chrome desktop (UTC time zone), 1600 px |
| Status | Fixed (verified 23/10/2026 v2.0.121; server side not tested directly) |
| Found / session | 23/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Unlock a Complete & Locked flight as in BUG-FD-008 (v2.0.120)
2. The save leaves the flight Complete with an empty leg route and PIC

## Expected
The Complete check runs on the new status and refuses the save, listing what is missing.

## Actual
Found 23/10/2026 on v2.0.120: saved as Complete with empty departure, destination and PIC, no popup and no server refusal. Retest 23/10/2026 (v2.0.121): fixed in the page. #42909 (Complete, empty leg) was blocked with "Leg 1: PIC, Departure, Destination, Flight total", with the hint "A locked flight can't be edited: unlock it to Open first". The server check was not tested by direct request.

## Evidence
- Screenshot: `screenshots/BUG-FD-010-1.png`
- Console / network errors: none

## Suspected cause (optional)
The check skipped flights whose stored status was locked instead of using the new status.

## Test data involved
Flight #42909 (BETA TEST ONLY, ZK-BTO)

## Related
BUG-FD-006

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
| 23/10/2026 | v2.0.121 | Fixed | See Actual |
