# iPad push/pull sync

- **Checklist ID prefix:** `IPSYNC`
- **Guide section:** `debugging/IPAD_SWIFT_AUDIT_PLAN.md` §3
- **Where:** iPad app — Create/update push, pull, out-of-sync behavior, conflicts, generated files
- **Permission:** Admin / Service Account unless a different permission level is identified in the row notes
- **Tester:** Devin
- **Date / DataHangar version:** 24/10/2026 / iPad DataHangar Flight 1.0.13 (46) on iOS 26.5 Simulator; stresstest v2.0.123
- **Account / level used:** Service Account unless a different account is identified in the row notes

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPSYNC-001 | Push to Server on local flight -> 'Create & Push Flight' confirm -> 'Flight Synced: Successfully pushed 1 leg to DataHangar Flight #42914.' (no thousands separator in alert). PASS (websit… | Behaves correctly / matches website | PASS |  | L63: Push to Server on local flight -> 'Create & Push Flight' confirm -> 'Flight Synced: Successfully pushed 1 leg to DataHangar Flight #42914.' (no thousands separator in alert). PASS (website verification pending) |
| IPSYNC-002 | Website Flight Schedule list: '#42914 ZK-HEL' Fri 23 Oct 2026 23:59-00:59, PIC: Cody Crawford. Wall-clock time preserved as entered on device (device TZ US/Pacific; server treats it as NZ… | Behaves correctly / matches website | PASS |  | L67: Website Flight Schedule list: '#42914 ZK-HEL' Fri 23 Oct 2026 23:59-00:59, PIC: Cody Crawford. Wall-clock time preserved as entered on device (device TZ US/Pacific; server treats it as NZ local). Times not shifted -> PASS for NZ devices; device-TZ != ops-TZ is a product decision (PD-IP-01). |
| IPSYNC-003 | Website #42914 Details: Aircraft ZK-HEL, PIC Cody Crawford, Route 'BETA TEST ONLY NZAA-NZCH', Notes 'BETA TEST ONLY iPad audit flight 1', Start 23/10/2026 23:59, End 24/10/2026 00:59, SAR… | Behaves correctly / matches website | PASS |  | L68: Website #42914 Details: Aircraft ZK-HEL, PIC Cody Crawford, Route 'BETA TEST ONLY NZAA-NZCH', Notes 'BETA TEST ONLY iPad audit flight 1', Start 23/10/2026 23:59, End 24/10/2026 00:59, SAR time 24/10 00:59, status Open, Files (1). Category/Activity empty (app create form has no category/activity fields - check Details tab in app). PASS |
| IPSYNC-004 | After local leg edits status badge changes to '#42,914 needs push' (orange). PASS (separator BUG-IPFL-001). | No defect (see Bug ID) | FAIL | BUG-IPFL-001 | L85: After local leg edits status badge changes to '#42,914 needs push' (orange). PASS (separator BUG-IPFL-001). |
| IPSYNC-006 | Earlier 'Category/Activity/EFI empty after push#2' not reproduced on push#3 (Solo/Charter/EFI persisted both directions). Probably push#2's update POST partially failed (forms_json die ->… | — | N/A |  | Candidate: one-off empty Category/Activity/EFI after push #2, not reproduced.<br>L100: Earlier 'Category/Activity/EFI empty after push#2' not reproduced on push#3 (Solo/Charter/EFI persisted both directions). Probably push#2's update POST partially failed (forms_json die -> rollback on server). Keep as 'observed once'. |
| IPSYNC-007 | BUG-IPSYNC-001 (Medium): Pull from Server did NOT bring server notes edit ('WEBEDIT'); local notes unchanged. 'Already Downloaded -> Pull from Server (overwrites local changes)' did not o… | No defect (see Bug ID) | FAIL | BUG-IPSYNC-001 | L105: FAIL BUG-IPSYNC-001 (Medium): Pull from Server did NOT bring server notes edit ('WEBEDIT'); local notes unchanged. 'Already Downloaded -> Pull from Server (overwrites local changes)' did not overwrite notes. landingTime format changed '00:07' -> '00:07:00' (server seconds format leaks). |
| IPSYNC-008 | (behavior) Pull = blind overwrite, no diff/merge/conflict UI; Download list shows green 'Downloaded' with no 'server updated' indicator even when server changed (list badge showed synced… | No defect (see Bug ID) | FAIL | BUG-IPSYNC-001 | L106: (behavior) Pull = blind overwrite, no diff/merge/conflict UI; Download list shows green 'Downloaded' with no 'server updated' indicator even when server changed (list badge showed synced #42,914 while notes were stale). |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Flights #42914 and #42915 | BETA test flights used for push/pull checks | No |
