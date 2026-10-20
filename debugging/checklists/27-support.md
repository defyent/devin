# Support tickets

- **Checklist ID prefix:** `SUP`
- **Guide section:** §11.7
- **Where:** Administration > Support / headset icon
- **Permission:** Support = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SUP-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SUP-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SUP-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SUP-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SUP-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SUP-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SUP-001 | Search by number, subject, person, priority, status, date | Works | TODO | | |
| SUP-002 | New Ticket each type; Bug Report extra fields | Fields shown for bug | TODO | | |
| SUP-003 | Attachments browse + paste screenshot (button and Ctrl+V) | Attached | TODO | | |
| SUP-004 | Submit BETA TEST ONLY ticket | Created | TODO | | |
| SUP-005 | View: reply, edit message/subject/description | Works; header badge updates | TODO | | |
| SUP-006 | Status / Priority change | Allowed per access | TODO | | |
| SUP-007 | Delete Ticket | Confirms | TODO | | |
| SUP-008 | Regular user vs admin | Own tickets vs all | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
