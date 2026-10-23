# DataHangar audit: bugs by module

Module = internal action name (`?action=`). Totals: 598 pass, 145 fail, 26 blocked, 190 bugs (10 High, 71 Medium, 109 Low).

## Summary

| Module | Pass | Fail | Blocked | Bugs |
|---|---|---|---|---|
| (setup) | 9 | 0 | 0 | 0 |
| login | 19 | 0 | 1 | 3 |
| main | 24 | 1 | 1 | 1 |
| (all modules) | 17 | 5 | 0 | 0 |
| settings_accessmanager | 36 | 1 | 0 | 7 |
| dashboard | 19 | 0 | 0 | 4 |
| flightschedule | 37 | 1 | 0 | 9 |
| flightdetails | 44 | 0 | 0 | 10 |
| activeflights | 19 | 0 | 0 | 5 |
| dailyflightrecord | 14 | 2 | 0 | 3 |
| locationplanner (no menu path) | 0 | 0 | 9 | 0 |
| personnellist | 10 | 1 | 0 | 2 |
| personneldetails | 21 | 15 | 0 | 20 |
| rosterviewer | 9 | 3 | 0 | 3 |
| settings_rosterbuilder | 13 | 8 | 0 | 8 |
| timesheets | 11 | 6 | 0 | 8 |
| flightandduty | 12 | 2 | 0 | 5 |
| notices | 12 | 4 | 0 | 4 |
| recencyandrenewals | 7 | 2 | 0 | 2 |
| smsreports | 18 | 2 | 1 | 5 |
| hazardregister | 8 | 2 | 0 | 3 |
| systemsettings | 10 | 1 | 0 | 0 |
| filebrowser | 8 | 6 | 0 | 7 |
| settings_formbuilder | 10 | 4 | 0 | 4 |
| formbrowser | 7 | 3 | 0 | 3 |
| tasktracker | 8 | 4 | 0 | 4 |
| reports | 13 | 3 | 0 | 4 |
| support | 11 | 3 | 0 | 4 |
| chat | 8 | 2 | 1 | 3 |
| settings_exambuilder / settings_examinstances | 10 | 6 | 0 | 10 |
| maintenance (no menu path) | 0 | 0 | 11 | 0 |
| settings_flightschedule | 12 | 0 | 0 | 2 |
| settings_dfr | 5 | 1 | 0 | 1 |
| settings_timezone | 7 | 4 | 0 | 3 |
| settings_resources | 16 | 2 | 0 | 1 |
| settings_wabconfigs | 9 | 4 | 0 | 5 |
| settings_extraflightinfo | 7 | 1 | 0 | 1 |
| settings_flighttypes | 5 | 2 | 0 | 2 |
| settings_waypoints | 8 | 3 | 0 | 4 |
| settings_shifttypes | 7 | 3 | 0 | 4 |
| settings_frms | 8 | 2 | 0 | 2 |
| settings_renewals | 5 | 4 | 0 | 4 |
| settings_lessonplans | 5 | 3 | 0 | 3 |
| settings_riskmatrix | 6 | 2 | 0 | 2 |
| settings_smsreports | 7 | 1 | 0 | 1 |
| settings_inspections | 6 | 3 | 0 | 3 |
| settings_googlecalendar / WhatsApp | 6 | 2 | 2 | 2 |
| settings_activitylog | 6 | 2 | 0 | 1 |
| (cross-cutting: permissions) | 10 | 0 | 0 | 4 |
| (cross-cutting: popups) | 4 | 4 | 0 | 0 |
| (cross-cutting: dates) | 3 | 4 | 0 | 2 |
| (cross-cutting: mobile) | 2 | 2 | 0 | 0 |
| (cross-cutting: UI/icons) | 3 | 4 | 0 | 0 |
| (cross-cutting: performance) | 1 | 3 | 0 | 1 |
| (end-to-end) | 0 | 0 | 0 | 0 |

