# BUG-TS-007: Reject Claim: leaving the reason empty closes the reject popup and throws a script error

| Field | Value |
|---|---|
| Checklist row | `TS-006` in `checklists/15-timesheets-leave.md` |
| Module | Timesheets |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Timesheets > open a person who has a pending claim (BETA TEST ONLY Second, 19 Oct).
2. View Claims > the reject (×) button on the claim.
3. Leave the reason empty and click Reject Claim.
4. Close the 'Validation Error' popup.

## Expected
The error shows next to the reason and the Reject Claim popup stays open, so you can type a reason.

## Actual
'Validation Error: Rejection reason is required' appears, but closing it also closes Reject Claim and the Claims list. The console shows "Cannot read properties of null (reading 'value')". You have to open View Claims and click reject again.

## Evidence
- Screenshot: `screenshots/BUG-TS-007-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
