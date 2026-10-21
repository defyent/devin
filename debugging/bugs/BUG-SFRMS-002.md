# BUG-SFRMS-002: FRMS Settings on a phone: the page scrolls sideways, "+ Add ... Rule" is off-screen and rule text is clipped

| Field | Value |
|---|---|
| Checklist row | `SFRMS-S05` in `checklists/40-settings-frms.md` |
| Module | Settings: FRMS |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open Settings and Tools > Fatigue Risk Management Settings at a 390 px width.
2. Pick Rostered Shift Rules (or any tab) from the section dropdown.

## Expected
The rule list, search and the Add button fit the screen.

## Actual
The page is 506 px wide, so it scrolls sideways. "+ Add Roster Rule" is off the right edge, and long rule names (e.g. "A 'Night Shift 12hr' shift can only be followed by: Rest Day") are cut off. The section dropdown itself works.

## Evidence
- Screenshot: `screenshots/BUG-SFRMS-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
The .table-header row (search + Add button) and .rule-list have fixed or minimum widths and don't wrap below 768 px.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
