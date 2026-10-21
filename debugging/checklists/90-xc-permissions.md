# Cross-cutting: permission levels

- **Checklist ID prefix:** `PERM`
- **Guide section:** §1.4, §5.4, §14, §15.1
- **Where:** All modules
- **Permission:** Needs one account per level
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| PERM-001 | For each permission type in §15.1, with a level-A account | Full access | TODO | | |
| PERM-002 | Same with RA | View all, no write controls | TODO | | |
| PERM-003 | Same with WG / RG | Only group-shared items; write only for WG | TODO | | |
| PERM-004 | Same with WO / RO | Only own items | TODO | | |
| PERM-005 | Flight Details WL (admin with explicit WL) | Can lock/unlock | TODO | | |
| PERM-006 | Admin with an explicit lower row | Explicit level wins (deliberate) | TODO | | |
| PERM-007 | No permission row | 'Access Denied' — never a blank page or JS error | PASS |  | 0-permission user: all 17 visible menu items show an Access Denied card, no blank page / JS error. But sidebar still lists them (BUG-PERM-001) |
| PERM-008 | Inactive user with permissions | No access at all | PASS |  | Inactive user with 1 permission: login refused with generic message; live session ends on next request |
| PERM-009 | Server-side enforcement: hidden button but action attempted (e.g. Delete key, drag) as read-only | Server rejects with Access Denied popup | TODO | | |
| PERM-010 | Group membership read/write flag caveat (§14) | Check whether Access Manager-saved memberships give WG schedule write | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
