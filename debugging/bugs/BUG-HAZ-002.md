# BUG-HAZ-002: Hazard Register details: Final Risk Assessment never shows the saved final risk

| Field | Value |
|---|---|
| Checklist row | `HAZ-003` in `checklists/20-hazard-register.md` |
| Module | Hazard Register |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Safety report #2060: Final Report tab, Final Risk Unlikely x Minor, Save Changes (saved: reloading the report shows Unlikely/Minor)
2. Flight Safety > Hazard Register > #2060 > Risk Assessment tab

## Expected
Final Risk & Review shows Likelihood Unlikely, Consequence Minor and the resulting risk level. The list's Risk column should then use the final risk too.

## Actual
Final Risk shows Likelihood '--', Consequence '--', risk '--'. Only the Closure Description is filled. The list Risk column shows the initial risk (Low).

## Evidence
- Screenshot: `screenshots/BUG-HAZ-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
hazarddetails.js (~line 221) only shows the card and the closure description. Its comment says 'You would need to fetch the final risk details from the API'; that was never done.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
