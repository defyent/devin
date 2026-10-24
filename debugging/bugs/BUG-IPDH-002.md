# BUG-IPDH-002: Empty-field authentication and sync buttons look enabled

| Field | Value |
|---|---|
| Checklist row | `IPDH-002` |
| Module | DataHangar configuration / button states |
| Severity | UI |
| Environment | Simulator iPad Pro 13" M5, iOS 26.5 |
| App version | 1.0.13 (Build 46) |
| DataHangar version | v2.0.123 (`https://stresstest.datahangar.net`) |
| Status | Open |
| Found / session | 2026-10-24, https://app.devin.ai/sessions/8b79cff4b7ea4af2989164dd937fd4e4 |

## Steps to reproduce
1. Open DataHangar configuration with the URL, username, and password fields empty.
2. Observe `Test Authentication` and `Sync All`, then tap each button.

## Expected
Buttons unavailable because required fields are empty are visibly disabled.

## Actual
`Test Authentication` and `Sync All` look enabled even though the fields are empty. Tapping them does nothing and provides no feedback.

## Evidence
- TBD — no matching evidence file is present in `evidence/`.

## Suspected cause (optional)
The disabled and enabled states use the same visual style.

## Code pointer
`PrimaryButtonStyle`.

## Test data involved
DataHangar configuration with all connection fields empty.

## Related
TBD
