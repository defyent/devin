# BUG-IPDH-001: Keychain save failure is silent

| Field | Value |
|---|---|
| Checklist row | `IPDH-001` |
| Module | DataHangar configuration / credentials |
| Severity | Low |
| Environment | Simulator iPad Pro 13" M5, iOS 26.5 |
| App version | 1.0.13 (Build 46) |
| DataHangar version | v2.0.123 (`https://stresstest.datahangar.net`) |
| Status | Open |
| Found / session | 2026-10-24, https://app.devin.ai/sessions/8b79cff4b7ea4af2989164dd937fd4e4 |

## Steps to reproduce
1. Run an unsigned Simulator build with `CODE_SIGNING_ALLOWED=NO`.
2. Enter the DataHangar URL, username, and password, then save/use the credentials.
3. Attempt authentication.

## Expected
The app reports a Keychain save failure, or credentials are saved successfully before authentication is attempted.

## Actual
The Keychain write failure is not surfaced. The fields remain filled, but authentication reports `Error: notConfigured`. An ad-hoc-signed rebuild avoided the unsigned-build condition.

## Evidence
- TBD — no matching evidence file is present in `screenshots/`.

## Suspected cause (optional)
The app ignores the `SecItemAdd` status returned from the Keychain save operation.

## Code pointer
`KeychainStore.setString`.

## Test data involved
Unsigned Simulator build; exact credential values are not recorded.

## Related
`BUG-IPDH-002`
