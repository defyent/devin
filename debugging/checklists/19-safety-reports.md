# Safety Reports (SMS)

- **Checklist ID prefix:** `SMS`
- **Guide section:** §10.4, §13.4
- **Where:** Flight Safety > Safety Reports
- **Permission:** Safety Reports + SMS Investigator/Reviewer
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SMS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SMS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SMS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SMS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SMS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SMS-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SMS-001 | List search; columns ID, Status, Type, Subject, Reporter, Date/Time, Resource, Initial/Final Risk | Works | TODO | | |
| SMS-002 | Click risk badge | Initial Risk Assessment Results | TODO | | |
| SMS-003 | New Report: submit empty | Required fields flagged (Subject, Type, Event Date/Time, Description, Risk Matrix, Likelihood, Consequence) | TODO | | |
| SMS-004 | Help icons on Confidential / Anonymous | Explain fields | TODO | | |
| SMS-005 | Create BETA TEST ONLY report with On Behalf Of, Resource, PIC | Submitted; permanent investigators/reviewers auto-assigned | TODO | | |
| SMS-006 | Risk Level display | Matches matrix cell | TODO | | |
| SMS-007 | Open Investigation (investigator) > Close Investigation > Close Report (reviewer) | Each confirms; progress bar updates | TODO | | |
| SMS-008 | Non-investigator / non-reviewer | Status buttons hidden | TODO | | |
| SMS-009 | Details tab: Extra Safety Report Info save | Saved | TODO | | |
| SMS-010 | Files, Comments, Forms, History tabs | Work | TODO | | |
| SMS-011 | Actions: Create New Action (assign, request) | Appears on assignee Dashboard Safety Actions; completing it records action taken | TODO | | |
| SMS-012 | Final Report: add/remove investigators & reviewers, summary, final risk | Saved | TODO | | |
| SMS-013 | Add to Hazard Register | Hazard appears in Hazard Register | TODO | | |
| SMS-014 | Confidential report as another user | Hidden appropriately | TODO | | |
| SMS-015 | WO / WG / RA accounts | Visibility matches §10.4 rules | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
