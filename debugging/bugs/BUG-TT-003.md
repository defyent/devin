# BUG-TT-003: Task Tracker on a phone: feature cards are pushed right and cut off

| Field | Value |
|---|---|
| Checklist row | `TT-S05` in `checklists/25-task-tracker.md` |
| Module | Task Tracker |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open Administration > Task Tracker on a 390px wide screen
2. Open a project with a component and features

## Expected
Feature cards fit the screen width.

## Actual
The feature card is indented about 90px and runs off the right edge; the feature progress % and task actions are cut off.

## Evidence
- Screenshot: `screenshots/BUG-TT-003-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
