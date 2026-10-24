# iPad: Security and data handling

- **Checklist ID prefix:** `IPSEC`
- **Guide section:** `ipad/IPAD_AUDIT_PLAN.md`
- **Where:** whole app
- **Frontend cross-reference:** 01-login-auth, 96-xc-attachments
- **Viewport:** P 820x1180 and L 1180x820 unless stated
- **Tester:**  
- **Date / app build / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID. Sync rows: put the frontend record checked in Notes.

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPSEC-001 | DataHangar password storage | Not stored in plain text in web storage | FAIL | BUG-IPSEC-001 | datahangarPassword and datahangarPassword_backup in localStorage, plain JSON string |
| IPSEC-002 | Session cookie handling (credentials: include), logout / Clear All Data removes session | Cleared | TODO |  |  |
| IPSEC-003 | API Debug Log masks password and session tokens | Masked | TODO |  |  |
| IPSEC-004 | Exported configuration contains no credentials | None | TODO |  |  |
| IPSEC-005 | flightdetails_json payload: only data the user may see (contacts, personnel lists) | Minimal | TODO |  |  |
| IPSEC-006 | Server rejects iPad POSTs that the user's permission level forbids | Rejected | TODO |  |  |
| IPSEC-007 | XSS: names/notes/chat with <script> rendered as text | Escaped | TODO |  |  |
| IPSEC-008 | Configuration PIN cannot be bypassed (reload, back) | Enforced | TODO |  |  |

## Test data created

| Record | Where | Cleaned up |
|---|---|---|
