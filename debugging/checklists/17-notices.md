# Notices

- **Checklist ID prefix:** `NOT`
- **Guide section:** §10.2, §13.6
- **Where:** Flight Safety > Notices / bell icon
- **Permission:** Notices A/RA/WG/RG
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| NOT-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| NOT-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| NOT-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| NOT-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| NOT-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| NOT-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| NOT-001 | List, search | Works | TODO | | |
| NOT-002 | New Notice (A/WG): missing Subject/Text/Groups | Validation | TODO | | |
| NOT-003 | Create BETA TEST ONLY notice with attachment for a group | Sent; members see bell badge + Dashboard Unread Notices | TODO | | |
| NOT-004 | WG user creating notice | Only own groups selectable | TODO | | |
| NOT-005 | Edit notice: change, manage files, add attachment | Works | TODO | | |
| NOT-006 | Notice details: attachments preview | Works | TODO | | |
| NOT-007 | Acknowledge | Clears from bell badge and Dashboard | TODO | | |
| NOT-008 | Comments | Send works | TODO | | |
| NOT-009 | Acknowledgement checklist | Shows who acknowledged | TODO | | |
| NOT-010 | Settings hub 'Notices' card | Staging shows the card with NO links — confirm whether intended | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
