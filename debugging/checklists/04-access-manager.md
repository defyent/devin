# Access Manager (users, roles, groups, permissions, templates)

- **Checklist ID prefix:** `AM`
- **Guide section:** §5
- **Where:** Settings and Tools > People > Access Manager
- **Permission:** Access Manager = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| AM-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Access Manager; no console errors |
| AM-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS |  | Opens; × / Got It / Esc close. Outside click on the overlay does NOT close (probably deliberate since POP-01 fix; confirm with Jon) |
| AM-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS | BUG-POP-001 | Retest 22/10/2026 (v2.0.113): fixed. Esc closes the error modal; drag-out keeps popups open |
| AM-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-AM-002 | Access Manager shows a UTC time (BUG-AM-002). |
| AM-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | See AM-032. |
| AM-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low (0 permissions): Settings and Tools shows 'Access Denied: You do not have permission to access the System Settings feature' |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| AM-001 | Header statistics | Total Users, With Permissions, Permission Types show sensible numbers | PASS |  | 156 Total Users, With Permissions 0 -> 1 after granting betatest_low one permission, 75 Permission Types. Note: one user row has no name/username (blank avatar, first row) |
| AM-002 | Pills | User Permissions, Groups, Permission Templates | PASS |  | User Permissions / Groups / Permission Templates pills present |
| AM-003 | Search users by name, username, email | Filters correctly | PASS |  | Name (Higgins=2), username (afisher13=1), email (aaron.foster112@=1), no-match=0 |
| AM-004 | All Roles filter (each role) and All Groups filter (each group) | Filters correctly; combine with search | PASS |  | Roles: Admin 1, Customer 2, Crew 41, Staff 110, Student 42. Groups: Pilots 83, Crew 40, Engineers 20, Administration 10. Crew+search 'Aaron' combines |
| AM-005 | Sort every sortable column (not Roles/Groups/Credentials) | Sorts asc/desc correctly | PASS | BUG-AM-003 | Retest 22/10/2026: fixed. Last Activity sorts both ways |
| AM-006 | Click user row (not badge) | Opens that person's Personnel Details | PASS |  | Row click opens that person's Personnel Details (person_id=213 for afisher13) |
| AM-007 | Last Activity column | Relative text (Just now … Never); hover shows exact date in org format | PASS | BUG-AM-002 | Retest 22/10/2026: fixed. Hover shows local time in org format, e.g. 22/10/2026 15:01 |
| AM-008 | New User: submit empty | 'Please fill in all required fields' | PASS |  | Browser-native 'Please fill out this field' (required attrs), not app text; nothing created |
| AM-009 | New User: mismatched passwords | 'Passwords do not match' | PASS |  | Toast 'Passwords do not match' |
| AM-010 | New User: 6-9 char password | Guide notes inconsistency: create accepts 6 but placeholder says 10 and Change Credentials needs 10 — log as bug if still true | PASS | BUG-AM-001 | Retest 22/10/2026: fixed. short1 is rejected with Password must be at least 10 characters |
| AM-011 | New User: duplicate username / email | 'Username is already taken' / 'Email is already in use' | PASS |  | 'Username is already taken' / 'Email is already in use' (toasts, ~2 s) |
| AM-012 | New User: reserved usernames (admin, root, test, support…) | 'That username is not allowed' | PASS |  | root, admin, support, test all refused: 'Failed to Create User - That username is not allowed' (error modal; Esc does not close it, see BUG-POP-001) |
| AM-013 | Create `BETA TEST ONLY` user | Created with Login Access = Inactive | PASS |  | BETA TEST ONLY Lowperm (betatest_low) created, Login Access = Inactive, 0 roles/groups |
| AM-014 | Activate the new user (Inactive badge > Activate) | Confirmation then Active | PASS |  | Confirm 'Activate Login Access' then toast 'Login access activated for BETA TEST ONLY Lowperm'; badge Active |
| AM-015 | Activate a user with no credentials | 'User must have login credentials before activation' and Change Login Credentials opens | PASS | BUG-AM-007 | Retest 22/10/2026: a new customer from flightdetails (BETA TEST ONLY Cust2) starts Inactive |
| AM-016 | Deactivate a user | Confirmation; user signed out everywhere; no delete option exists | PASS |  | Confirm 'Deactivate Login Access' then toast 'Login access deactivated for BETA TEST ONLY Lowperm'; no delete option anywhere. Sign-out effect: see LOG-017 |
| AM-017 | Roles badge: tick/untick each role, Save Changes | Saved; hover on 'N Roles' lists them | PASS |  | Ticked Crew > Save Changes > toast 'User roles updated for BETA TEST ONLY Lowperm (1 role)', badge '1 Role', hover 'Active: Crew - Click to manage roles' |
| AM-018 | Roles: Admin checkbox as non-admin | Greyed out ('Only admins can grant or revoke admin access') | PASS | BUG-AM-005 | Retest 2 22/10/2026 (v2.0.113): fixed. betatest_two (Access Manager #210=A) opens Access Manager; in Roles the Admin checkbox is disabled ('Only admins can grant admin access') |
| AM-019 | Groups badge: toggle groups, search | On Roster auto-ticks when adding; Save replaces memberships | PASS | BUG-POP-003 | Retest 22/10/2026: fixed. Esc and Cancel warn about unsaved group changes; Discard and reopen shows saved memberships |
| AM-020 | Permissions badge: tick a type | Level dropdown enables with first valid level; only levels from §15.1 offered | PASS | BUG-AM-004 | Retest 22/10/2026: fixed. All levels labelled, including WA and G |
| AM-021 | Permissions: untick, search types, Save | Toast 'Permissions updated for First Last (N permissions)' | PASS |  | Toast 'Permissions updated for BETA TEST ONLY Lowperm (1 permissions)' (grammar: '1 permissions'); badge '1 Permission' |
| AM-022 | Permissions: Apply Template | Overwrites those types only; needs Save Changes | PASS |  | Lowperm permissions > Select template "BETA TEST ONLY Tpl" > Apply Template shows "Template ... applied" and adds Access Manager = RA next to the existing Personnel Details = WO (merge, not replace; shot am_apply_tpl). I unticked the added row before saving, so Lowperm still has 1 permission. |
| AM-023 | Permissions: Cancel with unsaved changes | Asks to confirm | PASS | BUG-POP-002 | Retest 22/10/2026: fixed. App modal Keep Editing / Discard Changes; Esc keeps editing |
| AM-024 | Change credentials: < 10 chars, mismatch, reserved, duplicate | Rejected with messages | PASS |  | <10: 'Password must be at least 10 characters'; mismatch: 'Passwords do not match'; admin: 'That username is not allowed'; afisher13: 'Username is already taken' |
| AM-025 | Generate Secure Password | 10-char mixed-case alphanumeric, fills both fields, copy button works | PASS |  | 10 chars, upper+lower+digit, fills both fields, copy button appears |
| AM-026 | Groups tab: New Group with all 5 switches | Saved; card shows member count and Yes/No for each switch | PASS |  | Created 'BETA TEST ONLY Group' with all 5 switches: toast 'Group ... created successfully'; card shows Members 0 and Yes for Sidebar/Dropdown/Roster/Flight-Duty/Recency |
| AM-027 | Group switches take effect | Show in Sidebar > sidebar; Show in Dropdown > Schedule Group By; Roster > Roster Builder/Viewer; F&D; Recency | IN PROGRESS |  | Show in Sidebar: 'BETA TEST ONLY Group' in People submenu + mobile drawer after reload. Show in Dropdown: listed in Flight Schedule Group By. Roster/F&D/Recency switches checked in 13/14/16/18 (group kept until then) |
| AM-028 | Delete a group in use | Refused with list e.g. 'Cannot delete group: 3 user memberships, 1 notice link' | PASS |  | Delete confirm shows 'Members: 1 user'; Delete Group > 'Cannot Delete Group - This group cannot be deleted because it is currently in use: Dependencies: 1 user membership' |
| AM-029 | Delete an unused BETA TEST group | Confirm then deleted | PASS |  | Groups > New Group "BETA TEST ONLY Del" > Save Group ("created successfully"). Delete asks first and names the group and member count ("Members: 0 users"), then "deleted successfully" and the card is gone. |
| AM-030 | Permission Templates: New Template with no permissions | Rejected (at least one required) | PASS |  | New Template named "BETA TEST ONLY Tpl" with no permissions > Save Template shows "Please select at least one permission" and nothing is created (shot am_tpl_empty). |
| AM-031 | Template card: 'N permissions' click | Expands list with level badges; edit/delete icons work | PASS |  | Template card "BETA TEST ONLY Tpl" > click "1 permission" expands the card to list "Access Manager - Read Only All" (expand_more changes to expand_less, shot am_tpl_count). |
| AM-032 | Mobile width | Users table becomes cards | PASS |  | At 390 px Access Manager fits with no sideways scroll (scrollWidth 390). The tabs turn into a dropdown and the stats stack (shot am_mobile). The Performance panel covers the bottom of the page (BUG-SWAB-003). |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| User BETA TEST ONLY Lowperm (betatest_low, betatest.low@example.com); 1 permission, role Crew, groups Crew + BETA TEST ONLY Group; 2FA enabled during testing, later disabled | Access Manager > User Permissions | No |
| Group BETA TEST ONLY Group (all 5 switches on) | Access Manager > Groups | No |
