# iPad: Setup and baseline

- **Checklist ID prefix:** `IPSET`
- **Guide section:** `ipad/IPAD_AUDIT_PLAN.md`
- **Where:** /ipad/ in Chrome, emulated iPad
- **Frontend cross-reference:** 00-setup-and-accounts
- **Viewport:** P 820x1180 and L 1180x820 unless stated
- **Tester:**  
- **Date / app build / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID. Sync rows: put the frontend record checked in Notes.

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPSET-001 | Record app build (index.js size + Last-Modified; App Version/Build in Config if native) | Recorded | PASS |  | index.js 1,583,035 bytes, 24/10/2026; App Version not shown in Chrome (native only) |
| IPSET-002 | Record frontend version, account, level and site time zone | Recorded | PASS |  | Service Account (datahangar), admin; site TZ Pacific/Auckland (from flightdetails_json) |
| IPSET-003 | Start CDP capture (console, exceptions, HTTP >= 400) | Errors visible | PASS |  | Only favicon.ico 404 |
| IPSET-004 | Apply viewport emulation P (820x1180) and L (1180x820), mobile, DPR 2, touch | Layout renders as iPad | PASS |  | emulate.py helper; P done |
| IPSET-005 | Fresh device: clear site data, reload, first-run modal appears; Maybe Later dismisses; Go to Configuration opens Config | Works | PASS |  | Modal shown on first load; Go to Configuration works |
| IPSET-006 | Snapshot all localStorage keys and IndexedDB stores before changes | Baseline recorded | PASS |  | 42 localStorage keys (21 + *_backup); IDB DataHangarApp v1 store appData |
| IPSET-007 | Hard reload: app reloads from server with no stale bundle (check cache headers on index.js) | Fresh bundle | TODO |  |  |
| IPSET-008 | Record which test accounts per level will be used on the iPad | Mapped to checklist 00 accounts | TODO |  |  |

## Test data created

| Record | Where | Cleaned up |
|---|---|---|
