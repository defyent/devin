# BUG-SMS-001: New Safety Report: Escape on the Confidential/Anonymous help closes the report form behind it and loses what you typed

| Field | Value |
|---|---|
| Checklist row | `SMS-004` in `checklists/19-safety-reports.md` |
| Module | Safety Reports |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Safety > Safety Reports > New Report
2. Type a Subject
3. Click the (?) next to Confidential
4. Press Escape

## Expected
Escape closes only the help popup; the report form stays open with the Subject kept.

## Actual
The Create New Safety Report form closes and the help popup stays open. Reopening New Report shows an empty Subject.

## Evidence
- Screenshot: `screenshots/BUG-SMS-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
The global Escape handler in smsreports/index.js closes document.querySelector('.modal-overlay.active'), which is the first (outer) popup, not the top one.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
