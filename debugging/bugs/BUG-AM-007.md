# BUG-AM-007: Access Manager: a customer created from Flight Details is Active with no login credentials

| Field | Value |
|---|---|
| Checklist row | `AM-015` in `checklists/90-xc-permissions.md` |
| Module | Access Manager |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open flight #42910 > Customer tab > New Customer.
2. Enter First Name, Last Name, Company and Email, then click Save Changes.
3. Settings and Tools > Access Manager > search for the new customer.

## Expected
The new customer is Inactive until login credentials are set. The rule 'User must have login credentials before activation' also applies when the person is created.

## Actual
BETA TEST ONLY Customer (#279) shows Login Access = Active, with no username and Last Login 'Never'. If you deactivate it and then click Inactive, Change Login Credentials opens as it should, so the check only runs when you activate from Access Manager. Retest 22/10/2026 (v2.0.113, accessmanager/index.js?v=2.0.113): fixed. A new customer made from flightdetails #42910 > Customer > New Customer (BETA TEST ONLY Cust2) shows Login Access = Inactive in Access Manager.

## Evidence
- Screenshot: `screenshots/BUG-AM-007-1.png`, `screenshots/BUG-AM-007-2.png`, `screenshots/BUG-AM-007-3.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
