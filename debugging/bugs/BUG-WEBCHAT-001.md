# BUG-WEBCHAT-001 — Chat API used by the iPad app ignores the Chat permission (permission bypass)

**Severity:** High (security / access control)
**Area:** Server — Chat API (used by iPad app Comms tab); website Chat page itself enforces correctly
**Environment:** stresstest.datahangar.net v2.0.123; iPad app DataHangar Flight 1.0.13 (46), iPad mini (A17 Pro) iOS 26.5 Simulator

## Summary
A user with **0 permissions, 0 roles, 0 groups** is blocked from Chat on the website ("Access Denied: You do not have permission to access the Chat feature"), but the same user, logged into the iPad app, can list chat channels, read every message (including images) and post new messages. The server's chat endpoints the app calls do not check the Chat permission. Every other app area tested with the same user (Sync All, Flights download, Safety Reports download/options) is correctly denied.

## Steps
1. Website, Settings and Tools > Access Manager > New User: "BETA TEST ONLY LowPerm" (username betalowperm), no permissions/roles/groups. Activate Login Access.
2. Website (incognito) log in as betalowperm > header Chat icon -> Access Denied (correct).
3. iPad app (fresh install) > Configuration > DataHangar: log in as betalowperm. Test Authentication succeeds; Sync All -> 6x "Access denied" (correct).
4. Comms tab -> channel `#beta-test-only-ipad-chat` listed with 17 unread; open it -> Service Account messages and image visible.
5. Send "BETA TEST ONLY lowperm message" -> delivered, attributed to BETA TEST ONLY LowPerm.

## Expected
Chat API endpoints (channels list, messages, send, poll, image fetch, read tracking) return Access Denied for users without Chat permission, matching the website; app shows the same "Access denied" state it shows for Flights/Safety Reports.

## Actual
Full read and write access to chat through the API.

## Notes
- App side: `ChatService.swift` has no permission check beyond `isAdmin` (delete gating). App should also handle a denied response gracefully once the server enforces it.
- Also observed: non-admins cannot delete their own messages in the app (`CommsView.swift` context menu only `if isAdmin`) — parity with website TBD.

## Evidence
- screenshots/IPPERM-016_lowperm_comms_channel_visible.png
- screenshots/IPPERM-017_lowperm_comms_read.png
- screenshots/IPPERM-018_lowperm_send_ok.png
- screenshots/IPPERM-024_web_lowperm_chat_denied.png
- screenshots/IPPERM-025_web_shows_lowperm_message.png (server stored the unauthorised post)
- screenshots/IPPERM-011_lowperm_sync_denied.png (contrast: other areas denied)
