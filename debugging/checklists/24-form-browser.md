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
| FBR-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Administration > Form Browser loads (Home: Flights 13, People 8, SMS Reports 1), no page errors |
| FBR-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-FBR-001 | No Help (?) button on the page |
| FBR-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | No popups on the Form Browser page itself; Form Viewer opens in the same frame, not a popup |
| FBR-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-FBR-002 | Created shows 'Oct 21, 2026', not DD/MM/YYYY (FORM-08) |
| FBR-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | FAIL | BUG-FBR-003 | At 390px the table scrolls sideways; Created/Created By off-screen, no card view |
| FBR-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low still sees the menu link; the page shows 'Access Denied: You do not have permission to access the Form Browser' |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FBR-001 | Folders by source; columns Form Name, Status, Created, Created By, Forms | Correct | PASS |  | Home folders by source (Flights 13, People 8, SMS Reports 1) > year > month > 'Flight 42903 - 2026-10-21'; instance list has Form Name, Status, Created, Created By (folder levels show Form Name, Forms). QA Post-Flight Report #194 shows 'Submitted' though its required fields are empty (FORM-09) |
| FBR-002 | Search instances | Works | PASS |  | Search 'QA Post' from Home lists every QA Post-Flight Report with its folder path (Flight 42903, 42902, 42901, 42900, 8795) |
| FBR-003 | Open instance | Read-only Form Viewer; sections expand | PASS |  | Clicking QA Post-Flight Report #194 opens Form Viewer (read-only, 0 editable inputs); the section collapses and expands with the chevron; Back returns to Form Browser. Header date 'Oct 21, 2026 10:24 PM' (BUG-FBR-002); '0 / 11 fields' but status Submitted (FORM-09) |
| FBR-004 | RG user / confidential forms | Scoped correctly | PASS | fbr004_rg | Grpuser (Form Browser RG, BETA TEST ONLY Group) sees Flights 3 (the forms on the group's ZK-BTO flights), People 0 and SMS Reports 0. The admin sees Flights 13, People 8 and SMS Reports 1, so forms outside the group, including the SMS form, are hidden. There was no confidential form from another user to check. |

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
