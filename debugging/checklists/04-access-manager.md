# Access Manager (users, roles, groups, permissions, templates)

- **Checklist ID prefix:** `AM`
- **Guide section:** §5
- **Where:** Settings and Tools > People > Access Manager
- **Permission:** Access Manager = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| AM-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| AM-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| AM-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| AM-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| AM-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| AM-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| AM-001 | Header statistics | Total Users, With Permissions, Permission Types show sensible numbers | TODO | | |
| AM-002 | Pills | User Permissions, Groups, Permission Templates | TODO | | |
| AM-003 | Search users by name, username, email | Filters correctly | TODO | | |
| AM-004 | All Roles filter (each role) and All Groups filter (each group) | Filters correctly; combine with search | TODO | | |
| AM-005 | Sort every sortable column (not Roles/Groups/Credentials) | Sorts asc/desc correctly | TODO | | |
| AM-006 | Click user row (not badge) | Opens that person's Personnel Details | TODO | | |
| AM-007 | Last Activity column | Relative text (Just now … Never); hover shows exact date in org format | TODO | | |
| AM-008 | New User: submit empty | 'Please fill in all required fields' | TODO | | |
| AM-009 | New User: mismatched passwords | 'Passwords do not match' | TODO | | |
| AM-010 | New User: 6-9 char password | Guide notes inconsistency: create accepts 6 but placeholder says 10 and Change Credentials needs 10 — log as bug if still true | TODO | | |
| AM-011 | New User: duplicate username / email | 'Username is already taken' / 'Email is already in use' | TODO | | |
| AM-012 | New User: reserved usernames (admin, root, test, support…) | 'That username is not allowed' | TODO | | |
| AM-013 | Create `BETA TEST ONLY` user | Created with Login Access = Inactive | TODO | | |
| AM-014 | Activate the new user (Inactive badge > Activate) | Confirmation then Active | TODO | | |
| AM-015 | Activate a user with no credentials | 'User must have login credentials before activation' and Change Login Credentials opens | TODO | | |
| AM-016 | Deactivate a user | Confirmation; user signed out everywhere; no delete option exists | TODO | | |
| AM-017 | Roles badge: tick/untick each role, Save Changes | Saved; hover on 'N Roles' lists them | TODO | | |
| AM-018 | Roles: Admin checkbox as non-admin | Greyed out ('Only admins can grant or revoke admin access') | TODO | | |
| AM-019 | Groups badge: toggle groups, search | On Roster auto-ticks when adding; Save replaces memberships | TODO | | |
| AM-020 | Permissions badge: tick a type | Level dropdown enables with first valid level; only levels from §15.1 offered | TODO | | |
| AM-021 | Permissions: untick, search types, Save | Toast 'Permissions updated for First Last (N permissions)' | TODO | | |
| AM-022 | Permissions: Apply Template | Overwrites those types only; needs Save Changes | TODO | | |
| AM-023 | Permissions: Cancel with unsaved changes | Asks to confirm | TODO | | |
| AM-024 | Change credentials: < 10 chars, mismatch, reserved, duplicate | Rejected with messages | TODO | | |
| AM-025 | Generate Secure Password | 10-char mixed-case alphanumeric, fills both fields, copy button works | TODO | | |
| AM-026 | Groups tab: New Group with all 5 switches | Saved; card shows member count and Yes/No for each switch | TODO | | |
| AM-027 | Group switches take effect | Show in Sidebar > sidebar; Show in Dropdown > Schedule Group By; Roster > Roster Builder/Viewer; F&D; Recency | TODO | | |
| AM-028 | Delete a group in use | Refused with list e.g. 'Cannot delete group: 3 user memberships, 1 notice link' | TODO | | |
| AM-029 | Delete an unused BETA TEST group | Confirm then deleted | TODO | | |
| AM-030 | Permission Templates: New Template with no permissions | Rejected (at least one required) | TODO | | |
| AM-031 | Template card: 'N permissions' click | Expands list with level badges; edit/delete icons work | TODO | | |
| AM-032 | Mobile width | Users table becomes cards | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
