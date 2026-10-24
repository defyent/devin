# iPad: Configuration: General Info

- **Checklist ID prefix:** `IPCFG`
- **Guide section:** `ipad/IPAD_AUDIT_PLAN.md`
- **Where:** Config > General Info
- **Frontend cross-reference:** 33-settings-timezone
- **Viewport:** P 820x1180 and L 1180x820 unless stated
- **Tester:**  
- **Date / app build / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID. Sync rows: put the frontend record checked in Notes.

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPCFG-001 | Theme Dark / Midtone / Light: whole app restyles, persists after reload | Persists | TODO |  |  |
| IPCFG-002 | Toggle Theme header icon cycles themes | Cycles | TODO |  |  |
| IPCFG-003 | Automatic Time Offsets on/off and Time Offset (minutes): takeoff/shutdown derived from engine start/landing | Correct derived times | TODO |  |  |
| IPCFG-004 | Configuration PIN: set 4 digits; Config then requires PIN; wrong PIN shows 'Incorrect PIN. Try again.' | PIN enforced | TODO |  |  |
| IPCFG-005 | PIN default: help says 0000; check stored value and behaviour with no PIN set | Matches help text | TODO |  |  |
| IPCFG-006 | PIN keypad: Clear, backspace, Done, >4 digits rejected, letters rejected | Validated | TODO |  |  |
| IPCFG-007 | Aerodrome Proximity (NM): 0, negative, decimal, huge, empty | Validated; 'Now' uses value | TODO |  |  |
| IPCFG-008 | Coordinate Format DD/DDM/DMS: waypoints and nearby aerodromes display in chosen format, values correct | Correct conversions | TODO |  |  |
| IPCFG-009 | Personnel Weight Unit kg/lb: every weight shows converted, stored unit unchanged | Converted | TODO |  |  |
| IPCFG-010 | Time Format 24h/12h: leg times display; data sent to DataHangar stays 24h | Display only | TODO |  |  |
| IPCFG-011 | API Debug Mode: log captures requests/responses, password masked (***), Clear Log works | Masked, clears | TODO |  |  |
| IPCFG-012 | Export Configuration / Copy Configuration produce JSON; contents (does it include password?) | No secrets exported | TODO |  |  |
| IPCFG-013 | Import Configuration: valid file, invalid JSON ('Import Error'), wrong schema, older version | Clear messages, no partial import | TODO |  |  |
| IPCFG-014 | Clear All Data: confirm (danger), clears flights/aircraft/personnel/settings, credentials, *_backup keys | Fully cleared | TODO |  |  |
| IPCFG-015 | Done/back with unsaved changes ('Unsaved Changes' prompt) | Prompt shown | TODO |  |  |
| IPCFG-016 | Open Source Acknowledgements present and correct | Present | TODO |  |  |

## Test data created

| Record | Where | Cleaned up |
|---|---|---|
