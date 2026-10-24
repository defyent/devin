# BUG-CHAT-002: Chat times show 12-hour '01:32 AM' and date separators 'Thursday, October 22, 2026' instead of the org format

| Field | Value |
|---|---|
| Checklist row | `CHAT-S04` in `checklists/28-chat.md` |
| Module | Chat |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings > Time Zone has 24-hour HH:mm
2. Header chat icon > #beta-test-only-channel
3. Send a message and read its time

## Expected
01:32 (HH:mm) and 22/10/2026 (DD/MM/YYYY), local time.

## Actual
Message time '01:32 AM' (12-hour, external CHAT-01 still present) and day separator 'Thursday, October 22, 2026'.

## Evidence
- Screenshot: `screenshots/BUG-CHAT-002-1.png`, `screenshots/BUG-CHAT-002-2.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
