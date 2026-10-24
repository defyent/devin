# BUG-HAZ-001: Hazard Register details: Hazard Type always shows '--'

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
1. Flight Safety > Safety Reports > report #2060 > Final Report: Add to Hazard Register, Type = Hazard (later Risk), Save Changes
2. Flight Safety > Hazard Register > click #2060
3. Look at Hazard Details > HAZARD TYPE

## Expected
Shows the type picked on the safety report (Hazard / Risk).

## Actual
Shows '--'.

## Evidence
- Screenshot: `screenshots/BUG-HAZ-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
hazarddetails.js getHazardTypeText() only knows the codes E/S/I/C/P (Eliminate, Substitute, Isolate, Control, PPE). The Safety Report form saves Hazard/Risk, so every type falls back to '--'.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
