# Settings – Fatigue Risk Management

- **Checklist ID prefix:** `SFRMS`
- **Guide section:** §12.10
- **Where:** Settings and Tools > Safety > Fatigue Risk Management Settings
- **Permission:** settings_frms = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SFRMS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SFRMS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SFRMS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SFRMS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SFRMS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SFRMS-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SFRMS-001 | Flight/Duty Time limit rules CRUD with all fields | Saved; validation of Warning/Caution vs Max | TODO | | |
| SFRMS-002 | Rest & Recovery types | Saved | TODO | | |
| SFRMS-003 | Roster rules: Max Consecutive / Max in Period / Shift Sequence | Saved; Roster Builder violations | TODO | | |
| SFRMS-004 | AC119-2 wizard Next/Back through all 5 steps (add vs replace) | Rules imported | TODO | | |
| SFRMS-005 | Results appear in Schedule, Flight Details, F&D page, Roster Builder, Timesheets | Consistent | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
