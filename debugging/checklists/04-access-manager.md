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
| AM-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Access Manager; no console errors |
| AM-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS |  | Opens; × / Got It / Esc close. Outside click on the overlay does NOT close (probably deliberate since POP-01 fix; confirm with Jon) |
| AM-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | FAIL | BUG-POP-001 | Drag-out: New User, Help, Change Credentials stay open (OK). Error modal ignores Esc |
| AM-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| AM-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| AM-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low (0 permissions): Settings and Tools shows 'Access Denied: You do not have permission to access the System Settings feature' |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| AM-001 | Header statistics | Total Users, With Permissions, Permission Types show sensible numbers | PASS |  | 156 Total Users, With Permissions 0 -> 1 after granting betatest_low one permission, 75 Permission Types. Note: one user row has no name/username (blank avatar, first row) |
| AM-002 | Pills | User Permissions, Groups, Permission Templates | PASS |  | User Permissions / Groups / Permission Templates pills present |
| AM-003 | Search users by name, username, email | Filters correctly | PASS |  | Name (Higgins=2), username (afisher13=1), email (aaron.foster112@=1), no-match=0 |
| AM-004 | All Roles filter (each role) and All Groups filter (each group) | Filters correctly; combine with search | PASS |  | Roles: Admin 1, Customer 2, Crew 41, Staff 110, Student 42. Groups: Pilots 83, Crew 40, Engineers 20, Administration 10. Crew+search 'Aaron' combines |
| AM-005 | Sort every sortable column (not Roles/Groups/Credentials) | Sorts asc/desc correctly | FAIL | BUG-AM-003 | User and Username sort both ways; Last Activity order unchanged on repeat click |
| AM-006 | Click user row (not badge) | Opens that person's Personnel Details | PASS |  | Row click opens that person's Personnel Details (person_id=213 for afisher13) |
| AM-007 | Last Activity column | Relative text (Just now … Never); hover shows exact date in org format | FAIL | BUG-AM-002 | Relative text OK ('4 mins ago', 'Never'); hover '21 Oct 2026, 07:45 am' not org format and is UTC |
| AM-008 | New User: submit empty | 'Please fill in all required fields' | PASS |  | Browser-native 'Please fill out this field' (required attrs), not app text; nothing created |
| AM-009 | New User: mismatched passwords | 'Passwords do not match' | PASS |  | Toast 'Passwords do not match' |
| AM-010 | New User: 6-9 char password | Guide notes inconsistency: create accepts 6 but placeholder says 10 and Change Credentials needs 10 — log as bug if still true | FAIL | BUG-AM-001 | 6-char password 'short1' accepted; user created |
| AM-011 | New User: duplicate username / email | 'Username is already taken' / 'Email is already in use' | PASS |  | 'Username is already taken' / 'Email is already in use' (toasts, ~2 s) |
| AM-012 | New User: reserved usernames (admin, root, test, support…) | 'That username is not allowed' | PASS |  | root, admin, support, test all refused: 'Failed to Create User - That username is not allowed' (error modal; Esc does not close it, see BUG-POP-001) |
| AM-013 | Create `BETA TEST ONLY` user | Created with Login Access = Inactive | PASS |  | BETA TEST ONLY Lowperm (betatest_low) created, Login Access = Inactive, 0 roles/groups |
| AM-014 | Activate the new user (Inactive badge > Activate) | Confirmation then Active | PASS |  | Confirm 'Activate Login Access' then toast 'Login access activated for BETA TEST ONLY Lowperm'; badge Active |
| AM-015 | Activate a user with no credentials | 'User must have login credentials before activation' and Change Login Credentials opens | TODO | | |
| AM-016 | Deactivate a user | Confirmation; user signed out everywhere; no delete option exists | PASS |  | Confirm 'Deactivate Login Access' then toast 'Login access deactivated for BETA TEST ONLY Lowperm'; no delete option anywhere. Sign-out effect: see LOG-017 |
| AM-017 | Roles badge: tick/untick each role, Save Changes | Saved; hover on 'N Roles' lists them | PASS |  | Ticked Crew > Save Changes > toast 'User roles updated for BETA TEST ONLY Lowperm (1 role)', badge '1 Role', hover 'Active: Crew - Click to manage roles' |
| AM-018 | Roles: Admin checkbox as non-admin | Greyed out ('Only admins can grant or revoke admin access') | TODO | | |
| AM-019 | Groups badge: toggle groups, search | On Roster auto-ticks when adding; Save replaces memberships | FAIL | BUG-POP-003 | Search filters groups; ticking a group auto-ticks On Roster; Save > toast 'User groups updated ... (1 group)'. But Esc on a dirty Groups modal closes with no warning and the unsaved ticks are still shown when reopened |
| AM-020 | Permissions badge: tick a type | Level dropdown enables with first valid level; only levels from §15.1 offered | FAIL | BUG-AM-004 | Tick enables level dropdown with first valid level (RA). Options for Personnel Details: RA, WA, RO, WO, G; 'WA' and 'G' shown as bare codes |
| AM-021 | Permissions: untick, search types, Save | Toast 'Permissions updated for First Last (N permissions)' | PASS |  | Toast 'Permissions updated for BETA TEST ONLY Lowperm (1 permissions)' (grammar: '1 permissions'); badge '1 Permission' |
| AM-022 | Permissions: Apply Template | Overwrites those types only; needs Save Changes | TODO | | |
| AM-023 | Permissions: Cancel with unsaved changes | Asks to confirm | FAIL | BUG-POP-002 | Asks 'You have unsaved changes. Are you sure you want to cancel?' but as a native browser confirm(), not an app modal |
| AM-024 | Change credentials: < 10 chars, mismatch, reserved, duplicate | Rejected with messages | PASS |  | <10: 'Password must be at least 10 characters'; mismatch: 'Passwords do not match'; admin: 'That username is not allowed'; afisher13: 'Username is already taken' |
| AM-025 | Generate Secure Password | 10-char mixed-case alphanumeric, fills both fields, copy button works | PASS |  | 10 chars, upper+lower+digit, fills both fields, copy button appears |
| AM-026 | Groups tab: New Group with all 5 switches | Saved; card shows member count and Yes/No for each switch | PASS |  | Created 'BETA TEST ONLY Group' with all 5 switches: toast 'Group ... created successfully'; card shows Members 0 and Yes for Sidebar/Dropdown/Roster/Flight-Duty/Recency |
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
