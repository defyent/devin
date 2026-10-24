# BUG-IPCFG-001 — Configuration PIN saves non-4-digit values, permanently locking Configuration

- **Module:** iPad app — Configuration > Configuration PIN / PinPadView
- **Severity:** Medium (user can lock themselves out of all settings incl. DataHangar login; recovery = reinstall)
- **App:** DataHangar Flight 1.0.13 (46), iPad Pro 13" Simulator iOS 26.5

## Steps
1. Configuration > Configuration PIN, enter `12`, tap Done. Field shows `12` (saved).
2. Close Configuration, tap the gear again.

## Expected
PIN must be exactly 4 digits (reject/confirm before saving), or the gate accepts PINs of the saved length.

## Actual
`12` is saved to the Keychain immediately. The PIN gate (`PinPadView`) has 4 dots and only compares once 4 digits are entered, so `12` can never match -> Configuration unreachable. Wipe Data lives inside Configuration, so the only recovery is reinstalling the app.

## Cause
`ConfigView` binds `NumberPadField` directly to `KeychainStore.shared.configPin` (every keystroke persisted, no length/digit validation). The field's keypad also offers `.` and `+/-`. `PinPadView` `guard enteredPin.count < 4` / `if enteredPin.count == 4` compare.

## Also
- PIN displayed in plain text in Configuration.
- No confirm-PIN step.

## Evidence
- evidence/IPCFG-009_pin_2digit_saved.png
- evidence/IPCFG-007_pin_gate.png, screenshots/IPCFG-008_pin_correct_opens.png (4-digit PIN works)
