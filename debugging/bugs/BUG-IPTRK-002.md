# BUG-IPTRK-002: Live Tracking queue stores duplicate/stale pings; rejected pings are dropped

- Severity: Medium
- Area: iPad app > Live Tracking > offline queue
- Build: DataHangar Flight 1.0.13 (46), iPad Pro 13" Simulator iOS 26.5; site stresstest v2.0.123
- Status: Open

## Steps
1. Start tracking on #42914 (30 s interval) with the device stationary.
2. Make stresstest unreachable (host blackhole route) for about 75 s.
3. Inspect UserDefaults lt_pendingPings.

## Actual
- The queue holds 6–7 entries. Most are identical (same recorded_at 08:56:37.677Z, same lat/lng), because each timer tick re-sends lastKnownLocation even when there is no new fix.
- One queued entry is a fix from 08:52:55, taken in the previous session (before Stop and relaunch), and it now carries the new session_id.
- The queue drains only after a successful "Ok" ping. A non-"Ok" server response is never queued, so that position is lost.
- Stop Tracking does not clear lt_pendingPings (7 remained after Stop); they would be sent later under the stopped session id.

## Expected
One point per new fix, no stale fixes carried from an earlier session, and server-rejected pings either retried or reported.

## Evidence
results.md IPTRK-006 entries (plutil dump of lt_pendingPings)
