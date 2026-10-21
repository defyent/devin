# Hazard Register

- **Checklist ID prefix:** `HAZ`
- **Guide section:** §10.5
- **Where:** Flight Safety > Hazard Register
- **Permission:** Hazard Register A/RG
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| HAZ-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| HAZ-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| HAZ-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| HAZ-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| HAZ-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| HAZ-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| HAZ-001 | List columns ID, Type, Subject, Date/Time, Goal, Risk; search | Works | TODO | | |
| HAZ-002 | Create New Hazard entry | Also creates underlying safety report | TODO | | |
| HAZ-003 | Details tabs: Hazard Details, Original SMS Report, Risk Assessment | Correct data | TODO | | |
| HAZ-004 | Edit hazard fields (Type, Goal, Controls, Review Date, Responsible) | Saved | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| DATE-09 | Low | Open (external) | Hazard Register date has no leading zero ("8 Jan 2026") |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
