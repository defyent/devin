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
| SMS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Flight Safety > Safety Reports loads (274 total, 66 open, 147 closed, 0 high risk), no console errors |
| SMS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS |  | Help opens; closes with Got It, x, outside click and Esc |
| SMS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag-out keeps Help, Create New Safety Report and Initial Risk Assessment Results open |
| SMS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-SMS-002 | List Date/Time is DD/MM/YYYY HH:MM (28/12/2026 14:11), but New Report's Event Date/Time defaults to UTC (21/10/2026 11:37 while local was 22/10/2026 00:37) |
| SMS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | At 390px the list shows as cards (Status, Type, Reporter, Date/Time, Resource, risks); New Report fits the width (356px), document width 390px |
| SMS-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: 'Access Denied: You do not have permission to access SMS Reports' |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SMS-001 | List search; columns ID, Status, Type, Subject, Reporter, Date/Time, Resource, Initial/Final Risk | Works | PASS |  | Columns ID, Status, Type, Subject, Reporter, Date/Time, Resource, Initial Risk, Final Risk; search 'Landing light' filters, clear restores the list |
| SMS-002 | Click risk badge | Initial Risk Assessment Results | PASS |  | Clicking the Initial Risk badge opens Initial Risk Assessment Results (report 274: Likelihood Possible, Consequence Insignificant, Low) |
| SMS-003 | New Report: submit empty | Required fields flagged (Subject, Type, Event Date/Time, Description, Risk Matrix, Likelihood, Consequence) | PASS |  | Create Report with nothing filled gives 'Subject is required'; with Subject only, 'Report Type is required'. Typed text is kept. Note: errors come one at a time in a popup and the fields themselves aren't highlighted |
| SMS-004 | Help icons on Confidential / Anonymous | Explain fields | PASS | BUG-SMS-001 | Confidential and Anonymous (?) explain who can see the report and that the reporter shows as 'Anonymous'. But Escape on these help popups closes the report form behind them and loses the typed Subject (BUG-SMS-001) |
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

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| FORM-02 | High | Open (external) | Safety Report form edits are lost: Save Changes never enables, values gone after reopening |
| FORM-07 | Medium | Open (external) | Safety Report instance dates use MM/DD/YYYY and switch between UTC and local |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
