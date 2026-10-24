# iPad: DataHangar connection and Sync All Data

- **Checklist ID prefix:** `IPSYN`
- **Guide section:** `ipad/IPAD_AUDIT_PLAN.md`
- **Where:** Config > Datahangar
- **Frontend cross-reference:** 01-login-auth
- **Viewport:** P 820x1180 and L 1180x820 unless stated
- **Tester:**  
- **Date / app build / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID. Sync rows: put the frontend record checked in Notes.

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPSYN-001 | Test Authentication with valid credentials | 'Authentication Successful' | PASS |  | 24/10/2026 |
| IPSYN-002 | Sync All Data downloads aircraft, personnel, waypoints, flight types, forms, W&B master | All stores populated, 'Sync Complete' | PASS |  | 21 aircraft, 46 crew, 15 waypoints, 10 activities, 4 categories, forms |
| IPSYN-003 | Wrong password / unknown user | 'Authentication Failed', no data cleared | TODO |  |  |
| IPSYN-004 | Invalid URL, http vs https, trailing slash, other host | 'Invalid URL' / 'Connection Error' | TODO |  |  |
| IPSYN-005 | 2FA-enabled account | Handled (prompt or clear message) | TODO |  |  |
| IPSYN-006 | Inactive / locked account (01-login-auth) | Same generic message as frontend | TODO |  |  |
| IPSYN-007 | Request timeout (throttle network) | 'Request Timeout', retry possible | TODO |  |  |
| IPSYN-008 | Session expires mid-use (log out on frontend) | App re-authenticates or prompts | TODO |  |  |
| IPSYN-009 | Partial failure ('Sync Completed with Errors') lists what failed | Clear list | TODO |  |  |
| IPSYN-010 | Sync twice: no duplicate records in any store | No dupes | TODO |  |  |
| IPSYN-011 | Lower-permission account: what syncs, server rules respected | Matches frontend permissions | TODO |  |  |
| IPSYN-012 | Buttons disabled until URL/user/password entered | Disabled | TODO |  |  |
| IPSYN-013 | Password field: masked, no autofill leak, no reveal | Masked | TODO |  |  |

## Test data created

| Record | Where | Cleaned up |
|---|---|---|
