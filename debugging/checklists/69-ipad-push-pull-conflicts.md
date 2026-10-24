# iPad: Push, pull and conflicts

- **Checklist ID prefix:** `IPPP`
- **Guide section:** `ipad/IPAD_AUDIT_PLAN.md`
- **Where:** Flight header actions
- **Frontend cross-reference:** 07-flight-details
- **Viewport:** P 820x1180 and L 1180x820 unless stated
- **Tester:**  
- **Date / app build / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID. Sync rows: put the frontend record checked in Notes.

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPPP-001 | Edit leg times on iPad > Push to Server > frontend Flight Details shows change | Match | TODO |  |  |
| IPPP-002 | Edit crew/passengers > push > frontend | Match | TODO |  |  |
| IPPP-003 | Edit forms/files > push > frontend | Match | TODO |  |  |
| IPPP-004 | Create new flight on iPad > push > new flight on frontend with id; 'Failed to Create Flight' path | Created once | TODO |  |  |
| IPPP-005 | Edit on frontend > Pull from Server on iPad > values update | Updated | TODO |  |  |
| IPPP-006 | Edit on both sides > push > 'Server Flight Has Changed' prompt (Overwrite / Cancel) | Prompt shown (lastUpdatedAt currently null) | TODO |  |  |
| IPPP-007 | Pull with unsaved local edits: warned before overwrite | Warned | TODO |  |  |
| IPPP-008 | Push twice / double-tap push: no duplicate legs/files | No dupes | TODO |  |  |
| IPPP-009 | Network drop mid-push ('Push Failed'): no partial record, retry works | Atomic | TODO |  |  |
| IPPP-010 | Push as lower-permission user / locked flight (write-lock) | Server rejects, clear message | TODO |  |  |
| IPPP-011 | Flight deleted on frontend after download, then push | Handled | TODO |  |  |
| IPPP-012 | 'Not pushed' indicator for local changes; cleared after push | Accurate | TODO |  |  |
| IPPP-013 | Push result recalculates frontend Flight & Duty / DFR | Recalculated | TODO |  |  |

## Test data created

| Record | Where | Cleaned up |
|---|---|---|
