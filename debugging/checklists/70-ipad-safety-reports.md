# iPad: Safety reports

- **Checklist ID prefix:** `IPSMS`
- **Guide section:** `ipad/IPAD_AUDIT_PLAN.md`
- **Where:** Safety Reports tab
- **Frontend cross-reference:** 19-safety-reports, 20-hazard-register
- **Viewport:** P 820x1180 and L 1180x820 unless stated
- **Tester:**  
- **Date / app build / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID. Sync rows: put the frontend record checked in Notes.

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPSMS-001 | Download Safety Reports list = frontend Safety Reports (as same user) | Match | TODO |  |  |
| IPSMS-002 | New Safety Report: Select Category, Location & Date, Narrative, required fields | Created on frontend, BETA TEST ONLY | TODO |  |  |
| IPSMS-003 | Initial / Final Risk Assessment: likelihood x consequence uses frontend risk matrix and colours | Match | TODO |  |  |
| IPSMS-004 | Hazard Register link / Eliminate / Mitigate | Matches frontend | TODO |  |  |
| IPSMS-005 | Confidential Report and Submit Anonymously: frontend hides identity accordingly | Identity hidden | TODO |  |  |
| IPSMS-006 | Report detail: Report Information, Extra Info, Final Report Summary edits sync | Match | TODO |  |  |
| IPSMS-007 | New Action / Complete Action / Change Status sync both ways | Match | TODO |  |  |
| IPSMS-008 | Add comment / add personnel sync both ways | Match | TODO |  |  |
| IPSMS-009 | Upload / download / delete document | Match | TODO |  |  |
| IPSMS-010 | Attach forms to report (saveforms) | Match | TODO |  |  |
| IPSMS-011 | Activity Log matches frontend history | Match | TODO |  |  |
| IPSMS-012 | Delete Report permission | Per frontend rules | TODO |  |  |
| IPSMS-013 | WG/WO users see own reports (cf. BUG-SMS-005) | Own reports visible | TODO |  |  |
| IPSMS-014 | Offline create then sync later | Queued and sent once | TODO |  |  |

## Test data created

| Record | Where | Cleaned up |
|---|---|---|
