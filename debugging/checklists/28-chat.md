# Chat

- **Checklist ID prefix:** `CHAT`
- **Guide section:** §11.8
- **Where:** Header chat icon
- **Permission:** Chat = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| CHAT-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| CHAT-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| CHAT-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| CHAT-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| CHAT-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| CHAT-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| CHAT-001 | + channel (BETA TEST ONLY) | Created | TODO | | |
| CHAT-002 | Enter sends, Shift+Enter newline | Works | TODO | | |
| CHAT-003 | Image attach < 10 MB with preview; > 10 MB | Sent / rejected cleanly | TODO | | |
| CHAT-004 | Admin delete message / channel | Confirms; non-admins cannot | TODO | | |
| CHAT-005 | Badge + banner in another session | Updates within ~20 s | TODO | | |

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
| | | |
