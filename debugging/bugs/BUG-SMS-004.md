# BUG-SMS-004: Add to Hazard Register: Goal 'Mitigate' shows as 'Minimize' in the Hazard Register

| Field | Value |
|---|---|
| Checklist row | `SMS-013` in `checklists/19-safety-reports.md` |
| Module | Safety Reports / Hazard Register |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Safety > Safety Reports > open report #2060 > Final Report tab
2. Add to Hazard Register: Hazard 'BETA TEST ONLY hazard', Type Hazard, Goal Mitigate, Controls, Responsible Aisha Pearce
3. Save Changes
4. Flight Safety > Hazard Register

## Expected
Goal column shows Mitigate, the value picked.

## Actual
Goal column shows 'Minimize'. The two pages use different names for the same goal.

## Evidence
- Screenshot: `screenshots/BUG-SMS-004-1.png`, `screenshots/BUG-SMS-004-2.png`
- Console / network errors: none

## Suspected cause (optional)
templates2/hazardregister/index.js maps goal code 'M' to 'Minimize' (line ~584) while the Safety Report Final Report dropdown calls it 'Mitigate'.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
