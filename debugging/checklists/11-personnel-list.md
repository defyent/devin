# All Personnel (Personnel List)

- **Checklist ID prefix:** `PL`
- **Guide section:** §9.1
- **Where:** Personnel > All Personnel / group entries
- **Permission:** Personnel List A/RA/WG/RG/WO/RO
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| PL-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Sidebar > Personnel > All Personnel loads (action=personnellist), no console errors (shot pl_open) |
| PL-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-PL-001 | No Help (?) on the page |
| PL-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | All Personnel itself opens no popups (clicking a row opens Personnel Details). Popups in Personnel Details are covered in checklist 12 |
| PL-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | PASS |  | The list shows no dates or times; nothing to check |
| PL-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | 390 px: rows become cards (avatar, name, email, phone), search + group/role filters stay visible, page fits (385 <= 390) (shot pl_mobile). The role dropdown touches the right edge |
| PL-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low (no Personnel List right): link shown, 'Access Denied: You do not have permission to access the Personnel List.' (shot pl_low) |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| PL-001 | Search, All Groups, All Roles filters | Filter correctly and combine | PASS |  | Search: 'Atkinson' 3, 'paige atk' 1, phone '021-555-0081' 1, 'zzzq' 0. Group Engineers 20 (all Engineers); Engineers+Student 0; Pilots+Student all match; Pilots+Student+'Barnes' -> Ryan Barnes only. Filters combine (shot pl_filter). Scrolling loads 30 more (30 > 60) |
| PL-002 | Group sidebar entries (Administration, Crew, Engineers, Pilots) | Pre-filtered to that group | PASS |  | Sidebar group entries open All Personnel pre-filtered (usergroup_id, Group dropdown set): Administration 10, BETA TEST ONLY Group 1, Crew 30+, Engineers 20, Pilots 30+; every row in that group (shot pl_group_pilots) |
| PL-003 | Click person | Opens Personnel Details | PASS |  | Clicking a row opens Personnel Details for that person (person_id=274) |
| PL-004 | No create button | People created only in Access Manager | PASS |  | No create/add button on the page (only search + group/role filters); people are created in Access Manager |
| PL-005 | WG/RG/WO/RO accounts | See only group members / self | PASS | pl005_grp | Grpuser (Personnel List = RG) sees only the 3 BETA TEST ONLY Group members (Grpuser, Lowperm, Second). BETA TEST ONLY Second has no Personnel List permission and gets no list. WG/WO/RO levels aren't offered for this card. |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`STATUS.md`](../STATUS.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| UX-10 | Low | Open (external) | Personnel menu has an "Administration" group, the same name as the main section |
| DATA-02 | Low | Open (external) | Person with a blank name in All Personnel / Access Manager |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Pre-existing, not created in this run: person #274 with no name (Customer), found in PL-001 (BUG-PL-002) | All Personnel | No (check with Jon) |
