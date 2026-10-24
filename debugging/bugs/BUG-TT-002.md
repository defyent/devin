# BUG-TT-002: Task Tracker dates ignore the date setting ('Dec 31', '2026-10-21')

| Field | Value |
|---|---|
| Checklist row | `TT-S04` in `checklists/25-task-tracker.md` |
| Module | Task Tracker |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > Task Tracker > Add Project with Due Date 31/12/2026
2. Look at the Due Date and Created columns

## Expected
31/12/2026 and 21/10/2026, as set in Settings > Time Zone.

## Actual
Due Date shows 'Dec 31' (no year), Created shows '2026-10-21'. Created is also the UTC date; local was 22/10/2026.

## Evidence
- Screenshot: `screenshots/BUG-TT-002-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
