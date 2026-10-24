# BUG-IPSYNC-001: Push silently overwrites website-side Notes edits

| Field | Value |
|---|---|
| Checklist row | `IPSYNC-001` |
| Module | Flight sync / conflict handling |
| Severity | Medium |
| Environment | Simulator iPad Pro 13" M5, iOS 26.5 |
| App version | 1.0.13 (Build 46) |
| DataHangar version | v2.0.123 (`https://stresstest.datahangar.net`) |
| Status | Open |
| Found / session | 2026-10-24, https://app.devin.ai/sessions/8b79cff4b7ea4af2989164dd937fd4e4 |

## Steps to reproduce
1. On flight `#42914`, edit Notes on the website to `WEBEDIT`.
2. Make an offline Notes edit in the app.
3. Reconnect and push the app's flight changes.

## Expected
The app detects that the website Notes value changed since the app's copy was loaded and presents a conflict or otherwise prevents silently replacing the website edit.

## Actual
The push succeeds and replaces the website's `WEBEDIT` Notes value with the app's offline edit. No conflict is detected; the app uses last-write-wins behavior.

## Evidence
- `screenshots/IPOFF-005_push_after_reconnect.png`
- `screenshots/IPOFF-005_web_details_after_push.png`

## Suspected cause (optional)
No conflict detection during push; the app's stale local copy is sent as the latest value.

## Test data involved
Flight `#42914`; website Notes `WEBEDIT`; offline app Notes edit.

## Related
`BUG-IPSYNC-002`
