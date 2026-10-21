# Form Browser / Form Viewer

- **Checklist ID prefix:** `FBR`
- **Guide section:** §11.4
- **Where:** Administration > Form Browser
- **Permission:** Form Browser A/RG
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FBR-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| FBR-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| FBR-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| FBR-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| FBR-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| FBR-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FBR-001 | Folders by source; columns Form Name, Status, Created, Created By, Forms | Correct | TODO | | |
| FBR-002 | Search instances | Works | TODO | | |
| FBR-003 | Open instance | Read-only Form Viewer; sections expand | TODO | | |
| FBR-004 | RG user / confidential forms | Scoped correctly | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| FORM-04 | High | Open (external) | Form Viewer shows no value for Date and Time widgets |
| FORM-08 | Medium | Open (external) | Form Browser dates ignore the date setting ("Oct 17, 2026") |
| FORM-09 | Medium | Open (external) | Form Browser shows incomplete forms as "Submitted"; no Draft/Incomplete status |
| FORM-30 | Low | Open (external) | Viewer is read-only but List Box × buttons still look active |
| FORM-39 | Info | Info | Hidden empty "Error" modal in Form Viewer DOM (opacity 0, not visible) |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
