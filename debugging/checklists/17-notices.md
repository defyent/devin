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
| NOT-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Flight Safety > Notices loads (30 notices), no console errors |
| NOT-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-NOT-001 | No Help (?); Create New Notice ignores Escape |
| NOT-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Create New Notice stays open after mousedown in Subject / release outside |
| NOT-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | PASS |  | List, details, Posted on and comment dates all DD/MM/YYYY (22/10/2026, local date) |
| NOT-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | At 390px the list shows as cards, document width 375px, no tables overflowing |
| NOT-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: 'Access Denied: You do not have permission to access Notices' |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| NOT-001 | List, search | Works | PASS |  | List shows My Status, ID, Title, Files, Acknowledged, Date (DD/MM/YYYY); search 'Fuel' filters to matching titles |
| NOT-002 | New Notice (A/WG): missing Subject/Text/Groups | Validation | PASS |  | Empty Subject/Notice Text blocked by required fields ('Please fill out this field.'); no group gives 'Validation Error: Please select at least one group for this notice.' and keeps the typed text |
| NOT-003 | Create BETA TEST ONLY notice with attachment for a group | Sent; members see bell badge + Dashboard Unread Notices | BLOCKED |  | Created notice #1189 'BETA TEST ONLY Notice' with attachment for BETA TEST ONLY Group: list shows it at the top (attach_file 1, 0 / 1 acknowledged, 22/10/2026), but no toast. The only member, betatest_low, has no Notices or Dashboard permission (Access Denied) and shows no bell badge, so the member view can't be checked. Retest in 90 |
| NOT-004 | WG user creating notice | Only own groups selectable | BLOCKED |  | Needs a WG-level Notices user. Retest in 90 |
| NOT-005 | Edit notice: change, manage files, add attachment | Works | PASS |  | Edit #1189: subject changed to 'BETA TEST ONLY Notice edited', existing file listed with delete, second .txt added (attach_file 2). Note: saving the edit resets acknowledgements (1 / 1 back to 0 / 1, My Status unchecked) - confirm this is intended |
| NOT-006 | Notice details: attachments preview | Works | FAIL | BUG-NOT-002 | Details show Notice ID, Date Posted, Posted By, Groups, Attached Files, content; clicking the .txt attachment shows nothing |
| NOT-007 | Acknowledge | Clears from bell badge and Dashboard | PASS |  | Acknowledge shows 'Notice acknowledged!' and the Acknowledge button disappears. Service Account bell is 99+ so the badge change can't be seen; member view retest in 90 |
| NOT-008 | Comments | Send works | PASS |  | Posted 'BETA TEST ONLY comment': 'Comment posted successfully!', Comments (1) with name and date |
| NOT-009 | Acknowledgement checklist | Shows who acknowledged | PASS |  | Acknowledgements 0 / 1 lists the group and BETA TEST ONLY Lowperm (unchecked) |
| NOT-010 | Settings hub 'Notices' card | Staging shows the card with NO links — confirm whether intended | FAIL | BUG-NOT-003 | Card 'Notices - Manage system-wide notices and announcements.' shows with no links (confirmed). Logged as Low until you confirm it's intended |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Notice #1189 'BETA TEST ONLY Notice edited' (BETA TEST ONLY Group, 2 .txt attachments, 1 comment) | Flight Safety > Notices | No - the app has no delete for notices |
