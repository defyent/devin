# BUG-POP-002: Manage User Permissions uses a native browser confirm() for unsaved changes

| Field | Value |
|---|---|
| Checklist row | `AM-023` in `checklists/04-access-manager.md` |
| Module | Access Manager > Manage User Permissions |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Access Manager > a user's 'N Permissions' badge
2. Tick any permission type
3. Click Cancel

## Expected
App-styled confirm modal (like Activate Login Access / Logout), Esc = stay.

## Actual
Native Chrome confirm: 'You have unsaved changes. Are you sure you want to cancel?'. Looks out of place, cannot be styled, blocks the page.

## Evidence
- Screenshot: `screenshots/BUG-POP-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
accessmanager JS calls window.confirm() in the Cancel handler.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
