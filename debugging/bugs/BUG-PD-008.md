# BUG-PD-008: Personnel Details > Recency: the recency summary popup has no Add Manual Entry, no x, and doesn't close with Escape

| Field | Value |
|---|---|
| Checklist row | `PD-021` in `checklists/12-personnel-details.md` |
| Module | Personnel Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. All Personnel > Ethan Abbott > Recency and Renewals tab
2. Click the Day Landings count '0/0 in 90 days'
3. Look for Add Manual Entry and a close button; press Escape

## Expected
The popup lists the recency flights/entries, has Add Manual Entry (Date*, Value*, Notes) and closes with x, outside click and Escape.

## Actual
'Recency summary for Day Landings' lists 4 manual entries (03/02/2026, 15/06/2025, 02/06/2025, 17/04/2025) but has no buttons at all: no Add Manual Entry, no x. Escape does nothing; only clicking outside closes it. So manual recency entries can't be added from this page.

## Evidence
- Screenshot: `screenshots/BUG-PD-008-1.png`
- Console / network errors: none

## Suspected cause (optional)
Possibly the dialog buttons are built by the part of personneldetails/index.js that is cut off (BUG-PD-001).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
