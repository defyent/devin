# BUG-SFT-002: Flight Types: a duplicate Flight Category name ("PIC") is accepted

| Field | Value |
|---|---|
| Checklist row | `SFT-001` in `checklists/37-settings-flighttypes.md` |
| Module | Settings: Flight Types |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Configuration > Flight Types > Flight Categories.
2. Add Flight Category, name "PIC" (already exists as ID 3), then Save.

## Expected
Refused with a "name already exists" message.

## Actual
"Flight category added successfully". The list now has two "PIC" rows (ID 3 and ID 15), so the Flight Details, FRMS and Reports dropdowns would show two PIC options.

## Evidence
- Screenshot: `screenshots/BUG-SFT-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
No unique check on the name, either client-side or server-side.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
