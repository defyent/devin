# DataHangar audit: bugs by module

Totals: 557 pass, 186 fail, 27 blocked, 183 bugs (9 High, 70 Medium, 104 Low).

## Summary

| Module | Pass | Fail | Blocked | Bugs |
|---|---|---|---|---|
| Session setup, accounts and baseline | 9 | 0 | 0 | 0 |
| Login, 2FA, sessions, landing page | 16 | 3 | 1 | 3 |
| Application shell, sidebar, header, mobile | 23 | 2 | 1 | 1 |
| Common screen conventions (apply on every page) | 17 | 5 | 0 | 0 |
| Access Manager (users, roles, groups, permissions, templates) | 28 | 9 | 0 | 7 |
| Dashboard | 13 | 6 | 0 | 4 |
| Flight Schedule (incl. embedded Location Planner) | 30 | 8 | 1 | 9 |
| Flight Details | 37 | 7 | 0 | 6 |
| Active Flights and Live Tracking | 15 | 4 | 0 | 5 |
| Daily Flight Record | 14 | 2 | 0 | 3 |
| Location Planner (stand-alone) | 0 | 0 | 9 | 0 |
| All Personnel (Personnel List) | 10 | 1 | 0 | 2 |
| Personnel Details / My Account | 21 | 15 | 0 | 20 |
| Roster Viewer | 9 | 3 | 0 | 3 |
| Roster Builder | 13 | 8 | 0 | 8 |
| Timesheets, Timesheet Details, Leave Requests | 11 | 6 | 0 | 8 |
| Flight and Duty | 12 | 2 | 0 | 5 |
| Notices | 12 | 4 | 0 | 4 |
| Recency and Renewals (overview page) | 7 | 2 | 0 | 2 |
| Safety Reports (SMS) | 18 | 2 | 1 | 5 |
| Hazard Register | 8 | 2 | 0 | 3 |
| Settings and Tools hub | 10 | 1 | 0 | 0 |
| File Browser | 8 | 6 | 0 | 7 |
| Form Builder | 10 | 4 | 0 | 4 |
| Form Browser / Form Viewer | 7 | 3 | 0 | 3 |
| Task Tracker | 8 | 4 | 0 | 4 |
| Reports | 13 | 3 | 0 | 4 |
| Support tickets | 10 | 4 | 0 | 4 |
| Chat | 8 | 2 | 1 | 3 |
| Exam Builder, Exam Editor, Exam Instances | 10 | 6 | 0 | 8 |
| Maintenance Portal | 0 | 0 | 11 | 0 |
| Settings – Flight Schedule | 10 | 2 | 0 | 2 |
| Settings – Daily Flight Record | 5 | 1 | 0 | 1 |
| Settings – Time Zone (date/time matrix) | 7 | 4 | 0 | 3 |
| Settings – Resources (Aircraft) | 16 | 2 | 0 | 1 |
| Settings – Weight and Balance Configs | 9 | 4 | 0 | 5 |
| Settings – Extra Flight Info | 7 | 1 | 0 | 1 |
| Settings – Flight Types | 5 | 2 | 0 | 2 |
| Settings – Waypoint Locations | 8 | 3 | 0 | 4 |
| Settings – Roster Shifts | 7 | 3 | 0 | 4 |
| Settings – Fatigue Risk Management | 8 | 2 | 0 | 2 |
| Settings – Recency and Renewals | 5 | 4 | 0 | 4 |
| Settings – Lesson Plans | 5 | 3 | 0 | 3 |
| Settings – Risk Matrix | 6 | 2 | 0 | 2 |
| Settings – Safety Reports | 7 | 1 | 0 | 1 |
| Settings – Inspection Notifications | 6 | 3 | 0 | 3 |
| Settings – Google Calendar, WhatsApp | 6 | 2 | 2 | 2 |
| Settings – Activity Log | 6 | 2 | 0 | 1 |
| Cross-cutting: permission levels | 9 | 1 | 0 | 4 |
| Cross-cutting: popups/modals | 4 | 4 | 0 | 0 |
| Cross-cutting: date/time formats and pickers | 2 | 5 | 0 | 2 |
| Cross-cutting: mobile / narrow layout | 2 | 2 | 0 | 0 |
| Cross-cutting: UI consistency and icon inventory | 3 | 4 | 0 | 0 |
| Cross-cutting: performance, console and network | 1 | 3 | 0 | 1 |
| End-to-end workflows | 6 | 2 | 0 | 0 |

