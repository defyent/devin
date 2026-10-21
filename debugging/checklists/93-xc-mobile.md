# Cross-cutting: mobile / narrow layout

- **Checklist ID prefix:** `MOB`
- **Guide section:** §3.3
- **Where:** Every page at < 768 px
- **Permission:** n/a
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| MOB-001 | Navigation drawer and badges | Work | PASS |  | At 390 px the hamburger opens a Navigation drawer with sections, group links and the Notices 99+ badge, and an x to close it (shot mob_drawer). |
| MOB-002 | Tables > cards; pills > dropdown | On every module | FAIL | BUG-SWP-004 | Many tables don't switch to cards and are cut off or overlap on a phone: 15 bugs (BUG-PD-010, BUG-REC-002, BUG-FB-007, BUG-FBR-003, BUG-TT-003, BUG-RPT-003, BUG-EXM-005, BUG-SWAB-004, BUG-SWP-004, BUG-SST-004, BUG-SFRMS-002, BUG-SREN-004, BUG-SRM-002, BUG-RB-006, BUG-FBLD-004). Activity Log and Settings and Tools do switch to cards and dropdown pills. |
| MOB-003 | Flight Schedule list view; tap opens Flight Details | Works | PASS |  | At 390 px Flight Schedule shows the list view with no sideways scroll (scrollWidth 390). Tapping #42903 and its edit icon opens Flight Details (shot mob_fs). |
| MOB-004 | Popups, pickers, forms usable | No overflow / clipped buttons | FAIL | BUG-FBLD-004 | Popups fit on a phone. Some forms don't: the Form Builder Toolbox covers the form (BUG-FBLD-004), and the Roster Builder palette takes half the screen (BUG-RB-006). |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
