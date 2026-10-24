# Personnel Details / My Account

- **Checklist ID prefix:** `PD`
- **Guide section:** §9.2
- **Where:** Click a person / My Account
- **Permission:** Personnel Details A/RA/WG/RG/WO/RO
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| PD-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | FAIL | BUG-PD-001 | All Personnel > Ethan Abbott opens Personnel Details (person_id=81), but every load throws 'getPickerMod is not defined' (BUG-PD-001) (shot pd_open) |
| PD-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS |  | Help (?) opens 'Personnel Details Help'; closes with Escape, x and outside click; stays open on drag-out (shot pd_help) |
| PD-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | FAIL | BUG-PD-005 | Drag-out keeps Help, History and PDF Options open (pass). History and PDF Options don't close with Escape; PDF Options has no x (BUG-PD-005) |
| PD-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | PASS |  | Settings > Time Zone: Pacific/Auckland, DD/MM/YYYY, 24-hour. Personnel Details dates (files, flights, timesheets, recency) all show DD/MM/YYYY. Empty Birth Date showing today is BUG-PD-013 |
| PD-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | 390 px: tabs become a dropdown, no sideways scrolling, fields fit the width. The Performance panel (BUG-PD-010) covers the photo controls on mobile until closed |
| PD-S06 | Low-permission account | Access Denied or read-only as per permission | PASS | pd029_wo_self | Lowperm (Personnel Details WO) can edit only their own Personal Details. Second (WO) is the same: own details are editable with Save Changes. Grpuser (RG) gets their own details read-only. The low-permission behaviour matches each level. |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| PD-001 | Header: History, PDF (sections), Help, Save Changes | Work | PASS |  | History opens Personnel History; Personnel Pdf opens section options (Personal Details, Exams, Forms, Timesheets, Recency & Renewals) and Generate PDF downloads Ethan_Abbott_Personnel_File.pdf; Help opens help; Save Changes saves (PD-004) |
| PD-002 | Tabs shown | Personal Details, Flights, Exams, Recency, Forms, Files, Security always; Timesheets only Staff; Lesson Plans only Student; Customize only own/admin | PASS |  | Staff (Ethan Abbott): Personal Details, Flights, Timesheets, Exams, Recency and Renewals, Forms, Files, Security, Customize - no Lesson Plans. Student (Peter Archer): Lesson Plans shown, no Timesheets. Customize shown to Service Account (admin) (shots pd_open, pd_student) |
| PD-003 | Forms/Files count badges | Correct counts | PASS |  | Ethan Abbott Forms tab badge 2 = 2 attached forms (QA Annual Line Check, QA Equipment Issue); BETA TEST ONLY Lowperm has 0 forms and no badge |
| PD-004 | Personal Details: edit every field, Save | Saved; dirty-state buttons; leave prompt | FAIL | BUG-NAV-001 | On BETA TEST ONLY Lowperm: Save is disabled until a change, then highlighted (pending changes); Save shows 'Personal details saved successfully!' and the values persist after reopening (restored afterwards). But leaving through the sidebar with unsaved edits gives no prompt and the edits are lost (BUG-NAV-001) (shot pd_saved) |
| PD-005 | Weight KG/Lbs toggle | Converts; used on manifests | PASS |  | Weight 80 KG -> Lbs shows 176.4, back to KG 80.0 (manifest use covered in Flight Details FD kg/lbs check) |
| PD-006 | Photo upload / delete | Appears in top bar and Access Manager | PASS |  | Uploaded a 200x200 PNG on BETA TEST ONLY Lowperm: shows in the page header avatar, the Photo box and the Access Manager user list. Remove > confirm 'Remove Photo' > 'Photo removed successfully'; gone after reopening |
| PD-007 | Digital Signature: draw, refresh, password, Save | Saved; wrong password rejected | FAIL | BUG-PD-014 | Draw + Clear work; correct password saves ('Digital signature saved successfully'), button becomes Update Signature. Wrong password is rejected ('Incorrect password') but the popup closes and the drawing is lost; empty Save shows no message |
| PD-008 | Flights tab: search, click | Opens Flight Details | PASS |  | Flights tab lists the person's flights (ID, date, aircraft, PIC, SFC, flight/engine time, route). Search 'Charter' filters the list; clicking #7089 opens Flight Details for 7089 (shots pd_flights, pd_flight_open) |
| PD-009 | Timesheets tab: < > Today | Days with Roster, Duty, Total, Flight Time, F&D, Status | PASS |  | Ethan Abbott Timesheets: October 2026 with summary (Rostered Days, Duty Hours, Predicted, Claims, Flight Time) and day rows with Date, Roster, Duty, Total Duty, Flight Time, F&D, Status, Actions. < goes to Sep then Aug, > back to Sep, Today back to Oct (shot pd_timesheets) |
| PD-010 | Timesheet day: add/remove sessions, claims, files | 'Session added' / 'Session removed' | FAIL | BUG-PD-016 | Personnel Details > Timesheets (Ethan Abbott, viewed by Service Account) shows duty times as plain text with no add/remove session controls. Add Claim on 01/10 (enabled) does nothing. Sessions/files retest from Timesheet Details in 15 |
| PD-011 | Sign day (password) / Bulk Sign | Status Pending | PASS | pd011_signed | As BETA TEST ONLY Second (after rostering OH/PM/OC on 19-21 Oct): ticked 19 and 20 > Sign Selected (2) > "Sign Multiple Timesheets" asks for the password (and warns there is no digital signature on file) > Sign All. After a reload both days show Submitted ("Click to reopen"), and 21 stays Draft. Days with no roster have no checkbox and Add Claim is disabled. |
| PD-012 | Reopen approved/rejected | Works | PASS | pd012_reopen | As BETA TEST ONLY Second, clicking 21 Oct "Submitted - Click to reopen" asks for the password ("Reopen Timesheet"). After entering it the day shows "Draft - Click to sign". An Approved day (19 Oct) has no reopen action for the user. The approver has to unapprove it first (TS-004 Unapprove sets it back to Submitted). There is no day-level reject on Timesheets, so there is no rejected state to reopen. |
| PD-013 | External Flight Time (decimal hours + note) | Saved and counted | PASS | pd013_ext | Logged in as BETA TEST ONLY Second (Timesheets own access) > My Account > Timesheets. The flight_takeoff button on 21 Oct opens "External Flight Time" (decimal hours + note). Saved 1.5 / "BETA TEST ONLY ext". After a reload the row shows +1.50 and the Flight Time total shows 1.50. On a person with no roster, the Rostered Days count also went from 0 to 1. |
| PD-014 | Legacy Duty Browser | Opens | PASS |  | Timesheets > Legacy Duty Browser link opens the 'Legacy Duty Browser' popup with < October 2026 > / Today and columns Date, Duty Start/End, Duty Hours, Legacy/System Flight Time, Note ('No legacy duty or flight time recorded for this month.') and Close (shot pd_legacy) |
| PD-015 | Request Leave (type, dates, comments) > view/edit/withdraw | Works | PASS | pd015_withdrawn | As BETA TEST ONLY Second: My Account > Timesheets > Request Leave (Sick Leave, 12/11/2026, comment) > Submit. The day shows a "Sick Leave" Pending badge. Clicking it opens the request (status, dates, comments, Withdraw Request / Edit / Close). Edit > changed the comment > Save Changes, which was kept after a reload. Withdraw Request > "This cannot be undone" > Confirm, and the badge is gone after a reload. The dates default to the UTC date (BUG-PD-018). |
| PD-016 | F&D / Roster Violation Analysis popups | Explain breaches | FAIL | BUG-PD-015 | Ethan Abbott 01/10: F&D icon opens 'Flight & Duty Analysis' with Violations Detected (predicted duty 12.0 h > 8 h in 24 h), required rest and return time, plus Flight/Duty limit cards with usage bars. Title date is 2026-10-01, rest time is 12-hour US style, Escape ignored. Roster Violation Analysis not seen on this page |
| PD-017 | Exams tab: open instance > Previous/Next/Submit; leave and resume | Progress saved; Exam History | PASS | pd017_resume | As BETA TEST ONLY Second: Dashboard Exams > BETA TEST ONLY Exam opens Personnel Details > Exams; clicking the row opens the exam (Question 1 of 10, Previous/Next, numbered nav). Answered Q1-Q2, closed, reopened: "2 of 10 questions answered" with ticks kept (resumes on Q2, not where I left). Review shows 2 answered / 8 remaining; Submit Exam > OK grades it (Graded 18.00% Fail). Q10 hotspot shows a debug message (BUG-EXM-009). |
| PD-018 | Lesson Plans tab: Assign (plan, start, end) | Assigned; lessons + progress; Lesson Details flights | FAIL | BUG-PD-017 | Made "BETA TEST ONLY Plan" with "BETA TEST ONLY Lesson 1" and assigned it to BETA TEST ONLY Grpuser. You get "Lesson plan assigned successfully" and the lesson is offered on the student's flight #42909, but the Lesson Plans tab still says "No lesson plans assigned to this person" after you reopen the page. The dialog dates default to 21/10/2026, the UTC date. |
| PD-019 | Recency tab: table/card, Group by, Order by | Work | FAIL | BUG-PD-006 | Table shows Renewals and Recencies groups, but Group by and Order by are disabled and the Table/Card view buttons are hidden (BUG-PD-006) (shot pd_recency) |
| PD-020 | Add Item > Renewal / Recency | Search and add | FAIL | BUG-PD-006 | Add Item button (#add-recency-btn) is in the page but hidden, so no item can be added (BUG-PD-006) |
| PD-021 | Recency count > Recency Flights; Add Manual Entry (Date*, Value*, Notes) | Works | FAIL | BUG-PD-008 | Clicking the Day Landings count opens 'Recency summary for Day Landings' with 4 manual entries, but there is no Add Manual Entry, no x, and Escape doesn't close it (outside click does) (BUG-PD-008) (shot pd_recency_flights) |
| PD-022 | Renewal: Calculate, Today, Schedule with Flight, Complete Renewal (archive/keep attachments) | Dates correct in org format | FAIL | BUG-PD-006, BUG-PD-009 | Renewal edit page opens (Status, Renewal with Frequency/Last Conducted/Scheduled/Expires, Attached Forms/Files). Calculate gives the right date in org format (20/10/2028 = 21/10/2026 + 730) but Today/Calculate links can't be clicked normally (BUG-PD-009). Schedule with Flight opens a list of this person's crewed flights and closes with Escape. No Save / Complete Renewal / Cancel buttons are shown (BUG-PD-006); Go Back discards without asking (shots pd_renewal_calc, pd_renewal_sched) |
| PD-023 | Status legend colours | OK green, Caution yellow, Expired red, Empty grey | PASS |  | Status dots: OK green, Caution orange/yellow, Expired red (no Empty item on Ethan Abbott to check grey). Recency days/status values look wrong, see BUG-PD-007 |
| PD-024 | Forms tab: add, save, archive, unarchive, delete | Each confirms | PASS |  | On BETA TEST ONLY Lowperm: Add Form > QA Equipment Issue -> 'Form added successfully!' and badge 1; Archive asks 'Are you sure...' then moves it to Archived Forms; Unarchive asks and restores it ('Form unarchived successfully!'); Delete asks ('cannot be undone') and removes it. Save Changes stays disabled until a field changes (shots pd_form_archived, pd_form_deleted) |
| PD-025 | Files tab | Upload, preview, download, delete | FAIL | BUG-PD-012 | Upload (30 B txt) PASS, listed with date/uploader/size; Download PASS (BETA_TEST_ONLY_pd.txt); Delete with confirm PASS after reload. Clicking the file name gives 'File Access Error' showing the file text, and after that Delete shows nothing until reload |
| PD-026 | Security: change password (wrong current, < 8, mismatch) | Validation; success | FAIL | BUG-PD-011 | Validation messages work (empty, under 8 chars, mismatch), but a real change - correct or wrong current password - fails with 'Invalid Action: change_password' (BUG-PD-011). Tested by Service Account on BETA TEST ONLY Lowperm; password unchanged |
| PD-027 | Security: Enable 2FA (QR, backup codes download, verify) | Enabled | FAIL | BUG-PD-003 | Password prompt (wrong pw: 'Setup Error - Invalid password'), QR + manual key + 10 backup codes + Download, valid code -> '2FA enabled successfully!'. Wrong code closes the dialog and forces a new key |
| PD-028 | Customize: Login Landing Page | Saved; used on next login | PASS |  | Customize: set BETA TEST ONLY Lowperm landing page to Flight Schedule, Save gives 'Login landing page saved'; logging in as betatest_low opens Flight Schedule. Restored to Dashboard |
| PD-029 | Access as RO / WO / WG | Edit rights match level; WG can always edit self | FAIL | pd029_rg_click | WO: Second's My Account has editable Personal Details and Save Changes. RG: Grpuser's own My Account is read-only with no Save, which is right. But Grpuser can't open other group members from All Personnel (BUG-PL-003). WG isn't offered on the Personnel Details card used here. |
| PD-030 | No Personnel Details permission > My Account | Access Denied | PASS | pd030_none | I took Lowperm's only permission (Personnel Details WO) away for a moment. Clicking their name in the header (My Account, #276) then shows "Access Denied: You do not have permission to access the Personnel Details". I put WO back afterwards. |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`STATUS.md`](../STATUS.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| FORM-03 | High | Open (external) | Personnel "Archived Forms" section won't expand, so archived forms can't be viewed or unarchived |
| FORM-37 | Low | Open (external) | Personnel instance delete button has no tooltip; Archive has one |
| UX-02 | Medium | Open (external) | Personnel Details has no name/title and no back button |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| BETA TEST ONLY Lowperm: Middle Name 'BETA', City 'BETA TEST ONLY City', Weight 80 saved in PD-004 | Personnel Details #276 | Yes - cleared again |
| Form 'QA Equipment Issue' added to BETA TEST ONLY Lowperm in PD-024, archived, unarchived, deleted | Personnel Details #276 Forms | Yes - deleted |
| File BETA_TEST_ONLY_pd.txt uploaded to BETA TEST ONLY Lowperm in PD-025 | Personnel Details #276 Files | Yes - deleted |
| BETA TEST ONLY Lowperm login landing page set to Flight Schedule in PD-028 | Personnel Details #276 Customize | Yes - restored to Dashboard |
| Photo BETA_TEST_ONLY_photo.png uploaded to BETA TEST ONLY Lowperm in PD-006 | Personnel Details #276 Photo | Yes - removed |
| Digital signature drawn and saved for BETA TEST ONLY Lowperm in PD-007 | Personnel Details #276 Signature | No - no delete option (only Update Signature); remove in the database or leave |
