# Cross-cutting: attachments and file types

- **Checklist ID prefix:** `ATT`
- **Guide section:** §13 (files and attachments)
- **Where:** every attachment area: Flight Details, Personnel Details, Notices, Safety Reports, Support, File Browser, Settings > Waypoints, Chat
- **Permission:** admin (Service Account)
- **Tester:** Devin
- **Date / DataHangar version:** 24/10/2026 / v2.0.123
- **Account / level used:** Service Account (datahangar), admin

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Test files

18 BETA TEST ONLY files: `BETA TEST ONLY résumé #1 (copy).pdf` (spaces, accents, # and brackets), `BETA_TEST_ONLY_scan.pdf`, `_image.png`, `_image.jpg`, `_image.gif`, `_image.webp`, `_image.tiff`, `_photo.heic` (iPhone/iPad photo), `_drawing.svg`, `_document.docx`, `_sheet.xlsx`, `_data.csv`, `_notes.txt`, `_empty.txt` (0 bytes), `_archive.zip`, `_page.html`, `_program.exe` (fake, MZ header only), `_video.mp4`.

For each area: upload all 18, check the list, click each file (preview popup, new tab, alert or nothing), fetch the serve/download URL and compare the bytes with the original, then delete.

## Results

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| ATT-001 | Flight Details #42903 > Files: upload all 18 | All listed with their names | PASS | BUG-ATT-003 | Multi-select works, 18/18 listed. Accented name stored as BETA_TEST_ONLY_rsum_1_copy.pdf |
| ATT-002 | Flight Details: open each type | Preview or Download for every file | FAIL | BUG-FD-012, BUG-FD-013 | png/jpg/gif/webp/svg preview in popup. PDF opens TWO tabs. notes.txt -> "Required Information" alert with the file text; empty.txt -> "File not accessible"; html -> "An unexpected server error occurred". csv/tiff/heic/docx/xlsx/zip/exe/mp4 -> "cannot be previewed" + Download |
| ATT-003 | Flight Details: download | Same bytes as uploaded | PASS |  | 18/18 byte-identical (flightdetails_downloadfile, attachment) |
| ATT-004 | Flight Details: delete | File removed | PASS |  | flightdetails_deletefile Ok for all 18; file URL then says "File not found" |
| ATT-005 | Personnel Details (person 277) > Files: upload all 18 | All listed | PASS | BUG-ATT-003 | 18/18. Random suffix added, accents stripped |
| ATT-006 | Personnel Details: open each type | Preview or Download | FAIL | BUG-PD-012 | Images preview; PDF one tab; notes.txt -> "File Access Error" with the file text; empty.txt/html/others -> "cannot be previewed" |
| ATT-007 | Personnel Details: download | Same bytes | PASS |  | 18/18 byte-identical |
| ATT-008 | Personnel Details: delete | Removed | PASS |  | personneldetails_deletedocument Ok for all 18 |
| ATT-009 | Notices #1189 > Edit: add all 18 | All saved and listed | PASS | BUG-ATT-002 | All 18 saved, names kept exactly (incl. résumé). Accepted .exe/.html/.zip etc. although the label says "Supported formats: PDF, DOC, DOCX, TXT, JPG, JPEG, PNG" |
| ATT-010 | Notices: open each type | Preview or Download | FAIL | BUG-NOT-002 | Images incl. svg preview; PDFs open one tab; notes.txt -> nothing happens; empty.txt/html/others -> "cannot be previewed" + Download |
| ATT-011 | Notices: download | Same bytes | PASS |  | 18/18 byte-identical (noticedetails_servefile) |
| ATT-012 | Notices: several files at once; delete | Multi-select; remove works | FAIL | BUG-NOT-005 | One file per save (18 saves). Removing the 18 files in Edit and saving deleted them ("Document not found"); the 2 older files kept |
| ATT-013 | Safety Report #2060 > Files: upload all 18 | All listed | PASS | BUG-ATT-003 | 18/18, random suffix added |
| ATT-014 | Safety Reports: open each type | Preview or Download | PASS |  | No in-page preview or per-row Download button: clicking opens smsreportdetails_downloaddocument in a new tab; images/svg/pdf show in the tab, others download |
| ATT-015 | Safety Reports: download | Same bytes | PASS |  | 18/18 byte-identical |
| ATT-016 | Safety Reports: delete | Removed, clean message after | FAIL | BUG-SMS-006 | Delete Ok for all 18; the old link then shows the server path |
| ATT-021 | Support: new ticket with all 18 | All attached | PASS |  | Ticket #11, multi-select, names kept exactly |
| ATT-022 | Support: open each type | Preview or Download | FAIL | BUG-SUP-003 | Images shown inline in the thread and preview on click; PDFs one tab; notes.txt -> "Error" popup with the file text; empty.txt/html/others -> "cannot be previewed" + Download |
| ATT-023 | Support: download | Same bytes | PASS |  | 18/18 byte-identical; .html served as octet-stream (safe) |
| ATT-024 | Support: delete | Ticket and files removed | PASS |  | No per-file delete; deleting ticket #11 removed its files ("File not found") |
| ATT-025 | Waypoint ZZZQ > Files: upload all 18 | All listed | PASS | BUG-ATT-003 | 18/18, random suffix added |
| ATT-026 | Waypoints: open each type | Preview or Download | PASS |  | png/jpg/gif/webp preview; PDF previews inside the popup; others (incl. txt, svg) "Preview not available" + Download. Best of all modules |
| ATT-027 | Waypoints: list columns | Org date format, real size | FAIL | BUG-SWP-005 | Uploaded 10/24/2026, Size N/A for all |
| ATT-028 | Waypoints: download, delete | Same bytes; removed | PASS |  | 18/18 byte-identical; delete Ok for all 18 |
| ATT-029 | File Browser > BETA TEST ONLY Folder: upload, open, download, delete | All work | FAIL | BUG-FB-003, BUG-FB-009 | Single-file upload only (19 uploads). Images preview; PDFs one tab; notes.txt "File Access Error" with text; svg error popup with SVG code; others "cannot be previewed". Downloads byte-identical; delete Ok |
| ATT-030 | File Browser shows only its own files | No other modules' files | FAIL | BUG-FB-008 | Home listed the 18 waypoint files (file_513-530) |
| ATT-031 | Chat: send each image type | PNG/JPG/GIF/WebP display | PASS |  | 4 sent, shown inline, served byte-identical (chat_serve_image) |
| ATT-032 | Chat: non-image and unsupported image | Clear message | FAIL | BUG-CHAT-003 | Non-images ignored silently; svg/tiff/heic preview then fail on Send |
| ATT-033 | HTML/SVG uploads are not served as live pages | Download only or sanitised | FAIL | BUG-ATT-001 | FD/PD/WP/Notices serve .html as text/html and .svg as image/svg+xml inline; FB .html inline; SMS .svg inline |
| ATT-034 | File-type policy | Allow-list or documented policy, with message | FAIL | BUG-ATT-002 | Every type accepted everywhere |
| ATT-035 | File names with spaces/accents/symbols | Original name kept and shown | FAIL | BUG-ATT-003 | Only Notices and Support keep it |
| ATT-036 | Zero-byte file | Accepted or refused with a message | PASS |  | Accepted everywhere; download gives 0 bytes |
| ATT-037 | Form Builder image and Personnel photo uploads | Image types handled | N/A |  | Not attachment systems (single image fields); not tested in this run |

Delete for FD, PD, SMS, WP and File Browser was done with the same POST the page's delete button sends (`*_deletefile` / `*_deletedocument`), not by clicking each bin icon. Support (Delete + confirm) and Notices (remove in Edit + Save) were done through the page.

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| 18 files on flight #42903 (ids 459-476) | Flight Details > Files | Yes - deleted |
| 18 files on BETA TEST ONLY Grpuser (person 277, ids 477-494) | Personnel Details > Files | Yes - deleted |
| 18 files on Safety Report #2060 (ids 495-512) | Safety Reports > Files | Yes - deleted |
| 18 files on waypoint ZZZQ (ids 513-530) | Settings > Waypoints > Files | Yes - deleted |
| 19 files in BETA TEST ONLY Folder (ids 531-549) | File Browser | Yes - deleted |
| 18 files on notice #1189 (ids 550-567) | Notices | Yes - deleted (2 older test files kept) |
| Ticket #11 'BETA TEST ONLY file types' with 18 files | Administration > Support | Yes - deleted |
| Channel beta-test-only-files (id 4) with 4 images | Chat | Yes - deleted |
