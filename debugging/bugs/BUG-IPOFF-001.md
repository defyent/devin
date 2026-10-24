# BUG-IPOFF-001: Offline launch and push block for about a minute before timing out

| Field | Value |
|---|---|
| Checklist row | `IPOFF-001` |
| Module | Offline handling |
| Severity | Low |
| Environment | Simulator iPad Pro 13" M5, iOS 26.5 |
| App version | 1.0.13 (Build 46) |
| DataHangar version | v2.0.123 (`https://stresstest.datahangar.net`) |
| Status | Open |
| Found / session | 2026-10-24, https://app.devin.ai/sessions/8b79cff4b7ea4af2989164dd937fd4e4 |

## Steps to reproduce
1. Make the DataHangar host unreachable while leaving the Simulator online.
2. Launch the app and wait for the sync attempt to finish.
3. While still offline, attempt to push a flight.

## Expected
The app detects that it is offline and promptly explains that launch sync or push cannot proceed.

## Actual
Launch displays a blocking `Syncing Data` screen for about 60 seconds before `Authentication Error / The request timed out.` A push displays `Authenticating…` for about 60 seconds before `Push Failed / The request timed out.` No offline state is identified promptly.

## Evidence
- `screenshots/IPOFF-001_authenticating_spinner.png`
- `screenshots/IPOFF-001_push_timeout.png`
- `screenshots/IPOFF-003_launch_sync_blocking.png`
- `screenshots/IPOFF-003_launch_auth_error.png`

## Suspected cause (optional)
No prompt reachability check; the request waits for its timeout. Root cause is TBD.

## Test data involved
Offline test against `stresstest.datahangar.net`; local edits remained intact.

## Related
TBD
