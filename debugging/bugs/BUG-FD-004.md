# BUG-FD-004: Leg PIC / Secondary Flight Crew dropdowns offer passengers (e.g. a custom passenger can be chosen as leg PIC)

| Field | Value |
|---|---|
| Checklist row | `FD-005` in `checklists/07-flight-details.md` |
| Module | Flight Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 23/10/2026 v2.0.120; old-leg "(not crew)" and W&B front-seat group not tested) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open flight #42903 > Passenger List > Add Custom Passenger 'BETA TEST ONLY Pax'
2. Times and Weights > Add Leg
3. Open the leg PIC or Secondary Flight Crew dropdown

## Expected
Only Crew or Student role people (like the flight-level PIC list).

## Actual
Leg PIC and Secondary Flight Crew list 'BETA TEST ONLY Lowperm' and 'BETA TEST ONLY Pax' - the custom passenger can be picked as the leg's pilot, which would put a passenger's hours into crew/FRMS records.

Retest v2.0.119: #42903 leg 1 PIC options are 'Select...', 'BETA TEST ONLY Lowperm', 'BETA TEST ONLY Pax' - the passenger is still offered. Still fails.

## Evidence
- Screenshot: `screenshots/BUG-FD-004-1.png`
- Console / network errors: none

## Suspected cause (optional)
Leg crew dropdowns are filled from the whole manifest (crew + passengers) instead of crew only.

buildFrontSeatOptions() (index.js L2753-2776) deliberately adds a 'Passengers' optgroup from getOrderedManifestPeople() to the leg PIC and Secondary Flight Crew selects.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
| 23/10/2026 | v2.0.120 | Fixed | Leg PIC lists only crew (no passengers). Not tested: server refusal by direct request, legacy leg with a passenger PIC, W&B front-seat group. |
