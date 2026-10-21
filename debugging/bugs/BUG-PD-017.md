# BUG-PD-017: Personnel Details > Lesson Plans: an assigned plan is saved but never listed; the dialog's dates default to the UTC date

| Field | Value |
|---|---|
| Checklist row | `PD-018` in `checklists/12-personnel-details.md` |
| Module | Personnel Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings > Lesson Plans: make plan 'BETA TEST ONLY Plan' with lesson 'BETA TEST ONLY Lesson 1'.
2. Personnel > BETA TEST ONLY Group > BETA TEST ONLY Grpuser > Lesson Plans > Assign Lesson Plan.
3. Pick the plan, then click Assign Lesson Plan.
4. Leave the page and open Grpuser again, then the Lesson Plans tab.

## Expected
The plan is listed with its lessons and progress. Start Date defaults to today's local date (22/10/2026) and End Date is empty (optional).

## Actual
The toast says 'Lesson plan assigned successfully' and the server replies 'Ok', but the tab still says 'No lesson plans assigned to this person', even after you reopen the page. The plan is assigned, because its lesson shows on the Lesson tab of the student's flight #42909. Start Date and End Date both default to 21/10/2026, which is the UTC date.

## Evidence
- Screenshot: `screenshots/BUG-PD-017-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
