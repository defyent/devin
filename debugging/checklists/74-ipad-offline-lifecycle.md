# iPad: Offline, persistence and lifecycle

- **Checklist ID prefix:** `IPOFF`
- **Guide section:** `ipad/IPAD_AUDIT_PLAN.md`
- **Where:** whole app
- **Frontend cross-reference:** 95-xc-performance-errors
- **Viewport:** P 820x1180 and L 1180x820 unless stated
- **Tester:**  
- **Date / app build / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID. Sync rows: put the frontend record checked in Notes.

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPOFF-001 | Reload: flights, settings, credentials and theme persist | Persist | TODO |  |  |
| IPOFF-002 | Go offline (DevTools): app still opens and edits local flights | Works offline | TODO |  |  |
| IPOFF-003 | Push/pull/sync offline: clear 'Connection Error', no data loss | Clear | TODO |  |  |
| IPOFF-004 | Back/forward browser buttons do not lose data | No loss | TODO |  |  |
| IPOFF-005 | *_backup keys and flights_backup: when written, restored, and cleared | Defined | TODO |  |  |
| IPOFF-006 | Storage quota: many flights with images | Warned before full | TODO |  |  |
| IPOFF-007 | Two tabs open (simulates two devices): last-write handling | No corruption | TODO |  |  |
| IPOFF-008 | Background/foreground and WKWebView eviction | BLOCKED (native) | TODO |  |  |
| IPOFF-009 | Performance: Sync All Data and Download timings; large lists scroll smoothly | < 3 s, 60 fps | TODO |  |  |

## Test data created

| Record | Where | Cleaned up |
|---|---|---|
