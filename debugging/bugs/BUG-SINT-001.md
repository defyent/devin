# BUG-SINT-001: Google Calendar Settings: Help and Add Calendar don't close with Escape or an outside click

| Field | Value |
|---|---|
| Checklist row | `SINT-S02` in `checklists/46-settings-integrations.md` |
| Module | Settings: Google Calendar Sync |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Configuration > Google Calendar Sync.
2. Click the help (?) icon, then press Escape.
3. Open it again and click outside it.
4. Click Add Calendar and press Escape.

## Expected
Help closes with Got it/×, an outside click and Escape. Add Calendar closes with Escape.

## Actual
Help only closes with × or Close. Escape and an outside click leave it open. Escape also leaves Add Calendar open.

## Evidence
- Screenshot: `screenshots/BUG-SINT-001-1.png`, `screenshots/BUG-SINT-001-2.png`
- Console / network errors: none

## Suspected cause (optional)
The page modals have no Escape key handler and no overlay click handler.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
