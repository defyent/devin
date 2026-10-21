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
| NAV-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| NAV-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| NAV-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| NAV-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| NAV-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| NAV-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| NAV-001 | Logo + org name + version in top bar; click logo | Goes to landing page (Dashboard by default) | TODO | | |
| NAV-002 | UTC and Local clocks | Correct times; use Settings > Time Zone date/time formats; change format and confirm clocks follow | TODO | | |
| NAV-003 | My Account button | Shows your name (and photo if set); opens own Personnel Details | TODO | | |
| NAV-004 | Chat icon badge | Unread count; only shown with Chat permission; '99+' above 99 | TODO | | |
| NAV-005 | Notices bell badge | Unread notices for your groups; only with Notices permission; '99+' above 99 | TODO | | |
| NAV-006 | Support headset badge | Tickets with unread replies (admins: also new tickets) | TODO | | |
| NAV-007 | Sidebar menu button expand/collapse; reload | State remembered (cookie); new users start collapsed | TODO | | |
| NAV-008 | Collapsed sidebar: hover each section icon | Pop-out submenu appears and stays usable when moving mouse onto it | TODO | | |
| NAV-009 | Expanded sidebar: open one section then another | Opening one closes the others; current page highlighted | TODO | | |
| NAV-010 | Sidebar Flight Operations items | Dashboard, Flight Schedule, Active Flights, Daily Flight Record | TODO | | |
| NAV-011 | Sidebar Personnel items | Roster Viewer, All Personnel + one entry per group with Show in Sidebar (staging: Administration, Crew, Engineers, Pilots); each opens filtered list | TODO | | |
| NAV-012 | Sidebar Flight Safety items | Flight and Duty, Notices, Recency and Renewals, Safety Reports, Hazard Register | TODO | | |
| NAV-013 | Sidebar Administration items | Settings and Tools, File Browser, Form Browser, Task Tracker, Reports, Support | TODO | | |
| NAV-014 | Browser Back/Forward between modules | Moves between pages opened inside the shell | TODO | | |
| NAV-015 | Edit something, then click another menu item | 'The current page has unsaved changes...' modal; Cancel stays, Continue leaves | TODO | | |
| NAV-016 | Overdue alerts: enable setting, be Flight Follower on an open SAR-watched flight past end time | Banner within ~30 s with aircraft, PIC, route, hours overdue; click opens Active Flights; desktop notification when window inactive | TODO | | |
| NAV-017 | New chat message while Chat closed | Banner 'New message in #channel' with preview; disappears after 8 s; click opens Chat | TODO | | |
| NAV-018 | Resize to < 768 px | Burger opens Navigation drawer with sections + badges; tables become cards; pills become dropdown | TODO | | |
| NAV-019 | Menu link for a module without permission (use low-permission account) | Link visible; page shows 'Access Denied' | TODO | | |
| NAV-020 | Maintenance Portal reachability | Note: guide says only direct/admin-added link. Record whether any UI path exists (we do NOT use ?action= URLs) | TODO | | |
| NAV-021 | Icons load | Note: menu icons come from external CDN api.iconify.design (Jon prefers self-hosted icon pack) — log as UI finding | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| UX-03 | Low | Open (external) | Detail page URLs inconsistent (index.pl vs ?action=) |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
