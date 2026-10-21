# BUG-SMS-003: Safety Report Final Report: Likelihood and Consequence dropdowns list every option twice

| Field | Value |
|---|---|
| Checklist row | `SMS-012` in `checklists/19-safety-reports.md` |
| Module | Safety Reports |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Safety > Safety Reports > open report #2060
2. Final Report tab
3. Open the Final Risk Likelihood or Consequence dropdown

## Expected
Each option once (Almost Certain, Likely, Possible, Unlikely, Rare).

## Actual
Each option appears twice: Almost Certain, Likely, Possible, Unlikely, Rare, Almost Certain, Likely, ... Same for Consequence.

## Evidence
- Screenshot: `screenshots/BUG-SMS-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
smsreportdetails.js calls setupFinalRiskAssessment() twice (lines ~2828 and ~3557) and it appendChild()s the options without clearing the selects first.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
