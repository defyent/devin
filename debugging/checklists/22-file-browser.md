# File Browser

- **Checklist ID prefix:** `FB`
- **Guide section:** §11.2
- **Where:** Administration > File Browser
- **Permission:** File Browser = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FB-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| FB-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| FB-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| FB-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| FB-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| FB-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FB-001 | Folder tree, breadcrumbs, Back | Navigate correctly | TODO | | |
| FB-002 | System folders People/Flights/Notices/SMS Reports | Read-only by source; contain files uploaded elsewhere in this run | TODO | | |
| FB-003 | Make Folder (BETA TEST ONLY) | Created | TODO | | |
| FB-004 | Upload File (multiple) | Uploaded | TODO | | |
| FB-005 | Search current folder + sub-folders | Works | TODO | | |
| FB-006 | Preview / download | Works | TODO | | |
| FB-007 | Configure Item: Owner, Read/Write Access groups, Parent Folder move, Update Document | Saved | TODO | | |
| FB-008 | Delete file / folder | Confirms | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
