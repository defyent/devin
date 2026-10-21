# BUG-POP-003: Access Manager Groups popup: Esc closes with unsaved changes and no warning; reopening shows the unsaved ticks as if saved

| Field | Value |
|---|---|
| Checklist row | `AM-019` in `checklists/04-access-manager.md` |
| Module | Access Manager |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Access Manager, search betatest_low
2. Click the '0 Groups' badge
3. Tick 'Crew' (On Roster auto-ticks)
4. Press Esc
5. Note the row still says '0 Groups'
6. Click the Groups badge again

## Expected
Esc with unsaved changes asks to confirm (app modal); if discarded, the popup reopens with the saved memberships.

## Actual
Popup closes silently, nothing is saved, and on reopen 'Crew' is still ticked even though the user has 0 groups. Saving then would apply changes the user thought were thrown away.

## Evidence
- Screenshot: `screenshots/BUG-POP-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
Groups modal has no dirty check on Esc/close and doesn't reset its checkbox state from the server data when reopened.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
