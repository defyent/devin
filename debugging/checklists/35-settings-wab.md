# Settings – Weight and Balance Configs

- **Checklist ID prefix:** `SWAB`
- **Guide section:** §12.5
- **Where:** Settings and Tools > Configuration > Weight and Balance Configs
- **Permission:** settings_wabconfigs = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SWAB-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SWAB-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SWAB-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SWAB-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SWAB-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SWAB-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SWAB-001 | Active Master card: View / Export | Works | TODO | | |
| SWAB-002 | Revision History filter; Review, Export, Delete, Set as Master | Works | TODO | | |
| SWAB-003 | Import config file; New Draft | Works | TODO | | |
| SWAB-004 | Per-aircraft editor sections (General … Envelope Graphs) | Each saves | TODO | | |
| SWAB-005 | Copy W&B To Aircraft | Copied | TODO | | |
| SWAB-006 | Approved revision read-only; Create Draft Revision | Correct | TODO | | |
| SWAB-007 | Publish > Approve/Reject > Set as Master | Flight Details W&B toggle follows Master | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
