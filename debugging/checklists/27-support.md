# Support tickets

- **Checklist ID prefix:** `SUP`
- **Guide section:** §11.7
- **Where:** Administration > Support / headset icon
- **Permission:** Support = A
- **Tester:** Devin
- **Date / DataHangar version:** 2026-10-21 / v2.0.111
- **Account / level used:** Service Account (datahangar); betatest_low for S06

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SUP-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Administration > Support loads ('No support tickets found'), no console errors |
| SUP-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-SUP-001 | No Help (?) on Support. New Ticket: Escape does nothing; outside click closes it and the typed ticket is wiped |
| SUP-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | New Support Ticket stays open after mousedown in Subject and release outside |
| SUP-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | PASS |  | List Date Submitted and reply dates show 22/10/2026 (local date, DD/MM/YYYY) |
| SUP-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | At 390px tickets show as cards (#, status pill, subject, submitted by, latest reply, priority, date); no horizontal scroll |
| SUP-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low sees the Support menu link but gets 'Error Access Denied: You do not have permission to access the Support feature' (menu link visibility tracked in BUG-PERM-001) |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SUP-001 | Search by number, subject, person, priority, status, date | Works | PASS |  | Search box finds #8 by '8', subject 'edited', 'Service Account', 'Normal', 'In Progress', '22/10/2026'; 'zzqq' gives no rows |
| SUP-002 | New Ticket each type; Bug Report extra fields | Fields shown for bug | PASS |  | New Ticket types Bug Report, Feature Request, Support Question, General Inquiry. Bug Report adds 'Which DataHangar feature is affected?', expected, actual, steps to reproduce, how often (Every time..Only happened once), Additional Notes; others show Description only |
| SUP-003 | Attachments browse + paste screenshot (button and Ctrl+V) | Attached | FAIL | BUG-SUP-002 | Browse attach works (BETA_TEST_ONLY_sup.txt shown on ticket #8). Ctrl+V paste of an image into New Ticket attaches nothing (no paste handler). Paste Screenshot button needs clipboard permission |
| SUP-004 | Submit BETA TEST ONLY ticket | Created | PASS |  | Submit Ticket created #8 '[Bug Report] BETA TEST ONLY ticket', Service Account, Low, Open, 22/10/2026 (local date, DD/MM/YYYY) |
| SUP-005 | View: reply, edit message/subject/description | Works; header badge updates | FAIL | BUG-SUP-003 | Reply 'BETA TEST ONLY reply' shown (Support Staff, 22/10/2026); title edit (popup) and inline description edit saved and kept after reopen. Clicking the .txt attachment shows an Error popup with the file text. No header badge seen to update |
| SUP-006 | Status / Priority change | Allowed per access | PASS |  | Priority Low > Normal and Status Open > In Progress save immediately and show in the list and on reopen (Service Account) |
| SUP-007 | Delete Ticket | Confirms | PASS |  | Delete asks 'Delete Ticket - This will permanently delete this ticket, all of its replies and all attachments...' (Cancel keeps it; Escape does nothing - BUG-SUP-001). Delete removed #8; list shows 'No support tickets found' |
| SUP-008 | Regular user vs admin | Own tickets vs all | PASS | BUG-SUP-004 | Retest 22/10/2026 (v2.0.113): betatest_grp and betatest_low (Support Tickets #245=WO) each submitted a BETA TEST ONLY ticket (#9, #10) and each sees only their own; betatest_two (#245=A) and Service Account see both (shots re_sup004_list_*) |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Ticket #8 'BETA TEST ONLY ticket' with BETA_TEST_ONLY_sup.txt, reply | Administration > Support | Yes - deleted |
