# iPad DataHangar login and sync

- **Checklist ID prefix:** `IPDH`
- **Guide section:** `debugging/IPAD_SWIFT_AUDIT_PLAN.md` §3
- **Where:** iPad app — URL validation, login good/bad password, Test Connection, Sync All progress/errors, last sync, API debug log
- **Permission:** Admin / Service Account unless a different permission level is identified in the row notes
- **Tester:** Devin
- **Date / DataHangar version:** 24/10/2026 / iPad DataHangar Flight 1.0.13 (46) on iOS 26.5 Simulator; stresstest v2.0.123
- **Account / level used:** Service Account unless a different account is identified in the row notes

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPDH-007 | ENV note: unsigned (CODE_SIGNING_ALLOWED=NO) sim build -> Keychain writes fail silently -> "Error: notConfigured" with fields filled. Rebuilt with ad-hoc sign. App ignores SecItemAdd stat… | TBD (not recorded) | FAIL | BUG-IPDH-001 | L6: ENV note: unsigned (CODE_SIGNING_ALLOWED=NO) sim build -> Keychain writes fail silently -> "Error: notConfigured" with fields filled. Rebuilt with ad-hoc sign. App ignores SecItemAdd status (KeychainStore.setString) -> silent credential loss: BUG-IPDH-001 (Low) candidate. |
| IPDH-001 | Buttons disabled until URL/user/pass filled, but disabled style identical to enabled (PrimaryButtonStyle) -> tap does nothing, no feedback: BUG-IPDH-002 (UI) | TBD (not recorded) | FAIL | BUG-IPDH-002 | L8: Buttons disabled until URL/user/pass filled, but disabled style identical to enabled (PrimaryButtonStyle) -> tap does nothing, no feedback: BUG-IPDH-002 (UI) |
| IPDH-002 | URL auto-prefix https:// on blur: PASS (stresstest.datahangar.net -> https://...) | TBD (not recorded) | PASS |  | L9: URL auto-prefix https:// on blur: PASS (stresstest.datahangar.net -> https://...) |
| IPDH-003 | wrong password -> "Authentication Failed" popup: PASS | TBD (not recorded) | PASS |  | L10: wrong password -> "Authentication Failed" popup: PASS |
| IPDH-004 | debug log redacts password (form_password=***): PASS; failed notConfigured attempt not logged (minor) | TBD (not recorded) | PASS |  | L11: debug log redacts password (form_password=***): PASS; failed notConfigured attempt not logged (minor) |
| IPDH-005 | correct password -> "Authentication Successful": PASS | TBD (not recorded) | PASS |  | L12: correct password -> "Authentication Successful": PASS |
| IPDH-006 | Sync All: completed, Last synced 23 Oct 2026 11:50 PM; counts Aircraft 21, Personnel 44, Waypoints 15, Categories 4, Activities 10, Form Templates 7, Flight CF 0, Leg CF 0, W&B rev 3. Deb… | TBD (not recorded) | PASS |  | L13: Sync All: completed, Last synced 23 Oct 2026 11:50 PM; counts Aircraft 21, Personnel 44, Waypoints 15, Categories 4, Activities 10, Form Templates 7, Flight CF 0, Leg CF 0, W&B rev 3. Debug log sheet auto-opens after every action when debug mode on (by design?) PASS |
| IPDH-010 | DataHangar screen synced counts before re-sync: Aircraft 21, Personnel 44, Waypoints 16, Categories 4, Activities 10, Form Templates 7, Flight Custom Fields 0 (local store has 1 EFI - sti… | TBD (not recorded) | TODO |  | L320: DataHangar screen synced counts before re-sync: Aircraft 21, Personnel 44, Waypoints 16, Categories 4, Activities 10, Form Templates 7, Flight Custom Fields 0 (local store has 1 EFI - still open), Leg Custom Fields 0, W&B rev 3. Last synced 24 Oct 1:52 AM. Running Sync All for IPAC EW test. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
