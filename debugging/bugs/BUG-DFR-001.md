# BUG-DFR-001: Daily Flight Record has no page Help (?), and Manage Columns doesn't close with Escape

| Field | Value |
|---|---|
| Checklist row | `DFR-S02` in `checklists/09-daily-flight-record.md` |
| Module | Daily Flight Record |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Sidebar > Flight Operations > Daily Flight Record
2. Look for the Help (?) button in the page header
3. Click Columns (Manage Columns popup), press Escape

## Expected
A page Help (?) button like other modules; the Manage Columns popup closes with x, clicking outside and Escape.

## Actual
There is no Help (?) button on the page. Manage Columns closes with x, Done and clicking outside, and stays open on drag-out (correct), but Escape does nothing.

## Evidence
- Screenshot: `screenshots/BUG-DFR-001-1.png`, `screenshots/BUG-DFR-001-2.png`
- Console / network errors: none

## Suspected cause (optional)
No help content or button wired for this module; the column modal has no keydown Escape handler.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
