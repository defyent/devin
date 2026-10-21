# BUG-FD-001: Flight Details Save Changes does not return to the Flight Schedule and gives no success message

| Field | Value |
|---|---|
| Checklist row | `FD-034` in `checklists/07-flight-details.md` |
| Module | Flight Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Schedule > Schedule Only > week
2. Double-click flight #42903 > Flight Details
3. Add a passenger or comment
4. Click Save Changes

## Expected
Flight is saved and you return to where you came from (the Flight Schedule week you were on), as described in the guide.

## Actual
The page reloads in place (URL now has return_url=/index.pl?action=flightschedule) and stays on Flight Details. No toast or message says it was saved; only the greyed-out Save Changes button hints at it. The user has to click Back.

## Evidence
- Screenshot: `screenshots/BUG-FD-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
Save handler reloads the details page with return_url instead of navigating to return_url after a successful save.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
