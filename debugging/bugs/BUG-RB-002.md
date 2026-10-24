# BUG-RB-002: Roster Builder: Copy Live to Draft copies one shift at a time and takes about 6 minutes for one month

| Field | Value |
|---|---|
| Checklist row | `RB-003` in `checklists/14-roster-builder.md` |
| Module | Roster Builder |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Roster Builder
2. Select Roster View: BETA TEST ONLY Draft
3. Bulk actions > Copy Live to Draft > Clear then Copy

## Expected
Copy finishes in a few seconds (one server call for the month).

## Actual
An 'In Progress... Copying shift N of 1690 for <name>' dialog runs for about 6 minutes (10:41 to about 10:47 UTC on stresstest) and blocks the page. Closing the tab partway would leave a half-copied draft.

## Evidence
- Screenshot: `screenshots/BUG-RB-002-1.png`, `screenshots/BUG-RB-002-2.png`
- Console / network errors: none

## Suspected cause (optional)
Client loops over every live shift and saves each with its own request instead of a bulk copy endpoint.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
