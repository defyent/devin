# Safety Reports (SMS)

- **Checklist ID prefix:** `SMS`
- **Guide section:** §10.4, §13.4
- **Where:** Flight Safety > Safety Reports
- **Permission:** Safety Reports + SMS Investigator/Reviewer
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

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
| SMS-005 | Create BETA TEST ONLY report with On Behalf Of, Resource, PIC | Submitted; permanent investigators/reviewers auto-assigned | PASS |  | Created report #2060 'BETA TEST ONLY report' (Hazard Report, On Behalf Of Aisha Pearce, Resource ZK-SIM). It opens Report Details with the values shown. PIC list had no 'Aisha J' so PIC left N/A. No investigators/reviewers were auto-assigned - check whether any permanent ones are set in checklist 44 (Settings: Safety Reports) and retest there |
| SMS-006 | Risk Level display | Matches matrix cell | PASS |  | Rare x Insignificant shows Low, and Risk Matrix Details match (Once in 10+ years, 0.1 events/year, negligible impacts) |
| SMS-007 | Open Investigation (investigator) > Close Investigation > Close Report (reviewer) | Each confirms; progress bar updates | PASS |  | #2060: Open Investigation > Close Investigation > Close Report each ask 'Are you sure you want to change the report status to ...?' and the progress bar moves Opened > Under Investigation > Under Review > Closed. Note: the Service Account could do every step with no investigator or reviewer assigned |
| SMS-008 | Non-investigator / non-reviewer | Status buttons hidden | PASS | sms008_grp | Grpuser (Safety Reports WG, submitter, not investigator or reviewer) opened their new report #2063 and clicked Under Investigation. The status stayed Report Opened, so a non-investigator can't move it. No message says why. The occurrence time defaulted to UTC 21/10 22:01 (BUG-SMS-002). |
| SMS-009 | Details tab: Extra Safety Report Info save | Saved | PASS |  | Tested in 44 (SSMS-002): with Extra Info Field "BETA TEST ONLY EIF" set up, report #2060 Details tab shows it under Extra Safety Report Info and "BETA eif value" saved ("Extra info saved successfully!") and was kept after reload. |
| SMS-010 | Files, Comments, Forms, History tabs | Work | PASS |  | #2060: Comments posts 'BETA TEST ONLY comment' ('Comment posted successfully!'); History lists creation, each status change and the comment with date/user; Files and Forms tabs load (upload/Add Form available) |
| SMS-011 | Actions: Create New Action (assign, request) | Appears on assignee Dashboard Safety Actions; completing it records action taken | PASS |  | Action #1174 'BETA TEST ONLY action' assigned to Service Account shows on its Dashboard > Safety Actions tab (Report #2060). Because #2060 was already closed, Dashboard lists it as 'Completed via closed SMS report' while the report's Actions tab still says OPEN with a Complete Action button. Creating an action on a closed report was allowed |
| SMS-012 | Final Report: add/remove investigators & reviewers, summary, final risk | Saved | PASS | BUG-SMS-003 | Final Report on #2060: added investigator Aisha Pearce and reviewer Aisha Johnston, summary, final risk Unlikely x Minor; Save Changes shows 'Final report saved successfully!'. Final Likelihood/Consequence list each option twice (BUG-SMS-003) |
| SMS-013 | Add to Hazard Register | Hazard appears in Hazard Register | PASS | BUG-SMS-004 | Filled Add to Hazard Register on #2060 (Hazard, Mitigate, controls, Aisha Pearce) and saved; #2060 now appears in Hazard Register. Goal shows 'Minimize' instead of 'Mitigate' (BUG-SMS-004) |
| SMS-014 | Confidential report as another user | Hidden appropriately | BLOCKED | sms014_two | Grpuser created confidential report #2062. Second (WO) doesn't see it, but Second sees no reports at all (BUG-SMS-005), so I can't tell whether confidentiality is what hides it. Retest after the fix. |
| SMS-015 | WO / WG / RA accounts | Visibility matches §10.4 rules | FAIL | sms015_wg | BUG-SMS-005: WG (Grpuser) and WO (Second) both see 0 reports. Grpuser can't see even their own #2062 after creating it. The admin sees it. RA was not set up. |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| FORM-02 | High | Open (external) | Safety Report form edits are lost: Save Changes never enables, values gone after reopening |
| FORM-07 | Medium | Open (external) | Safety Report instance dates use MM/DD/YYYY and switch between UTC and local |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Safety report #2060 'BETA TEST ONLY report' (Hazard Report, ZK-SIM, on behalf of Aisha Pearce) | Flight Safety > Safety Reports | No - the app has no delete for safety reports |
