# iPad: Flights list and Download

- **Checklist ID prefix:** `IPFL`
- **Guide section:** `ipad/IPAD_AUDIT_PLAN.md`
- **Where:** Flights tab
- **Frontend cross-reference:** 06-flight-schedule
- **Viewport:** P 820x1180 and L 1180x820 unless stated
- **Tester:**  
- **Date / app build / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID. Sync rows: put the frontend record checked in Notes.

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPFL-001 | Download Flights opens week picker (Mon-Sun) with frontend flights | Same flights as Flight Schedule week | PASS |  | Oct 19-25 list loaded |
| IPFL-002 | Download one flight | 'Downloaded Flight #n — x legs, y files', shown in list | PASS |  | #8893: 1 leg, 0 files |
| IPFL-003 | Downloaded list = Flight Schedule for same week (count, times in site TZ, aircraft, PIC, crew, type, customer) | Matches frontend | TODO |  |  |
| IPFL-004 | Previous/next week navigation, empty week ('No flights scheduled this week') | Works | TODO |  |  |
| IPFL-005 | Download already-downloaded flight ('Already Downloaded') | Prompt, no duplicate | TODO |  |  |
| IPFL-006 | Unlink flight: local copy kept/removed as documented; frontend untouched | Defined | TODO |  |  |
| IPFL-007 | Search flights (rego, #id, route) | Filters | TODO |  |  |
| IPFL-008 | Flight row content: date, route, legs, sync badge; long titles | Readable | TODO |  |  |
| IPFL-009 | Delete Flight (local) confirm; frontend flight not deleted | Local only | TODO |  |  |
| IPFL-010 | Flights without PIC/crew/route (e.g. #42913) display sensibly | No blank/dash artefacts | TODO |  |  |
| IPFL-011 | Cancelled / completed / template flights in the download list | Handled per frontend status | TODO |  |  |

## Test data created

| Record | Where | Cleaned up |
|---|---|---|
