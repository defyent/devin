# BUG-CHAT-001: Chat has no page Help (?); Escape doesn't close Create Channel; empty name does nothing with no message

| Field | Value |
|---|---|
| Checklist row | `CHAT-S02` in `checklists/28-chat.md` |
| Module | Chat |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Click the header chat icon
2. Look for a Help (?) button
3. Click + (Create channel), click Create with no name
4. Press Escape

## Expected
Help (?) exists; empty name shows a message; Escape closes the popup.

## Actual
No Help button. Create with an empty name does nothing and shows nothing (external CHAT-05). Escape leaves the popup open (external CHAT-06); outside click now closes it.

## Evidence
- Screenshot: `screenshots/BUG-CHAT-001-1.png`, `screenshots/BUG-CHAT-001-2.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
