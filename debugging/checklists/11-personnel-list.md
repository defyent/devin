# All Personnel (Personnel List)

- **Checklist ID prefix:** `PL`
- **Guide section:** §9.1
- **Where:** Personnel > All Personnel / group entries
- **Permission:** Personnel List A/RA/WG/RG/WO/RO
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| PL-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| PL-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| PL-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| PL-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| PL-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| PL-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| PL-001 | Search, All Groups, All Roles filters | Filter correctly and combine | TODO | | |
| PL-002 | Group sidebar entries (Administration, Crew, Engineers, Pilots) | Pre-filtered to that group | TODO | | |
| PL-003 | Click person | Opens Personnel Details | TODO | | |
| PL-004 | No create button | People created only in Access Manager | TODO | | |
| PL-005 | WG/RG/WO/RO accounts | See only group members / self | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| UX-10 | Low | Open (external) | Personnel menu has an "Administration" group, the same name as the main section |
| DATA-02 | Low | Open (external) | Person with a blank name in All Personnel / Access Manager |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
