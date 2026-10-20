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

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
