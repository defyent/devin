# BUG-AM-006: Access Manager has no Chat permission, so you can't give Chat to a non-admin user

| Field | Value |
|---|---|
| Checklist row | `CHAT-005` in `checklists/28-chat.md` |
| Module | Access Manager / Chat |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Access Manager > BETA TEST ONLY Second > Permissions.
2. Look through all 76 permission cards for Chat (or Comms).
3. Log in as BETA TEST ONLY Grpuser and click the chat icon in the header.

## Expected
There is a Chat card (the checklist says Chat = A), so an admin can let staff use Chat.

## Actual
None of the 76 cards is Chat or Comms. Every non-admin test user sees the chat icon in the header but gets 'Access Denied: You do not have permission to access the Chat feature'. Only the admin can use Chat, so you can't test unread badges between two users.

## Evidence
- Screenshot: `screenshots/BUG-AM-006-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
