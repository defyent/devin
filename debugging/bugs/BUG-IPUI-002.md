# BUG-IPUI-002 — Light theme: Configuration values/toggles unreadable (white on white)

- **Module:** iPad app — Configuration > General
- **Severity:** Low (UI / accessibility contrast)
- **App:** DataHangar Flight 1.0.13 (46), iPad Pro 13" Simulator iOS 26.5

## Steps
1. Configuration > Theme = Light.
2. Look at Device Identifier and Automatic Time Offsets.

## Expected
Values and controls legible (WCAG AA contrast), as in Dark/Midtone.

## Actual
Device Identifier value `iPad-F6EC` is white text on a white card (unreadable). The OFF state of the Automatic Time Offsets toggle is a near-white track on white, barely visible.

## Evidence
- screenshots/IPCFG-001_config_general.png (Midtone, readable)
- screenshots/IPCFG-002_light_theme.png, screenshots/IPCFG-003_light_contrast.png (Light)

## Notes
Likely a hard-coded light text colour / toggle tint not using theme tokens. Check other screens in Light during row 78.
