# BUG-PD-005: Personnel Details: History, PDF Options and Legacy Duty Browser popups don't close with Escape, and PDF Options has no x

| Field | Value |
|---|---|
| Checklist row | `PD-S03` in `checklists/12-personnel-details.md` |
| Module | Personnel Details |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. All Personnel > Ethan Abbott (Personnel Details)
2. Click History, press Escape
3. Click Personnel Pdf, press Escape, look for an x
4. Timesheets tab > Legacy Duty Browser, press Escape

## Expected
Like the Help popup on this page, every popup closes with x, clicking outside and Escape.

## Actual
Help closes with Escape, x and outside click. Personnel History closes with x and outside click but not Escape. Personnel PDF Options has no x (only Cancel / Generate PDF) and does not close with Escape. All three stay open on drag-out (correct). Timesheets > Legacy Duty Browser popup also ignores Escape (its Close button works).

## Evidence
- Screenshot: `screenshots/BUG-PD-005-1.png`, `screenshots/BUG-PD-005-2.png`, `screenshots/BUG-PD-005-3.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
