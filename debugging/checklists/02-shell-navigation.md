# Application shell, sidebar, header, mobile

- **Checklist ID prefix:** `NAV`
- **Guide section:** §3
- **Where:** Every page
- **Permission:** n/a
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| NAV-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | All 21 sidebar items open with no console errors |
| NAV-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | N/A |  | Shell has no help button |
| NAV-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Logout confirm survives drag-out |
| NAV-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | PASS |  | Clocks use DD/MM/YYYY HH:mm |
| NAV-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | 700 px: drawer + card list work; see NAV-018 |
| NAV-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: sidebar renders, links to modules without permission open an Access Denied card (see NAV-019, AM-S06, PERM-007) |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| NAV-001 | Logo + org name + version in top bar; click logo | Goes to landing page (Dashboard by default) | PASS |  | Logo returns to Dashboard |
| NAV-002 | UTC and Local clocks | Correct times; use Settings > Time Zone date/time formats; change format and confirm clocks follow | PASS |  | UTC 07:37 / Local 20:37 NZDT correct; format follow-through checked in 33-settings-timezone |
| NAV-003 | My Account button | Shows your name (and photo if set); opens own Personnel Details | PASS |  | Opens own Personnel Details (no photo set) |
| NAV-004 | Chat icon badge | Unread count; only shown with Chat permission; '99+' above 99 | PASS |  | No unread chat, no badge |
| NAV-005 | Notices bell badge | Unread notices for your groups; only with Notices permission; '99+' above 99 | PASS |  | 99+ |
| NAV-006 | Support headset badge | Tickets with unread replies (admins: also new tickets) | PASS |  | No badge (no unread tickets) |
| NAV-007 | Sidebar menu button expand/collapse; reload | State remembered (cookie); new users start collapsed | PASS |  | sidebar_state=open cookie, kept after reload |
| NAV-008 | Collapsed sidebar: hover each section icon | Pop-out submenu appears and stays usable when moving mouse onto it | PASS |  | Pop-out submenus usable |
| NAV-009 | Expanded sidebar: open one section then another | Opening one closes the others; current page highlighted | PASS |  | One section open at a time; current page highlighted |
| NAV-010 | Sidebar Flight Operations items | Dashboard, Flight Schedule, Active Flights, Daily Flight Record | PASS |  |  |
| NAV-011 | Sidebar Personnel items | Roster Viewer, All Personnel + one entry per group with Show in Sidebar (staging: Administration, Crew, Engineers, Pilots); each opens filtered list | PASS |  | Administration, Crew, Engineers, Pilots open filtered lists |
| NAV-012 | Sidebar Flight Safety items | Flight and Duty, Notices, Recency and Renewals, Safety Reports, Hazard Register | PASS |  |  |
| NAV-013 | Sidebar Administration items | Settings and Tools, File Browser, Form Browser, Task Tracker, Reports, Support | PASS |  |  |
| NAV-014 | Browser Back/Forward between modules | Moves between pages opened inside the shell | PASS |  | Back/Forward move between modules |
| NAV-015 | Edit something, then click another menu item | 'The current page has unsaved changes...' modal; Cancel stays, Continue leaves | FAIL | BUG-NAV-001 | Retest 22/10/2026: still fails. Shell modal works when setDirty(true) is called (Cancel keeps the edit, Continue leaves), but personneldetails never reports dirty, so no prompt and the edit is lost |
| NAV-016 | Overdue alerts: enable setting, be Flight Follower on an open SAR-watched flight past end time | Banner within ~30 s with aircraft, PIC, route, hours overdue; click opens Active Flights; desktop notification when window inactive | PASS | nav016_banner | Overdue Alerts on, Service Account is Flight Follower, and BETA flight #42910 is Open with SAR Watch and planned 08:00-09:00 local (now past). The banner showed within 35 s: "Overdue Flight Alert ZK-BTO - BETA TEST ONLY Second Route: NZWN-NZWN Overdue: 1 hours". Clicking it opens Active Flights. With the window reported as unfocused (document.hasFocus forced false, because the VM browser can't lose focus), the app called new Notification("Overdue Flight Alert", ...) with the same text. Notification permission was granted. |
| NAV-017 | New chat message while Chat closed | Banner 'New message in #channel' with preview; disappears after 8 s; click opens Chat | BLOCKED | chat005_channel | No second user can be given Chat: Access Manager has no Chat permission (BUG-AM-006), and every non-admin gets Access Denied. Same blocker as CHAT-005. |
| NAV-018 | Resize to < 768 px | Burger opens Navigation drawer with sections + badges; tables become cards; pills become dropdown | PASS |  | Burger drawer has all sections + badges; Personnel shows cards |
| NAV-019 | Menu link for a module without permission (use low-permission account) | Link visible; page shows 'Access Denied' | PASS |  | betatest_low (Crew, no Flight Schedule permission): Flight Schedule link shown in the sidebar; opening it shows 'Access Denied: You do not have permission to access the flight schedule' (shot fs_lowperm) |
| NAV-020 | Maintenance Portal reachability | Note: guide says only direct/admin-added link. Record whether any UI path exists (we do NOT use ?action= URLs) | PASS |  | No UI path to Maintenance Portal in sidebar or Settings (only Inspection Notifications) |
| NAV-021 | Icons load | Note: menu icons come from external CDN api.iconify.design (Jon prefers self-hosted icon pack) — log as UI finding | PASS | ICON-01 | Retest 22/10/2026: sidebar icons fixed. 48 sidebar SVGs load from /templates2/main/icons/, 0 broken, 0 requests to api.iconify.design. Material Icons/Symbols Sharp still come from fonts.googleapis.com (see UI-002) |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| UX-03 | Low | Open (external) | Detail page URLs inconsistent (index.pl vs ?action=) |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