## Bugs

| Module | Bug | Severity | Title |
|---|---|---|---|
| login | BUG-LOG-003 | Medium | 'Trust this device for 30 days' is lost on Logout (logout deletes the trusted-device cookie) |
| login | BUG-LOG-001 | Low | Login Message popup reappears on every browser reload |
| login | BUG-LOG-002 | Low | Logout throws JS error removeChild; Esc doesn't close the Log Out confirm |
| main | BUG-NAV-001 | Medium | Leaving a page with unsaved changes gives no warning; edits are lost |
| settings_accessmanager | BUG-AM-001 | Medium | New User accepts a 6-character password (placeholder and Change Credentials require 10) |
| settings_accessmanager | BUG-POP-003 | Medium | Access Manager Groups popup: Esc closes with unsaved changes and no warning; reopening shows the unsaved ticks as if saved |
| settings_accessmanager | BUG-AM-002 | Low | Last Activity hover date ignores Settings > Time Zone format |
| settings_accessmanager | BUG-AM-003 | Low | Last Activity column sort does not change order |
| settings_accessmanager | BUG-AM-004 | Low | Permission level dropdown shows bare codes 'WA' and 'G' next to full labels |
| settings_accessmanager | BUG-POP-001 | Low | Error modal ('Failed to Create User') does not close with Esc |
| settings_accessmanager | BUG-POP-002 | Low | Manage User Permissions uses a native browser confirm() for unsaved changes |
| dashboard | BUG-DSH-003 | Medium | Dashboard recency item opens Personnel Details on the wrong tab (Personal Details instead of Recency and Renewals) |
| dashboard | BUG-DSH-004 | Medium | Dashboard: My Flights and On Duty open on the UTC date, not today's local date |
| dashboard | BUG-DSH-005 | Medium | Dashboard Project Tasks: clicking a task opens an empty project list instead of the project |
| dashboard | BUG-DSH-001 | Low | Dashboard side tabs are icon-only with no tooltip or label |
| flightschedule | BUG-FS-008 | High | Flight Schedule: a group-level user (G / WG) sees no flights, even on aircraft in their own group |
| flightschedule | BUG-FS-001 | Medium | New flight defaults to the current UTC time instead of local time (SAR TIME labelled LOCAL shows UTC+1h) |
| flightschedule | BUG-FS-002 | Medium | Esc does not end copy/paste mode on the Flight Schedule - the next click + Ctrl+V creates another flight |
| flightschedule | BUG-FS-003 | Medium | Flight Schedule header overlaps when Live Edit is on - title covered, location pill cut off and its 'Show All' button cannot be clicked |
| flightschedule | BUG-FS-004 | Medium | Planner Add Location replaces the New Booking popup - typed booking and location input is lost |
| flightschedule | BUG-FS-006 | Medium | Flight Schedule month view is slow: flightschedule_json takes ~1.6 s and rendering 2,500 events ~4.5 s |
| flightschedule | BUG-FS-007 | Medium | Edit-mode idle timeout switches Live Edit off silently, throws 'calendarEl is not defined' and leaves the schedule blank |
| flightschedule | BUG-FS-005 | Low | JS error on every Live Edit toggle: Cannot read properties of null (reading 'scrollTop') |
| flightschedule | BUG-POP-004 | Low | Flight Schedule popups (View Details, Double Booking alert, note modals) do not close with Esc |
| flightdetails | BUG-FD-001 | Medium | Flight Details Save Changes does not return to the Flight Schedule and gives no success message |
| flightdetails | BUG-FD-002 | Medium | Flight Details History misses edits saved in Flight Details and shows a false 'Aircraft: ZK-SIM > Unassigned' on schedule moves |
| flightdetails | BUG-FD-004 | Medium | Leg PIC / Secondary Flight Crew dropdowns offer passengers (e.g. a custom passenger can be chosen as leg PIC) |
| flightdetails | BUG-FD-005 | Medium | Leg with two unknown waypoints: only the first is offered for adding, the second is silently dropped on save |
| flightdetails | BUG-FD-006 | Medium | Flight can be set to Complete with no times or destination on a leg; no 'Required Information' prompt |
| flightdetails | BUG-FD-003 | Low | Times and Meters: no link to the previous flight next to 'Previous' meter readings |
| activeflights | BUG-AF-004 | High | Active Flights overdue and active times are 13 h out: local SAR/start times are compared with UTC 'now' |
| activeflights | BUG-AF-002 | Medium | Active Flights lists future flights that have no SAR time, and the stats cards don't count them |
| activeflights | BUG-AF-005 | Medium | Active Flights: a Read Only Group (RG) user sees every company flight, not only their group's |
| activeflights | BUG-AF-001 | Low | Active Flights shows SAR Time '01/01/1970 00:00' for flights with SAR watch disabled |
| activeflights | BUG-AF-003 | Low | Active Flights has no page Help (?), and its popups (About Live Tracking, Adjust SAR, Add Note) don't close with Escape |
| dailyflightrecord | BUG-DFR-002 | Medium | Daily Flight Record: Clear Filters unticks every status (lists Open, Cancelled and Deleted flights), and the date fields show today's date when no date filter is applied |
| dailyflightrecord | BUG-DFR-003 | Medium | Daily Flight Record: changing filters quickly appends results instead of replacing them, showing duplicate and wrong-status rows |
| dailyflightrecord | BUG-DFR-001 | Low | Daily Flight Record has no page Help (?), and its popups (Manage Columns, Notes full text) don't close with Escape |
| personnellist | BUG-PL-001 | Low | All Personnel has no page Help (?) |
| personnellist | BUG-PL-002 | Low | A person with no name exists and is listed as '?' at the top of All Personnel (person #274, Customer) |
| personneldetails | BUG-PD-006 | High | Personnel Details > Recency and Renewals: action buttons are hidden (Add Item, Table/Card view, renewal Save / Complete Renewal / Cancel) and Group by / Order by are disabled |
| personneldetails | BUG-PD-011 | High | Personnel Details > Security: Change Password always fails with 'Invalid Action: change_password' |
| personneldetails | BUG-PD-001 | Medium | personneldetails/index.js is truncated: ReferenceError getPickerMod on every load |
| personneldetails | BUG-PD-003 | Medium | 2FA setup: one wrong verification code closes the setup dialog and issues a new secret |
| personneldetails | BUG-PD-007 | Medium | Personnel Details > Recency: 'Days Until Expiry' and status don't match the Last Conducted date |
| personneldetails | BUG-PD-008 | Medium | Personnel Details > Recency: the recency summary popup has no Add Manual Entry, no x, and doesn't close with Escape |
| personneldetails | BUG-PD-009 | Medium | Personnel Details > Renewal edit: the Today and Calculate links can't be clicked because the date fields cover them |
| personneldetails | BUG-PD-012 | Medium | Personnel Details > Files: opening a file shows 'File Access Error' with the file's contents as the message |
| personneldetails | BUG-PD-016 | Medium | Personnel Details > Timesheets: Add Claim button does nothing |
| personneldetails | BUG-PD-017 | Medium | Personnel Details > Lesson Plans: an assigned plan is saved but never listed; the dialog's dates default to the UTC date |
| personneldetails | BUG-PL-003 | Medium | All Personnel: a Read Only Group (RG) user can't open the details of anyone in their group |
| personneldetails | BUG-EXM-009 | Low | Exams: a hotspot question with no image shows a developer debug message to the person taking the exam |
| personneldetails | BUG-PD-002 | Low | Personnel Details modals (Enable 2FA, Setup Error alert): title right-aligned, away from its icon |
| personneldetails | BUG-PD-004 | Low | Security tab 'Enabled on' date ignores Settings > Time Zone format |
| personneldetails | BUG-PD-005 | Low | Personnel Details: History, PDF Options and Legacy Duty Browser popups don't close with Escape, and PDF Options has no x |
| personneldetails | BUG-PD-010 | Low | Personnel Details: the 'Performance' timing panel is shown to users and covers buttons |
| personneldetails | BUG-PD-013 | Low | Personnel Details: an empty Birth Date shows today's date |
| personneldetails | BUG-PD-014 | Low | Digital Signature: wrong password closes the popup and throws away the drawing; empty Save gives no message |
| personneldetails | BUG-PD-015 | Low | Flight & Duty Analysis popup: title date is YYYY-MM-DD and Escape doesn't close it |
| personneldetails | BUG-PD-018 | Low | Request Leave: Start and End Date default to the UTC date, not today's local date |
| rosterviewer | BUG-RV-002 | Medium | Roster Viewer: clicking a shift does not open Shift Details |
| rosterviewer | BUG-RV-001 | Low | Roster Viewer: no page Help (?) and Group Visibility popup ignores Escape |
| rosterviewer | BUG-RV-003 | Low | Roster Viewer shift note popup shows the date as 'October 5, 2026', not the configured DD/MM/YYYY |
| settings_rosterbuilder | BUG-RB-007 | High | Roster Builder: Clear then Publish of a draft month with no shifts does not clear the live roster and shows no message |
| settings_rosterbuilder | BUG-RB-002 | Medium | Roster Builder: Copy Live to Draft copies one shift at a time and takes about 6 minutes for one month |
| settings_rosterbuilder | BUG-RB-003 | Medium | Roster Builder: copy/paste still works with violation checking ON |
| settings_rosterbuilder | BUG-RB-005 | Medium | Roster Builder: every validation error throws a JS error instead of showing a message (e.g. Apply Shift Pattern with no shifts) |
| settings_rosterbuilder | BUG-RB-008 | Medium | Roster Builder can only be opened from Settings and Tools, so a Roster Builder user without System Settings can't reach it |
| settings_rosterbuilder | BUG-RB-001 | Low | Roster Builder: no page Help (?); Copy/Paste Instructions popup ignores Escape and outside click |
| settings_rosterbuilder | BUG-RB-004 | Low | Roster Builder: Rule Violations popup shows 'Monday, October 5' instead of the configured DD/MM/YYYY date |
| settings_rosterbuilder | BUG-RB-006 | Low | Roster Builder: at phone width the shift palette takes half the screen and the Draft Edit Mode banner covers the search box and palette |
| timesheets | BUG-TS-002 | Medium | Timesheet Approval: status filter 'Unsigned' shows 'No personnel found' although everyone has unsigned days |
| timesheets | BUG-TS-003 | Medium | Timesheet Approval list totals don't match Timesheet Details (Rostered Days and Duty Hours) |
| timesheets | BUG-TS-008 | Medium | Approving a leave request doesn't change the rostered shifts, and rejecting with no reason gives no message |
| timesheets | BUG-TS-001 | Low | Timesheets: no page Help on Timesheet Approval, and the Help (?) on Timesheet Details does nothing |
| timesheets | BUG-TS-004 | Low | Timesheet Details shows dates as 'Oct 5' and times with seconds (14:00:00) |
| timesheets | BUG-TS-005 | Low | Timesheet Details: F&D and Roster Violation popups ignore Escape and show ISO dates in the title |
| timesheets | BUG-TS-006 | Low | Leave Types: a validation error closes the Add Leave Type popup and throws away what you typed; the popup ignores Escape |
| timesheets | BUG-TS-007 | Low | Reject Claim: leaving the reason empty closes the reject popup and throws a script error |
| flightandduty | BUG-FAD-001 | Low | Flight and Duty has no page Help (?) |
| flightandduty | BUG-FAD-002 | Low | Flight and Duty popups (Flight Details, Duty Time Details, Roster Violations, Resolutions Required) ignore Escape |
| flightandduty | BUG-FAD-003 | Low | Flight and Duty popups show dates as '16 Oct 2026' instead of the configured DD/MM/YYYY |
| flightandduty | BUG-FAD-004 | Low | Flight and Duty column headers are ambiguous: two '1 Days' and two '24 Hours' columns, and '1 Days' is ungrammatical |
| flightandduty | BUG-FAD-005 | Low | Flight and Duty 'View as Date' defaults to the UTC date instead of the local date |
| notices | BUG-NOT-002 | Medium | Notice Details: clicking a .txt attachment does nothing (no preview, no download) |
| notices | BUG-NOT-004 | Medium | Notices: a Write Group (WG) user gets 'An error occurred' when clicking New Notice |
| notices | BUG-NOT-001 | Low | Notices has no page Help (?), and the Create New Notice popup ignores Escape |
| notices | BUG-NOT-003 | Low | Settings and Tools hub: 'Notices' card has no links |
| recencyandrenewals | BUG-REC-001 | Low | Recency and Renewals overview has no page Help (?) |
| recencyandrenewals | BUG-REC-002 | Low | Recency and Renewals at phone width: the table is cut off, so Total Items and Actions are hidden |
| smsreports | BUG-SMS-005 | High | Safety Reports: group-level (WG) and own-level (WO) users see no reports at all, not even ones they submitted |
| smsreports | BUG-SMS-001 | Medium | New Safety Report: Escape on the Confidential/Anonymous help closes the report form behind it and loses what you typed |
| smsreports | BUG-SMS-002 | Medium | New Safety Report: Event Date/Time defaults to the UTC date and time, not local |
| smsreports | BUG-SMS-003 | Low | Safety Report Final Report: Likelihood and Consequence dropdowns list every option twice |
| smsreports | BUG-SMS-004 | Low | Add to Hazard Register: Goal 'Mitigate' shows as 'Minimize' in the Hazard Register |
| hazardregister | BUG-HAZ-001 | Medium | Hazard Register details: Hazard Type always shows '--' |
| hazardregister | BUG-HAZ-002 | Medium | Hazard Register details: Final Risk Assessment never shows the saved final risk |
| hazardregister | BUG-HAZ-003 | Low | Hazard Register has no way to create a hazard entry |
| filebrowser | BUG-FB-003 | Medium | File Browser: clicking a .txt file shows 'File Access Error' with the file's own text |
| filebrowser | BUG-FB-005 | Medium | File Browser: Read/Write Access groups are not kept after Update Document |
| filebrowser | BUG-FB-006 | Medium | File Browser: deleting a folder fails with 'Invalid Action: filebrowser_deletefolder' |
| filebrowser | BUG-FB-001 | Low | File Browser has no page Help (?) |
| filebrowser | BUG-FB-002 | Low | File Browser shows Date Uploaded as 'Oct 22, 2026' instead of DD/MM/YYYY |
| filebrowser | BUG-FB-004 | Low | File Browser: Escape doesn't close the Create New Folder or Configure File popups |
| filebrowser | BUG-FB-007 | Low | File Browser on a phone: table is cut off, edit buttons are off-screen |
| settings_formbuilder | BUG-FBLD-002 | Medium | Form Builder View Form: Date and Time widgets default to UTC, not local time |
| settings_formbuilder | BUG-FBLD-003 | Medium | Form Builder: table conditions do nothing in View Form |
| settings_formbuilder | BUG-FBLD-001 | Low | Form Builder: popups ignore Escape and outside clicks (Help, Create New Form Template, Edit Options) |
| settings_formbuilder | BUG-FBLD-004 | Low | Form Builder on a phone: page is wider than the screen and the Toolbox covers the form |
| formbrowser | BUG-FBR-001 | Low | Form Browser has no page Help (?) |
| formbrowser | BUG-FBR-002 | Low | Form Browser and Form Viewer dates ignore the date setting ('Oct 21, 2026', '10:24 PM') |
| formbrowser | BUG-FBR-003 | Low | Form Browser on a phone: table is cut off, Created and Created By are off-screen |
| tasktracker | BUG-TT-004 | Medium | Task Tracker: a Write Group (WG) user is treated as read-only and can't add a project |
| tasktracker | BUG-TT-001 | Low | Task Tracker: Escape doesn't close Help or Add Project |
| tasktracker | BUG-TT-002 | Low | Task Tracker dates ignore the date setting ('Dec 31', '2026-10-21') |
| tasktracker | BUG-TT-003 | Low | Task Tracker on a phone: feature cards are pushed right and cut off |
| reports | BUG-RPT-003 | Medium | Reports tables overlap on a phone: column text is drawn on top of other columns |
| reports | BUG-RPT-001 | Low | Reports has no page Help (?), and Escape doesn't close New Report Template |
| reports | BUG-RPT-002 | Low | Reports Export CSV writes dates as '2026-10-16 06:00:00' instead of the org date format |
| reports | BUG-RPT-004 | Low | Reports: the Flight Hours meter column shows the aircraft's current meter on every flight, and Total adds them up |
| support | BUG-SUP-001 | Medium | Support has no page Help (?); Escape doesn't close New Ticket, but a click outside closes it and wipes everything typed |
| support | BUG-SUP-004 | Medium | Support: the only permission level is All Access, so regular staff can't raise or see their own tickets |
| support | BUG-SUP-002 | Low | Support New Ticket: Ctrl+V doesn't paste a screenshot, though the error message tells you to use Ctrl+V |
| support | BUG-SUP-003 | Low | Support ticket: clicking a .txt attachment shows an 'Error' popup containing the file's text |
| chat | BUG-AM-006 | Medium | Access Manager has no Chat permission, so you can't give Chat to a non-admin user |
| chat | BUG-CHAT-001 | Low | Chat has no page Help (?); Escape doesn't close Create Channel; empty name does nothing with no message |
| chat | BUG-CHAT-002 | Low | Chat times show 12-hour '01:32 AM' and date separators 'Thursday, October 22, 2026' instead of the org format |
| settings_exambuilder / settings_examinstances | BUG-EXM-006 | High | Taking an exam: Multi-Response checkboxes toggle twice, so clicking the box does nothing and the saved answer can differ from what is ticked |
| settings_exambuilder / settings_examinstances | BUG-EXM-004 | Medium | Exam Builder has no way to link or unlink user groups on an exam group |
| settings_exambuilder / settings_examinstances | BUG-EXM-008 | Medium | Exam Builder: deleting an exam or exam group that has instances fails silently (error only in the console), and graded instances can't be removed |
| settings_exambuilder / settings_examinstances | BUG-EXM-001 | Low | Exam Builder/Editor have no page Help (?); Escape doesn't close Add Group, Add Exam or Choose Question Type |
| settings_exambuilder / settings_examinstances | BUG-EXM-002 | Low | Exam dates ignore the org format: 'Oct 22, 2026' in Exam Builder and '10/22/2026 01:46 AM' in Exam Instances batches |
| settings_exambuilder / settings_examinstances | BUG-EXM-003 | Low | Exam viewer 'Read Only' still shows Add Question, Add Group and Save Question |
| settings_exambuilder / settings_examinstances | BUG-EXM-005 | Low | Exam Builder on a phone: exam table columns and action icons overlap |
| settings_exambuilder / settings_examinstances | BUG-EXM-007 | Low | Exam Instances batch: deleting a person's instance shows success but the row stays until the page is reloaded |
| settings_flightschedule | BUG-SFS-002 | High | Changing Schedule Start Time saves a full date-time, and the setting then shows NaN:NaN |
| settings_flightschedule | BUG-SFS-001 | Low | Flight Schedule settings: Slot Duration + goes past 120 and typed values over 120 are accepted |
| settings_dfr | BUG-SDFR-001 | Low | Daily Flight Record Settings loads a colorpicker.js that does not exist (404 in the console) |
| settings_timezone | BUG-STZ-001 | Medium | Time Zone settings: the Example preview shows UTC, not the selected time zone |
| settings_timezone | BUG-STZ-003 | Medium | Time Zone settings: the Example preview shows MM/DD/YYYY for every date format except DD/MM/YYYY |
| settings_timezone | BUG-STZ-002 | Low | Time Zone settings page has no Help (?) |
| settings_resources | BUG-SRES-001 | Low | Resources: the meter "Last:" dates show as YYYY-MM-DD instead of the Time Zone date format |
| settings_wabconfigs | BUG-SWAB-001 | Low | Weight & Balance Configs: no Help (?), and Escape does not close popups |
| settings_wabconfigs | BUG-SWAB-002 | Low | Weight & Balance Configs: dates show as "14 Oct 2026" / "29 Sept 2026" instead of DD/MM/YYYY |
| settings_wabconfigs | BUG-SWAB-003 | Low | Weight & Balance Configs shows a debug "Performance" timing panel to users |
| settings_wabconfigs | BUG-SWAB-004 | Low | Weight & Balance Configs: on a phone the page is wider than the screen |
| settings_wabconfigs | BUG-SWAB-005 | Low | W&B Configs: two revisions show the same number ("Rev 5") until another import renumbers them |
| settings_extraflightinfo | BUG-SEFI-001 | Low | Extra Flight Info Settings: no Help (?), and Escape does not close Add Field |
| settings_flighttypes | BUG-SFT-002 | Medium | Flight Types: a duplicate Flight Category name ("PIC") is accepted |
| settings_flighttypes | BUG-SFT-001 | Low | Flight Types Settings: no Help (?), and Escape does not close popups |
| settings_waypoints | BUG-SWP-002 | Medium | Waypoints: moving a waypoint about 250 nm saves with no "Significant Location Change" warning |
| settings_waypoints | BUG-SWP-004 | Medium | Waypoints on a phone: table columns overlap and Add Waypoint is off-screen |
| settings_waypoints | BUG-SWP-001 | Low | Waypoints Settings: no Help (?), and Escape does not close popups |
| settings_waypoints | BUG-SWP-003 | Low | Waypoints: the list is not refreshed after you save or delete on the detail page |
| settings_shifttypes | BUG-SST-004 | Medium | Roster Shifts on a phone: the table scrolls the page sideways and the group tabs are hidden |
| settings_shifttypes | BUG-SST-001 | Low | Roster Shifts (Shift Type Editor): no Help (?), and Escape does not close popups |
| settings_shifttypes | BUG-SST-002 | Low | New Shift Type: Duty Start/End Time default to the current UTC time |
| settings_shifttypes | BUG-SST-003 | Low | Roster Shifts: after Edit Group the selected group jumps back to Duty, so the next New Shift Type goes into the wrong group |
| settings_frms | BUG-SFRMS-001 | Low | FRMS Settings: no Help (?), and Escape does not close popups |
| settings_frms | BUG-SFRMS-002 | Low | FRMS Settings on a phone: the page scrolls sideways, "+ Add ... Rule" is off-screen and rule text is clipped |
| settings_renewals | BUG-SREN-002 | Medium | Add Recency accepts negative Days, and a Caution value higher than Warning |
| settings_renewals | BUG-SREN-003 | Medium | Add Renewal Type accepts negative Days to Notify and a Frequency of 0 days |
| settings_renewals | BUG-SREN-001 | Low | Recency & Renewals Settings: no Help (?), and Escape does not close popups |
| settings_renewals | BUG-SREN-004 | Low | Recency & Renewals Settings on a phone: table columns overlap each other |
| settings_lessonplans | BUG-SLP-002 | High | Lesson Plan Settings: Exercises are never saved; add/edit/delete only change the page and are lost when you leave |
| settings_lessonplans | BUG-SLP-001 | Low | Lesson Plan Settings: no Help (?), and Escape does not close popups |
| settings_lessonplans | BUG-SLP-003 | Low | Add Lesson accepts negative hours (Solo Hours -1 is saved and shown as "Solo: -1h") |
| settings_riskmatrix | BUG-SRM-001 | Low | Risk Matrix Settings: no Help (?), and Escape does not close popups |
| settings_riskmatrix | BUG-SRM-002 | Low | Risk Matrix Settings on a phone: the page scrolls sideways and "+ Add Level" is cut off |
| settings_smsreports | BUG-SSMS-001 | Low | Safety Reports Settings: no Help (?), and Escape does not close popups |
| settings_inspections | BUG-SINS-002 | Medium | Inspection Notifications: a meter inspection on an aircraft at 0.0 hours is never Overdue, and negative meter values are accepted |
| settings_inspections | BUG-SINS-001 | Low | Inspection Notifications Settings: no Help (?), and Escape does not close popups |
| settings_inspections | BUG-SINS-003 | Low | Inspection Notifications: trigger date shows as 2026-10-01, Add Inspection defaults to the UTC date, and the overdue day count is one day short |
| settings_googlecalendar / WhatsApp | BUG-SINT-001 | Low | Google Calendar Settings: Help and Add Calendar don't close with Escape or an outside click |
| settings_googlecalendar / WhatsApp | BUG-SINT-002 | Low | Google Calendar Sync Status: flight dates show as 2024-01-01 07:55 instead of DD/MM/YYYY |
| settings_activitylog | BUG-SLOG-001 | Low | Activity Log: no page Help (?), and dates show as "22 Oct 2026, 02:51 am" |
| (cross-cutting: permissions) | BUG-AM-005 | Medium | Access Manager: 16 permission types appear twice with the same name (e.g. two "Flight Schedule" cards with different levels) |
| (cross-cutting: permissions) | BUG-PERM-002 | Medium | User with no permissions cannot open their own My Account (no self-service password / 2FA) |
| (cross-cutting: permissions) | BUG-AM-007 | Low | Access Manager: a customer created from Flight Details is Active with no login credentials |
| (cross-cutting: permissions) | BUG-PERM-001 | Low | Sidebar lists modules the user has no permission for (all lead to Access Denied) |
| (cross-cutting: dates) | BUG-DATE-001 | Medium | Flight time across a DST change is out by an hour (01:00-05:00 on 04/04/2027 gives 4.0 instead of 5.0) |
| (cross-cutting: dates) | BUG-FD-007 | Medium | New flight defaults its leg date/time to UTC instead of local time |
| (cross-cutting: performance) | BUG-PERF-001 | Low | 'Performance' debug timing panel shown on every page, including to non-admin users |
| flightdetails | BUG-FD-008 | High | Unlocking a Complete & Locked flight wipes its leg route, leg PIC, leg passengers and manifest |
| flightdetails | BUG-FD-009 | Medium | A user without lock rights (not WL) can lock a flight; the server accepted status complete_locked |
| flightdetails | BUG-FD-010 | Medium | Required Information check skipped on unlock saves: a flight was saved Complete with no departure, destination or PIC |
| flightdetails | BUG-FD-011 | Low | History labels lock and unlock differently ("Locked: No > Yes" vs "Status: Locked > Unlocked") |
| settings_exambuilder / settings_examinstances | BUG-EXM-010 | Medium | Taking an exam as a read-only (group-level) user: saves and submit return Access Denied, and Previous/Close/Submit are hidden |
| settings_exambuilder / settings_examinstances | BUG-EXM-011 | Low | Taking an exam: "N of 10 questions answered" and the navigator tick only update after moving to another question |
