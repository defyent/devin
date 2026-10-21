# BUG-FAD-004: Flight and Duty column headers are ambiguous: two '1 Days' and two '24 Hours' columns, and '1 Days' is ungrammatical

| Field | Value |
|---|---|
| Checklist row | `FAD-002` in `checklists/16-flight-and-duty.md` |
| Module | Flight and Duty |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Safety > Flight and Duty
2. Scroll to the Pilots group and read the column headers

## Expected
Each FRMS rule column can be told apart (e.g. rule name or limit in the header) and singular periods read '1 Day'.

## Actual
Flight Time: 24 Hours (10h), 1 Days (8h), 1 Days (8h), 7 Days (40h). Duty Time: 24 Hours (14h), 24 Hours (8h), 28 Days (180h). The two '1 Days' and the two '24 Hours' columns only differ by the small limit in brackets.

## Evidence
- Screenshot: `screenshots/BUG-FAD-004-1.png`
- Console / network errors: none

## Suspected cause (optional)
Header uses only the rule period ('<n> Days'/'<n> Hours') with no rule name and no singular form.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
