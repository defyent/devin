# iPad: Comms (chat)

- **Checklist ID prefix:** `IPCOM`
- **Guide section:** `ipad/IPAD_AUDIT_PLAN.md`
- **Where:** Comms tab
- **Frontend cross-reference:** 28-chat
- **Viewport:** P 820x1180 and L 1180x820 unless stated
- **Tester:**  
- **Date / app build / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID. Sync rows: put the frontend record checked in Notes.

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPCOM-001 | Channel list = frontend Chat channels for same user | Match | TODO |  |  |
| IPCOM-002 | Send message: appears on frontend with sender/time | Match | TODO |  |  |
| IPCOM-003 | Message from frontend appears on iPad (polling chat_new_messages_json) | Appears | TODO |  |  |
| IPCOM-004 | Load older messages / scroll position | Works | TODO |  |  |
| IPCOM-005 | Send image; chat_serve_image renders on both sides | Renders | TODO |  |  |
| IPCOM-006 | Delete Message (own / admin) | Per frontend rules | TODO |  |  |
| IPCOM-007 | Create Channel (admin only, chat_is_admin_json) | Admin only | TODO |  |  |
| IPCOM-008 | Special characters / HTML / emoji not executed | Escaped | TODO |  |  |
| IPCOM-009 | 'Chat Not Available' when not configured / offline | Clear | TODO |  |  |

## Test data created

| Record | Where | Cleaned up |
|---|---|---|
