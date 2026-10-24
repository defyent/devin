# iPad configuration — general

- **Checklist ID prefix:** `IPCFG`
- **Guide section:** `debugging/IPAD_SWIFT_AUDIT_PLAN.md` §3
- **Where:** iPad app — PIN gate (set/change/wrong PIN), theme, time format/offset, proximity, coordinate format, weight unit, device ID, debug mode
- **Permission:** Admin / Service Account unless a different permission level is identified in the row notes
- **Tester:** Devin
- **Date / DataHangar version:** 24/10/2026 / iPad DataHangar Flight 1.0.13 (46) on iOS 26.5 Simulator; stresstest v2.0.123
- **Account / level used:** Service Account unless a different account is identified in the row notes

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPCFG-001 | Config General screen: Theme (Light/Dark/Midtone), Time Format, Auto Time Offsets, Config PIN, Aerodrome Proximity, Coordinate Format, Personnel Weight Unit, Device Identifier (iPad-F6EC)… | Behaves correctly / matches website | PASS |  | L293: Config General screen: Theme (Light/Dark/Midtone), Time Format, Auto Time Offsets, Config PIN, Aerodrome Proximity, Coordinate Format, Personnel Weight Unit, Device Identifier (iPad-F6EC), API Debug Mode. Evidence [IPCFG-001_config_general.png](../bugs/screenshots/IPCFG-001_config_general.png). |
| IPCFG-002 | Theme Light applies immediately (whole app). Checking contrast of value text in Light. | No defect (see Bug ID) | FAIL | BUG-IPUI-002 | L294: Theme Light applies immediately (whole app). Checking contrast of value text in Light. |
| IPCFG-003 | : Light theme - Device Identifier value 'iPad-F6EC' renders white-on-white (unreadable); Automatic Time Offsets toggle OFF state almost invisible. -> BUG-IPUI-002. Evidence IPCFG-003_ligh… | No defect (see Bug ID) | FAIL | BUG-IPUI-002 | L297: FAIL (Low/UI): Light theme - Device Identifier value 'iPad-F6EC' renders white-on-white (unreadable); Automatic Time Offsets toggle OFF state almost invisible. -> BUG-IPUI-002. Evidence [IPCFG-003_light_contrast.png](../bugs/screenshots/IPCFG-003_light_contrast.png) |
| IPCFG-005 | Time Format 12h: DatePickers switch to en_US AM/PM correctly (2:13 AM), 24h -> 02:14. Display formatting itself PASS (values wrong due to BUG-IPFL-003). | No defect (see Bug ID) | FAIL | BUG-IPFL-003 | L299: Time Format 12h: DatePickers switch to en_US AM/PM correctly (2:13 AM), 24h -> 02:14. Display formatting itself PASS (values wrong due to BUG-IPFL-003). |
| IPCFG-006 | Config PIN: source review - PIN field writes every keystroke straight to Keychain (no confirm, no 4-digit validation); PinPadView requires exactly 4 digits. Entering 1-3 digits would lock… | No defect (see Bug ID) | FAIL | BUG-IPCFG-001 | L300: Config PIN: source review - PIN field writes every keystroke straight to Keychain (no confirm, no 4-digit validation); PinPadView requires exactly 4 digits. Entering 1-3 digits would lock Configuration behind a PIN that cannot be entered (only Wipe/reinstall recovers). Interactive test next. |
| IPCFG-007 | PIN 1234 set via config keypad; closing + reopening Configuration shows 'Enter Configuration PIN' gate (4 dots) -> PASS. Note: PIN entry keypad in Config offers '.' and '+/-' keys (non-di… | Behaves correctly / matches website | PASS |  | L301: PIN 1234 set via config keypad; closing + reopening Configuration shows 'Enter Configuration PIN' gate (4 dots) -> PASS. Note: PIN entry keypad in Config offers '.' and '+/-' keys (non-digit PIN possible). |
| IPCFG-008 | PIN gate: 0000 rejected (config did not open), 1234 opens Configuration -> PASS. Note: PIN shown in plaintext (1234) in Config field. | Behaves correctly / matches website | PASS |  | L302: PIN gate: 0000 rejected (config did not open), 1234 opens Configuration -> PASS. Note: PIN shown in plaintext (1234) in Config field. |
| IPCFG-009 | BUG-IPCFG-001: Config PIN field accepts and saves '12' (2 digits) with no validation; PinPadView only checks at exactly 4 digits, so such a PIN can never be entered -> Configuration locke… | No defect (see Bug ID) | FAIL | BUG-IPCFG-001 | L303: FAIL (Medium) -> BUG-IPCFG-001: Config PIN field accepts and saves '12' (2 digits) with no validation; PinPadView only checks at exactly 4 digits, so such a PIN can never be entered -> Configuration locked out (Wipe is inside Configuration; only reinstall / Keychain reset recovers, losing credentials). Not live-locked to preserve the session; PIN cleared afterwards. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
