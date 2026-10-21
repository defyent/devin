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
| FB-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Administration > File Browser loads (Home with system folders Flights, Notices, People, SMS Reports), no page errors |
| FB-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-FB-001 | No Help (?) button on the page |
| FB-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS | BUG-FB-004 | Drag-out keeps Create New Folder open. Escape does not close it (BUG-FB-004) |
| FB-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-FB-002 | Date Uploaded shows 'Oct 22, 2026', not DD/MM/YYYY |
| FB-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | FAIL | BUG-FB-007 | At 390px the table is 585px wide and scrolls sideways; edit buttons off-screen, no card view |
| FB-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low still sees the menu link; the page shows 'Access Denied: You do not have permission to access the File Browser' |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FB-001 | Folder tree, breadcrumbs, Back | Navigate correctly | PASS |  | Home > SMS Reports > 2026 > October: folders open, breadcrumb shows 'Home / SMS Reports', Back returns to Home and is disabled at Home |
| FB-002 | System folders People/Flights/Notices/SMS Reports | Read-only by source; contain files uploaded elsewhere in this run | PASS |  | System folders Flights, Notices, People, SMS Reports have no Make Folder/Upload buttons and hold files uploaded elsewhere in this run (SMS Reports/2026/October/SMS Report 2060/BETA_TEST_ONLY_notice-GCKLCWJK.txt, the notice #1189 files, the flight #42903 file) |
| FB-003 | Make Folder (BETA TEST ONLY) | Created | PASS |  | Make Folder 'BETA TEST ONLY Folder' at Home: 'Folder created successfully!', listed under Uploaded Files |
| FB-004 | Upload File (multiple) | Uploaded | PASS |  | Upload Files with 2 files selected ('2 files selected') puts BETA_TEST_ONLY_fbA.txt and BETA_TEST_ONLY_fbB.txt in the folder |
| FB-005 | Search current folder + sub-folders | Works | PASS |  | Search 'BETA_TEST_ONLY' from Home finds all 4 test files across sub-folders, with their folder |
| FB-006 | Preview / download | Works | FAIL | BUG-FB-003 | Clicking a .txt file shows 'File Access Error' with the file's text; no preview or download |
| FB-007 | Configure Item: Owner, Read/Write Access groups, Parent Folder move, Update Document | Saved | FAIL | BUG-FB-005 | Owner list only has Service Account. Parent Folder move to Root saves. Read Access 'BETA TEST ONLY Group' is sent but shows unticked when reopened |
| FB-008 | Delete file / folder | Confirms | FAIL | BUG-FB-006 | Delete File asks 'Are you sure...' and deletes (fbA, fbB gone). Delete Folder fails: 'Invalid Action: filebrowser_deletefolder' |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| VIS-22 | Low | Open (external) | Files Upload button uses a sync-style icon; dark navy buttons differ from app blue |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Folder 'BETA TEST ONLY Folder' (files fbA, fbB deleted) | Administration > File Browser > Home | No - folder can't be deleted (BUG-FB-006) |
