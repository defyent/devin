# BUG-RB-005: Roster Builder: every validation error throws a JS error instead of showing a message (e.g. Apply Shift Pattern with no shifts)

| Field | Value |
|---|---|
| Checklist row | `RB-008` in `checklists/14-roster-builder.md` |
| Module | Roster Builder |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Roster Builder, select a draft
2. Click a person's name > Shift Summary > Apply Shift Pattern
3. Leave the pattern empty and click Apply

## Expected
Error popup 'Please add at least one shift to the pattern.' and the pattern popup stays open.

## Actual
The pattern popup closes, no message appears, and the console shows 'Cannot read properties of undefined (reading 'overlay')'.

## Evidence
- Screenshot: `screenshots/BUG-RB-005-1.png`
- Console / network errors: none

## Suspected cause (optional)
openErrorModal() (rosterbuilder/index.js line 5057) hides elements.predictModal.overlay, but there is no predictModal in the elements map, so it throws before showing the error. Every openErrorModal call on the page is affected.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
