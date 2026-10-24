# BUG-IPSYNC-002: Pull from Server does not reliably update website-edited Notes

| Field | Value |
|---|---|
| Checklist row | `IPSYNC-002` |
| Module | Flight sync / pull |
| Severity | Medium |
| Environment | Simulator iPad Pro 13" M5, iOS 26.5 |
| App version | 1.0.13 (Build 46) |
| DataHangar version | v2.0.123 (`https://stresstest.datahangar.net`) |
| Status | Open |
| Found / session | 2026-10-24, https://app.devin.ai/sessions/8b79cff4b7ea4af2989164dd937fd4e4 |

## Steps to reproduce
1. Edit the Notes on website flight `#42914` to `WEBEDIT`.
2. In the app, use `Already Downloaded` > `Pull from Server (overwrites local changes)`.
3. Check the flight's Notes in the app.

## Expected
The app replaces its stale Notes value with the website value `WEBEDIT`.

## Actual
Pull from Server leaves the app's Notes unchanged even though the action says it overwrites local changes. The pulled leg times also changed from `00:07` to `00:07:00`; that format problem is tracked separately as BUG-IPFL-003.

## Evidence
- `screenshots/IPPERM-063_web_42914_notes_server.png` (website Notes)
- `screenshots/IPPERM-064_app_42914_notes_RO_synced.png` (app after Pull: local text kept, marked synced)

## Suspected cause (optional)
Not fully traced: the Pull path in `FlightSyncService.swift` refreshes sync timestamps and leg data but does not replace local flight-level fields such as Notes, and it clears the needs-push flag.

## Test data involved
Flight `#42914`; website Notes `WEBEDIT`.

## Related
`BUG-IPSYNC-001`

## Additional evidence (permissions run, iPad mini, user betalowperm)
1. Downloaded #42914, edited Notes to append " RO" (flight flagged "needs push").
2. Push failed client-side (Aircraft configuration (nil) not found) - nothing sent; server `serverLastUpdatedAt` stayed 2026-10-24 20:46:40.
3. Ran Pull from Server -> app status became "#42,914 synced" but Notes still "BETA TEST ONLY OFFLINE EDIT RO" (local store `notes` field confirmed via SQLite, `lastSyncedAt` 10:01:57Z).
4. Website Flight #42914 Notes = "BETA TEST ONLY OFFLINE EDIT".

Result: Pull keeps unpushed local Notes and clears the needs-push flag, so the edit is never sent and the app silently disagrees with the server.
Evidence: `screenshots/IPPERM-063_web_42914_notes_server.png`, `screenshots/IPPERM-064_app_42914_notes_RO_synced.png`.
Severity raised to Medium-High (silent divergence, confirmed with screenshots).

## Retest 24/10/2026 (IPPERM-061/063) — worse than first recorded
- Website #42914 Notes = 'BETA TEST ONLY OFFLINE EDIT'. App had an unpushed local edit 'BETA TEST ONLY OFFLINE EDIT RO' (push had failed).
- After Pull from Server the app kept the local text **and** changed the badge to '#42,914 synced', clearing needs-push. The edit is now never sent and the divergence is hidden.
- `screenshots/IPPERM-063_web_42914_notes_server.png`
- `screenshots/IPPERM-064_app_42914_notes_RO_synced.png`
