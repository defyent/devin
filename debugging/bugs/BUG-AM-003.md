# BUG-AM-003: Last Activity column sort does not change order

| Field | Value |
|---|---|
| Checklist row | `AM-005` in `checklists/04-access-manager.md` |
| Module | Access Manager |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Access Manager > User Permissions
2. Click the Last Activity header, then click it again

## Expected
Ascending then descending: Service Account (only user with activity) moves from top to bottom.

## Actual
Same order both times: Service Account, Alex Richards, Zoe Mason, Curtis Porter... User and Username sort correctly. Retest 22/10/2026 (v2.0.113, accessmanager/index.js?v=2.0.113): fixed. The first click puts the most recent activity at the top (Service Account, Just now); the second click reverses it (Never rows first).

## Evidence
- Screenshot: `screenshots/BUG-AM-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
Sort comparator for Last Activity ignores direction (or sorts on the relative text with 'Never' handled separately).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
