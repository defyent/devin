# BUG-IPTRK-001: Live Tracking UI/state issues (raw HTML error, stale/global menu, no offline indicator)

- Severity: Low
- Area: iPad app > Live Tracking
- Build: DataHangar Flight 1.0.13 (46), iPad Pro 13" Simulator iOS 26.5; site stresstest v2.0.123
- Status: Open

## Findings
1. Error modal shows the server's raw HTML ("Server returned: <!DOCTYPE html>..."). (LiveTrackingService.sendPing sets lastError to the first 200 chars of the response.)
2. After Start Tracking, the flight detail menu still says "Start Tracking" (FlightDetailView reads LiveTrackingService.shared.isActive without observing it). Tapping it again starts a new session ID.
3. The menu shows the global session state: flight #8884, which was not being tracked, showed "Stop Tracking" while #42914 was tracked. Tapping it would stop the other flight's session.
4. While offline, the toolbar icon stays green/active; network errors only set lastError.
5. No confirmation or toast after Start Tracking from the flight menu.

## Evidence
screenshots/IPTRK-002_menu_still_start.png, screenshots/IPTRK-003_app_tracking_error.png, screenshots/IPTRK-006_other_flight_shows_stop.png, screenshots/IPTRK-006_offline_icon_green.png
