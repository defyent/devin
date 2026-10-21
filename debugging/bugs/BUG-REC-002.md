# BUG-REC-002: Recency and Renewals at phone width: the table is cut off, so Total Items and Actions are hidden

| Field | Value |
|---|---|
| Checklist row | `REC-S05` in `checklists/18-recency.md` |
| Module | Recency and Renewals |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Safety > Recency and Renewals
2. Narrow the window to 390px

## Expected
Cards or a usable layout, with all columns reachable.

## Actual
The table stays a table (423px wide inside a 303px card). The Total Items column is cut off and Actions (edit) can't be seen. There's no card view.

## Evidence
- Screenshot: `screenshots/BUG-REC-002-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