## Bugs

| Module | Bug | Severity | Title |
|---|---|---|---|
| Login, 2FA, sessions, landing page | BUG-LOG-003 | Medium | 'Trust this device for 30 days' is lost on Logout (logout deletes the trusted-device cookie) |
| Login, 2FA, sessions, landing page | BUG-LOG-001 | Low | Login Message popup reappears on every browser reload |
| Login, 2FA, sessions, landing page | BUG-LOG-002 | Low | Logout throws JS error removeChild; Esc doesn't close the Log Out confirm |
| Application shell, sidebar, header, mobile | BUG-NAV-001 | Medium | Leaving a page with unsaved changes gives no warning; edits are lost |
| Access Manager (users, roles, groups, permissions, templates) | BUG-AM-001 | Medium | New User accepts a 6-character password (placeholder and Change Credentials require 10) |
| Access Manager (users, roles, groups, permissions, templates) | BUG-POP-003 | Medium | Access Manager Groups popup: Esc closes with unsaved changes and no warning; reopening shows the unsaved ticks as if saved |
| Access Manager (users, roles, groups, permissions, templates) | BUG-AM-002 | Low | Last Activity hover date ignores Settings > Time Zone format |
| Access Manager (users, roles, groups, permissions, templates) | BUG-AM-003 | Low | Last Activity column sort does not change order |
| Access Manager (users, roles, groups, permissions, templates) | BUG-AM-004 | Low | Permission level dropdown shows bare codes 'WA' and 'G' next to full labels |
| Access Manager (users, roles, groups, permissions, templates) | BUG-POP-001 | Low | Error modal ('Failed to Create User') does not close with Esc |
| Access Manager (users, roles, groups, permissions, templates) | BUG-POP-002 | Low | Manage User Permissions uses a native browser confirm() for unsaved changes |
| Dashboard | BUG-DSH-003 | Medium | Dashboard recency item opens Personnel Details on the wrong tab (Personal Details instead of Recency and Renewals) |
| Dashboard | BUG-DSH-004 | Medium | Dashboard: My Flights and On Duty open on the UTC date, not today's local date |
| Dashboard | BUG-DSH-005 | Medium | Dashboard Project Tasks: clicking a task opens an empty project list instead of the project |
| Dashboard | BUG-DSH-001 | Low | Dashboard side tabs are icon-only with no tooltip or label |
| Flight Schedule (incl. embedded Location Planner) | BUG-FS-008 | High | Flight Schedule: a group-level user (G / WG) sees no flights, even on aircraft in their own group |
| Flight Schedule (incl. embedded Location Planner) | BUG-FS-001 | Medium | New flight defaults to the current UTC time instead of local time (SAR TIME labelled LOCAL shows UTC+1h) |
| Flight Schedule (incl. embedded Location Planner) | BUG-FS-002 | Medium | Esc does not end copy/paste mode on the Flight Schedule - the next click + Ctrl+V creates another flight |
| Flight Schedule (incl. embedded Location Planner) | BUG-FS-003 | Medium | Flight Schedule header overlaps when Live Edit is on - title covered, location pill cut off and its 'Show All' button cannot be clicked |
| Flight Schedule (incl. embedded Location Planner) | BUG-FS-004 | Medium | Planner Add Location replaces the New Booking popup - typed booking and location input is lost |
| Flight Schedule (incl. embedded Location Planner) | BUG-FS-006 | Medium | Flight Schedule month view is slow: flightschedule_json takes ~1.6 s and rendering 2,500 events ~4.5 s |
| Flight Schedule (incl. embedded Location Planner) | BUG-FS-007 | Medium | Edit-mode idle timeout switches Live Edit off silently, throws 'calendarEl is not defined' and leaves the schedule blank |
| Flight Schedule (incl. embedded Location Planner) | BUG-FS-005 | Low | JS error on every Live Edit toggle: Cannot read properties of null (reading 'scrollTop') |
| Flight Schedule (incl. embedded Location Planner) | BUG-POP-004 | Low | Flight Schedule popups (View Details, Double Booking alert, note modals) do not close with Esc |
| Flight Details | BUG-FD-001 | Medium | Flight Details Save Changes does not return to the Flight Schedule and gives no success message |
| Flight Details | BUG-FD-002 | Medium | Flight Details History misses edits saved in Flight Details and shows a false 'Aircraft: ZK-SIM > Unassigned' on schedule moves |
| Flight Details | BUG-FD-004 | Medium | Leg PIC / Secondary Flight Crew dropdowns offer passengers (e.g. a custom passenger can be chosen as leg PIC) |
| Flight Details | BUG-FD-005 | Medium | Leg with two unknown waypoints: only the first is offered for adding, the second is silently dropped on save |
| Flight Details | BUG-FD-006 | Medium | Flight can be set to Complete with no times or destination on a leg; no 'Required Information' prompt |
| Flight Details | BUG-FD-003 | Low | Times and Meters: no link to the previous flight next to 'Previous' meter readings |
| Active Flights and Live Tracking | BUG-AF-004 | High | Active Flights overdue and active times are 13 h out: local SAR/start times are compared with UTC 'now' |
| Active Flights and Live Tracking | BUG-AF-002 | Medium | Active Flights lists future flights that have no SAR time, and the stats cards don't count them |
| Active Flights and Live Tracking | BUG-AF-005 | Medium | Active Flights: a Read Only Group (RG) user sees every company flight, not only their group's |
| Active Flights and Live Tracking | BUG-AF-001 | Low | Active Flights shows SAR Time '01/01/1970 00:00' for flights with SAR watch disabled |
| Active Flights and Live Tracking | BUG-AF-003 | Low | Active Flights has no page Help (?), and its popups (About Live Tracking, Adjust SAR, Add Note) don't close with Escape |
| Daily Flight Record | BUG-DFR-002 | Medium | Daily Flight Record: Clear Filters unticks every status (lists Open, Cancelled and Deleted flights), and the date fields show today's date when no date filter is applied |
| Daily Flight Record | BUG-DFR-003 | Medium | Daily Flight Record: changing filters quickly appends results instead of replacing them, showing duplicate and wrong-status rows |
| Daily Flight Record | BUG-DFR-001 | Low | Daily Flight Record has no page Help (?), and its popups (Manage Columns, Notes full text) don't close with Escape |
| All Personnel (Personnel List) | BUG-PL-001 | Low | All Personnel has no page Help (?) |
| All Personnel (Personnel List) | BUG-PL-002 | Low | A person with no name exists and is listed as '?' at the top of All Personnel (person #274, Customer) |
| Personnel Details / My Account | BUG-PD-006 | High | Personnel Details > Recency and Renewals: action buttons are hidden (Add Item, Table/Card view, renewal Save / Complete Renewal / Cancel) and Group by / Order by are disabled |
| Personnel Details / My Account | BUG-PD-011 | High | Personnel Details > Security: Change Password always fails with 'Invalid Action: change_password' |
| Personnel Details / My Account | BUG-PD-001 | Medium | personneldetails/index.js is truncated: ReferenceError getPickerMod on every load |
| Personnel Details / My Account | BUG-PD-003 | Medium | 2FA setup: one wrong verification code closes the setup dialog and issues a new secret |
| Personnel Details / My Account | BUG-PD-007 | Medium | Personnel Details > Recency: 'Days Until Expiry' and status don't match the Last Conducted date |
| Personnel Details / My Account | BUG-PD-008 | Medium | Personnel Details > Recency: the recency summary popup has no Add Manual Entry, no x, and doesn't close with Escape |
| Personnel Details / My Account | BUG-PD-009 | Medium | Personnel Details > Renewal edit: the Today and Calculate links can't be clicked because the date fields cover them |
| Personnel Details / My Account | BUG-PD-012 | Medium | Personnel Details > Files: opening a file shows 'File Access Error' with the file's contents as the message |
| Personnel Details / My Account | BUG-PD-016 | Medium | Personnel Details > Timesheets: Add Claim button does nothing |
| Personnel Details / My Account | BUG-PD-017 | Medium | Personnel Details > Lesson Plans: an assigned plan is saved but never listed; the dialog's dates default to the UTC date |
| Personnel Details / My Account | BUG-PL-003 | Medium | All Personnel: a Read Only Group (RG) user can't open the details of anyone in their group |
| Personnel Details / My Account | BUG-EXM-009 | Low | Exams: a hotspot question with no image shows a developer debug message to the person taking the exam |
| Personnel Details / My Account | BUG-PD-002 | Low | Personnel Details modals (Enable 2FA, Setup Error alert): title right-aligned, away from its icon |
| Personnel Details / My Account | BUG-PD-004 | Low | Security tab 'Enabled on' date ignores Settings > Time Zone format |
| Personnel Details / My Account | BUG-PD-005 | Low | Personnel Details: History, PDF Options and Legacy Duty Browser popups don't close with Escape, and PDF Options has no x |
| Personnel Details / My Account | BUG-PD-010 | Low | Personnel Details: the 'Performance' timing panel is shown to users and covers buttons |
| Personnel Details / My Account | BUG-PD-013 | Low | Personnel Details: an empty Birth Date shows today's date |
| Personnel Details / My Account | BUG-PD-014 | Low | Digital Signature: wrong password closes the popup and throws away the drawing; empty Save gives no message |
| Personnel Details / My Account | BUG-PD-015 | Low | Flight & Duty Analysis popup: title date is YYYY-MM-DD and Escape doesn't close it |
| Personnel Details / My Account | BUG-PD-018 | Low | Request Leave: Start and End Date default to the UTC date, not today's local date |
| Roster Viewer | BUG-RV-002 | Medium | Roster Viewer: clicking a shift does not open Shift Details |
| Roster Viewer | BUG-RV-001 | Low | Roster Viewer: no page Help (?) and Group Visibility popup ignores Escape |
| Roster Viewer | BUG-RV-003 | Low | Roster Viewer shift note popup shows the date as 'October 5, 2026', not the configured DD/MM/YYYY |
| Roster Builder | BUG-RB-007 | High | Roster Builder: Clear then Publish of a draft month with no shifts does not clear the live roster and shows no message |
| Roster Builder | BUG-RB-002 | Medium | Roster Builder: Copy Live to Draft copies one shift at a time and takes about 6 minutes for one month |
| Roster Builder | BUG-RB-003 | Medium | Roster Builder: copy/paste still works with violation checking ON |
| Roster Builder | BUG-RB-005 | Medium | Roster Builder: every validation error throws a JS error instead of showing a message (e.g. Apply Shift Pattern with no shifts) |
| Roster Builder | BUG-RB-008 | Medium | Roster Builder can only be opened from Settings and Tools, so a Roster Builder user without System Settings can't reach it |
| Roster Builder | BUG-RB-001 | Low | Roster Builder: no page Help (?); Copy/Paste Instructions popup ignores Escape and outside click |
| Roster Builder | BUG-RB-004 | Low | Roster Builder: Rule Violations popup shows 'Monday, October 5' instead of the configured DD/MM/YYYY date |
| Roster Builder | BUG-RB-006 | Low | Roster Builder: at phone width the shift palette takes half the screen and the Draft Edit Mode banner covers the search box and palette |
| Timesheets, Timesheet Details, Leave Requests | BUG-TS-002 | Medium | Timesheet Approval: status filter 'Unsigned' shows 'No personnel found' although everyone has unsigned days |
| Timesheets, Timesheet Details, Leave Requests | BUG-TS-003 | Medium | Timesheet Approval list totals don't match Timesheet Details (Rostered Days and Duty Hours) |
| Timesheets, Timesheet Details, Leave Requests | BUG-TS-008 | Medium | Approving a leave request doesn't change the rostered shifts, and rejecting with no reason gives no message |
| Timesheets, Timesheet Details, Leave Requests | BUG-TS-001 | Low | Timesheets: no page Help on Timesheet Approval, and the Help (?) on Timesheet Details does nothing |
| Timesheets, Timesheet Details, Leave Requests | BUG-TS-004 | Low | Timesheet Details shows dates as 'Oct 5' and times with seconds (14:00:00) |
| Timesheets, Timesheet Details, Leave Requests | BUG-TS-005 | Low | Timesheet Details: F&D and Roster Violation popups ignore Escape and show ISO dates in the title |
| Timesheets, Timesheet Details, Leave Requests | BUG-TS-006 | Low | Leave Types: a validation error closes the Add Leave Type popup and throws away what you typed; the popup ignores Escape |
| Timesheets, Timesheet Details, Leave Requests | BUG-TS-007 | Low | Reject Claim: leaving the reason empty closes the reject popup and throws a script error |
| Flight and Duty | BUG-FAD-001 | Low | Flight and Duty has no page Help (?) |
| Flight and Duty | BUG-FAD-002 | Low | Flight and Duty popups (Flight Details, Duty Time Details, Roster Violations, Resolutions Required) ignore Escape |
| Flight and Duty | BUG-FAD-003 | Low | Flight and Duty popups show dates as '16 Oct 2026' instead of the configured DD/MM/YYYY |
| Flight and Duty | BUG-FAD-004 | Low | Flight and Duty column headers are ambiguous: two '1 Days' and two '24 Hours' columns, and '1 Days' is ungrammatical |
| Flight and Duty | BUG-FAD-005 | Low | Flight and Duty 'View as Date' defaults to the UTC date instead of the local date |
| Notices | BUG-NOT-002 | Medium | Notice Details: clicking a .txt attachment does nothing (no preview, no download) |
| Notices | BUG-NOT-004 | Medium | Notices: a Write Group (WG) user gets 'An error occurred' when clicking New Notice |
| Notices | BUG-NOT-001 | Low | Notices has no page Help (?), and the Create New Notice popup ignores Escape |
| Notices | BUG-NOT-003 | Low | Settings and Tools hub: 'Notices' card has no links |
| Recency and Renewals (overview page) | BUG-REC-001 | Low | Recency and Renewals overview has no page Help (?) |
| Recency and Renewals (overview page) | BUG-REC-002 | Low | Recency and Renewals at phone width: the table is cut off, so Total Items and Actions are hidden |
| Safety Reports (SMS) | BUG-SMS-005 | High | Safety Reports: group-level (WG) and own-level (WO) users see no reports at all, not even ones they submitted |
| Safety Reports (SMS) | BUG-SMS-001 | Medium | New Safety Report: Escape on the Confidential/Anonymous help closes the report form behind it and loses what you typed |
| Safety Reports (SMS) | BUG-SMS-002 | Medium | New Safety Report: Event Date/Time defaults to the UTC date and time, not local |
| Safety Reports (SMS) | BUG-SMS-003 | Low | Safety Report Final Report: Likelihood and Consequence dropdowns list every option twice |
| Safety Reports (SMS) | BUG-SMS-004 | Low | Add to Hazard Register: Goal 'Mitigate' shows as 'Minimize' in the Hazard Register |
| Hazard Register | BUG-HAZ-001 | Medium | Hazard Register details: Hazard Type always shows '--' |
| Hazard Register | BUG-HAZ-002 | Medium | Hazard Register details: Final Risk Assessment never shows the saved final risk |
| Hazard Register | BUG-HAZ-003 | Low | Hazard Register has no way to create a hazard entry |
| File Browser | BUG-FB-003 | Medium | File Browser: clicking a .txt file shows 'File Access Error' with the file's own text |
| File Browser | BUG-FB-005 | Medium | File Browser: Read/Write Access groups are not kept after Update Document |
| File Browser | BUG-FB-006 | Medium | File Browser: deleting a folder fails with 'Invalid Action: filebrowser_deletefolder' |
| File Browser | BUG-FB-001 | Low | File Browser has no page Help (?) |
| File Browser | BUG-FB-002 | Low | File Browser shows Date Uploaded as 'Oct 22, 2026' instead of DD/MM/YYYY |
| File Browser | BUG-FB-004 | Low | File Browser: Escape doesn't close the Create New Folder or Configure File popups |
| File Browser | BUG-FB-007 | Low | File Browser on a phone: table is cut off, edit buttons are off-screen |
| Form Builder | BUG-FBLD-002 | Medium | Form Builder View Form: Date and Time widgets default to UTC, not local time |
| Form Builder | BUG-FBLD-003 | Medium | Form Builder: table conditions do nothing in View Form |
| Form Builder | BUG-FBLD-001 | Low | Form Builder: popups ignore Escape and outside clicks (Help, Create New Form Template, Edit Options) |
| Form Builder | BUG-FBLD-004 | Low | Form Builder on a phone: page is wider than the screen and the Toolbox covers the form |
| Form Browser / Form Viewer | BUG-FBR-001 | Low | Form Browser has no page Help (?) |
| Form Browser / Form Viewer | BUG-FBR-002 | Low | Form Browser and Form Viewer dates ignore the date setting ('Oct 21, 2026', '10:24 PM') |
| Form Browser / Form Viewer | BUG-FBR-003 | Low | Form Browser on a phone: table is cut off, Created and Created By are off-screen |
| Task Tracker | BUG-TT-004 | Medium | Task Tracker: a Write Group (WG) user is treated as read-only and can't add a project |
| Task Tracker | BUG-TT-001 | Low | Task Tracker: Escape doesn't close Help or Add Project |
| Task Tracker | BUG-TT-002 | Low | Task Tracker dates ignore the date setting ('Dec 31', '2026-10-21') |
| Task Tracker | BUG-TT-003 | Low | Task Tracker on a phone: feature cards are pushed right and cut off |
| Reports | BUG-RPT-003 | Medium | Reports tables overlap on a phone: column text is drawn on top of other columns |
| Reports | BUG-RPT-001 | Low | Reports has no page Help (?), and Escape doesn't close New Report Template |
| Reports | BUG-RPT-002 | Low | Reports Export CSV writes dates as '2026-10-16 06:00:00' instead of the org date format |
| Reports | BUG-RPT-004 | Low | Reports: the Flight Hours meter column shows the aircraft's current meter on every flight, and Total adds them up |
| Support tickets | BUG-SUP-001 | Medium | Support has no page Help (?); Escape doesn't close New Ticket, but a click outside closes it and wipes everything typed |
| Support tickets | BUG-SUP-004 | Medium | Support: the only permission level is All Access, so regular staff can't raise or see their own tickets |
| Support tickets | BUG-SUP-002 | Low | Support New Ticket: Ctrl+V doesn't paste a screenshot, though the error message tells you to use Ctrl+V |
| Support tickets | BUG-SUP-003 | Low | Support ticket: clicking a .txt attachment shows an 'Error' popup containing the file's text |
| Chat | BUG-AM-006 | Medium | Access Manager has no Chat permission, so you can't give Chat to a non-admin user |
| Chat | BUG-CHAT-001 | Low | Chat has no page Help (?); Escape doesn't close Create Channel; empty name does nothing with no message |
| Chat | BUG-CHAT-002 | Low | Chat times show 12-hour '01:32 AM' and date separators 'Thursday, October 22, 2026' instead of the org format |
| Exam Builder, Exam Editor, Exam Instances | BUG-EXM-006 | High | Taking an exam: Multi-Response checkboxes toggle twice, so clicking the box does nothing and the saved answer can differ from what is ticked |
| Exam Builder, Exam Editor, Exam Instances | BUG-EXM-004 | Medium | Exam Builder has no way to link or unlink user groups on an exam group |
| Exam Builder, Exam Editor, Exam Instances | BUG-EXM-008 | Medium | Exam Builder: deleting an exam or exam group that has instances fails silently (error only in the console), and graded instances can't be removed |
| Exam Builder, Exam Editor, Exam Instances | BUG-EXM-001 | Low | Exam Builder/Editor have no page Help (?); Escape doesn't close Add Group, Add Exam or Choose Question Type |
| Exam Builder, Exam Editor, Exam Instances | BUG-EXM-002 | Low | Exam dates ignore the org format: 'Oct 22, 2026' in Exam Builder and '10/22/2026 01:46 AM' in Exam Instances batches |
| Exam Builder, Exam Editor, Exam Instances | BUG-EXM-003 | Low | Exam viewer 'Read Only' still shows Add Question, Add Group and Save Question |
| Exam Builder, Exam Editor, Exam Instances | BUG-EXM-005 | Low | Exam Builder on a phone: exam table columns and action icons overlap |
| Exam Builder, Exam Editor, Exam Instances | BUG-EXM-007 | Low | Exam Instances batch: deleting a person's instance shows success but the row stays until the page is reloaded |
| Settings – Flight Schedule | BUG-SFS-002 | High | Changing Schedule Start Time saves a full date-time, and the setting then shows NaN:NaN |
| Settings – Flight Schedule | BUG-SFS-001 | Low | Flight Schedule settings: Slot Duration + goes past 120 and typed values over 120 are accepted |
| Settings – Daily Flight Record | BUG-SDFR-001 | Low | Daily Flight Record Settings loads a colorpicker.js that does not exist (404 in the console) |
| Settings – Time Zone (date/time matrix) | BUG-STZ-001 | Medium | Time Zone settings: the Example preview shows UTC, not the selected time zone |
| Settings – Time Zone (date/time matrix) | BUG-STZ-003 | Medium | Time Zone settings: the Example preview shows MM/DD/YYYY for every date format except DD/MM/YYYY |
| Settings – Time Zone (date/time matrix) | BUG-STZ-002 | Low | Time Zone settings page has no Help (?) |
| Settings – Resources (Aircraft) | BUG-SRES-001 | Low | Resources: the meter "Last:" dates show as YYYY-MM-DD instead of the Time Zone date format |
| Settings – Weight and Balance Configs | BUG-SWAB-001 | Low | Weight & Balance Configs: no Help (?), and Escape does not close popups |
| Settings – Weight and Balance Configs | BUG-SWAB-002 | Low | Weight & Balance Configs: dates show as "14 Oct 2026" / "29 Sept 2026" instead of DD/MM/YYYY |
| Settings – Weight and Balance Configs | BUG-SWAB-003 | Low | Weight & Balance Configs shows a debug "Performance" timing panel to users |
| Settings – Weight and Balance Configs | BUG-SWAB-004 | Low | Weight & Balance Configs: on a phone the page is wider than the screen |
| Settings – Weight and Balance Configs | BUG-SWAB-005 | Low | W&B Configs: two revisions show the same number ("Rev 5") until another import renumbers them |
| Settings – Extra Flight Info | BUG-SEFI-001 | Low | Extra Flight Info Settings: no Help (?), and Escape does not close Add Field |
| Settings – Flight Types | BUG-SFT-002 | Medium | Flight Types: a duplicate Flight Category name ("PIC") is accepted |
| Settings – Flight Types | BUG-SFT-001 | Low | Flight Types Settings: no Help (?), and Escape does not close popups |
| Settings – Waypoint Locations | BUG-SWP-002 | Medium | Waypoints: moving a waypoint about 250 nm saves with no "Significant Location Change" warning |
| Settings – Waypoint Locations | BUG-SWP-004 | Medium | Waypoints on a phone: table columns overlap and Add Waypoint is off-screen |
| Settings – Waypoint Locations | BUG-SWP-001 | Low | Waypoints Settings: no Help (?), and Escape does not close popups |
| Settings – Waypoint Locations | BUG-SWP-003 | Low | Waypoints: the list is not refreshed after you save or delete on the detail page |
| Settings – Roster Shifts | BUG-SST-004 | Medium | Roster Shifts on a phone: the table scrolls the page sideways and the group tabs are hidden |
| Settings – Roster Shifts | BUG-SST-001 | Low | Roster Shifts (Shift Type Editor): no Help (?), and Escape does not close popups |
| Settings – Roster Shifts | BUG-SST-002 | Low | New Shift Type: Duty Start/End Time default to the current UTC time |
| Settings – Roster Shifts | BUG-SST-003 | Low | Roster Shifts: after Edit Group the selected group jumps back to Duty, so the next New Shift Type goes into the wrong group |
| Settings – Fatigue Risk Management | BUG-SFRMS-001 | Low | FRMS Settings: no Help (?), and Escape does not close popups |
| Settings – Fatigue Risk Management | BUG-SFRMS-002 | Low | FRMS Settings on a phone: the page scrolls sideways, "+ Add ... Rule" is off-screen and rule text is clipped |
| Settings – Recency and Renewals | BUG-SREN-002 | Medium | Add Recency accepts negative Days, and a Caution value higher than Warning |
| Settings – Recency and Renewals | BUG-SREN-003 | Medium | Add Renewal Type accepts negative Days to Notify and a Frequency of 0 days |
| Settings – Recency and Renewals | BUG-SREN-001 | Low | Recency & Renewals Settings: no Help (?), and Escape does not close popups |
| Settings – Recency and Renewals | BUG-SREN-004 | Low | Recency & Renewals Settings on a phone: table columns overlap each other |
| Settings – Lesson Plans | BUG-SLP-002 | High | Lesson Plan Settings: Exercises are never saved; add/edit/delete only change the page and are lost when you leave |
| Settings – Lesson Plans | BUG-SLP-001 | Low | Lesson Plan Settings: no Help (?), and Escape does not close popups |
| Settings – Lesson Plans | BUG-SLP-003 | Low | Add Lesson accepts negative hours (Solo Hours -1 is saved and shown as "Solo: -1h") |
| Settings – Risk Matrix | BUG-SRM-001 | Low | Risk Matrix Settings: no Help (?), and Escape does not close popups |
| Settings – Risk Matrix | BUG-SRM-002 | Low | Risk Matrix Settings on a phone: the page scrolls sideways and "+ Add Level" is cut off |
| Settings – Safety Reports | BUG-SSMS-001 | Low | Safety Reports Settings: no Help (?), and Escape does not close popups |
| Settings – Inspection Notifications | BUG-SINS-002 | Medium | Inspection Notifications: a meter inspection on an aircraft at 0.0 hours is never Overdue, and negative meter values are accepted |
| Settings – Inspection Notifications | BUG-SINS-001 | Low | Inspection Notifications Settings: no Help (?), and Escape does not close popups |
| Settings – Inspection Notifications | BUG-SINS-003 | Low | Inspection Notifications: trigger date shows as 2026-10-01, Add Inspection defaults to the UTC date, and the overdue day count is one day short |
| Settings – Google Calendar, WhatsApp | BUG-SINT-001 | Low | Google Calendar Settings: Help and Add Calendar don't close with Escape or an outside click |
| Settings – Google Calendar, WhatsApp | BUG-SINT-002 | Low | Google Calendar Sync Status: flight dates show as 2024-01-01 07:55 instead of DD/MM/YYYY |
| Settings – Activity Log | BUG-SLOG-001 | Low | Activity Log: no page Help (?), and dates show as "22 Oct 2026, 02:51 am" |
| Cross-cutting: permission levels | BUG-AM-005 | Medium | Access Manager: 16 permission types appear twice with the same name (e.g. two "Flight Schedule" cards with different levels) |
| Cross-cutting: permission levels | BUG-PERM-002 | Medium | User with no permissions cannot open their own My Account (no self-service password / 2FA) |
| Cross-cutting: permission levels | BUG-AM-007 | Low | Access Manager: a customer created from Flight Details is Active with no login credentials |
| Cross-cutting: permission levels | BUG-PERM-001 | Low | Sidebar lists modules the user has no permission for (all lead to Access Denied) |
| Cross-cutting: date/time formats and pickers | BUG-DATE-001 | Medium | Flight time across a DST change is out by an hour (01:00-05:00 on 04/04/2027 gives 4.0 instead of 5.0) |
| Cross-cutting: date/time formats and pickers | BUG-FD-007 | Medium | New flight defaults its leg date/time to UTC instead of local time |
| Cross-cutting: performance, console and network | BUG-PERF-001 | Low | 'Performance' debug timing panel shown on every page, including to non-admin users |
