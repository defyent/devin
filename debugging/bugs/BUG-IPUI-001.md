# BUG-IPUI-001: Hardware-keyboard focus leaks through sheets and keypads

| Field | Value |
|---|---|
| Checklist row | `IPUI-001` |
| Module | iPad UI / keyboard focus |
| Severity | Medium |
| Environment | Simulator iPad Pro 13" M5, iOS 26.5 |
| App version | 1.0.13 (Build 46) |
| DataHangar version | v2.0.123 (`https://stresstest.datahangar.net`) |
| Status | Open |
| Found / session | 2026-10-24, https://app.devin.ai/sessions/8b79cff4b7ea4af2989164dd937fd4e4 |

## Steps to reproduce
1. In a flight leg, enter `NZAA` in Departure and open the seat-assignment sheet.
2. Open Override Weight's custom numeric keypad and type `85` using a hardware keyboard.
3. In the Details tab, open the meter keypad and type a value while Notes had previously been active.
4. In a form, focus the textarea, then tap a key-value field and type using the hardware keyboard.

## Expected
Hardware-keyboard input is directed only to the field or control in the active sheet, keypad, or form widget.

## Actual
Typing goes into a field behind the sheet/keypad. Departure became `NZAA8585`; meter input was appended to Notes; and key-value field input was appended to the form textarea, corrupting its saved value.

## Evidence
- `screenshots/IPLEG-005_focus_leak_departure.png`
- `screenshots/IPXC-002_focus_leak_notes.png`
- `IPJSON-001_export.json`

## Suspected cause (optional)
The results note that custom keypads do not resign the previous first responder.

## Test data involved
Departure `NZAA`; Notes and form textarea.

## Related
TBD
