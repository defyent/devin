# BUG-RB-007: Roster Builder: Clear then Publish of a draft month with no shifts does not clear the live roster and shows no message

| Field | Value |
|---|---|
| Checklist row | `RB-013` in `checklists/14-roster-builder.md` |
| Module | Roster Builder |
| Severity | High |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Roster Builder, pick a month that has a shift in the Live Roster (test used December 2027 with one BETA TEST ONLY Office Hours shift)
2. Select a draft that has no shifts for that month
3. Publish Month > Clear then Publish
4. Accept the browser confirm 'The draft ... has no shifts for December 2027. Publishing it will clear the live roster for this month. Do you want to continue?'
5. Switch to Live Roster (also after changing month and back)

## Expected
Live roster for the month is cleared and a 'published successfully' message shows.

## Actual
No toast or message at all, and the live shift is still there after reloading the month. Publish Only (Merge) with one shift worked ('published to live roster successfully').

## Evidence
- Screenshot: `screenshots/BUG-RB-007-1.png`
- Console / network errors: none

## Suspected cause (optional)
Suspected: publishDraft() (rosterbuilder/index.js around line 4139) hits an error in the clear/publish path, and the catch calls openErrorModal(), which itself throws (BUG-RB-005), so the failure is swallowed with no message. The 'draft has no shifts' path also uses a native confirm() instead of the app's popup.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
