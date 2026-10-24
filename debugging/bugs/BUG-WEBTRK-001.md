# BUG-WEBTRK-001: Live tracking pings fail on stresstest - live_tracking table missing

- Severity: High (Live Tracking unusable); Security note: raw SQL error page exposed
- Area: Website/server > wab_live_tracking_post (used by iPad app Live Tracking)
- Build: stresstest v2.0.123; iPad app DataHangar Flight 1.0.13 (46)
- Status: Open

## Steps
1. iPad app: Config > DataHangar > Live Tracking ON, interval 30s.
2. Open pushed flight #42914 > menu > Start Tracking (Simulator location Auckland, moving).
3. Leg toolbar tracking icon turns red; tap it.

## Expected
Ping saved; aircraft appears on Active Flights > Live Tracking map.

## Actual
Every ping gets an HTML "Error" page:
`exec_sql: Can't execute (INSERT INTO live_tracking (session_id, flight_id, person_id, lat, lng, altitude_m, speed_ms, heading_deg, accuracy_m, device_id, recorded_at) ...): DBD::mysql::st execute failed: Table 'stresstest.live_tracking' doesn't exist at /var/www/datahangar/DHLib/DHMysql.pm line 363.`
The map shows nothing. The error page shows SQL text, parameters and a server path to the client.

## Notes
- The stored recorded_at looks like the server receive time (NZ), not the device's recorded_at (UTC ISO); device_id has its hyphen stripped. Re-verify once the table exists.
- Check whether production has the table (missing migration?).
- App side: non-"Ok" responses are dropped, not queued (LiveTrackingService.sendPing), and the raw HTML is shown in the error modal.

## Evidence
evidence/IPTRK-003_app_tracking_error.png, screenshots/IPTRK-003_web_active_flights.png; full error text from app URLCache (Cache.db-wal)
