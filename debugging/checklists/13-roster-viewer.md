# Roster Viewer

- **Checklist ID prefix:** `RV`
- **Guide section:** §9.3
- **Where:** Personnel > Roster Viewer
- **Permission:** Roster Viewer A/RG/RO
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| RV-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| RV-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| RV-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| RV-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| RV-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| RV-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| RV-001 | Month grid, < > This Month | Published (live) roster shown | TODO | | |
| RV-002 | Groups shown | Only Show Group in Roster; people only On Roster | TODO | | |
| RV-003 | Search staff… | Filters | TODO | | |
| RV-004 | Click shift | Shift Details | TODO | | |
| RV-005 | Group Visibility > Apply | Hides/shows groups | TODO | | |
| RV-006 | RG / RO | Only own groups / self | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| VIS-20 | Low | Open (external) | Text "< >" arrows used in Roster Viewer, Roster Builder and date picker; "today" vs "Today" |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
