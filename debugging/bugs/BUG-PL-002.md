# BUG-PL-002: A person with no name exists and is listed as '?' at the top of All Personnel (person #274, Customer)

| Field | Value |
|---|---|
| Checklist row | `PL-001` in `checklists/11-all-personnel.md` |
| Module | All Personnel |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Sidebar > Personnel > All Personnel
2. Look at the first row (or set All Roles > Customer)
3. Click it

## Expected
Every person has at least a name or company; creating a person or customer without one is refused.

## Actual
The first row has a '?' avatar, an empty name, No Groups and role Customer. It opens Personnel Details for person_id=274 with First, Middle, Last Name and Company all empty. Its History only shows forms filled by Service Account on 17 Oct 2026 (AUDIT All Widgets), so it already existed before this run. How it was created isn't known; possibly an empty New Customer save in Flight Details.

## Evidence
- Screenshot: `screenshots/BUG-PL-002-1.png`, `screenshots/BUG-PL-002-2.png`, `screenshots/BUG-PL-002-3.png`
- Console / network errors: none

## Suspected cause (optional)
Person/customer create path allows saving with all name fields empty.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
