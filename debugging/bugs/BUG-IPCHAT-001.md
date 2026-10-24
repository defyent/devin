# BUG-IPCHAT-001: Chat message typed while offline is discarded on send

- Severity: Medium
- Area: iPad app > Comms
- Build: DataHangar Flight 1.0.13 (46), iPad Pro 13" Simulator iOS 26.5; site stresstest v2.0.123
- Status: Open

## Steps
1. Comms > select a channel.
2. Make stresstest unreachable (host blackhole route; device otherwise online).
3. Type "BETA TEST ONLY offline message" and tap Send.

## Expected
Message kept (pending bubble / outbox with retry), or input left intact with a quick "offline" error.

## Actual
Input clears immediately; no pending bubble or offline indicator. About 60-70 s later: "Error Sending Message - The request timed out." The text is gone and must be retyped. The message never reached the server.

## Cause
`CommsView.handleSend()` clears `messageText` and the pending image before `chatService.sendMessage`; the catch block only shows a popup. `DataHangarAPI` uses a 60 s request timeout.

## Suggested fix
Restore content/image on failure (or keep a pending bubble with Retry); check reachability before sending.

## Evidence
screenshots/IPCHAT-010_app_offline_after_send.png, screenshots/IPCHAT-010_app_offline_65s.png, screenshots/IPCHAT-010_app_offline_timeout_error.png, screenshots/IPCHAT-010_app_resend_online.png
