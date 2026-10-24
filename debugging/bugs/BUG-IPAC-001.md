# BUG-IPAC-001 — Aircraft editor edits to server aircraft are local-only and silently reverted by Sync All

- **Module:** iPad app — Configuration > Aircraft > editor; SyncService.syncAircraft
- **Severity:** Medium (W&B inputs silently change; iPad and website diverge)
- **App:** DataHangar Flight 1.0.13 (46), iPad Pro 13" Simulator iOS 26.5; website v2.0.123

## Steps
1. Configuration > Aircraft > ZK-FLY (tagged "Server"). Set Empty Weight 600, Save. List shows "BEW 600 kg".
2. Configuration > DataHangar > Sync All Data.
3. Re-open Aircraft list.

## Expected
Either the edit is pushed to DataHangar, or the editor marks server-owned fields read-only / warns that changes are device-only and will be overwritten on sync.

## Actual
Sync All replaces Empty Weight with the server value (0); "BEW 600 kg" disappears with no message. Nothing is sent to the website (`AircraftEditorView.save()` -> `aircraftStore.upsert` only).
`SyncService` re-sync keeps the local W&B config (seats, arms, equipment, profiles, graphs) but overwrites emptyWeight, MTOW, type, registration, meters and time settings - so a single aircraft ends up as a mix of server and local values, and the iPad's W&B for that aircraft can differ from the website's with no indication.

## Evidence
- screenshots/IPAC-005_zkfly_bew600_saved.png
- screenshots/IPAC-006_zkfly_ew_reverted_after_sync.png
