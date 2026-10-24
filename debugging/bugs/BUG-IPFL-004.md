# BUG-IPFL-004 — Flight downloaded before aircraft sync keeps aircraft "None" forever; Pull never re-links; push fails with "(nil)"

- **Severity:** Medium
- **Area:** iPad app, Flights (download/pull/push)
- **Found:** 2026-10-24, iPad mini (A17 Pro) Simulator, iOS 26.5, DataHangar Flight 1.0.13 (46), stresstest v2.0.123

## Steps
1. Log the app in as a user who cannot sync aircraft yet (no Resources permission), or download a flight before running Sync All.
2. Download BETA flight #42914 (ZK-HEL on the website).
3. Grant the user aircraft access (Resources + W&B Config Download) and run Sync All. Aircraft now sync.
4. Open #42914 and run Pull from Server.
5. Push the flight.

## Expected
Pull (or Sync All) re-links the flight to ZK-HEL (`dh-<resourceId>`), and push works. If it can't, the message should say the aircraft isn't available on this iPad and how to fix it.

## Actual
- The Aircraft field stays "None" and Category/Activity stay blank after Sync All and after Pull.
- Every push fails with "Push Failed: Could not push flight data to DataHangar. Aircraft configuration (nil) not found for this flight."
- The website still has ZK-HEL. Nothing was sent, so no server data was lost.

## Cause (source)
- `FlightSyncService.swift:129/142` sets `flight.aircraftId` from `aircraftStore.aircraft(id: "dh-\(serverFlight.resourceId)")` only on the first download.
- Pull (`~line 195`) reuses `localFlight.aircraftId` and never re-resolves it.
- `FlightUploadService.swift:41` and `FlightPayloadBuilder.swift:132` show the Swift `nil` text in the user-facing message.

## Evidence
- `evidence/IPPERM-050_readonly_flight_details_missing_ref.png`
- `evidence/IPPERM-052_readonly_push_nil_config.png`
- `evidence/IPPERM-057_5perm_sync_3_denied.png`
- `evidence/IPPERM-066_push_nil_config_after_aircraft_sync.png`
