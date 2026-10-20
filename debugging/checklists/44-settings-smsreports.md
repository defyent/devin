# Settings – Safety Reports

- **Checklist ID prefix:** `SSMS`
- **Guide section:** §12.14
- **Where:** Settings and Tools > Safety > Safety Reports
- **Permission:** settings_smsreports = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SSMS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SSMS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SSMS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SSMS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SSMS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SSMS-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SSMS-001 | Report Types Name/Status, reorder | New Report type search follows | TODO | | |
| SSMS-002 | Extra Info Fields (types) | Shown under Extra Safety Report Info | TODO | | |
| SSMS-003 | Permanent Investigators & Reviewers | Auto-assigned to new reports | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
