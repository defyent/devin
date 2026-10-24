# BUG-IPPERM-001: App lets read-only users edit and push flights and only fails at the server, showing a raw "Error block Error" message

- **Severity:** Medium (UX/data: edits made can never be saved; the server enforces permissions correctly)
- **Area:** iPad app, Flights, permissions
- **Found:** 2026-10-24, iPad mini (A17 Pro) Simulator, iOS 26.5, DataHangar Flight 1.0.13 (46), stresstest v2.0.123
- **User:** BETA TEST ONLY LowPerm. Permissions: Flight Schedule = Read Only All, Flight Details = Read Only All, Resources = All Access, W&B Config Download = All Access, Safety Reports = Write Own.

## Steps
1. Log in to the app as the read-only user and download flight #42914.
2. Edit Notes (Add Leg and all the fields are enabled too).
3. Set the aircraft if needed (see BUG-IPFL-004), then choose ... > Push to Server > Push.

## Expected
The app should see that the user can't edit flights (the server already exposes per-user permissions, as Safety Reports do). It should then show the flight read-only, hide Add Leg and Push, or warn before any edits are made.

## Actual
- Every edit control and Push stays enabled.
- The confirmation dialog appears, then the push fails with: "Push Failed - Could not push flight data to DataHangar. Error block Error Access Denied: You do not have permission to create or modify flights."
- The message includes raw markup text ("Error block Error").
- The local edit stays "needs push" forever. After a Pull it is silently kept and marked synced (BUG-IPSYNC-002).

## Server
It correctly rejects the write (PASS). Website #42914 is unchanged.

## Evidence
- `evidence/IPPERM-049_readonly_flight_editable.png`
- `evidence/IPPERM-068_readonly_push_confirm_zkhel.png`
- `evidence/IPPERM-069_readonly_push_server_denied.png`
