# Chat

- **Checklist ID prefix:** `CHAT`
- **Guide section:** §11.8
- **Where:** Header chat icon
- **Permission:** Chat = A
- **Tester:** Devin
- **Date / DataHangar version:** 2026-10-21 / v2.0.111
- **Account / level used:** Service Account (datahangar); betatest_low for S06/004/005

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| CHAT-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Header chat icon opens Comms (index.pl?action=chat): 'No channels yet. Create one!', no console errors |
| CHAT-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-CHAT-001 | No Help (?) on Comms. Create Channel: Escape does nothing, outside click closes; empty name does nothing (CHAT-05 still open) |
| CHAT-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Create Channel popup stays open after mousedown in the name box and release outside |
| CHAT-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-CHAT-002 | Message time shows '01:32 AM' (12-hour) instead of HH:mm (CHAT-01 still open) |
| CHAT-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | At 390px the channel opens full-width with the channel list behind the menu button; message box and send usable, no horizontal scroll |
| CHAT-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low sees the header chat icon but gets 'Error Access Denied: You do not have permission to access the Chat feature' (header icon visibility tracked in BUG-PERM-001) |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| CHAT-001 | + channel (BETA TEST ONLY) | Created | PASS |  | + > 'BETA TEST ONLY Channel' > Create: toast 'Channel #BETA TEST ONLY Channel created', listed as #beta-test-only-channel |
| CHAT-002 | Enter sends, Shift+Enter newline | Works | PASS |  | Shift+Enter adds a new line in the box; Enter sends; message shows both lines and the box clears. Web address not turned into a link (CHAT-07 still open) |
| CHAT-003 | Image attach < 10 MB with preview; > 10 MB | Sent / rejected cleanly | PASS |  | File picker accepts image/*. 104 B PNG shows a preview and sends (serve_image link shown in the channel). 11 MB PNG is rejected with 'Images must be less than 10MB.' |
| CHAT-004 | Admin delete message / channel | Confirms; non-admins cannot | PASS |  | As admin: message delete asks 'Are you sure you want to permanently delete this message?' and removes it; channel delete (hover-only button) asks 'permanently delete #beta-test-only-channel? All messages and uploaded files will be deleted' and removes it. Escape doesn't close either confirm (BUG-CHAT-001). Non-admin hiding is in code (isAdmin) but not tried with a non-admin Chat user - retest in 90 |
| CHAT-005 | Badge + banner in another session | Updates within ~20 s | BLOCKED | chat005_channel | Channel "BETA TEST ONLY Chat" was created as admin, but no second user can get into Chat: Access Manager has no Chat permission (BUG-AM-006), and Grpuser gets Access Denied. The unread badge can't be tested. |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| FUNC-01 | n/a | Fixed (retested 17/10) | Chat failed to load. Re-tested 17 Oct: fixed, Chat now loads and works |
| CHAT-01 | Medium | Open (external) | Message times show 12-hour "01:53 PM" although the time format is set to HH:mm |
| CHAT-02 | Low | Open (external) | Delete message uses an × (close) icon but Delete channel uses a trash icon; the two confirm popups use different title icons (delete vs delete_forever) |
| CHAT-03 | Low | Open (external) | Page title is "Comms" but the header button is "Chat" |
| CHAT-04 | Low | Open (external) | Chat uses the wider font and only the old Material Icons font |
| CHAT-05 | Low | Open (external) | Create Channel with an empty name does nothing and shows no message |
| CHAT-06 | Low | Open (external) | Esc and outside click don't close Chat popups, but Esc does close the Login Message popup |
| CHAT-07 | Low | Open (external) | Web addresses in messages aren't turned into links |
| CHAT-08 | Low | Open (external) | Channel list is on the right (lists are on the left elsewhere); delete buttons only appear on hover, so they're hard to find and don't work on touch screens |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Channel 'BETA TEST ONLY Channel' with test messages/images | Chat (header icon) | Yes - channel deleted |
