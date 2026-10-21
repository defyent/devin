# Personnel Details / My Account

- **Checklist ID prefix:** `PD`
- **Guide section:** §9.2
- **Where:** Click a person / My Account
- **Permission:** Personnel Details A/RA/WG/RG/WO/RO
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| PD-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | FAIL | BUG-PD-001 | All Personnel > Ethan Abbott opens Personnel Details (person_id=81), but every load throws 'getPickerMod is not defined' (BUG-PD-001) (shot pd_open) |
| PD-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS |  | Help (?) opens 'Personnel Details Help'; closes with Escape, x and outside click; stays open on drag-out (shot pd_help) |
| PD-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | FAIL | BUG-PD-005 | Drag-out keeps Help, History and PDF Options open (pass). History and PDF Options don't close with Escape; PDF Options has no x (BUG-PD-005) |
| PD-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| PD-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | 390 px: tabs become a dropdown, no sideways scrolling, fields fit the width. The Performance panel (BUG-PD-010) covers the photo controls on mobile until closed |
| PD-S06 | Low-permission account | Access Denied or read-only as per permission | BLOCKED |  | betatest_low opens its own My Account and can edit Personal Details; whether that is right depends on its permission level, checked in 90 Permission levels (same as PD-030) |

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
| PD-010 | Timesheet day: add/remove sessions, claims, files | 'Session added' / 'Session removed' | TODO | | |
| PD-011 | Sign day (password) / Bulk Sign | Status Pending | TODO | | |
| PD-012 | Reopen approved/rejected | Works | TODO | | |
| PD-013 | External Flight Time (decimal hours + note) | Saved and counted | TODO | | |
| PD-014 | Legacy Duty Browser | Opens | PASS |  | Timesheets > Legacy Duty Browser link opens the 'Legacy Duty Browser' popup with < October 2026 > / Today and columns Date, Duty Start/End, Duty Hours, Legacy/System Flight Time, Note ('No legacy duty or flight time recorded for this month.') and Close (shot pd_legacy) |
| PD-015 | Request Leave (type, dates, comments) > view/edit/withdraw | Works | TODO | | |
| PD-016 | F&D / Roster Violation Analysis popups | Explain breaches | TODO | | |
| PD-017 | Exams tab: open instance > Previous/Next/Submit; leave and resume | Progress saved; Exam History | TODO | | |
| PD-018 | Lesson Plans tab: Assign (plan, start, end) | Assigned; lessons + progress; Lesson Details flights | TODO | | |
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
| PD-029 | Access as RO / WO / WG | Edit rights match level; WG can always edit self | BLOCKED |  | Needs users at RO / WO / WG for Personnel Details; run with 90 Permission levels |
| PD-030 | No Personnel Details permission > My Account | Access Denied | BLOCKED |  | betatest_low: clicking its name in the header opens its own Personnel Details (My Account, #276) with Personal Details editable. Whether that is right depends on its Personnel Details permission level; checked again in 90 Permission levels |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

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
