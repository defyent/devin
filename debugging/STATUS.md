# DataHangar bug status

Every bug found in the DataHangar beta audit, and where it stands. Ticked = fixed or closed. Click a bug ID for the full write-up (steps, expected vs actual, cause, fix, screenshots, retest history).

**234 bugs: 185 open, 48 fixed, 1 closed.** Last updated 24/10/2026.

## Bug checklist

### Login, 2FA, sessions, landing page (0 open, 3 fixed)

- [x] [BUG-LOG-003](bugs/BUG-LOG-003.md) · **Fixed (22/10/2026)** · Medium · 'Trust this device for 30 days' is lost on Logout (logout deletes the trusted-device cookie)
- [x] [BUG-LOG-001](bugs/BUG-LOG-001.md) · **Fixed (22/10/2026)** · Low · Login Message popup reappears on every browser reload
- [x] [BUG-LOG-002](bugs/BUG-LOG-002.md) · **Fixed (22/10/2026)** · Low · Logout throws JS error removeChild; Esc doesn't close the Log Out confirm

### Application shell, sidebar, header, mobile (0 open, 1 fixed)

- [x] [BUG-NAV-001](bugs/BUG-NAV-001.md) · **Fixed (22/10/2026)** · Medium · Leaving a page with unsaved changes gives no warning; edits are lost

### Access Manager (users, roles, groups, permissions, templates) (0 open, 7 fixed)

- [x] [BUG-AM-001](bugs/BUG-AM-001.md) · **Fixed (22/10/2026)** · Medium · New User accepts a 6-character password (placeholder and Change Credentials require 10)
- [x] [BUG-POP-003](bugs/BUG-POP-003.md) · **Fixed (22/10/2026)** · Medium · Access Manager Groups popup: Esc closes with unsaved changes and no warning; reopening shows the…
- [x] [BUG-AM-002](bugs/BUG-AM-002.md) · **Fixed (22/10/2026)** · Low · Last Activity hover date ignores Settings > Time Zone format
- [x] [BUG-AM-003](bugs/BUG-AM-003.md) · **Fixed (22/10/2026)** · Low · Last Activity column sort does not change order
- [x] [BUG-AM-004](bugs/BUG-AM-004.md) · **Fixed (22/10/2026)** · Low · Permission level dropdown shows bare codes 'WA' and 'G' next to full labels
- [x] [BUG-POP-001](bugs/BUG-POP-001.md) · **Fixed (22/10/2026)** · Low · Error modal ('Failed to Create User') does not close with Esc
- [x] [BUG-POP-002](bugs/BUG-POP-002.md) · **Fixed (22/10/2026)** · Low · Manage User Permissions uses a native browser confirm() for unsaved changes

### Dashboard (0 open, 5 fixed)

- [x] [BUG-DSH-003](bugs/BUG-DSH-003.md) · **Fixed (22/10/2026)** · Medium · Dashboard recency item opens Personnel Details on the wrong tab (Personal Details instead of…
- [x] [BUG-DSH-004](bugs/BUG-DSH-004.md) · **Fixed (22/10/2026)** · Medium · My Flights and On Duty open on the UTC date, not today's local date
- [x] [BUG-DSH-005](bugs/BUG-DSH-005.md) · **Fixed (22/10/2026)** · Medium · Dashboard Project Tasks: clicking a task opens an empty project list instead of the project
- [x] [BUG-DSH-001](bugs/BUG-DSH-001.md) · **Fixed (22/10/2026)** · Low · Dashboard side tabs are icon-only with no tooltip or label
- [x] [BUG-DSH-006](bugs/BUG-DSH-006.md) · **Fixed (22/10/2026)** · Low · Dashboard My Flights shows a canceled flight's status as 'Unknown'

### Flight Schedule (incl. embedded Location Planner) (0 open, 9 fixed)

- [x] [BUG-FS-008](bugs/BUG-FS-008.md) · **Fixed (22/10/2026)** · High · A group-level user (G / WG) sees no flights, even on aircraft in their own group
- [x] [BUG-FS-002](bugs/BUG-FS-002.md) · **Fixed (22/10/2026)** · Medium · Esc does not end copy/paste mode on the Flight Schedule - the next click + Ctrl+V creates another…
- [x] [BUG-FS-003](bugs/BUG-FS-003.md) · **Fixed (22/10/2026)** · Medium · Flight Schedule header overlaps when Live Edit is on - title covered, location pill cut off and its…
- [x] [BUG-FS-004](bugs/BUG-FS-004.md) · **Fixed (22/10/2026)** · Medium · Planner Add Location replaces the New Booking popup - typed booking and location input is lost
- [x] [BUG-FS-006](bugs/BUG-FS-006.md) · **Fixed (22/10/2026)** · Medium · Flight Schedule month view is slow: flightschedule_json takes ~1.6 s and rendering 2,500 events…
- [x] [BUG-FS-007](bugs/BUG-FS-007.md) · **Fixed (22/10/2026)** · Medium · Edit-mode idle timeout switches Live Edit off silently, throws 'calendarEl is not defined' and…
- [x] [BUG-FS-001](bugs/BUG-FS-001.md) · **Fixed (23/10/2026, v2.0.120)** · Low · New flight defaults (and Planner 'today') follow the browser time zone instead of Settings > Time…
- [x] [BUG-FS-005](bugs/BUG-FS-005.md) · **Fixed (22/10/2026)** · Low · JS error on every Live Edit toggle: Cannot read properties of null (reading 'scrollTop')
- [x] [BUG-POP-004](bugs/BUG-POP-004.md) · **Fixed (22/10/2026)** · Low · Flight Schedule popups (View Details, Double Booking alert, note modals) do not close with Esc

### Flight Details (3 open, 9 fixed)

- [ ] [BUG-FD-012](bugs/BUG-FD-012.md) · **Open, not retested** · Medium · Flight Details Files: .txt shows its text in a "Required Information" alert; empty .txt and .html…
- [ ] [BUG-FD-011](bugs/BUG-FD-011.md) · **Open, not retested** · Low · History labels lock and unlock differently ("Locked: No > Yes" vs "Status: Locked > Unlocked")
- [ ] [BUG-FD-013](bugs/BUG-FD-013.md) · **Open, not retested** · Low · Flight Details Files: clicking a PDF opens it in two new tabs
- [x] [BUG-FD-008](bugs/BUG-FD-008.md) · **Fixed (23/10/2026, v2.0.121)** · High · Unlocking a Complete & Locked flight wipes its leg route, leg PIC, leg passengers and manifest
- [x] [BUG-FD-001](bugs/BUG-FD-001.md) · **Fixed (23/10/2026, v2.0.121)** · Medium · Flight Details Save Changes does not return to the Flight Schedule and gives no success message
- [x] [BUG-FD-002](bugs/BUG-FD-002.md) · **Fixed (23/10/2026, v2.0.121)** · Medium · Flight Details History misses edits saved in Flight Details and shows a false 'Aircraft: ZK-SIM >…
- [x] [BUG-FD-004](bugs/BUG-FD-004.md) · **Fixed (23/10/2026, v2.0.120)** · Medium · Leg PIC / Secondary Flight Crew dropdowns offer passengers (e.g. a custom passenger can be chosen…
- [x] [BUG-FD-005](bugs/BUG-FD-005.md) · **Fixed (23/10/2026, v2.0.120)** · Medium · Leg with two unknown waypoints: only the first is offered for adding, the second is silently…
- [x] [BUG-FD-006](bugs/BUG-FD-006.md) · **Fixed (23/10/2026, v2.0.121)** · Medium · Flight can be set to Complete with no times or destination on a leg; no 'Required Information'…
- [x] [BUG-FD-009](bugs/BUG-FD-009.md) · **Fixed (23/10/2026, v2.0.121)** · Medium · A user without lock rights (not WL) can lock a flight; the server accepted status complete_locked
- [x] [BUG-FD-010](bugs/BUG-FD-010.md) · **Fixed (23/10/2026, v2.0.121)** · Medium · Required Information check skipped on unlock saves: a flight was saved Complete with no departure…
- [x] [BUG-FD-003](bugs/BUG-FD-003.md) · **Fixed (23/10/2026, v2.0.120)** · Low · Times and Meters: no link to the previous flight next to 'Previous' meter readings

### Active Flights and Live Tracking (0 open, 4 fixed, 1 closed)

- [x] [BUG-AF-004](bugs/BUG-AF-004.md) · **Fixed (24/10/2026, v2.0.123)** · High · Active Flights overdue and active times are 13 h out: local SAR/start times are compared with UTC…
- [x] [BUG-AF-002](bugs/BUG-AF-002.md) · **Fixed (24/10/2026, v2.0.123)** · Medium · Active Flights lists future flights that have no SAR time, and the stats cards don't count them
- [x] [BUG-AF-001](bugs/BUG-AF-001.md) · **Fixed (24/10/2026, v2.0.123)** · Low · Active Flights shows SAR Time '01/01/1970 00:00' for flights with SAR watch disabled
- [x] [BUG-AF-003](bugs/BUG-AF-003.md) · **Fixed (24/10/2026, v2.0.123)** · Low · Active Flights has no page Help (?), and its popups (About Live Tracking, Adjust SAR, Add Note)…
- [x] [BUG-AF-005](bugs/BUG-AF-005.md) · **Closed, by design (24/10/2026)** · Medium · A Read Only Group (RG) user sees every company flight, not only their group's

### Daily Flight Record (3 open)

- [ ] [BUG-DFR-002](bugs/BUG-DFR-002.md) · **Open, not retested** · Medium · Clear Filters unticks every status (lists Open, Cancelled and Deleted flights), and the date fields…
- [ ] [BUG-DFR-003](bugs/BUG-DFR-003.md) · **Open, not retested** · Medium · Changing filters quickly appends results instead of replacing them, showing duplicate and…
- [ ] [BUG-DFR-001](bugs/BUG-DFR-001.md) · **Open, not retested** · Low · Daily Flight Record has no page Help (?), and its popups (Manage Columns, Notes full text) don't…

### All Personnel (Personnel List) (2 open)

- [ ] [BUG-PL-001](bugs/BUG-PL-001.md) · **Open, not retested** · Low · All Personnel has no page Help (?)
- [ ] [BUG-PL-002](bugs/BUG-PL-002.md) · **Open, not retested** · Low · A person with no name exists and is listed as '?' at the top of All Personnel (person #274…

### Personnel Details / My Account (20 open)

- [ ] [BUG-PD-006](bugs/BUG-PD-006.md) · **Open, not retested** · High · Personnel Details > Recency and Renewals: action buttons are hidden (Add Item, Table/Card view…
- [ ] [BUG-PD-011](bugs/BUG-PD-011.md) · **Open, not retested** · High · Personnel Details > Security: Change Password always fails with 'Invalid Action: change_password'
- [ ] [BUG-PD-001](bugs/BUG-PD-001.md) · **Open, not retested** · Medium · personneldetails/index.js is truncated: ReferenceError getPickerMod on every load
- [ ] [BUG-PD-003](bugs/BUG-PD-003.md) · **Open, not retested** · Medium · 2FA setup: one wrong verification code closes the setup dialog and issues a new secret
- [ ] [BUG-PD-007](bugs/BUG-PD-007.md) · **Open, not retested** · Medium · Personnel Details > Recency: 'Days Until Expiry' and status don't match the Last Conducted date
- [ ] [BUG-PD-008](bugs/BUG-PD-008.md) · **Open, not retested** · Medium · Personnel Details > Recency: the recency summary popup has no Add Manual Entry, no x, and doesn't…
- [ ] [BUG-PD-009](bugs/BUG-PD-009.md) · **Open, not retested** · Medium · Personnel Details > Renewal edit: the Today and Calculate links can't be clicked because the date…
- [ ] [BUG-PD-012](bugs/BUG-PD-012.md) · **Open, still failing (24/10/2026, v2.0.123)** · Medium · Personnel Details > Files: opening a file shows 'File Access Error' with the file's contents as the…
- [ ] [BUG-PD-016](bugs/BUG-PD-016.md) · **Open, not retested** · Medium · Personnel Details > Timesheets: Add Claim button does nothing
- [ ] [BUG-PD-017](bugs/BUG-PD-017.md) · **Open, not retested** · Medium · Personnel Details > Lesson Plans: an assigned plan is saved but never listed; the dialog's dates…
- [ ] [BUG-PL-003](bugs/BUG-PL-003.md) · **Open, not retested** · Medium · All Personnel: a Read Only Group (RG) user can't open the details of anyone in their group
- [ ] [BUG-EXM-009](bugs/BUG-EXM-009.md) · **Open, not retested** · Low · A hotspot question with no image shows a developer debug message to the person taking the exam
- [ ] [BUG-PD-002](bugs/BUG-PD-002.md) · **Open, not retested** · Low · Personnel Details modals (Enable 2FA, Setup Error alert): title right-aligned, away from its icon
- [ ] [BUG-PD-004](bugs/BUG-PD-004.md) · **Open, not retested** · Low · Security tab 'Enabled on' date ignores Settings > Time Zone format
- [ ] [BUG-PD-005](bugs/BUG-PD-005.md) · **Open, not retested** · Low · History, PDF Options and Legacy Duty Browser popups don't close with Escape, and PDF Options has no…
- [ ] [BUG-PD-010](bugs/BUG-PD-010.md) · **Open, not retested** · Low · The 'Performance' timing panel is shown to users and covers buttons
- [ ] [BUG-PD-013](bugs/BUG-PD-013.md) · **Open, not retested** · Low · An empty Birth Date shows today's date
- [ ] [BUG-PD-014](bugs/BUG-PD-014.md) · **Open, not retested** · Low · Digital Signature: wrong password closes the popup and throws away the drawing; empty Save gives no…
- [ ] [BUG-PD-015](bugs/BUG-PD-015.md) · **Open, not retested** · Low · Flight & Duty Analysis popup: title date is YYYY-MM-DD and Escape doesn't close it
- [ ] [BUG-PD-018](bugs/BUG-PD-018.md) · **Open, not retested** · Low · Request Leave: Start and End Date default to the UTC date, not today's local date

### Roster Viewer (3 open)

- [ ] [BUG-RV-002](bugs/BUG-RV-002.md) · **Open, not retested** · Medium · Clicking a shift does not open Shift Details
- [ ] [BUG-RV-001](bugs/BUG-RV-001.md) · **Open, not retested** · Low · No page Help (?) and Group Visibility popup ignores Escape
- [ ] [BUG-RV-003](bugs/BUG-RV-003.md) · **Open, not retested** · Low · Roster Viewer shift note popup shows the date as 'October 5, 2026', not the configured DD/MM/YYYY

### Roster Builder (8 open)

- [ ] [BUG-RB-007](bugs/BUG-RB-007.md) · **Open, not retested** · High · Clear then Publish of a draft month with no shifts does not clear the live roster and shows no…
- [ ] [BUG-RB-002](bugs/BUG-RB-002.md) · **Open, not retested** · Medium · Copy Live to Draft copies one shift at a time and takes about 6 minutes for one month
- [ ] [BUG-RB-003](bugs/BUG-RB-003.md) · **Open, not retested** · Medium · Copy/paste still works with violation checking ON
- [ ] [BUG-RB-005](bugs/BUG-RB-005.md) · **Open, not retested** · Medium · Every validation error throws a JS error instead of showing a message (e.g. Apply Shift Pattern…
- [ ] [BUG-RB-008](bugs/BUG-RB-008.md) · **Open, not retested** · Medium · Roster Builder can only be opened from Settings and Tools, so a Roster Builder user without System…
- [ ] [BUG-RB-001](bugs/BUG-RB-001.md) · **Open, not retested** · Low · No page Help (?); Copy/Paste Instructions popup ignores Escape and outside click
- [ ] [BUG-RB-004](bugs/BUG-RB-004.md) · **Open, not retested** · Low · Rule Violations popup shows 'Monday, October 5' instead of the configured DD/MM/YYYY date
- [ ] [BUG-RB-006](bugs/BUG-RB-006.md) · **Open, not retested** · Low · At phone width the shift palette takes half the screen and the Draft Edit Mode banner covers the…

### Timesheets, Timesheet Details, Leave Requests (8 open)

- [ ] [BUG-TS-002](bugs/BUG-TS-002.md) · **Open, not retested** · Medium · Timesheet Approval: status filter 'Unsigned' shows 'No personnel found' although everyone has…
- [ ] [BUG-TS-003](bugs/BUG-TS-003.md) · **Open, not retested** · Medium · Timesheet Approval list totals don't match Timesheet Details (Rostered Days and Duty Hours)
- [ ] [BUG-TS-008](bugs/BUG-TS-008.md) · **Open, not retested** · Medium · Approving a leave request doesn't change the rostered shifts, and rejecting with no reason gives no…
- [ ] [BUG-TS-001](bugs/BUG-TS-001.md) · **Open, not retested** · Low · No page Help on Timesheet Approval, and the Help (?) on Timesheet Details does nothing
- [ ] [BUG-TS-004](bugs/BUG-TS-004.md) · **Open, not retested** · Low · Timesheet Details shows dates as 'Oct 5' and times with seconds (14:00:00)
- [ ] [BUG-TS-005](bugs/BUG-TS-005.md) · **Open, not retested** · Low · Timesheet Details: F&D and Roster Violation popups ignore Escape and show ISO dates in the title
- [ ] [BUG-TS-006](bugs/BUG-TS-006.md) · **Open, not retested** · Low · Leave Types: a validation error closes the Add Leave Type popup and throws away what you typed; the…
- [ ] [BUG-TS-007](bugs/BUG-TS-007.md) · **Open, not retested** · Low · Reject Claim: leaving the reason empty closes the reject popup and throws a script error

### Flight and Duty (5 open)

- [ ] [BUG-FAD-001](bugs/BUG-FAD-001.md) · **Open, not retested** · Low · Flight and Duty has no page Help (?)
- [ ] [BUG-FAD-002](bugs/BUG-FAD-002.md) · **Open, not retested** · Low · Flight and Duty popups (Flight Details, Duty Time Details, Roster Violations, Resolutions Required)…
- [ ] [BUG-FAD-003](bugs/BUG-FAD-003.md) · **Open, not retested** · Low · Flight and Duty popups show dates as '16 Oct 2026' instead of the configured DD/MM/YYYY
- [ ] [BUG-FAD-004](bugs/BUG-FAD-004.md) · **Open, not retested** · Low · Flight and Duty column headers are ambiguous: two '1 Days' and two '24 Hours' columns, and '1 Days'…
- [ ] [BUG-FAD-005](bugs/BUG-FAD-005.md) · **Open, not retested** · Low · Flight and Duty 'View as Date' defaults to the UTC date instead of the local date

### Notices (5 open)

- [ ] [BUG-NOT-002](bugs/BUG-NOT-002.md) · **Open, still failing (24/10/2026, v2.0.123)** · Medium · Notice Details: clicking a .txt attachment does nothing (no preview, no download)
- [ ] [BUG-NOT-004](bugs/BUG-NOT-004.md) · **Open, not retested** · Medium · A Write Group (WG) user gets 'An error occurred' when clicking New Notice
- [ ] [BUG-NOT-001](bugs/BUG-NOT-001.md) · **Open, not retested** · Low · Notices has no page Help (?), and the Create New Notice popup ignores Escape
- [ ] [BUG-NOT-003](bugs/BUG-NOT-003.md) · **Open, not retested** · Low · Settings and Tools hub: 'Notices' card has no links
- [ ] [BUG-NOT-005](bugs/BUG-NOT-005.md) · **Open, not retested** · Low · Only one attachment can be added per save

### Recency and Renewals (overview page) (2 open)

- [ ] [BUG-REC-001](bugs/BUG-REC-001.md) · **Open, not retested** · Low · Recency and Renewals overview has no page Help (?)
- [ ] [BUG-REC-002](bugs/BUG-REC-002.md) · **Open, not retested** · Low · Recency and Renewals at phone width: the table is cut off, so Total Items and Actions are hidden

### Safety Reports (SMS) (6 open)

- [ ] [BUG-SMS-005](bugs/BUG-SMS-005.md) · **Open, not retested** · High · Group-level (WG) and own-level (WO) users see no reports at all, not even ones they submitted
- [ ] [BUG-SMS-001](bugs/BUG-SMS-001.md) · **Open, not retested** · Medium · New Safety Report: Escape on the Confidential/Anonymous help closes the report form behind it and…
- [ ] [BUG-SMS-002](bugs/BUG-SMS-002.md) · **Open, not retested** · Medium · New Safety Report: Event Date/Time defaults to the UTC date and time, not local
- [ ] [BUG-SMS-003](bugs/BUG-SMS-003.md) · **Open, not retested** · Low · Safety Report Final Report: Likelihood and Consequence dropdowns list every option twice
- [ ] [BUG-SMS-004](bugs/BUG-SMS-004.md) · **Open, not retested** · Low · Add to Hazard Register: Goal 'Mitigate' shows as 'Minimize' in the Hazard Register
- [ ] [BUG-SMS-006](bugs/BUG-SMS-006.md) · **Open, not retested** · Low · Safety Report document link for a deleted file shows the server's file path

### Hazard Register (3 open)

- [ ] [BUG-HAZ-001](bugs/BUG-HAZ-001.md) · **Open, not retested** · Medium · Hazard Register details: Hazard Type always shows '--'
- [ ] [BUG-HAZ-002](bugs/BUG-HAZ-002.md) · **Open, not retested** · Medium · Hazard Register details: Final Risk Assessment never shows the saved final risk
- [ ] [BUG-HAZ-003](bugs/BUG-HAZ-003.md) · **Open, not retested** · Low · Hazard Register has no way to create a hazard entry

### File Browser (9 open)

- [ ] [BUG-FB-003](bugs/BUG-FB-003.md) · **Open, still failing (24/10/2026, v2.0.123)** · Medium · Clicking a .txt file shows 'File Access Error' with the file's own text
- [ ] [BUG-FB-005](bugs/BUG-FB-005.md) · **Open, not retested** · Medium · Read/Write Access groups are not kept after Update Document
- [ ] [BUG-FB-006](bugs/BUG-FB-006.md) · **Open, not retested** · Medium · Deleting a folder fails with 'Invalid Action: filebrowser_deletefolder'
- [ ] [BUG-FB-008](bugs/BUG-FB-008.md) · **Open, not retested** · Medium · Files attached to a waypoint also appear in the File Browser Home folder
- [ ] [BUG-FB-001](bugs/BUG-FB-001.md) · **Open, not retested** · Low · File Browser has no page Help (?)
- [ ] [BUG-FB-002](bugs/BUG-FB-002.md) · **Open, not retested** · Low · File Browser shows Date Uploaded as 'Oct 22, 2026' instead of DD/MM/YYYY
- [ ] [BUG-FB-004](bugs/BUG-FB-004.md) · **Open, not retested** · Low · Escape doesn't close the Create New Folder or Configure File popups
- [ ] [BUG-FB-007](bugs/BUG-FB-007.md) · **Open, not retested** · Low · File Browser on a phone: table is cut off, edit buttons are off-screen
- [ ] [BUG-FB-009](bugs/BUG-FB-009.md) · **Open, not retested** · Low · Clicking an .svg shows an error popup with the raw SVG code

### Form Builder (4 open)

- [ ] [BUG-FBLD-002](bugs/BUG-FBLD-002.md) · **Open, not retested** · Medium · Form Builder View Form: Date and Time widgets default to UTC, not local time
- [ ] [BUG-FBLD-003](bugs/BUG-FBLD-003.md) · **Open, not retested** · Medium · Table conditions do nothing in View Form
- [ ] [BUG-FBLD-001](bugs/BUG-FBLD-001.md) · **Open, not retested** · Low · Popups ignore Escape and outside clicks (Help, Create New Form Template, Edit Options)
- [ ] [BUG-FBLD-004](bugs/BUG-FBLD-004.md) · **Open, not retested** · Low · Form Builder on a phone: page is wider than the screen and the Toolbox covers the form

### Form Browser / Form Viewer (3 open)

- [ ] [BUG-FBR-001](bugs/BUG-FBR-001.md) · **Open, not retested** · Low · Form Browser has no page Help (?)
- [ ] [BUG-FBR-002](bugs/BUG-FBR-002.md) · **Open, not retested** · Low · Form Browser and Form Viewer dates ignore the date setting ('Oct 21, 2026', '10:24 PM')
- [ ] [BUG-FBR-003](bugs/BUG-FBR-003.md) · **Open, not retested** · Low · Form Browser on a phone: table is cut off, Created and Created By are off-screen

### Task Tracker (4 open)

- [ ] [BUG-TT-004](bugs/BUG-TT-004.md) · **Open, not retested** · Medium · A Write Group (WG) user is treated as read-only and can't add a project
- [ ] [BUG-TT-001](bugs/BUG-TT-001.md) · **Open, not retested** · Low · Escape doesn't close Help or Add Project
- [ ] [BUG-TT-002](bugs/BUG-TT-002.md) · **Open, not retested** · Low · Task Tracker dates ignore the date setting ('Dec 31', '2026-10-21')
- [ ] [BUG-TT-003](bugs/BUG-TT-003.md) · **Open, not retested** · Low · Task Tracker on a phone: feature cards are pushed right and cut off

### Reports (4 open)

- [ ] [BUG-RPT-003](bugs/BUG-RPT-003.md) · **Open, not retested** · Medium · Reports tables overlap on a phone: column text is drawn on top of other columns
- [ ] [BUG-RPT-001](bugs/BUG-RPT-001.md) · **Open, not retested** · Low · Reports has no page Help (?), and Escape doesn't close New Report Template
- [ ] [BUG-RPT-002](bugs/BUG-RPT-002.md) · **Open, not retested** · Low · Reports Export CSV writes dates as '2026-10-16 06:00:00' instead of the org date format
- [ ] [BUG-RPT-004](bugs/BUG-RPT-004.md) · **Open, not retested** · Low · The Flight Hours meter column shows the aircraft's current meter on every flight, and Total adds…

### Support tickets (3 open, 1 fixed)

- [ ] [BUG-SUP-001](bugs/BUG-SUP-001.md) · **Open, not retested** · Medium · Support has no page Help (?); Escape doesn't close New Ticket, but a click outside closes it and…
- [ ] [BUG-SUP-002](bugs/BUG-SUP-002.md) · **Open, not retested** · Low · Support New Ticket: Ctrl+V doesn't paste a screenshot, though the error message tells you to use…
- [ ] [BUG-SUP-003](bugs/BUG-SUP-003.md) · **Open, still failing (24/10/2026, v2.0.123)** · Low · Support ticket: clicking a .txt attachment shows an 'Error' popup containing the file's text
- [x] [BUG-SUP-004](bugs/BUG-SUP-004.md) · **Fixed (22/10/2026)** · Medium · Support: the only permission level is All Access, so regular staff can't raise or see their own…

### Chat (4 open)

- [ ] [BUG-AM-006](bugs/BUG-AM-006.md) · **Open, part fixed (22/10/2026)** · Medium · Access Manager has no Chat permission, so you can't give Chat to a non-admin user
- [ ] [BUG-CHAT-001](bugs/BUG-CHAT-001.md) · **Open, not retested** · Low · Chat has no page Help (?); Escape doesn't close Create Channel; empty name does nothing with no…
- [ ] [BUG-CHAT-002](bugs/BUG-CHAT-002.md) · **Open, not retested** · Low · Chat times show 12-hour '01:32 AM' and date separators 'Thursday, October 22, 2026' instead of the…
- [ ] [BUG-CHAT-003](bugs/BUG-CHAT-003.md) · **Open, not retested** · Low · Chat image button: non-images are ignored with no message; SVG/TIFF/HEIC preview then fail on Send

### Exam Builder, Exam Editor, Exam Instances (7 open, 3 fixed)

- [ ] [BUG-EXM-004](bugs/BUG-EXM-004.md) · **Open, not retested** · Medium · Exam Builder has no way to link or unlink user groups on an exam group
- [ ] [BUG-EXM-008](bugs/BUG-EXM-008.md) · **Open, not retested** · Medium · Exam Builder: deleting an exam or exam group that has instances fails silently (error only in the…
- [ ] [BUG-EXM-001](bugs/BUG-EXM-001.md) · **Open, not retested** · Low · Exam Builder/Editor have no page Help (?); Escape doesn't close Add Group, Add Exam or Choose…
- [ ] [BUG-EXM-002](bugs/BUG-EXM-002.md) · **Open, not retested** · Low · Exam dates ignore the org format: 'Oct 22, 2026' in Exam Builder and '10/22/2026 01:46 AM' in Exam…
- [ ] [BUG-EXM-003](bugs/BUG-EXM-003.md) · **Open, not retested** · Low · Exam viewer 'Read Only' still shows Add Question, Add Group and Save Question
- [ ] [BUG-EXM-005](bugs/BUG-EXM-005.md) · **Open, not retested** · Low · Exam Builder on a phone: exam table columns and action icons overlap
- [ ] [BUG-EXM-007](bugs/BUG-EXM-007.md) · **Open, not retested** · Low · Exam Instances batch: deleting a person's instance shows success but the row stays until the page…
- [x] [BUG-EXM-006](bugs/BUG-EXM-006.md) · **Fixed (23/10/2026, v2.0.121)** · High · Taking an exam: Multi-Response checkboxes toggle twice, so clicking the box does nothing and the…
- [x] [BUG-EXM-010](bugs/BUG-EXM-010.md) · **Fixed (23/10/2026, v2.0.122)** · Medium · Taking an exam as a read-only (group-level) user: saves and submit return Access Denied, and…
- [x] [BUG-EXM-011](bugs/BUG-EXM-011.md) · **Fixed (23/10/2026, v2.0.122)** · Low · Taking an exam: "N of 10 questions answered" and the navigator tick only update after moving to…

### Settings – Flight Schedule (0 open, 2 fixed)

- [x] [BUG-SFS-002](bugs/BUG-SFS-002.md) · **Fixed (22/10/2026)** · High · Changing Schedule Start Time saves a full date-time, and the setting then shows NaN:NaN
- [x] [BUG-SFS-001](bugs/BUG-SFS-001.md) · **Fixed (22/10/2026)** · Low · Flight Schedule settings: Slot Duration + goes past 120 and typed values over 120 are accepted

### Settings – Daily Flight Record (1 open)

- [ ] [BUG-SDFR-001](bugs/BUG-SDFR-001.md) · **Open, not retested** · Low · Daily Flight Record Settings loads a colorpicker.js that does not exist (404 in the console)

### Settings – Time Zone (date/time matrix) (3 open)

- [ ] [BUG-STZ-001](bugs/BUG-STZ-001.md) · **Open, not retested** · Medium · Time Zone settings: the Example preview shows UTC, not the selected time zone
- [ ] [BUG-STZ-003](bugs/BUG-STZ-003.md) · **Open, not retested** · Medium · Time Zone settings: the Example preview shows MM/DD/YYYY for every date format except DD/MM/YYYY
- [ ] [BUG-STZ-002](bugs/BUG-STZ-002.md) · **Open, not retested** · Low · Time Zone settings page has no Help (?)

### Settings – Resources (Aircraft) (1 open)

- [ ] [BUG-SRES-001](bugs/BUG-SRES-001.md) · **Open, not retested** · Low · The meter "Last:" dates show as YYYY-MM-DD instead of the Time Zone date format

### Settings – Weight and Balance Configs (5 open)

- [ ] [BUG-SWAB-001](bugs/BUG-SWAB-001.md) · **Open, not retested** · Low · Weight & Balance Configs: no Help (?), and Escape does not close popups
- [ ] [BUG-SWAB-002](bugs/BUG-SWAB-002.md) · **Open, not retested** · Low · Weight & Balance Configs: dates show as "14 Oct 2026" / "29 Sept 2026" instead of DD/MM/YYYY
- [ ] [BUG-SWAB-003](bugs/BUG-SWAB-003.md) · **Open, not retested** · Low · Weight & Balance Configs shows a debug "Performance" timing panel to users
- [ ] [BUG-SWAB-004](bugs/BUG-SWAB-004.md) · **Open, not retested** · Low · Weight & Balance Configs: on a phone the page is wider than the screen
- [ ] [BUG-SWAB-005](bugs/BUG-SWAB-005.md) · **Open, not retested** · Low · W&B Configs: two revisions show the same number ("Rev 5") until another import renumbers them

### Settings – Extra Flight Info (1 open)

- [ ] [BUG-SEFI-001](bugs/BUG-SEFI-001.md) · **Open, not retested** · Low · No Help (?), and Escape does not close Add Field

### Settings – Flight Types (2 open)

- [ ] [BUG-SFT-002](bugs/BUG-SFT-002.md) · **Open, not retested** · Medium · A duplicate Flight Category name ("PIC") is accepted
- [ ] [BUG-SFT-001](bugs/BUG-SFT-001.md) · **Open, not retested** · Low · No Help (?), and Escape does not close popups

### Settings – Waypoint Locations (5 open)

- [ ] [BUG-SWP-002](bugs/BUG-SWP-002.md) · **Open, not retested** · Medium · Moving a waypoint about 250 nm saves with no "Significant Location Change" warning
- [ ] [BUG-SWP-004](bugs/BUG-SWP-004.md) · **Open, not retested** · Medium · Waypoints on a phone: table columns overlap and Add Waypoint is off-screen
- [ ] [BUG-SWP-001](bugs/BUG-SWP-001.md) · **Open, not retested** · Low · No Help (?), and Escape does not close popups
- [ ] [BUG-SWP-003](bugs/BUG-SWP-003.md) · **Open, not retested** · Low · The list is not refreshed after you save or delete on the detail page
- [ ] [BUG-SWP-005](bugs/BUG-SWP-005.md) · **Open, not retested** · Low · Waypoint Files list shows the Uploaded date as MM/DD/YYYY and Size N/A for every file

### Settings – Roster Shifts (4 open)

- [ ] [BUG-SST-004](bugs/BUG-SST-004.md) · **Open, not retested** · Medium · Roster Shifts on a phone: the table scrolls the page sideways and the group tabs are hidden
- [ ] [BUG-SST-001](bugs/BUG-SST-001.md) · **Open, not retested** · Low · Roster Shifts (Shift Type Editor): no Help (?), and Escape does not close popups
- [ ] [BUG-SST-002](bugs/BUG-SST-002.md) · **Open, not retested** · Low · New Shift Type: Duty Start/End Time default to the current UTC time
- [ ] [BUG-SST-003](bugs/BUG-SST-003.md) · **Open, not retested** · Low · Roster Shifts: after Edit Group the selected group jumps back to Duty, so the next New Shift Type…

### Settings – Fatigue Risk Management (2 open)

- [ ] [BUG-SFRMS-001](bugs/BUG-SFRMS-001.md) · **Open, not retested** · Low · No Help (?), and Escape does not close popups
- [ ] [BUG-SFRMS-002](bugs/BUG-SFRMS-002.md) · **Open, not retested** · Low · FRMS Settings on a phone: the page scrolls sideways, "+ Add ... Rule" is off-screen and rule text…

### Settings – Recency and Renewals (4 open)

- [ ] [BUG-SREN-002](bugs/BUG-SREN-002.md) · **Open, not retested** · Medium · Add Recency accepts negative Days, and a Caution value higher than Warning
- [ ] [BUG-SREN-003](bugs/BUG-SREN-003.md) · **Open, not retested** · Medium · Add Renewal Type accepts negative Days to Notify and a Frequency of 0 days
- [ ] [BUG-SREN-001](bugs/BUG-SREN-001.md) · **Open, not retested** · Low · Recency & Renewals Settings: no Help (?), and Escape does not close popups
- [ ] [BUG-SREN-004](bugs/BUG-SREN-004.md) · **Open, not retested** · Low · Recency & Renewals Settings on a phone: table columns overlap each other

### Settings – Lesson Plans (3 open)

- [ ] [BUG-SLP-002](bugs/BUG-SLP-002.md) · **Open, not retested** · High · Lesson Plan Settings: Exercises are never saved; add/edit/delete only change the page and are lost…
- [ ] [BUG-SLP-001](bugs/BUG-SLP-001.md) · **Open, not retested** · Low · Lesson Plan Settings: no Help (?), and Escape does not close popups
- [ ] [BUG-SLP-003](bugs/BUG-SLP-003.md) · **Open, not retested** · Low · Add Lesson accepts negative hours (Solo Hours -1 is saved and shown as "Solo: -1h")

### Settings – Risk Matrix (2 open)

- [ ] [BUG-SRM-001](bugs/BUG-SRM-001.md) · **Open, not retested** · Low · No Help (?), and Escape does not close popups
- [ ] [BUG-SRM-002](bugs/BUG-SRM-002.md) · **Open, not retested** · Low · Risk Matrix Settings on a phone: the page scrolls sideways and "+ Add Level" is cut off

### Settings – Safety Reports (1 open)

- [ ] [BUG-SSMS-001](bugs/BUG-SSMS-001.md) · **Open, not retested** · Low · No Help (?), and Escape does not close popups

### Settings – Inspection Notifications (3 open)

- [ ] [BUG-SINS-002](bugs/BUG-SINS-002.md) · **Open, not retested** · Medium · A meter inspection on an aircraft at 0.0 hours is never Overdue, and negative meter values are…
- [ ] [BUG-SINS-001](bugs/BUG-SINS-001.md) · **Open, not retested** · Low · No Help (?), and Escape does not close popups
- [ ] [BUG-SINS-003](bugs/BUG-SINS-003.md) · **Open, not retested** · Low · Trigger date shows as 2026-10-01, Add Inspection defaults to the UTC date, and the overdue day…

### Settings – Google Calendar, WhatsApp (2 open)

- [ ] [BUG-SINT-001](bugs/BUG-SINT-001.md) · **Open, not retested** · Low · Google Calendar Settings: Help and Add Calendar don't close with Escape or an outside click
- [ ] [BUG-SINT-002](bugs/BUG-SINT-002.md) · **Open, not retested** · Low · Google Calendar Sync Status: flight dates show as 2024-01-01 07:55 instead of DD/MM/YYYY

### Settings – Activity Log (1 open)

- [ ] [BUG-SLOG-001](bugs/BUG-SLOG-001.md) · **Open, not retested** · Low · No page Help (?), and dates show as "22 Oct 2026, 02:51 am"

### iPad setup and install (1 open)

- [ ] [BUG-IPSET-001](bugs/BUG-IPSET-001.md) · **Open, still failing** · Medium · Unit-test target does not compile

### iPad configuration – general (2 open)

- [ ] [BUG-IPCFG-001](bugs/BUG-IPCFG-001.md) · **Open, still failing** · Medium · Configuration PIN saves non-4-digit values, permanently locking Configuration
- [ ] [BUG-IPUI-002](bugs/BUG-IPUI-002.md) · **Open, still failing** · Low · Light theme: Configuration values/toggles unreadable (white on white)

### iPad DataHangar login and sync (2 open)

- [ ] [BUG-IPDH-001](bugs/BUG-IPDH-001.md) · **Open, still failing** · Low · Keychain save failure is silent
- [ ] [BUG-IPDH-002](bugs/BUG-IPDH-002.md) · **Open, still failing** · Low · Empty-field authentication and sync buttons look enabled

### iPad aircraft editor (1 open)

- [ ] [BUG-IPAC-001](bugs/BUG-IPAC-001.md) · **Open, still failing** · Medium · Aircraft editor edits to server aircraft are local-only and silently reverted by Sync All

### iPad personnel and waypoints (1 open)

- [ ] [BUG-IPWPT-001](bugs/BUG-IPWPT-001.md) · **Open, still failing** · Medium · Code-less server waypoints show blank titles; editing them stores 0,0 coordinates; edits are…

### iPad flights list (3 open)

- [ ] [BUG-IPFL-002](bugs/BUG-IPFL-002.md) · **Open, still failing** · High · Flights with a Student PIC cannot be pushed from the app
- [ ] [BUG-IPFL-003](bugs/BUG-IPFL-003.md) · **Open, still failing** · High · Leg times pulled from DataHangar ("HH:MM:SS") display as the current time; editing overwrites them
- [ ] [BUG-IPFL-001](bugs/BUG-IPFL-001.md) · **Open, still failing** · Low · Flight ID badges and labels add thousands separators

### iPad weight and balance (2 open)

- [ ] [BUG-IPWB-001](bugs/BUG-IPWB-001.md) · **Open, still failing** · Low · Weight and balance summary rounds equipment weight to whole kilograms
- [ ] [BUG-IPWB-002](bugs/BUG-IPWB-002.md) · **Open, still failing** · Low · Cabin occupancy count includes hidden seats

### iPad flight times and meters (1 open)

- [ ] [BUG-IPREF-001](bugs/BUG-IPREF-001.md) · **Open, still failing** · Low · Sync All reports zero Flight Custom Fields when a custom EFI field is present

### iPad flight forms (2 open)

- [ ] [BUG-IPFORM-001](bugs/BUG-IPFORM-001.md) · **Open, still failing** · High · Pushed form uses the wrong template and loses widget data
- [ ] [BUG-IPFORM-002](bugs/BUG-IPFORM-002.md) · **Open, still failing** · High · Pull creates phantom form instances and pushed updates are ignored

### iPad safety reports (5 open)

- [ ] [BUG-IPFORM-003](bugs/BUG-IPFORM-003.md) · **Open, still failing** · High · Form Date/Time widgets ignore website values and show (and can save) the current date/time
- [ ] [BUG-IPSMS-001](bugs/BUG-IPSMS-001.md) · **Open, still failing** · High · Safety Report form attached in iPad app is silently lost on push
- [ ] [BUG-IPSMS-002](bugs/BUG-IPSMS-002.md) · **Open, still failing** · Medium · Final Report tab shows stale values after Pull (overwrite risk)
- [ ] [BUG-IPSMS-004](bugs/BUG-IPSMS-004.md) · **Open, still failing** · Medium · Safety Report push can report success after form or status updates fail
- [ ] [BUG-IPSMS-003](bugs/BUG-IPSMS-003.md) · **Open, still failing** · Low · Safety Report action assignee picker includes a blank Unassigned row

### iPad communications and chat (1 open)

- [ ] [BUG-IPCHAT-001](bugs/BUG-IPCHAT-001.md) · **Open, still failing** · Medium · Chat message typed while offline is discarded on send

### iPad calculator (1 open)

- [ ] [BUG-IPCALC-001](bugs/BUG-IPCALC-001.md) · **Open, still failing** · High · Unit Converter: NM <-> Statute Miles conversion inverted; large values shown in scientific notation

### iPad live tracking (3 open)

- [ ] [BUG-WEBTRK-001](bugs/BUG-WEBTRK-001.md) · **Open, still failing** · High · Live tracking pings fail on stresstest - live_tracking table missing
- [ ] [BUG-IPTRK-002](bugs/BUG-IPTRK-002.md) · **Open, still failing** · Medium · Live Tracking queue stores duplicate/stale pings; rejected pings are dropped
- [ ] [BUG-IPTRK-001](bugs/BUG-IPTRK-001.md) · **Open, still failing** · Low · Live Tracking UI/state issues (raw HTML error, stale/global menu, no offline indicator)

### iPad cross-cutting checks (4 open)

- [ ] [BUG-IPSYNC-001](bugs/BUG-IPSYNC-001.md) · **Open, still failing** · Medium · Push silently overwrites website-side Notes edits
- [ ] [BUG-IPUI-001](bugs/BUG-IPUI-001.md) · **Open, still failing** · Medium · Hardware-keyboard focus leaks through sheets and keypads
- [ ] [BUG-IPOFF-001](bugs/BUG-IPOFF-001.md) · **Open, still failing** · Low · Offline launch and push block for about a minute before timing out
- [ ] [BUG-IPUI-003](bugs/BUG-IPUI-003.md) · **Open, still failing** · Low · Sparse VoiceOver labels and partial Dynamic Type support

### iPad permissions and end-to-end (4 open)

- [ ] [BUG-WEBCHAT-001](bugs/BUG-WEBCHAT-001.md) · **Open, still failing** · High · Chat API used by the iPad app ignores the Chat permission (permission bypass)
- [ ] [BUG-IPFL-004](bugs/BUG-IPFL-004.md) · **Open, still failing** · Medium · Flight downloaded before aircraft sync keeps aircraft "None" forever; Pull never re-links; push…
- [ ] [BUG-IPPERM-001](bugs/BUG-IPPERM-001.md) · **Open, still failing** · Medium · App lets read-only users edit and push flights and only fails at the server, showing a raw "Error…
- [ ] [BUG-IPSYNC-002](bugs/BUG-IPSYNC-002.md) · **Open, still failing** · Medium · Pull from Server does not reliably update website-edited Notes

### Cross-cutting: permission levels (2 open, 2 fixed)

- [ ] [BUG-PERM-002](bugs/BUG-PERM-002.md) · **Open, not retested** · Medium · User with no permissions cannot open their own My Account (no self-service password / 2FA)
- [ ] [BUG-PERM-001](bugs/BUG-PERM-001.md) · **Open, still failing (22/10/2026)** · Low · Sidebar lists modules the user has no permission for (all lead to Access Denied)
- [x] [BUG-AM-005](bugs/BUG-AM-005.md) · **Fixed (22/10/2026)** · Medium · 16 permission types appear twice with the same name (e.g. two "Flight Schedule" cards with…
- [x] [BUG-AM-007](bugs/BUG-AM-007.md) · **Fixed (22/10/2026)** · Low · A customer created from Flight Details is Active with no login credentials

### Cross-cutting: date/time formats and pickers (0 open, 2 fixed)

- [x] [BUG-DATE-001](bugs/BUG-DATE-001.md) · **Fixed (23/10/2026, v2.0.121)** · Medium · Flight time across a DST change is out by an hour (01:00-05:00 on 04/04/2027 gives 4.0 instead of…
- [x] [BUG-FD-007](bugs/BUG-FD-007.md) · **Fixed (23/10/2026, v2.0.120)** · Low · New flight defaults its leg date/time to UTC instead of local time

### Cross-cutting: performance, console and network (1 open)

- [ ] [BUG-PERF-001](bugs/BUG-PERF-001.md) · **Open, not retested** · Low · 'Performance' debug timing panel shown on every page, including to non-admin users

### Cross-cutting: attachments and file types (3 open)

- [ ] [BUG-ATT-001](bugs/BUG-ATT-001.md) · **Open, not retested** · High · Uploaded .html and .svg files are served inline from the DataHangar site (stored XSS risk)
- [ ] [BUG-ATT-002](bugs/BUG-ATT-002.md) · **Open, not retested** · Medium · No file-type check on any upload: .exe, .html and anything else is accepted; Notices "Supported…
- [ ] [BUG-ATT-003](bugs/BUG-ATT-003.md) · **Open, not retested** · Low · File names are changed differently in each module; accents and symbols are stripped ("résumé"…

## Summary

| Bugs | High | Medium | Low | Total |
|---|---|---|---|---|
| Open | 15 | 62 | 108 | **185** |
| Fixed (verified by retest) | 5 | 24 | 19 | **48** |
| Closed (by design) | 0 | 1 | 0 | **1** |
| **All** | 20 | 87 | 127 | **234** |

- 146 of the 185 open bugs have never been retested since they were found, so some may already be fixed.
- Checklists: 76 of 76 done. 1082 checks: 782 pass, 224 fail, 26 blocked, 48 N/A.
- Issues from the two earlier external audits are listed separately under "External audit issues".

## Decisions needed and not yet tested

<!-- keep:todo -->
**Needs Jon's decision**
- Exams: should a group-level user (e.g. BETA TEST ONLY Grpuser) be able to read the answers and scores of other people's exam attempts? On v2.0.122 he can.

**Agreed product decisions (don't report as bugs)**
- Active Flights shows all flights to anyone with access to the module, so flight followers never have flights hidden (BUG-AF-005 closed, 24/10/2026).
- There is no "all day" booking and there won't be one.
- Sub-1-second load times aren't a target on stresstest (large data set); Flight Schedule now lazy-loads.

**Not tested yet**
- Flight Details: whether the server rejects an unknown waypoint, a non-crew PIC, or a Complete save with missing data when sent directly (not through the page).
- Flight Details: an old leg with a passenger as PIC, the W&B front-seat passenger group, and Save from Active Flights.
- Exams: saving progress on someone else's unstarted attempt; question types other than Multi-Response and Multiple Choice taken live.
- Active Flights v2.0.123: a SAR time just after a daylight-saving change, iPad Safari, and Escape/x on the Notes, PIC contact and error popups.
- Most open bugs have never been retested (see section 1); they need a retest pass once fixes are deployed.
<!-- /keep:todo -->

## Open High bugs

| Bug | Module | Title | Status | Last retest |
|---|---|---|---|---|
| [BUG-PD-006](bugs/BUG-PD-006.md) | Personnel Details | Personnel Details > Recency and Renewals: action buttons are hidden (Add Item, Table/Card view, renewal Save / Complete Renewal / Cancel) and Group by / Order by are disabled | Open, not retested | - |
| [BUG-PD-011](bugs/BUG-PD-011.md) | Personnel Details | Personnel Details > Security: Change Password always fails with 'Invalid Action: change_password' | Open, not retested | - |
| [BUG-RB-007](bugs/BUG-RB-007.md) | Roster Builder | Roster Builder: Clear then Publish of a draft month with no shifts does not clear the live roster and shows no message | Open, not retested | - |
| [BUG-SLP-002](bugs/BUG-SLP-002.md) | Settings: Lesson Plans | Lesson Plan Settings: Exercises are never saved; add/edit/delete only change the page and are lost when you leave | Open, not retested | - |
| [BUG-SMS-005](bugs/BUG-SMS-005.md) | Safety Reports | Safety Reports: group-level (WG) and own-level (WO) users see no reports at all, not even ones they submitted | Open, not retested | - |
| [BUG-ATT-001](bugs/BUG-ATT-001.md) | Attachments (all modules) | Uploaded .html and .svg files are served inline from the DataHangar site (stored XSS risk) | Open, not retested | - |
| [BUG-IPCALC-001](bugs/BUG-IPCALC-001.md) | iPad app — Calculator > Unit Converter (Distance) | Unit Converter: NM <-> Statute Miles conversion inverted; large values shown in scientific notation | Open, still failing | - |
| [BUG-IPFL-002](bugs/BUG-IPFL-002.md) | Flight sync / personnel | Flights with a Student PIC cannot be pushed from the app | Open, still failing | - |
| [BUG-IPFL-003](bugs/BUG-IPFL-003.md) | iPad app — Flights > Leg Detail > Route & Times (also time engine) | Leg times pulled from DataHangar ("HH:MM:SS") display as the current time; editing overwrites them | Open, still failing | - |
| [BUG-IPFORM-001](bugs/BUG-IPFORM-001.md) | Flight forms / upload | Pushed form uses the wrong template and loses widget data | Open, still failing | - |
| [BUG-IPFORM-002](bugs/BUG-IPFORM-002.md) | Flight forms / sync | Pull creates phantom form instances and pushed updates are ignored | Open, still failing | - |
| [BUG-IPFORM-003](bugs/BUG-IPFORM-003.md) | iPad app — Forms engine (Safety Report forms and Flight forms), checklist 70/74 | Form Date/Time widgets ignore website values and show (and can save) the current date/time | Open, still failing | - |
| [BUG-IPSMS-001](bugs/BUG-IPSMS-001.md) | iPad app — Safety Reports > Forms (checklist 74) | Safety Report form attached in iPad app is silently lost on push | Open, still failing | - |
| [BUG-WEBCHAT-001](bugs/BUG-WEBCHAT-001.md) | Website / Chat API | Chat API used by the iPad app ignores the Chat permission (permission bypass) | Open, still failing | - |
| [BUG-WEBTRK-001](bugs/BUG-WEBTRK-001.md) | Website / Live Tracking API | Live tracking pings fail on stresstest - live_tracking table missing | Open, still failing | - |

## Progress by checklist

| Checklist | Prefix | Area | Checks | Pass | Fail | Blocked | N/A | Bugs | Fixed | Closed | Open | State |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [00-setup-and-accounts](checklists/00-setup-and-accounts.md) | `SET` | Session setup, accounts and baseline | 9 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | DONE |
| [01-login-auth](checklists/01-login-auth.md) | `LOG` | Login, 2FA, sessions, landing page | 25 | 19 | 0 | 1 | 5 | 3 | 3 | 0 | 0 | DONE |
| [02-shell-navigation](checklists/02-shell-navigation.md) | `NAV` | Application shell, sidebar, header, mobile | 27 | 24 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | DONE |
| [03-common-conventions](checklists/03-common-conventions.md) | `CON` | Common screen conventions (apply on every page) | 22 | 17 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | DONE |
| [04-access-manager](checklists/04-access-manager.md) | `AM` | Access Manager (users, roles, groups, permissions, templates) | 38 | 36 | 1 | 0 | 0 | 7 | 7 | 0 | 0 | DONE |
| [05-dashboard](checklists/05-dashboard.md) | `DSH` | Dashboard | 19 | 19 | 0 | 0 | 0 | 5 | 5 | 0 | 0 | DONE |
| [06-flight-schedule](checklists/06-flight-schedule.md) | `FS` | Flight Schedule (incl. embedded Location Planner) | 40 | 37 | 1 | 0 | 1 | 9 | 9 | 0 | 0 | DONE |
| [07-flight-details](checklists/07-flight-details.md) | `FD` | Flight Details | 44 | 44 | 0 | 0 | 0 | 12 | 9 | 0 | 3 | DONE |
| [08-active-flights](checklists/08-active-flights.md) | `AF` | Active Flights and Live Tracking | 19 | 19 | 0 | 0 | 0 | 5 | 4 | 1 | 0 | DONE |
| [09-daily-flight-record](checklists/09-daily-flight-record.md) | `DFR` | Daily Flight Record | 16 | 14 | 2 | 0 | 0 | 3 | 0 | 0 | 3 | DONE |
| [10-location-planner](checklists/10-location-planner.md) | `LP` | Location Planner (stand-alone) | 9 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | DONE |
| [11-personnel-list](checklists/11-personnel-list.md) | `PL` | All Personnel (Personnel List) | 11 | 10 | 1 | 0 | 0 | 2 | 0 | 0 | 2 | DONE |
| [12-personnel-details](checklists/12-personnel-details.md) | `PD` | Personnel Details / My Account | 36 | 21 | 15 | 0 | 0 | 20 | 0 | 0 | 20 | DONE |
| [13-roster-viewer](checklists/13-roster-viewer.md) | `RV` | Roster Viewer | 12 | 9 | 3 | 0 | 0 | 3 | 0 | 0 | 3 | DONE |
| [14-roster-builder](checklists/14-roster-builder.md) | `RB` | Roster Builder | 21 | 13 | 8 | 0 | 0 | 8 | 0 | 0 | 8 | DONE |
| [15-timesheets-leave](checklists/15-timesheets-leave.md) | `TS` | Timesheets, Timesheet Details, Leave Requests | 17 | 11 | 6 | 0 | 0 | 8 | 0 | 0 | 8 | DONE |
| [16-flight-and-duty](checklists/16-flight-and-duty.md) | `FAD` | Flight and Duty | 14 | 12 | 2 | 0 | 0 | 5 | 0 | 0 | 5 | DONE |
| [17-notices](checklists/17-notices.md) | `NOT` | Notices | 16 | 12 | 4 | 0 | 0 | 5 | 0 | 0 | 5 | DONE |
| [18-recency-renewals](checklists/18-recency-renewals.md) | `REC` | Recency and Renewals (overview page) | 11 | 7 | 2 | 0 | 2 | 2 | 0 | 0 | 2 | DONE |
| [19-safety-reports](checklists/19-safety-reports.md) | `SMS` | Safety Reports (SMS) | 21 | 18 | 2 | 1 | 0 | 6 | 0 | 0 | 6 | DONE |
| [20-hazard-register](checklists/20-hazard-register.md) | `HAZ` | Hazard Register | 10 | 8 | 2 | 0 | 0 | 3 | 0 | 0 | 3 | DONE |
| [21-settings-hub](checklists/21-settings-hub.md) | `HUB` | Settings and Tools hub | 11 | 10 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | DONE |
| [22-file-browser](checklists/22-file-browser.md) | `FB` | File Browser | 14 | 8 | 6 | 0 | 0 | 9 | 0 | 0 | 9 | DONE |
| [23-form-builder](checklists/23-form-builder.md) | `FBLD` | Form Builder | 14 | 10 | 4 | 0 | 0 | 4 | 0 | 0 | 4 | DONE |
| [24-form-browser](checklists/24-form-browser.md) | `FBR` | Form Browser / Form Viewer | 10 | 7 | 3 | 0 | 0 | 3 | 0 | 0 | 3 | DONE |
| [25-task-tracker](checklists/25-task-tracker.md) | `TT` | Task Tracker | 12 | 8 | 4 | 0 | 0 | 4 | 0 | 0 | 4 | DONE |
| [26-reports](checklists/26-reports.md) | `RPT` | Reports | 16 | 13 | 3 | 0 | 0 | 4 | 0 | 0 | 4 | DONE |
| [27-support](checklists/27-support.md) | `SUP` | Support tickets | 14 | 11 | 3 | 0 | 0 | 4 | 1 | 0 | 3 | DONE |
| [28-chat](checklists/28-chat.md) | `CHAT` | Chat | 11 | 8 | 2 | 1 | 0 | 4 | 0 | 0 | 4 | DONE |
| [29-exams](checklists/29-exams.md) | `EXM` | Exam Builder, Exam Editor, Exam Instances | 16 | 10 | 6 | 0 | 0 | 10 | 3 | 0 | 7 | DONE |
| [30-maintenance](checklists/30-maintenance.md) | `MX` | Maintenance Portal | 11 | 0 | 0 | 11 | 0 | 0 | 0 | 0 | 0 | DONE |
| [31-settings-flightschedule](checklists/31-settings-flightschedule.md) | `SFS` | Settings – Flight Schedule | 13 | 12 | 0 | 0 | 1 | 2 | 2 | 0 | 0 | DONE |
| [32-settings-dfr](checklists/32-settings-dfr.md) | `SDFR` | Settings – Daily Flight Record | 7 | 5 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | DONE |
| [33-settings-timezone](checklists/33-settings-timezone.md) | `STZ` | Settings – Time Zone (date/time matrix) | 11 | 7 | 4 | 0 | 0 | 3 | 0 | 0 | 3 | DONE |
| [34-settings-resources](checklists/34-settings-resources.md) | `SRES` | Settings – Resources (Aircraft) | 18 | 16 | 2 | 0 | 0 | 1 | 0 | 0 | 1 | DONE |
| [35-settings-wab](checklists/35-settings-wab.md) | `SWAB` | Settings – Weight and Balance Configs | 13 | 9 | 4 | 0 | 0 | 5 | 0 | 0 | 5 | DONE |
| [36-settings-extraflightinfo](checklists/36-settings-extraflightinfo.md) | `SEFI` | Settings – Extra Flight Info | 9 | 7 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | DONE |
| [37-settings-flighttypes](checklists/37-settings-flighttypes.md) | `SFT` | Settings – Flight Types | 8 | 5 | 2 | 0 | 1 | 2 | 0 | 0 | 2 | DONE |
| [38-settings-waypoints](checklists/38-settings-waypoints.md) | `SWP` | Settings – Waypoint Locations | 12 | 8 | 3 | 0 | 1 | 5 | 0 | 0 | 5 | DONE |
| [39-settings-shifttypes](checklists/39-settings-shifttypes.md) | `SST` | Settings – Roster Shifts | 10 | 7 | 3 | 0 | 0 | 4 | 0 | 0 | 4 | DONE |
| [40-settings-frms](checklists/40-settings-frms.md) | `SFRMS` | Settings – Fatigue Risk Management | 11 | 8 | 2 | 0 | 1 | 2 | 0 | 0 | 2 | DONE |
| [41-settings-renewals](checklists/41-settings-renewals.md) | `SREN` | Settings – Recency and Renewals | 10 | 5 | 4 | 0 | 1 | 4 | 0 | 0 | 4 | DONE |
| [42-settings-lessonplans](checklists/42-settings-lessonplans.md) | `SLP` | Settings – Lesson Plans | 9 | 5 | 3 | 0 | 1 | 3 | 0 | 0 | 3 | DONE |
| [43-settings-riskmatrix](checklists/43-settings-riskmatrix.md) | `SRM` | Settings – Risk Matrix | 9 | 6 | 2 | 0 | 1 | 2 | 0 | 0 | 2 | DONE |
| [44-settings-smsreports](checklists/44-settings-smsreports.md) | `SSMS` | Settings – Safety Reports | 9 | 7 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | DONE |
| [45-settings-inspections](checklists/45-settings-inspections.md) | `SINS` | Settings – Inspection Notifications | 9 | 6 | 3 | 0 | 0 | 3 | 0 | 0 | 3 | DONE |
| [46-settings-integrations](checklists/46-settings-integrations.md) | `SINT` | Settings – Google Calendar, WhatsApp | 10 | 6 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | DONE |
| [47-settings-activitylog](checklists/47-settings-activitylog.md) | `SLOG` | Settings – Activity Log | 9 | 6 | 2 | 0 | 1 | 1 | 0 | 0 | 1 | DONE |
| [60-ipad-setup-install](checklists/60-ipad-setup-install.md) | `IPSET` | iPad setup and install | 3 | 2 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | DONE |
| [61-ipad-config-general](checklists/61-ipad-config-general.md) | `IPCFG` | iPad configuration – general | 8 | 3 | 5 | 0 | 0 | 2 | 0 | 0 | 2 | DONE |
| [62-ipad-datahangar-login](checklists/62-ipad-datahangar-login.md) | `IPDH` | iPad DataHangar login and sync | 8 | 6 | 2 | 0 | 0 | 2 | 0 | 0 | 2 | DONE |
| [63-ipad-sync-reference-data](checklists/63-ipad-sync-reference-data.md) | `IPREF` | iPad sync reference data | 10 | 9 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | DONE |
| [64-ipad-aircraft-editor](checklists/64-ipad-aircraft-editor.md) | `IPAC` | iPad aircraft editor | 10 | 7 | 2 | 0 | 1 | 1 | 0 | 0 | 1 | DONE |
| [65-ipad-personnel-waypoints](checklists/65-ipad-personnel-waypoints.md) | `IPPW` | iPad personnel and waypoints | 11 | 7 | 3 | 0 | 1 | 1 | 0 | 0 | 1 | DONE |
| [66-ipad-flights-list](checklists/66-ipad-flights-list.md) | `IPFL` | iPad flights list | 14 | 6 | 6 | 0 | 2 | 3 | 0 | 0 | 3 | DONE |
| [67-ipad-flight-legs](checklists/67-ipad-flight-legs.md) | `IPLEG` | iPad flight legs | 8 | 7 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | DONE |
| [68-ipad-weight-balance](checklists/68-ipad-weight-balance.md) | `IPWB` | iPad weight and balance | 6 | 3 | 3 | 0 | 0 | 2 | 0 | 0 | 2 | DONE |
| [69-ipad-flight-times-meters](checklists/69-ipad-flight-times-meters.md) | `IPFT` | iPad flight times and meters | 9 | 7 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | DONE |
| [70-ipad-flight-forms](checklists/70-ipad-flight-forms.md) | `IPFORM` | iPad flight forms | 7 | 4 | 3 | 0 | 0 | 2 | 0 | 0 | 2 | DONE |
| [71-ipad-flight-files](checklists/71-ipad-flight-files.md) | `IPFILE` | iPad flight files | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | DONE |
| [72-ipad-push-pull-sync](checklists/72-ipad-push-pull-sync.md) | `IPSYNC` | iPad push/pull sync | 7 | 3 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | DONE |
| [73-ipad-pdf-json-export](checklists/73-ipad-pdf-json-export.md) | `IPPDF` | iPad PDF/JSON export | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | DONE |
| [74-ipad-safety-reports](checklists/74-ipad-safety-reports.md) | `IPSMS` | iPad safety reports | 18 | 10 | 7 | 0 | 1 | 5 | 0 | 0 | 5 | DONE |
| [75-ipad-comms-chat](checklists/75-ipad-comms-chat.md) | `IPCHAT` | iPad communications and chat | 12 | 9 | 1 | 0 | 2 | 1 | 0 | 0 | 1 | DONE |
| [76-ipad-calculator](checklists/76-ipad-calculator.md) | `IPCALC` | iPad calculator | 12 | 11 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | DONE |
| [77-ipad-live-tracking](checklists/77-ipad-live-tracking.md) | `IPTRK` | iPad live tracking | 5 | 3 | 2 | 0 | 0 | 3 | 0 | 0 | 3 | DONE |
| [78-ipad-cross-cutting](checklists/78-ipad-cross-cutting.md) | `IPXC` | iPad cross-cutting checks | 23 | 14 | 8 | 0 | 1 | 4 | 0 | 0 | 4 | DONE |
| [79-ipad-permissions-e2e](checklists/79-ipad-permissions-e2e.md) | `IPE2E` | iPad permissions and end-to-end | 76 | 43 | 17 | 0 | 16 | 4 | 0 | 0 | 4 | DONE |
| [90-xc-permissions](checklists/90-xc-permissions.md) | `PERM` | Cross-cutting: permission levels | 10 | 10 | 0 | 0 | 0 | 4 | 2 | 0 | 2 | DONE |
| [91-xc-popups](checklists/91-xc-popups.md) | `POP` | Cross-cutting: popups/modals | 8 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | DONE |
| [92-xc-dates-timezones](checklists/92-xc-dates-timezones.md) | `DATE` | Cross-cutting: date/time formats and pickers | 7 | 3 | 4 | 0 | 0 | 2 | 2 | 0 | 0 | DONE |
| [93-xc-mobile](checklists/93-xc-mobile.md) | `MOB` | Cross-cutting: mobile / narrow layout | 4 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | DONE |
| [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | `UI` | Cross-cutting: UI consistency and icon inventory | 7 | 3 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | DONE |
| [95-xc-performance-errors](checklists/95-xc-performance-errors.md) | `PERF` | Cross-cutting: performance, console and network | 4 | 1 | 3 | 0 | 0 | 1 | 0 | 0 | 1 | DONE |
| [96-xc-attachments](checklists/96-xc-attachments.md) | `ATT` | Cross-cutting: attachments and file types | 33 | 19 | 13 | 0 | 1 | 3 | 0 | 0 | 3 | DONE |
| [99-e2e-workflows](checklists/99-e2e-workflows.md) | `E2E` | End-to-end workflows | 8 | 6 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | DONE |

## Bug details

Full title, checklist row and latest retest for every bug, open first. The bug files have the complete write-up.

| Bug | Severity | Checklist row | Module | Title | Status | Last retest |
|---|---|---|---|---|---|---|
| [BUG-PD-006](bugs/BUG-PD-006.md) | High | `PD-019` | Personnel Details | Personnel Details > Recency and Renewals: action buttons are hidden (Add Item, Table/Card view, renewal Save / Complete Renewal / Cancel) and Group by / Order by are disabled | Open (not retested) | - |
| [BUG-PD-011](bugs/BUG-PD-011.md) | High | `PD-026` | Personnel Details | Personnel Details > Security: Change Password always fails with 'Invalid Action: change_password' | Open (not retested) | - |
| [BUG-RB-007](bugs/BUG-RB-007.md) | High | `RB-013` | Roster Builder | Roster Builder: Clear then Publish of a draft month with no shifts does not clear the live roster and shows no message | Open (not retested) | - |
| [BUG-SMS-005](bugs/BUG-SMS-005.md) | High | `SMS-015` | Safety Reports | Safety Reports: group-level (WG) and own-level (WO) users see no reports at all, not even ones they submitted | Open (not retested) | - |
| [BUG-SLP-002](bugs/BUG-SLP-002.md) | High | `SLP-001` | Settings: Lesson Plans | Lesson Plan Settings: Exercises are never saved; add/edit/delete only change the page and are lost when you leave | Open (not retested) | - |
| [BUG-IPFL-002](bugs/BUG-IPFL-002.md) | High | `IPFL-002f` | Flight sync / personnel | Flights with a Student PIC cannot be pushed from the app | Open | - |
| [BUG-IPFL-003](bugs/BUG-IPFL-003.md) | High | `IPFL-010` | iPad app — Flights > Leg Detail > Route & Times (also time engine) | Leg times pulled from DataHangar ("HH:MM:SS") display as the current time; editing overwrites them | Open | - |
| [BUG-IPFORM-001](bugs/BUG-IPFORM-001.md) | High | `IPFORM-003` | Flight forms / upload | Pushed form uses the wrong template and loses widget data | Open | - |
| [BUG-IPFORM-002](bugs/BUG-IPFORM-002.md) | High | `IPFORM-004` | Flight forms / sync | Pull creates phantom form instances and pushed updates are ignored | Open | - |
| [BUG-IPFORM-003](bugs/BUG-IPFORM-003.md) | High | `IPSMS-014` | iPad app — Forms engine (Safety Report forms and Flight forms), checklist 70/74 | Form Date/Time widgets ignore website values and show (and can save) the current date/time | Open | - |
| [BUG-IPSMS-001](bugs/BUG-IPSMS-001.md) | High | `IPSMS-013` | iPad app — Safety Reports > Forms (checklist 74) | Safety Report form attached in iPad app is silently lost on push | Open | - |
| [BUG-IPCALC-001](bugs/BUG-IPCALC-001.md) | High | `IPCALC-010` | iPad app — Calculator > Unit Converter (Distance) | Unit Converter: NM <-> Statute Miles conversion inverted; large values shown in scientific notation | Open | - |
| [BUG-WEBTRK-001](bugs/BUG-WEBTRK-001.md) | High | `IPTRK-003` | Website / Live Tracking API | Live tracking pings fail on stresstest - live_tracking table missing | Open | - |
| [BUG-WEBCHAT-001](bugs/BUG-WEBCHAT-001.md) | High | `IPPERM-024` | Website / Chat API | Chat API used by the iPad app ignores the Chat permission (permission bypass) | Open | - |
| [BUG-ATT-001](bugs/BUG-ATT-001.md) | High | `ATT-033` | Attachments (all modules) | Uploaded .html and .svg files are served inline from the DataHangar site (stored XSS risk) | Open (not retested) | - |
| [BUG-FD-012](bugs/BUG-FD-012.md) | Medium | `ATT-002` | Flight Details | Flight Details Files: .txt shows its text in a "Required Information" alert; empty .txt and .html show error messages | Open (not retested) | - |
| [BUG-DFR-002](bugs/BUG-DFR-002.md) | Medium | `DFR-008` | Daily Flight Record | Daily Flight Record: Clear Filters unticks every status (lists Open, Cancelled and Deleted flights), and the date fields show today's date when no date filter is applied | Open (not retested) | - |
| [BUG-DFR-003](bugs/BUG-DFR-003.md) | Medium | `DFR-008` | Daily Flight Record | Daily Flight Record: changing filters quickly appends results instead of replacing them, showing duplicate and wrong-status rows | Open (not retested) | - |
| [BUG-PD-001](bugs/BUG-PD-001.md) | Medium | `PD-S01` | Personnel Details / My Account | personneldetails/index.js is truncated: ReferenceError getPickerMod on every load | Open (not retested) | - |
| [BUG-PD-003](bugs/BUG-PD-003.md) | Medium | `PD-027` | Personnel Details > Security | 2FA setup: one wrong verification code closes the setup dialog and issues a new secret | Open (not retested) | - |
| [BUG-PD-007](bugs/BUG-PD-007.md) | Medium | `PD-021` | Personnel Details | Personnel Details > Recency: 'Days Until Expiry' and status don't match the Last Conducted date | Open (not retested) | - |
| [BUG-PD-008](bugs/BUG-PD-008.md) | Medium | `PD-021` | Personnel Details | Personnel Details > Recency: the recency summary popup has no Add Manual Entry, no x, and doesn't close with Escape | Open (not retested) | - |
| [BUG-PD-009](bugs/BUG-PD-009.md) | Medium | `PD-022` | Personnel Details | Personnel Details > Renewal edit: the Today and Calculate links can't be clicked because the date fields cover them | Open (not retested) | - |
| [BUG-PD-012](bugs/BUG-PD-012.md) | Medium | `PD-025` | Personnel Details | Personnel Details > Files: opening a file shows 'File Access Error' with the file's contents as the message | Not fixed (retested 24/10/2026 v2.0.123) | 24/10/2026 v2.0.123: Not fixed |
| [BUG-PD-016](bugs/BUG-PD-016.md) | Medium | `PD-010` | Personnel Details | Personnel Details > Timesheets: Add Claim button does nothing | Open (not retested) | - |
| [BUG-PD-017](bugs/BUG-PD-017.md) | Medium | `PD-018` | Personnel Details | Personnel Details > Lesson Plans: an assigned plan is saved but never listed; the dialog's dates default to the UTC date | Open (not retested) | - |
| [BUG-PL-003](bugs/BUG-PL-003.md) | Medium | `PD-029` | Personnel List / Personnel Details | All Personnel: a Read Only Group (RG) user can't open the details of anyone in their group | Open (not retested) | - |
| [BUG-RV-002](bugs/BUG-RV-002.md) | Medium | `RV-004` | Roster Viewer | Roster Viewer: clicking a shift does not open Shift Details | Open (not retested) | - |
| [BUG-RB-002](bugs/BUG-RB-002.md) | Medium | `RB-003` | Roster Builder | Roster Builder: Copy Live to Draft copies one shift at a time and takes about 6 minutes for one month | Open (not retested) | - |
| [BUG-RB-003](bugs/BUG-RB-003.md) | Medium | `RB-006` | Roster Builder | Roster Builder: copy/paste still works with violation checking ON | Open (not retested) | - |
| [BUG-RB-005](bugs/BUG-RB-005.md) | Medium | `RB-008` | Roster Builder | Roster Builder: every validation error throws a JS error instead of showing a message (e.g. Apply Shift Pattern with no shifts) | Open (not retested) | - |
| [BUG-RB-008](bugs/BUG-RB-008.md) | Medium | `RB-015` | Roster Builder | Roster Builder can only be opened from Settings and Tools, so a Roster Builder user without System Settings can't reach it | Open (not retested) | - |
| [BUG-TS-002](bugs/BUG-TS-002.md) | Medium | `TS-001` | Timesheets | Timesheet Approval: status filter 'Unsigned' shows 'No personnel found' although everyone has unsigned days | Open (not retested) | - |
| [BUG-TS-003](bugs/BUG-TS-003.md) | Medium | `TS-002` | Timesheets | Timesheet Approval list totals don't match Timesheet Details (Rostered Days and Duty Hours) | Open (not retested) | - |
| [BUG-TS-008](bugs/BUG-TS-008.md) | Medium | `TS-008` | Timesheets / Leave Requests | Approving a leave request doesn't change the rostered shifts, and rejecting with no reason gives no message | Open (not retested) | - |
| [BUG-NOT-002](bugs/BUG-NOT-002.md) | Medium | `NOT-006` | Notices | Notice Details: clicking a .txt attachment does nothing (no preview, no download) | Not fixed (retested 24/10/2026 v2.0.123) | 24/10/2026 v2.0.123: Not fixed |
| [BUG-NOT-004](bugs/BUG-NOT-004.md) | Medium | `NOT-004` | Notices | Notices: a Write Group (WG) user gets 'An error occurred' when clicking New Notice | Open (not retested) | - |
| [BUG-SMS-001](bugs/BUG-SMS-001.md) | Medium | `SMS-004` | Safety Reports | New Safety Report: Escape on the Confidential/Anonymous help closes the report form behind it and loses what you typed | Open (not retested) | - |
| [BUG-SMS-002](bugs/BUG-SMS-002.md) | Medium | `SMS-S04` | Safety Reports | New Safety Report: Event Date/Time defaults to the UTC date and time, not local | Open (not retested) | - |
| [BUG-HAZ-001](bugs/BUG-HAZ-001.md) | Medium | `HAZ-003` | Hazard Register | Hazard Register details: Hazard Type always shows '--' | Open (not retested) | - |
| [BUG-HAZ-002](bugs/BUG-HAZ-002.md) | Medium | `HAZ-003` | Hazard Register | Hazard Register details: Final Risk Assessment never shows the saved final risk | Open (not retested) | - |
| [BUG-FB-003](bugs/BUG-FB-003.md) | Medium | `FB-006` | File Browser | File Browser: clicking a .txt file shows 'File Access Error' with the file's own text | Not fixed (retested 24/10/2026 v2.0.123) | 24/10/2026 v2.0.123: Not fixed |
| [BUG-FB-005](bugs/BUG-FB-005.md) | Medium | `FB-007` | File Browser | File Browser: Read/Write Access groups are not kept after Update Document | Open (not retested) | - |
| [BUG-FB-006](bugs/BUG-FB-006.md) | Medium | `FB-008` | File Browser | File Browser: deleting a folder fails with 'Invalid Action: filebrowser_deletefolder' | Open (not retested) | - |
| [BUG-FB-008](bugs/BUG-FB-008.md) | Medium | `ATT-030` | File Browser | Files attached to a waypoint also appear in the File Browser Home folder | Open (not retested) | - |
| [BUG-FBLD-002](bugs/BUG-FBLD-002.md) | Medium | `FBLD-S04` | Form Builder | Form Builder View Form: Date and Time widgets default to UTC, not local time | Open (not retested) | - |
| [BUG-FBLD-003](bugs/BUG-FBLD-003.md) | Medium | `FBLD-005` | Form Builder | Form Builder: table conditions do nothing in View Form | Open (not retested) | - |
| [BUG-TT-004](bugs/BUG-TT-004.md) | Medium | `TT-006` | Task Tracker | Task Tracker: a Write Group (WG) user is treated as read-only and can't add a project | Open (not retested) | - |
| [BUG-RPT-003](bugs/BUG-RPT-003.md) | Medium | `RPT-S05` | Reports | Reports tables overlap on a phone: column text is drawn on top of other columns | Open (not retested) | - |
| [BUG-SUP-001](bugs/BUG-SUP-001.md) | Medium | `SUP-S02` | Support | Support has no page Help (?); Escape doesn't close New Ticket, but a click outside closes it and wipes everything typed | Open (not retested) | - |
| [BUG-AM-006](bugs/BUG-AM-006.md) | Medium | `CHAT-005` | Access Manager / Chat | Access Manager has no Chat permission, so you can't give Chat to a non-admin user | Open (retested 22/10/2026, part fixed) | - |
| [BUG-EXM-004](bugs/BUG-EXM-004.md) | Medium | `EXM-003` | Exams | Exam Builder has no way to link or unlink user groups on an exam group | Open (not retested) | - |
| [BUG-EXM-008](bugs/BUG-EXM-008.md) | Medium | `EXM-001` | Exams | Exam Builder: deleting an exam or exam group that has instances fails silently (error only in the console), and graded instances can't be removed | Open (not retested) | - |
| [BUG-STZ-001](bugs/BUG-STZ-001.md) | Medium | `STZ-S04` | Settings: Time Zone | Time Zone settings: the Example preview shows UTC, not the selected time zone | Open (not retested) | - |
| [BUG-STZ-003](bugs/BUG-STZ-003.md) | Medium | `STZ-002` | Settings: Time Zone | Time Zone settings: the Example preview shows MM/DD/YYYY for every date format except DD/MM/YYYY | Open (not retested) | - |
| [BUG-SFT-002](bugs/BUG-SFT-002.md) | Medium | `SFT-001` | Settings: Flight Types | Flight Types: a duplicate Flight Category name ("PIC") is accepted | Open (not retested) | - |
| [BUG-SWP-002](bugs/BUG-SWP-002.md) | Medium | `SWP-006` | Settings: Waypoints | Waypoints: moving a waypoint about 250 nm saves with no "Significant Location Change" warning | Open (not retested) | - |
| [BUG-SWP-004](bugs/BUG-SWP-004.md) | Medium | `SWP-S05` | Settings: Waypoints | Waypoints on a phone: table columns overlap and Add Waypoint is off-screen | Open (not retested) | - |
| [BUG-SST-004](bugs/BUG-SST-004.md) | Medium | `SST-S05` | Settings: Shift Types | Roster Shifts on a phone: the table scrolls the page sideways and the group tabs are hidden | Open (not retested) | - |
| [BUG-SREN-002](bugs/BUG-SREN-002.md) | Medium | `SREN-001` | Settings: Recency and Renewals | Add Recency accepts negative Days, and a Caution value higher than Warning | Open (not retested) | - |
| [BUG-SREN-003](bugs/BUG-SREN-003.md) | Medium | `SREN-002` | Settings: Recency and Renewals | Add Renewal Type accepts negative Days to Notify and a Frequency of 0 days | Open (not retested) | - |
| [BUG-SINS-002](bugs/BUG-SINS-002.md) | Medium | `SINS-002` | Settings: Inspection Notifications | Inspection Notifications: a meter inspection on an aircraft at 0.0 hours is never Overdue, and negative meter values are accepted | Open (not retested) | - |
| [BUG-IPSET-001](bugs/BUG-IPSET-001.md) | Medium | `IPSET-001` | Unit tests | Unit-test target does not compile | Open | - |
| [BUG-IPCFG-001](bugs/BUG-IPCFG-001.md) | Medium | `IPCFG-009` | iPad app — Configuration > Configuration PIN / PinPadView | Configuration PIN saves non-4-digit values, permanently locking Configuration | Open | - |
| [BUG-IPAC-001](bugs/BUG-IPAC-001.md) | Medium | `IPAC-006` | iPad app — Configuration > Aircraft > editor; SyncService.syncAircraft | Aircraft editor edits to server aircraft are local-only and silently reverted by Sync All | Open | - |
| [BUG-IPWPT-001](bugs/BUG-IPWPT-001.md) | Medium | `IPWPT-004` | iPad app — Configuration > Waypoints | Code-less server waypoints show blank titles; editing them stores 0,0 coordinates; edits are local-only | Open | - |
| [BUG-IPSMS-002](bugs/BUG-IPSMS-002.md) | Medium | `IPSMS-016` | iPad app — Safety Reports > Final Report | Final Report tab shows stale values after Pull (overwrite risk) | Open | - |
| [BUG-IPSMS-004](bugs/BUG-IPSMS-004.md) | Medium | `IPSMS-009` | iPad app — Safety Reports > push/sync | Safety Report push can report success after form or status updates fail | Open | - |
| [BUG-IPCHAT-001](bugs/BUG-IPCHAT-001.md) | Medium | `IPCHAT-010` |  | Chat message typed while offline is discarded on send | Open | - |
| [BUG-IPTRK-002](bugs/BUG-IPTRK-002.md) | Medium | `IPTRK-006` | iPad app — Live Tracking | Live Tracking queue stores duplicate/stale pings; rejected pings are dropped | Open | - |
| [BUG-IPSYNC-001](bugs/BUG-IPSYNC-001.md) | Medium | `IPOFF-005` | Flight sync / conflict handling | Push silently overwrites website-side Notes edits | Open | - |
| [BUG-IPUI-001](bugs/BUG-IPUI-001.md) | Medium | `IPXC-002` | iPad UI / keyboard focus | Hardware-keyboard focus leaks through sheets and keypads | Open | - |
| [BUG-IPFL-004](bugs/BUG-IPFL-004.md) | Medium | `IPPERM-067` | iPad app, Flights (download/pull/push) | Flight downloaded before aircraft sync keeps aircraft "None" forever; Pull never re-links; push fails with "(nil)" | Open | - |
| [BUG-IPPERM-001](bugs/BUG-IPPERM-001.md) | Medium | `IPPERM-049` | iPad app, Flights, permissions | App lets read-only users edit and push flights and only fails at the server, showing a raw "Error block Error" message | Open | - |
| [BUG-IPSYNC-002](bugs/BUG-IPSYNC-002.md) | Medium | `IPPERM-063` | Flight sync / pull | Pull from Server does not reliably update website-edited Notes | Open | - |
| [BUG-PERM-002](bugs/BUG-PERM-002.md) | Medium | `PERM-007` | Personnel Details / My Account | User with no permissions cannot open their own My Account (no self-service password / 2FA) | Open (not retested) | - |
| [BUG-ATT-002](bugs/BUG-ATT-002.md) | Medium | `ATT-034` | Attachments (all modules) | No file-type check on any upload: .exe, .html and anything else is accepted; Notices "Supported formats" isn't enforced | Open (not retested) | - |
| [BUG-FD-011](bugs/BUG-FD-011.md) | Low | `FD-037` | Flight Details | History labels lock and unlock differently ("Locked: No > Yes" vs "Status: Locked > Unlocked") | Open (not retested) | - |
| [BUG-FD-013](bugs/BUG-FD-013.md) | Low | `ATT-002` | Flight Details | Flight Details Files: clicking a PDF opens it in two new tabs | Open (not retested) | - |
| [BUG-DFR-001](bugs/BUG-DFR-001.md) | Low | `DFR-S02` | Daily Flight Record | Daily Flight Record has no page Help (?), and its popups (Manage Columns, Notes full text) don't close with Escape | Open (not retested) | - |
| [BUG-PL-001](bugs/BUG-PL-001.md) | Low | `PL-S02` | All Personnel | All Personnel has no page Help (?) | Open (not retested) | - |
| [BUG-PL-002](bugs/BUG-PL-002.md) | Low | `PL-001` | All Personnel | A person with no name exists and is listed as '?' at the top of All Personnel (person #274, Customer) | Open (not retested) | - |
| [BUG-EXM-009](bugs/BUG-EXM-009.md) | Low | `PD-017` | Exams | Exams: a hotspot question with no image shows a developer debug message to the person taking the exam | Open (not retested) | - |
| [BUG-PD-002](bugs/BUG-PD-002.md) | Low | `PD-027` | Personnel Details > Security | Personnel Details modals (Enable 2FA, Setup Error alert): title right-aligned, away from its icon | Open (not retested) | - |
| [BUG-PD-004](bugs/BUG-PD-004.md) | Low | `PD-S04` | Personnel Details > Security | Security tab 'Enabled on' date ignores Settings > Time Zone format | Open (not retested) | - |
| [BUG-PD-005](bugs/BUG-PD-005.md) | Low | `PD-S03` | Personnel Details | Personnel Details: History, PDF Options and Legacy Duty Browser popups don't close with Escape, and PDF Options has no x | Open (not retested) | - |
| [BUG-PD-010](bugs/BUG-PD-010.md) | Low | `PD-024` | Personnel Details | Personnel Details: the 'Performance' timing panel is shown to users and covers buttons | Open (not retested) | - |
| [BUG-PD-013](bugs/BUG-PD-013.md) | Low | `PD-004` | Personnel Details | Personnel Details: an empty Birth Date shows today's date | Open (not retested) | - |
| [BUG-PD-014](bugs/BUG-PD-014.md) | Low | `PD-007` | Personnel Details | Digital Signature: wrong password closes the popup and throws away the drawing; empty Save gives no message | Open (not retested) | - |
| [BUG-PD-015](bugs/BUG-PD-015.md) | Low | `PD-016` | Personnel Details | Flight & Duty Analysis popup: title date is YYYY-MM-DD and Escape doesn't close it | Open (not retested) | - |
| [BUG-PD-018](bugs/BUG-PD-018.md) | Low | `PD-015` | Personnel Details | Request Leave: Start and End Date default to the UTC date, not today's local date | Open (not retested) | - |
| [BUG-RV-001](bugs/BUG-RV-001.md) | Low | `RV-S02` | Roster Viewer | Roster Viewer: no page Help (?) and Group Visibility popup ignores Escape | Open (not retested) | - |
| [BUG-RV-003](bugs/BUG-RV-003.md) | Low | `RV-S04` | Roster Viewer | Roster Viewer shift note popup shows the date as 'October 5, 2026', not the configured DD/MM/YYYY | Open (not retested) | - |
| [BUG-RB-001](bugs/BUG-RB-001.md) | Low | `RB-S02` | Roster Builder | Roster Builder: no page Help (?); Copy/Paste Instructions popup ignores Escape and outside click | Open (not retested) | - |
| [BUG-RB-004](bugs/BUG-RB-004.md) | Low | `RB-S04` | Roster Builder | Roster Builder: Rule Violations popup shows 'Monday, October 5' instead of the configured DD/MM/YYYY date | Open (not retested) | - |
| [BUG-RB-006](bugs/BUG-RB-006.md) | Low | `RB-S05` | Roster Builder | Roster Builder: at phone width the shift palette takes half the screen and the Draft Edit Mode banner covers the search box and palette | Open (not retested) | - |
| [BUG-TS-001](bugs/BUG-TS-001.md) | Low | `TS-S02` | Timesheets | Timesheets: no page Help on Timesheet Approval, and the Help (?) on Timesheet Details does nothing | Open (not retested) | - |
| [BUG-TS-004](bugs/BUG-TS-004.md) | Low | `TS-S04` | Timesheets | Timesheet Details shows dates as 'Oct 5' and times with seconds (14:00:00) | Open (not retested) | - |
| [BUG-TS-005](bugs/BUG-TS-005.md) | Low | `TS-007` | Timesheets | Timesheet Details: F&D and Roster Violation popups ignore Escape and show ISO dates in the title | Open (not retested) | - |
| [BUG-TS-006](bugs/BUG-TS-006.md) | Low | `TS-010` | Leave Requests | Leave Types: a validation error closes the Add Leave Type popup and throws away what you typed; the popup ignores Escape | Open (not retested) | - |
| [BUG-TS-007](bugs/BUG-TS-007.md) | Low | `TS-006` | Timesheets | Reject Claim: leaving the reason empty closes the reject popup and throws a script error | Open (not retested) | - |
| [BUG-FAD-001](bugs/BUG-FAD-001.md) | Low | `FAD-S02` | Flight and Duty | Flight and Duty has no page Help (?) | Open (not retested) | - |
| [BUG-FAD-002](bugs/BUG-FAD-002.md) | Low | `FAD-S02` | Flight and Duty | Flight and Duty popups (Flight Details, Duty Time Details, Roster Violations, Resolutions Required) ignore Escape | Open (not retested) | - |
| [BUG-FAD-003](bugs/BUG-FAD-003.md) | Low | `FAD-S04` | Flight and Duty | Flight and Duty popups show dates as '16 Oct 2026' instead of the configured DD/MM/YYYY | Open (not retested) | - |
| [BUG-FAD-004](bugs/BUG-FAD-004.md) | Low | `FAD-002` | Flight and Duty | Flight and Duty column headers are ambiguous: two '1 Days' and two '24 Hours' columns, and '1 Days' is ungrammatical | Open (not retested) | - |
| [BUG-FAD-005](bugs/BUG-FAD-005.md) | Low | `FAD-003` | Flight and Duty | Flight and Duty 'View as Date' defaults to the UTC date instead of the local date | Open (not retested) | - |
| [BUG-NOT-001](bugs/BUG-NOT-001.md) | Low | `NOT-S02` | Notices | Notices has no page Help (?), and the Create New Notice popup ignores Escape | Open (not retested) | - |
| [BUG-NOT-003](bugs/BUG-NOT-003.md) | Low | `NOT-010` | Notices | Settings and Tools hub: 'Notices' card has no links | Open (not retested) | - |
| [BUG-NOT-005](bugs/BUG-NOT-005.md) | Low | `ATT-012` | Notices | Notices: only one attachment can be added per save | Open (not retested) | - |
| [BUG-REC-001](bugs/BUG-REC-001.md) | Low | `REC-S02` | Recency and Renewals | Recency and Renewals overview has no page Help (?) | Open (not retested) | - |
| [BUG-REC-002](bugs/BUG-REC-002.md) | Low | `REC-S05` | Recency and Renewals | Recency and Renewals at phone width: the table is cut off, so Total Items and Actions are hidden | Open (not retested) | - |
| [BUG-SMS-003](bugs/BUG-SMS-003.md) | Low | `SMS-012` | Safety Reports | Safety Report Final Report: Likelihood and Consequence dropdowns list every option twice | Open (not retested) | - |
| [BUG-SMS-004](bugs/BUG-SMS-004.md) | Low | `SMS-013` | Safety Reports / Hazard Register | Add to Hazard Register: Goal 'Mitigate' shows as 'Minimize' in the Hazard Register | Open (not retested) | - |
| [BUG-SMS-006](bugs/BUG-SMS-006.md) | Low | `ATT-016` | Safety Reports | Safety Report document link for a deleted file shows the server's file path | Open (not retested) | - |
| [BUG-HAZ-003](bugs/BUG-HAZ-003.md) | Low | `HAZ-002` | Hazard Register | Hazard Register has no way to create a hazard entry | Open (not retested) | - |
| [BUG-FB-001](bugs/BUG-FB-001.md) | Low | `FB-S02` | File Browser | File Browser has no page Help (?) | Open (not retested) | - |
| [BUG-FB-002](bugs/BUG-FB-002.md) | Low | `FB-S04` | File Browser | File Browser shows Date Uploaded as 'Oct 22, 2026' instead of DD/MM/YYYY | Open (not retested) | - |
| [BUG-FB-004](bugs/BUG-FB-004.md) | Low | `FB-S03` | File Browser | File Browser: Escape doesn't close the Create New Folder or Configure File popups | Open (not retested) | - |
| [BUG-FB-007](bugs/BUG-FB-007.md) | Low | `FB-S05` | File Browser | File Browser on a phone: table is cut off, edit buttons are off-screen | Open (not retested) | - |
| [BUG-FB-009](bugs/BUG-FB-009.md) | Low | `ATT-029` | File Browser | File Browser: clicking an .svg shows an error popup with the raw SVG code | Open (not retested) | - |
| [BUG-FBLD-001](bugs/BUG-FBLD-001.md) | Low | `FBLD-S02` | Form Builder | Form Builder: popups ignore Escape and outside clicks (Help, Create New Form Template, Edit Options) | Open (not retested) | - |
| [BUG-FBLD-004](bugs/BUG-FBLD-004.md) | Low | `FBLD-S05` | Form Builder | Form Builder on a phone: page is wider than the screen and the Toolbox covers the form | Open (not retested) | - |
| [BUG-FBR-001](bugs/BUG-FBR-001.md) | Low | `FBR-S02` | Form Browser | Form Browser has no page Help (?) | Open (not retested) | - |
| [BUG-FBR-002](bugs/BUG-FBR-002.md) | Low | `FBR-S04` | Form Browser | Form Browser and Form Viewer dates ignore the date setting ('Oct 21, 2026', '10:24 PM') | Open (not retested) | - |
| [BUG-FBR-003](bugs/BUG-FBR-003.md) | Low | `FBR-S05` | Form Browser | Form Browser on a phone: table is cut off, Created and Created By are off-screen | Open (not retested) | - |
| [BUG-TT-001](bugs/BUG-TT-001.md) | Low | `TT-S02` | Task Tracker | Task Tracker: Escape doesn't close Help or Add Project | Open (not retested) | - |
| [BUG-TT-002](bugs/BUG-TT-002.md) | Low | `TT-S04` | Task Tracker | Task Tracker dates ignore the date setting ('Dec 31', '2026-10-21') | Open (not retested) | - |
| [BUG-TT-003](bugs/BUG-TT-003.md) | Low | `TT-S05` | Task Tracker | Task Tracker on a phone: feature cards are pushed right and cut off | Open (not retested) | - |
| [BUG-RPT-001](bugs/BUG-RPT-001.md) | Low | `RPT-S02` | Reports | Reports has no page Help (?), and Escape doesn't close New Report Template | Open (not retested) | - |
| [BUG-RPT-002](bugs/BUG-RPT-002.md) | Low | `RPT-009` | Reports | Reports Export CSV writes dates as '2026-10-16 06:00:00' instead of the org date format | Open (not retested) | - |
| [BUG-RPT-004](bugs/BUG-RPT-004.md) | Low | `RPT-006` | Reports | Reports: the Flight Hours meter column shows the aircraft's current meter on every flight, and Total adds them up | Open (not retested) | - |
| [BUG-SUP-002](bugs/BUG-SUP-002.md) | Low | `SUP-003` | Support | Support New Ticket: Ctrl+V doesn't paste a screenshot, though the error message tells you to use Ctrl+V | Open (not retested) | - |
| [BUG-SUP-003](bugs/BUG-SUP-003.md) | Low | `SUP-005` | Support | Support ticket: clicking a .txt attachment shows an 'Error' popup containing the file's text | Not fixed (retested 24/10/2026 v2.0.123) | 24/10/2026 v2.0.123: Not fixed |
| [BUG-CHAT-001](bugs/BUG-CHAT-001.md) | Low | `CHAT-S02` | Chat | Chat has no page Help (?); Escape doesn't close Create Channel; empty name does nothing with no message | Open (not retested) | - |
| [BUG-CHAT-002](bugs/BUG-CHAT-002.md) | Low | `CHAT-S04` | Chat | Chat times show 12-hour '01:32 AM' and date separators 'Thursday, October 22, 2026' instead of the org format | Open (not retested) | - |
| [BUG-CHAT-003](bugs/BUG-CHAT-003.md) | Low | `ATT-032` | Chat | Chat image button: non-images are ignored with no message; SVG/TIFF/HEIC preview then fail on Send | Open (not retested) | - |
| [BUG-EXM-001](bugs/BUG-EXM-001.md) | Low | `EXM-S02` | Exams | Exam Builder/Editor have no page Help (?); Escape doesn't close Add Group, Add Exam or Choose Question Type | Open (not retested) | - |
| [BUG-EXM-002](bugs/BUG-EXM-002.md) | Low | `EXM-S04` | Exams | Exam dates ignore the org format: 'Oct 22, 2026' in Exam Builder and '10/22/2026 01:46 AM' in Exam Instances batches | Open (not retested) | - |
| [BUG-EXM-003](bugs/BUG-EXM-003.md) | Low | `EXM-004` | Exams | Exam viewer 'Read Only' still shows Add Question, Add Group and Save Question | Open (not retested) | - |
| [BUG-EXM-005](bugs/BUG-EXM-005.md) | Low | `EXM-S05` | Exams | Exam Builder on a phone: exam table columns and action icons overlap | Open (not retested) | - |
| [BUG-EXM-007](bugs/BUG-EXM-007.md) | Low | `EXM-009` | Exams | Exam Instances batch: deleting a person's instance shows success but the row stays until the page is reloaded | Open (not retested) | - |
| [BUG-SDFR-001](bugs/BUG-SDFR-001.md) | Low | `SDFR-S01` | Settings: Daily Flight Record | Daily Flight Record Settings loads a colorpicker.js that does not exist (404 in the console) | Open (not retested) | - |
| [BUG-STZ-002](bugs/BUG-STZ-002.md) | Low | `STZ-S02` | Settings: Time Zone | Time Zone settings page has no Help (?) | Open (not retested) | - |
| [BUG-SRES-001](bugs/BUG-SRES-001.md) | Low | `SRES-S04` | Settings: Resources (Aircraft) | Resources: the meter "Last:" dates show as YYYY-MM-DD instead of the Time Zone date format | Open (not retested) | - |
| [BUG-SWAB-001](bugs/BUG-SWAB-001.md) | Low | `SWAB-S02` | Settings: Weight and Balance | Weight & Balance Configs: no Help (?), and Escape does not close popups | Open (not retested) | - |
| [BUG-SWAB-002](bugs/BUG-SWAB-002.md) | Low | `SWAB-S04` | Settings: Weight and Balance | Weight & Balance Configs: dates show as "14 Oct 2026" / "29 Sept 2026" instead of DD/MM/YYYY | Open (not retested) | - |
| [BUG-SWAB-003](bugs/BUG-SWAB-003.md) | Low | `SWAB-S01` | Settings: Weight and Balance | Weight & Balance Configs shows a debug "Performance" timing panel to users | Open (not retested) | - |
| [BUG-SWAB-004](bugs/BUG-SWAB-004.md) | Low | `SWAB-S05` | Settings: Weight and Balance | Weight & Balance Configs: on a phone the page is wider than the screen | Open (not retested) | - |
| [BUG-SWAB-005](bugs/BUG-SWAB-005.md) | Low | `SWAB-003` | Settings: Weight and Balance | W&B Configs: two revisions show the same number ("Rev 5") until another import renumbers them | Open (not retested) | - |
| [BUG-SEFI-001](bugs/BUG-SEFI-001.md) | Low | `SEFI-S02` | Settings: Extra Flight Info | Extra Flight Info Settings: no Help (?), and Escape does not close Add Field | Open (not retested) | - |
| [BUG-SFT-001](bugs/BUG-SFT-001.md) | Low | `SFT-S02` | Settings: Flight Types | Flight Types Settings: no Help (?), and Escape does not close popups | Open (not retested) | - |
| [BUG-SWP-001](bugs/BUG-SWP-001.md) | Low | `SWP-S02` | Settings: Waypoints | Waypoints Settings: no Help (?), and Escape does not close popups | Open (not retested) | - |
| [BUG-SWP-003](bugs/BUG-SWP-003.md) | Low | `SWP-005` | Settings: Waypoints | Waypoints: the list is not refreshed after you save or delete on the detail page | Open (not retested) | - |
| [BUG-SWP-005](bugs/BUG-SWP-005.md) | Low | `ATT-027` | Settings: Waypoints | Waypoint Files list shows the Uploaded date as MM/DD/YYYY and Size N/A for every file | Open (not retested) | - |
| [BUG-SST-001](bugs/BUG-SST-001.md) | Low | `SST-S02` | Settings: Shift Types | Roster Shifts (Shift Type Editor): no Help (?), and Escape does not close popups | Open (not retested) | - |
| [BUG-SST-002](bugs/BUG-SST-002.md) | Low | `SST-002` | Settings: Shift Types | New Shift Type: Duty Start/End Time default to the current UTC time | Open (not retested) | - |
| [BUG-SST-003](bugs/BUG-SST-003.md) | Low | `SST-001` | Settings: Shift Types | Roster Shifts: after Edit Group the selected group jumps back to Duty, so the next New Shift Type goes into the wrong group | Open (not retested) | - |
| [BUG-SFRMS-001](bugs/BUG-SFRMS-001.md) | Low | `SFRMS-S02` | Settings: FRMS | FRMS Settings: no Help (?), and Escape does not close popups | Open (not retested) | - |
| [BUG-SFRMS-002](bugs/BUG-SFRMS-002.md) | Low | `SFRMS-S05` | Settings: FRMS | FRMS Settings on a phone: the page scrolls sideways, "+ Add ... Rule" is off-screen and rule text is clipped | Open (not retested) | - |
| [BUG-SREN-001](bugs/BUG-SREN-001.md) | Low | `SREN-S02` | Settings: Recency and Renewals | Recency & Renewals Settings: no Help (?), and Escape does not close popups | Open (not retested) | - |
| [BUG-SREN-004](bugs/BUG-SREN-004.md) | Low | `SREN-S05` | Settings: Recency and Renewals | Recency & Renewals Settings on a phone: table columns overlap each other | Open (not retested) | - |
| [BUG-SLP-001](bugs/BUG-SLP-001.md) | Low | `SLP-S02` | Settings: Lesson Plans | Lesson Plan Settings: no Help (?), and Escape does not close popups | Open (not retested) | - |
| [BUG-SLP-003](bugs/BUG-SLP-003.md) | Low | `SLP-003` | Settings: Lesson Plans | Add Lesson accepts negative hours (Solo Hours -1 is saved and shown as "Solo: -1h") | Open (not retested) | - |
| [BUG-SRM-001](bugs/BUG-SRM-001.md) | Low | `SRM-S02` | Settings: Risk Matrix | Risk Matrix Settings: no Help (?), and Escape does not close popups | Open (not retested) | - |
| [BUG-SRM-002](bugs/BUG-SRM-002.md) | Low | `SRM-S05` | Settings: Risk Matrix | Risk Matrix Settings on a phone: the page scrolls sideways and "+ Add Level" is cut off | Open (not retested) | - |
| [BUG-SSMS-001](bugs/BUG-SSMS-001.md) | Low | `SSMS-S02` | Settings: Safety Reports | Safety Reports Settings: no Help (?), and Escape does not close popups | Open (not retested) | - |
| [BUG-SINS-001](bugs/BUG-SINS-001.md) | Low | `SINS-S02` | Settings: Inspection Notifications | Inspection Notifications Settings: no Help (?), and Escape does not close popups | Open (not retested) | - |
| [BUG-SINS-003](bugs/BUG-SINS-003.md) | Low | `SINS-S04` | Settings: Inspection Notifications | Inspection Notifications: trigger date shows as 2026-10-01, Add Inspection defaults to the UTC date, and the overdue day count is one day short | Open (not retested) | - |
| [BUG-SINT-001](bugs/BUG-SINT-001.md) | Low | `SINT-S02` | Settings: Google Calendar Sync | Google Calendar Settings: Help and Add Calendar don't close with Escape or an outside click | Open (not retested) | - |
| [BUG-SINT-002](bugs/BUG-SINT-002.md) | Low | `SINT-S04` | Settings: Google Calendar Sync | Google Calendar Sync Status: flight dates show as 2024-01-01 07:55 instead of DD/MM/YYYY | Open (not retested) | - |
| [BUG-SLOG-001](bugs/BUG-SLOG-001.md) | Low | `SLOG-S04` | Settings: Activity Log | Activity Log: no page Help (?), and dates show as "22 Oct 2026, 02:51 am" | Open (not retested) | - |
| [BUG-IPUI-002](bugs/BUG-IPUI-002.md) | Low | `IPCFG-003` | iPad app — Configuration > General | Light theme: Configuration values/toggles unreadable (white on white) | Open | - |
| [BUG-IPDH-001](bugs/BUG-IPDH-001.md) | Low | `IPDH-007` | DataHangar configuration / credentials | Keychain save failure is silent | Open | - |
| [BUG-IPDH-002](bugs/BUG-IPDH-002.md) | Low | `IPDH-001` | DataHangar configuration / button states | Empty-field authentication and sync buttons look enabled | Open | - |
| [BUG-IPFL-001](bugs/BUG-IPFL-001.md) | Low | `IPFL-003` | Flights / flight ID display | Flight ID badges and labels add thousands separators | Open | - |
| [BUG-IPWB-001](bugs/BUG-IPWB-001.md) | Low | `IPWB-002` | iPad app — Weight and balance summary | Weight and balance summary rounds equipment weight to whole kilograms | Open | - |
| [BUG-IPWB-002](bugs/BUG-IPWB-002.md) | Low | `IPWB-003` | iPad app — Weight and balance cabin seating | Cabin occupancy count includes hidden seats | Open | - |
| [BUG-IPREF-001](bugs/BUG-IPREF-001.md) | Low | `IPFT-006` | iPad app — Sync All / Flight Custom Fields | Sync All reports zero Flight Custom Fields when a custom EFI field is present | Open | - |
| [BUG-IPSMS-003](bugs/BUG-IPSMS-003.md) | Low | `IPSMS-007` | iPad app — Safety Reports > Actions | Safety Report action assignee picker includes a blank Unassigned row | Open | - |
| [BUG-IPTRK-001](bugs/BUG-IPTRK-001.md) | Low | `IPTRK-003` | iPad app — Live Tracking | Live Tracking UI/state issues (raw HTML error, stale/global menu, no offline indicator) | Open | - |
| [BUG-IPOFF-001](bugs/BUG-IPOFF-001.md) | Low | `IPOFF-003` | Offline handling | Offline launch and push block for about a minute before timing out | Open | - |
| [BUG-IPUI-003](bugs/BUG-IPUI-003.md) | Low | `IPUI-013` | iPad app — cross-cutting accessibility | Sparse VoiceOver labels and partial Dynamic Type support | Open | - |
| [BUG-PERM-001](bugs/BUG-PERM-001.md) | Low | `PERM-007` | Shell (main) sidebar | Sidebar lists modules the user has no permission for (all lead to Access Denied) | Open (confirmed 22/10/2026) | - |
| [BUG-PERF-001](bugs/BUG-PERF-001.md) | Low | `PERF-001` | All modules (debug panel) | 'Performance' debug timing panel shown on every page, including to non-admin users | Open (not retested) | - |
| [BUG-ATT-003](bugs/BUG-ATT-003.md) | Low | `ATT-035` | Attachments (all modules) | File names are changed differently in each module; accents and symbols are stripped ("résumé" becomes "rsum") | Open (not retested) | - |
| [BUG-FS-008](bugs/BUG-FS-008.md) | High | `FS-027` | Flight Schedule | Flight Schedule: a group-level user (G / WG) sees no flights, even on aircraft in their own group | Fixed (verified 22/10/2026) | - |
| [BUG-FD-008](bugs/BUG-FD-008.md) | High | `FD-030` | Flight Details | Unlocking a Complete & Locked flight wipes its leg route, leg PIC, leg passengers and manifest | Fixed (verified 23/10/2026 v2.0.121) | 23/10/2026 v2.0.121: Fixed |
| [BUG-AF-004](bugs/BUG-AF-004.md) | High | `AF-004` | Active Flights | Active Flights overdue and active times are 13 h out: local SAR/start times are compared with UTC 'now' | Fixed (verified 24/10/2026 v2.0.123) | 24/10/2026 v2.0.123: Fixed |
| [BUG-EXM-006](bugs/BUG-EXM-006.md) | High | `EXM-010` | Exams | Taking an exam: Multi-Response checkboxes toggle twice, so clicking the box does nothing and the saved answer can differ from what is ticked | Fixed (verified 23/10/2026 v2.0.121; regression OK v2.0.122) | 23/10/2026 v2.0.121: Fixed |
| [BUG-SFS-002](bugs/BUG-SFS-002.md) | High | `SFS-004` | Settings: Flight Schedule | Changing Schedule Start Time saves a full date-time, and the setting then shows NaN:NaN | Fixed (verified 22/10/2026) | - |
| [BUG-LOG-003](bugs/BUG-LOG-003.md) | Medium | `LOG-010` | Login / 2FA (main) | 'Trust this device for 30 days' is lost on Logout (logout deletes the trusted-device cookie) | Fixed (verified 22/10/2026) | - |
| [BUG-NAV-001](bugs/BUG-NAV-001.md) | Medium | `NAV-015` | Shell (main) / Personnel Details | Leaving a page with unsaved changes gives no warning; edits are lost | Fixed (verified 22/10/2026) | - |
| [BUG-AM-001](bugs/BUG-AM-001.md) | Medium | `AM-010` | Access Manager | New User accepts a 6-character password (placeholder and Change Credentials require 10) | Fixed (verified 22/10/2026) | - |
| [BUG-POP-003](bugs/BUG-POP-003.md) | Medium | `AM-019` | Access Manager | Access Manager Groups popup: Esc closes with unsaved changes and no warning; reopening shows the unsaved ticks as if saved | Fixed (verified 22/10/2026) | - |
| [BUG-DSH-003](bugs/BUG-DSH-003.md) | Medium | `DSH-006` | Dashboard / Personnel Details | Dashboard recency item opens Personnel Details on the wrong tab (Personal Details instead of Recency and Renewals) | Fixed (verified 22/10/2026) | - |
| [BUG-DSH-004](bugs/BUG-DSH-004.md) | Medium | `DSH-005` | Dashboard | Dashboard: My Flights and On Duty open on the UTC date, not today's local date | Fixed (verified 22/10/2026) | - |
| [BUG-DSH-005](bugs/BUG-DSH-005.md) | Medium | `DSH-011` | Dashboard | Dashboard Project Tasks: clicking a task opens an empty project list instead of the project | Fixed (verified 22/10/2026) | - |
| [BUG-FS-002](bugs/BUG-FS-002.md) | Medium | `FS-021` | Flight Schedule | Esc does not end copy/paste mode on the Flight Schedule - the next click + Ctrl+V creates another flight | Fixed (verified 22/10/2026) | - |
| [BUG-FS-003](bugs/BUG-FS-003.md) | Medium | `FS-008` | Flight Schedule | Flight Schedule header overlaps when Live Edit is on - title covered, location pill cut off and its 'Show All' button cannot be clicked | Fixed (verified 22/10/2026) | - |
| [BUG-FS-004](bugs/BUG-FS-004.md) | Medium | `FS-029` | Flight Schedule > Location Planner | Planner Add Location replaces the New Booking popup - typed booking and location input is lost | Fixed (verified 22/10/2026) | - |
| [BUG-FS-006](bugs/BUG-FS-006.md) | Medium | `FS-034` | Flight Schedule | Flight Schedule month view is slow: flightschedule_json takes ~1.6 s and rendering 2,500 events ~4.5 s | Fixed (verified 22/10/2026) | - |
| [BUG-FS-007](bugs/BUG-FS-007.md) | Medium | `FS-025` | Flight Schedule | Edit-mode idle timeout switches Live Edit off silently, throws 'calendarEl is not defined' and leaves the schedule blank | Fixed (verified 22/10/2026) | - |
| [BUG-FD-001](bugs/BUG-FD-001.md) | Medium | `FD-034` | Flight Details | Flight Details Save Changes does not return to the Flight Schedule and gives no success message | Fixed (verified 23/10/2026 v2.0.121) | 23/10/2026 v2.0.121: Fixed |
| [BUG-FD-002](bugs/BUG-FD-002.md) | Medium | `FD-037` | Flight Details | Flight Details History misses edits saved in Flight Details and shows a false 'Aircraft: ZK-SIM > Unassigned' on schedule moves | Fixed (verified 23/10/2026 v2.0.121) | 23/10/2026 v2.0.121: Fixed |
| [BUG-FD-004](bugs/BUG-FD-004.md) | Medium | `FD-005` | Flight Details | Leg PIC / Secondary Flight Crew dropdowns offer passengers (e.g. a custom passenger can be chosen as leg PIC) | Fixed (verified 23/10/2026 v2.0.120; old-leg "(not crew)" and W&B front-seat group not tested) | 23/10/2026 v2.0.120: Fixed |
| [BUG-FD-005](bugs/BUG-FD-005.md) | Medium | `FD-022` | Flight Details | Leg with two unknown waypoints: only the first is offered for adding, the second is silently dropped on save | Fixed (verified 23/10/2026 v2.0.120) | 23/10/2026 v2.0.120: Fixed |
| [BUG-FD-006](bugs/BUG-FD-006.md) | Medium | `FD-031` | Flight Details | Flight can be set to Complete with no times or destination on a leg; no 'Required Information' prompt | Fixed (verified 23/10/2026 v2.0.121) | 23/10/2026 v2.0.121: Fixed |
| [BUG-FD-009](bugs/BUG-FD-009.md) | Medium | `FD-029` | Flight Details | A user without lock rights (not WL) can lock a flight; the server accepted status complete_locked | Fixed (verified 23/10/2026 v2.0.121) | 23/10/2026 v2.0.121: Fixed |
| [BUG-FD-010](bugs/BUG-FD-010.md) | Medium | `FD-030` | Flight Details | Required Information check skipped on unlock saves: a flight was saved Complete with no departure, destination or PIC | Fixed (verified 23/10/2026 v2.0.121; server side not tested directly) | 23/10/2026 v2.0.121: Fixed |
| [BUG-AF-002](bugs/BUG-AF-002.md) | Medium | `AF-001` | Active Flights | Active Flights lists future flights that have no SAR time, and the stats cards don't count them | Fixed (verified 24/10/2026 v2.0.123) | 24/10/2026 v2.0.123: Fixed |
| [BUG-SUP-004](bugs/BUG-SUP-004.md) | Medium | `SUP-008` | Support / Access Manager | Support: the only permission level is All Access, so regular staff can't raise or see their own tickets | Fixed (verified 22/10/2026) | - |
| [BUG-EXM-010](bugs/BUG-EXM-010.md) | Medium | `EXM-010` | Personnel Details > Exams (personneldetails) | Taking an exam as a read-only (group-level) user: saves and submit return Access Denied, and Previous/Close/Submit are hidden | Fixed (verified 23/10/2026 v2.0.122) | 23/10/2026 v2.0.122: Fixed |
| [BUG-AM-005](bugs/BUG-AM-005.md) | Medium | `PERM-001` | Access Manager | Access Manager: 16 permission types appear twice with the same name (e.g. two "Flight Schedule" cards with different levels) | Fixed (verified 22/10/2026) | - |
| [BUG-DATE-001](bugs/BUG-DATE-001.md) | Medium | `DATE-006` | Flight Details | Flight time across a DST change is out by an hour (01:00-05:00 on 04/04/2027 gives 4.0 instead of 5.0) | Fixed (verified 23/10/2026 v2.0.121) | 23/10/2026 v2.0.121: Fixed |
| [BUG-LOG-001](bugs/BUG-LOG-001.md) | Low | `LOG-013` | Shell (main) | Login Message popup reappears on every browser reload | Fixed (verified 22/10/2026) | - |
| [BUG-LOG-002](bugs/BUG-LOG-002.md) | Low | `LOG-016` | Shell (main) | Logout throws JS error removeChild; Esc doesn't close the Log Out confirm | Fixed (verified 22/10/2026) | - |
| [BUG-AM-002](bugs/BUG-AM-002.md) | Low | `AM-007` | Access Manager | Last Activity hover date ignores Settings > Time Zone format | Fixed (verified 22/10/2026) | - |
| [BUG-AM-003](bugs/BUG-AM-003.md) | Low | `AM-005` | Access Manager | Last Activity column sort does not change order | Fixed (verified 22/10/2026) | - |
| [BUG-AM-004](bugs/BUG-AM-004.md) | Low | `AM-020` | Access Manager > Manage User Permissions | Permission level dropdown shows bare codes 'WA' and 'G' next to full labels | Fixed (verified 22/10/2026) | - |
| [BUG-POP-001](bugs/BUG-POP-001.md) | Low | `AM-S03` | Access Manager (shared errorModal) | Error modal ('Failed to Create User') does not close with Esc | Fixed (verified 22/10/2026) | - |
| [BUG-POP-002](bugs/BUG-POP-002.md) | Low | `AM-023` | Access Manager > Manage User Permissions | Manage User Permissions uses a native browser confirm() for unsaved changes | Fixed (verified 22/10/2026) | - |
| [BUG-DSH-001](bugs/BUG-DSH-001.md) | Low | `DSH-012` | Dashboard | Dashboard side tabs are icon-only with no tooltip or label | Fixed (verified 22/10/2026) | - |
| [BUG-DSH-006](bugs/BUG-DSH-006.md) | Low | `DSH-005` | Dashboard | Dashboard My Flights shows a canceled flight's status as 'Unknown' | Fixed (verified 22/10/2026) | - |
| [BUG-FS-001](bugs/BUG-FS-001.md) | Low | `FS-011` | Flight Schedule > Flight Details (new) | New flight defaults (and Planner 'today') follow the browser time zone instead of Settings > Time Zone | Fixed (verified 23/10/2026 v2.0.120) | 23/10/2026 v2.0.120: Fixed |
| [BUG-FS-005](bugs/BUG-FS-005.md) | Low | `FS-008` | Flight Schedule | JS error on every Live Edit toggle: Cannot read properties of null (reading 'scrollTop') | Fixed (verified 22/10/2026) | - |
| [BUG-POP-004](bugs/BUG-POP-004.md) | Low | `FS-013` | Flight Schedule | Flight Schedule popups (View Details, Double Booking alert, note modals) do not close with Esc | Fixed (verified 22/10/2026) | - |
| [BUG-FD-003](bugs/BUG-FD-003.md) | Low | `FD-019` | Flight Details | Times and Meters: no link to the previous flight next to 'Previous' meter readings | Fixed (verified 23/10/2026 v2.0.120) | 23/10/2026 v2.0.120: Fixed |
| [BUG-AF-001](bugs/BUG-AF-001.md) | Low | `AF-004` | Active Flights | Active Flights shows SAR Time '01/01/1970 00:00' for flights with SAR watch disabled | Fixed (verified 24/10/2026 v2.0.123) | 24/10/2026 v2.0.123: Fixed |
| [BUG-AF-003](bugs/BUG-AF-003.md) | Low | `AF-S02` | Active Flights | Active Flights has no page Help (?), and its popups (About Live Tracking, Adjust SAR, Add Note) don't close with Escape | Fixed (verified 24/10/2026 v2.0.123) | 24/10/2026 v2.0.123: Fixed |
| [BUG-EXM-011](bugs/BUG-EXM-011.md) | Low | `EXM-010` | Personnel Details > Exams (personneldetails) | Taking an exam: "N of 10 questions answered" and the navigator tick only update after moving to another question | Fixed (verified 23/10/2026 v2.0.122) | 23/10/2026 v2.0.122: Fixed |
| [BUG-SFS-001](bugs/BUG-SFS-001.md) | Low | `SFS-003` | Settings: Flight Schedule | Flight Schedule settings: Slot Duration + goes past 120 and typed values over 120 are accepted | Fixed (verified 22/10/2026) | - |
| [BUG-AM-007](bugs/BUG-AM-007.md) | Low | `AM-015` | Access Manager | Access Manager: a customer created from Flight Details is Active with no login credentials | Fixed (verified 22/10/2026) | - |
| [BUG-FD-007](bugs/BUG-FD-007.md) | Low | `DATE-005` | Flight Details | New flight defaults its leg date/time to UTC instead of local time | Fixed (verified 23/10/2026 v2.0.120) | 23/10/2026 v2.0.120: Fixed |
| [BUG-AF-005](bugs/BUG-AF-005.md) | Medium | `FS-027` | Active Flights | Active Flights: a Read Only Group (RG) user sees every company flight, not only their group's | Closed - by design (confirmed by Jon 24/10/2026) | 24/10/2026 v2.0.123: Closed (by design) |

## Test data left on stresstest

### From the checklist runs

| Checklist | Record | Where | Cleanup done? |
|---|---|---|---|
| 04-access-manager | User BETA TEST ONLY Lowperm (betatest_low, betatest.low@example.com); 1 permission, role Crew, groups Crew + BETA TEST ONLY Group; 2FA enabled during testing, later disabled | Access Manager > User Permissions | No |
| 04-access-manager | Group BETA TEST ONLY Group (all 5 switches on) | Access Manager > Groups | No |
| 06-flight-schedule | Note 'BETA TEST ONLY Note' (21/10/2026) | Flight Schedule | Yes (deleted in FS-024) |
| 06-flight-schedule | Flight #42903 ZK-SIM, PIC BETA TEST ONLY Lowperm, route NZWN-NZWN, notes 'BETA TEST ONLY flight', 21/10/2026 08:30 | Flight Schedule / Flight Details | No |
| 06-flight-schedule | Flights #42904, #42905, #42906 (pasted copies of #42903, week 19-25 Oct 2026; #42906 from BUG-FS-002) | Flight Schedule | Yes (deleted in FS-020) |
| 06-flight-schedule | Planner booking ZK-SIM @ AKL Auckland Base 31/10-02/11/2026, notes 'BETA TEST ONLY booking' | Flight Schedule > Planner | No |
| 06-flight-schedule | Flight template 'BETA TEST ONLY Template' (ZK-SIM, PIC BETA TEST ONLY Lowperm) on the AKL booking | Flight Schedule > Planner > Templates | No |
| 06-flight-schedule | Flight #42908 ZK-SIM, PIC BETA TEST ONLY Lowperm, 22/10/2026 15:10-16:10 (pasted from the template) | Flight Schedule | Yes - deleted in FD-038 |
| 06-flight-schedule | Location 'BETA TEST ONLY Loc' (code BTO) | Flight Schedule > Planner > Add Location | No |
| 07-flight-details | Custom passenger 'BETA TEST ONLY Pax' (80 kg, NOK 'BETA TEST ONLY NOK 000') | Flight #42903 > Passenger List | No |
| 07-flight-details | Comment 'BETA TEST ONLY comment' | Flight #42903 > Comments | No |
| 07-flight-details | Leg 1 (Departure ZZZQ) | Flight #42903 > Times and Weights | No |
| 07-flight-details | Waypoint 'ZZZQ' (added from the leg prompt) | Settings > Waypoints | No |
| 07-flight-details | Notify Overdue by Text / Email switched on; status set to Complete | Flight #42903 > Details / Flight Status | No (deleted with the flight) |
| 07-flight-details | Pre-existing, not created in this run: customer 'DEVIN TEST Customer Ltd' | Customers | No (check with Jon) |
| 08-active-flights | Flight #42903 set to Open, SAR moved to 23:30, then Complete again (AF-011) | Flight #42903 | No (delete with the flight) |
| 08-active-flights | Note 'BETA TEST ONLY AF note' | Flight #42903 notes | No |
| 11-personnel-list | Pre-existing, not created in this run: person #274 with no name (Customer), found in PL-001 (BUG-PL-002) | All Personnel | No (check with Jon) |
| 12-personnel-details | BETA TEST ONLY Lowperm: Middle Name 'BETA', City 'BETA TEST ONLY City', Weight 80 saved in PD-004 | Personnel Details #276 | Yes - cleared again |
| 12-personnel-details | Form 'QA Equipment Issue' added to BETA TEST ONLY Lowperm in PD-024, archived, unarchived, deleted | Personnel Details #276 Forms | Yes - deleted |
| 12-personnel-details | File BETA_TEST_ONLY_pd.txt uploaded to BETA TEST ONLY Lowperm in PD-025 | Personnel Details #276 Files | Yes - deleted |
| 12-personnel-details | BETA TEST ONLY Lowperm login landing page set to Flight Schedule in PD-028 | Personnel Details #276 Customize | Yes - restored to Dashboard |
| 12-personnel-details | Photo BETA_TEST_ONLY_photo.png uploaded to BETA TEST ONLY Lowperm in PD-006 | Personnel Details #276 Photo | Yes - removed |
| 12-personnel-details | Digital signature drawn and saved for BETA TEST ONLY Lowperm in PD-007 | Personnel Details #276 Signature | No - no delete option (only Update Signature); remove in the database or leave |
| 14-roster-builder | Draft rosters 'New Draft 1' and 'New Draft 2' (renamed 'BETA TEST ONLY Draft', live October 2026 copied in, pattern/notes/paste tests) | Roster Builder drafts | Yes - both deleted with Delete entire draft permanently |
| 14-roster-builder | Aisha Johnston October 2026 shifts cleared (Clear Month test) | BETA TEST ONLY Draft only | Yes - draft deleted, live untouched |
| 14-roster-builder | Pilots custom order (Aisha Pearce first) | Roster Builder Pilots group | Yes - Reset Order, alphabetical again |
| 14-roster-builder | One Office Hours shift for Aisha Pearce on 01/12/2027 published to live | Live roster December 2027 | Yes - removed with Live Edit, December 2027 empty |
| 15-timesheets-leave | Leave type 'BETA TEST ONLY Leave' (#AB12CD, sort 70) | Leave Requests > Leave Types | Partly - deactivated (Inactive); the app has no delete for leave types |
| 17-notices | Notice #1189 'BETA TEST ONLY Notice edited' (BETA TEST ONLY Group, 2 .txt attachments, 1 comment) | Flight Safety > Notices | No - the app has no delete for notices |
| 19-safety-reports | Safety report #2060 'BETA TEST ONLY report' (Hazard Report, ZK-SIM, on behalf of Aisha Pearce) | Flight Safety > Safety Reports | No - the app has no delete for safety reports |
| 20-hazard-register | Hazard entry for safety report #2060 'BETA TEST ONLY hazard' (goal Eliminate, controls edited, responsible Aisha Pearce) | Flight Safety > Hazard Register (edited via Safety Reports > #2060 > Final Report) | No - goes with report #2060 |
| 22-file-browser | Folder 'BETA TEST ONLY Folder' (files fbA, fbB deleted) | Administration > File Browser > Home | No - folder can't be deleted (BUG-FB-006) |
| 23-form-builder | Form group 'BETA TEST ONLY Forms' (template 'BETA TEST ONLY Form' deleted, auto-attach unticked) | Settings and Tools > Form Builder | No - empty group stays, no way to delete groups |
| 25-task-tracker | Project 'BETA TEST ONLY Project' (component, 2 features, 4 tasks, comment) | Administration > Task Tracker | Yes - project deleted ('Project deleted successfully!') |
| 26-reports | Report template 'BETA TEST ONLY Report', its copy and its result | Administration > Reports | Yes - all deleted |
| 27-support | Ticket #8 'BETA TEST ONLY ticket' with BETA_TEST_ONLY_sup.txt, reply | Administration > Support | Yes - deleted |
| 28-chat | Channel 'BETA TEST ONLY Channel' with test messages/images | Chat (header icon) | Yes - channel deleted |
| 29-exams | Exam group 'BETA TEST ONLY Exams', exam 'BETA TEST ONLY Exam' (10 questions, Rev 2), its instance/batch for BETA TEST ONLY Lowperm | Exam Builder / Exam Instances | No - delete fails once taken (BUG-EXM-008) |
| 31-settings-flightschedule | Secondary status "BETA TEST ONLY Status" | Settings > Flight Schedule | Removed (Update Changes, checked after reload) |
| 31-settings-flightschedule | Cancellation reason "BETA TEST ONLY Reason" | Settings > Flight Schedule | Deleted. Tester error during cleanup: my test script clicked the wrong delete button, so the original "Aircraft Maintenance" and "Airspace Closure" reasons (not in use) were deleted. I added them back with the same names, but they now have new IDs (15, 16). |
| 34-settings-resources | Resource "BETA TEST ONLY R" / ZK-BTO (Cessna 172, BETA TEST ONLY Group, Flight Hours meter from 100) | Settings > Resources | No - kept for testing; delete after the audit |
| 39-settings-shifttypes | Shift group "BETA TEST ONLY Grp3" and shift type "BETA TEST ONLY Shift" (BETAT) | Settings > Roster Shifts > View Deleted | Partly - deleted, but the app only soft-deletes them |
| 44-settings-smsreports | Safety report #2061 "BETA TEST ONLY report 2 (permanent investigator)" | Flight Safety > Safety Reports | No - the app has no delete for safety reports |
| 44-settings-smsreports | Extra Info Field "BETA TEST ONLY EIF" (id 8) | Settings > Safety Reports > Extra Info Fields | Partly - set Inactive; can't delete because report #2060 has a value in it |
| 45-settings-inspections | Two BETA TEST ONLY inspections (date trigger and meter trigger) | Settings > Inspections, aircraft ZK-BTO | No - kept with test aircraft ZK-BTO; delete with it |
| 66-ipad-flights-list | Flights #42914 and #42915 | DataHangar flights used for the app flight-list and PIC-sync checks | No |
| 67-ipad-flight-legs | Flights #42914 and #42915 | DataHangar flights used for leg/crew checks | No |
| 68-ipad-weight-balance | Flight #42914 | BETA test flight used for W&B checks | No |
| 69-ipad-flight-times-meters | Flights #42914 and #42915 | BETA test flights used for time and meter checks | No |
| 70-ipad-flight-forms | Flight #42914 | BETA test flight used for flight-form checks | No |
| 71-ipad-flight-files | Safety Report #2064 | BETA test report used for file upload/delete checks | No |
| 72-ipad-push-pull-sync | Flights #42914 and #42915 | BETA test flights used for push/pull checks | No |
| 73-ipad-pdf-json-export | Flights #42914 and #42915 | BETA test flights used for PDF/JSON export checks | No |
| 74-ipad-safety-reports | Safety Reports #2064 and #2065 | BETA test reports used for forms, files and permissions checks | No |
| 75-ipad-comms-chat | BETA chat channels | `#beta-test-only-ipad-chat` and `beta-test-only-web-chat` | No |
| 77-ipad-live-tracking | Flight #42914 | BETA test flight used for live-tracking checks | No |
| 78-ipad-cross-cutting | Flight #42914 | BETA test flight referenced in UI/offline checks | No |
| 79-ipad-permissions-e2e | Flights #42914 and #42915 | BETA test flights used in permission and sync scenarios | No |
| 79-ipad-permissions-e2e | Safety Reports #2064 and #2065 | BETA test reports used in permission scenarios | No |
| 79-ipad-permissions-e2e | BETA chat channel | `#beta-test-only-ipad-chat` | No |
| 79-ipad-permissions-e2e | User `betalowperm` | Login Access set Inactive; 4 permissions remain (Flight Schedule RO, Flight Details RO, Resources, W&B Config Download) | Yes |
| 96-xc-attachments | 18 files on flight #42903 (ids 459-476) | Flight Details > Files | Yes - deleted |
| 96-xc-attachments | 18 files on BETA TEST ONLY Grpuser (person 277, ids 477-494) | Personnel Details > Files | Yes - deleted |
| 96-xc-attachments | 18 files on Safety Report #2060 (ids 495-512) | Safety Reports > Files | Yes - deleted |
| 96-xc-attachments | 18 files on waypoint ZZZQ (ids 513-530) | Settings > Waypoints > Files | Yes - deleted |
| 96-xc-attachments | 19 files in BETA TEST ONLY Folder (ids 531-549) | File Browser | Yes - deleted |
| 96-xc-attachments | 18 files on notice #1189 (ids 550-567) | Notices | Yes - deleted (2 older test files kept) |
| 96-xc-attachments | Ticket #11 'BETA TEST ONLY file types' with 18 files | Administration > Support | Yes - deleted |
| 96-xc-attachments | Channel beta-test-only-files (id 4) with 4 images | Chat | Yes - deleted |

### From retests

<!-- keep:testdata -->
#### Blocked-row retest and Flight Schedule retests (22/10/2026)
- Users betatest_grp (#277), betatest_two (roles, group BETA TEST ONLY Group, temporary permissions)
- Flights #42909 (ZK-BTO, 22/10 10:00, Complete, lesson + Day Landings 3), #42910 (22/10 13:00, Maintenance Test, form QA Equipment Issue, EFI value), #42911 (copy of #42910, 24/10 06:10)
- Lesson plan "BETA TEST ONLY Plan" (#15) with "BETA TEST ONLY Lesson 1"; assigned to Grpuser twice
- Recency "Day Landings" added to Grpuser
- Extra Flight Info field "BETA TEST ONLY EFI" (#24)
- QA Equipment Issue Auto-Attach: activity Maintenance Test ticked (unticked again; checked after reload)
- ZK-BTO Time Inputs: Engine Start/Stop turned off for a test, now back on (checked)
- W&B: Rev 4 imported from Rev 3 export, ZK-HEL copied to ZK-BTO, approved (Rev 3 is Master again, see below)
- W&B: Rev 5 (same as Rev 4) approved and set as Master to test the newer-revision prompt (Rev 3 is Master again, see below)
- FRMS rule "Max 0.5 flight time hours in any 1 days" for BETA TEST ONLY Group (deleted, checked after reload)
- Timesheets for BETA TEST ONLY Second: roster shifts OH 19/10, PM 20/10, OC 21/10, DS 26-27/11; external flight time 21/10 1.5 h "BETA TEST ONLY ext"; 19/10 Approved, 20/10 Submitted, 21/10 Draft
- Meal claim 19/10 $25 "BETA TEST ONLY claim" (Approved)
- Leave requests for Second: Annual Leave 5-6/11 (Rejected, "BETA TEST ONLY reject"), Annual Leave 26-27/11 (Approved)
- Flight #42910 moved to 22/10 08:00-09:00 for the overdue alert test; now set to Canceled (no reason) so it no longer alerts
- Safety reports #2062 "BETA TEST ONLY confidential" and #2063 "BETA TEST ONLY report 4" (by Grpuser; the app can't delete reports)
- Chat channel "BETA TEST ONLY Chat" (deleted)
- Lowperm Personnel Details WO was removed for a moment for PD-030 and has been put back (1 permission)
- Customer "BETA TEST ONLY Customer" / "BETA TEST ONLY Cust Ltd" created from flight #42910 (FD-014, AM-015)
- Flight #42911 moved to 04/04/2027 01:00-05:00 (across the NZ DST change) for DATE-006
- Safety action "BETA TEST ONLY action for DSH-009" on report #2063, assigned to Second (Open)
- Exam "BETA TEST ONLY Exam" assigned to Second (instance + batch, unstarted)
- Task Tracker project "BETA TEST ONLY TT DSH" (group BETA TEST ONLY Group) with component "BETA TEST ONLY Comp" and feature "BETA TEST ONLY Feature" (deleted with its task; "Project deleted")
- W&B: Rev 3 set back as Master (checked: "Revision 3, 1 aircraft"). Revs 4-6 stay as Approved history (the app has no delete for approved revisions)
- Exam "BETA TEST ONLY Exam" instance for Second submitted and Graded (18% Fail); graded instances can't be removed (BUG-EXM-008)
- Temporary Reports (A) permission on BETA TEST ONLY Second for RPT-002 (removed after the test; checked)
- Flight Schedule retest 22/10/2026: flight #42912 (paste of #42909, ZK-BTO 24/10 14:10-15:10) created for FS-021, deleted via Flight Details > delete (gone from the schedule)
- Location "BETA TEST ONLY Loc2" / BT2 created from Planner > New Booking > Add Location for FS-029 (kept; no delete found in the Locations popup). The New Booking was cancelled, not saved
- Settings > Flight Schedule > Schedule Start Time broke to NaN:NaN during the SFS-004 retest (BUG-SFS-002); the UI could not fix it, so it was restored to 07:00 by rewriting the save request (checked after reload: 07:00, Slot Duration 30)
- Flight #42910 was found back at Open on 22/10/2026 (raising an "Overdue: 9 hours" alert for ZK-BTO); set back to Canceled from Flight Details > Flight Status (checked after reload)
- Second Flight Schedule retest 22/10/2026: Schedule Start Time broke to NaN:NaN again in the SFS-004 test and was restored to 07:00 the same way (checked after reload: 07:00, Slot Duration 30). No flights created; #42910 still Canceled
- Third Flight Schedule retest 22/10/2026 (v2.0.115): Schedule Start Time broke to NaN:NaN again and was restored to 07:00 by rewriting the save request (checked after reload: 07:00, Slot Duration 30). No flights created
- Fourth Flight Schedule retest 22/10/2026 (v2.0.117): Schedule Start Time set to 06:00 for the SFS-004 test and back to 07:00 through the UI (checked after reload: 07:00, Slot Duration 30). No flights created
- Server-side settings check 22/10/2026 (v2.0.117): bad save requests (slotDuration 200/7, scheduleStartTime NaN:NaN/25:99) were rejected; settings confirmed at 07:00 / 30 after a normal save. Double Booking Esc check used existing flight #8852 (only opened the alert, nothing changed)
- Lazy loading check 22/10/2026 (v2.0.118): view-only (month/week navigation, copy then Esc); no data created or changed
- Flight Schedule retest 23/10/2026 (v2.0.119): no flights created or saved; the Add Flight forms (one with test text in Notes) were left without saving

#### Flight Details 8-bug retest (v2.0.119, 23/10/2026)
- #42903: leg 1 Departure/Destination/PIC changed for BUG-FD-005/006, then restored to empty.
- #42903: two test resizes (end 09:45, then back to 09:30) overwrote SAR Time 21/10 23:30 > 21/10 09:30 (BUG-FD-002). Left as is (BETA TEST ONLY flight).
- Waypoint `BTQA` created by the BUG-FD-005 test. Retained: no delete path found.
- #42911: a leg was added but not saved. No change. No settings changed.

#### Flight Details retest v2.0.120 / v2.0.121 (23/10/2026)
- #42909: unlock test on v2.0.120 wiped its leg data; restored on v2.0.121 (leg Wellington Airport > Wellington Airport, PIC + pax BETA TEST ONLY Grpuser, manifest Grpuser). Still different from the original: SAR 22/10/2026 11:30 (was 21/10 21:40), Flight Hours 101 (was 100). Several schedule resizes, put back to 10:00-11:00.
- #42911: unchanged (no legs; the DST checks were not saved).
- Waypoint BTQC probably created by the waypoint test (not checked); BTQA still there. No delete path found.
- Service Account temporary Flight Details WL row (214) removed again (back to A).

#### Exam retest v2.0.121 / v2.0.122 (23/10/2026)
- BETA TEST ONLY Lowperm: new attempt of "BETA TEST ONLY Exam", Graded 18% Fail. Graded attempts can't be removed (BUG-EXM-008).
- BETA TEST ONLY Grpuser: new attempt (instance 6167), Graded 18% Fail. Can't be removed (BUG-EXM-008).
- No unstarted BETA TEST ONLY Exam attempts remain; assign a new one for the next retest.

#### Active Flights retest v2.0.122 / v2.0.123 (23-24/10/2026)
- No data changed: Adjust SAR and Add Note were opened and cancelled without saving.
<!-- /keep:testdata -->

## External audit issues

<!-- keep:external -->
137 issues imported from [`external-audits/`](external-audits/). They keep their original IDs (`FORM-NN`, `POP-NN`, `DATE-NN`, …; two-digit, unlike checklist rows `POP-001`). Full details, evidence and coverage matrices are in the source audit. When an issue is reproduced in our run, create `BUG-<PREFIX>-<NNN>.md` and put the external ID under *Related*.

| Ext ID | Checklist | Severity | Status | Issue | Source |
|---|---|---|---|---|---|
| FORM-01 | [07-flight-details](checklists/07-flight-details.md) | High | Open (external) | Flight Details saves a form with 9 empty required fields, no warning | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-02 | [19-safety-reports](checklists/19-safety-reports.md) | High | Open (external) | Safety Report form edits are lost: Save Changes never enables, values gone after reopening | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-03 | [12-personnel-details](checklists/12-personnel-details.md) | High | Open (external) | Personnel "Archived Forms" section won't expand, so archived forms can't be viewed or unarchived | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-04 | [24-form-browser](checklists/24-form-browser.md) | High | Open (external) | Form Viewer shows no value for Date and Time widgets | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-05 | [23-form-builder](checklists/23-form-builder.md) | High | Open (external) | Invalid/cleared Date or Time keeps the old hidden value, so it saves something the user can't see | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-06 | [23-form-builder](checklists/23-form-builder.md) | Medium | Open (external) | Time widget defaults to current UTC time, not local time | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-07 | [19-safety-reports](checklists/19-safety-reports.md) | Medium | Open (external) | Safety Report instance dates use MM/DD/YYYY and switch between UTC and local | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-08 | [24-form-browser](checklists/24-form-browser.md) | Medium | Open (external) | Form Browser dates ignore the date setting ("Oct 17, 2026") | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-09 | [24-form-browser](checklists/24-form-browser.md) | Medium | Open (external) | Form Browser shows incomplete forms as "Submitted"; no Draft/Incomplete status | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-10 | [07-flight-details](checklists/07-flight-details.md) | Medium | Open (external) | Field count differs: Viewer 8/11 vs Flight Details 11/11; defaults count as filled | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-11 | [07-flight-details](checklists/07-flight-details.md) | Medium | Open (external) | "Updated" time doesn't change after a later save of a flight form | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-12 | [23-form-builder](checklists/23-form-builder.md) | Medium | Open (external) | Three save models: Flight = manual Save, Personnel = auto-save on add, Safety = add only | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-13 | [23-form-builder](checklists/23-form-builder.md) | Medium | Open (external) | Three different Add Form pickers (Flight, Personnel, Safety) | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-14 | [23-form-builder](checklists/23-form-builder.md) | Medium | Open (external) | Add Form lists every template everywhere (Personnel forms on flights, etc.) | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-15 | [23-form-builder](checklists/23-form-builder.md) | Medium | Open (external) | Add Form search: template name only, no group names, no punctuation-tolerant match | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-16 | [23-form-builder](checklists/23-form-builder.md) | Medium | Open (external) | Toggle shows as a plain checkbox in attached forms and Viewer | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-17 | [23-form-builder](checklists/23-form-builder.md) | Medium | Open (external) | Rendered Form preview: List Box, Scribble and Checkbox don't work; no validation test | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-18 | [23-form-builder](checklists/23-form-builder.md) | Medium | Open (external) | Conditions are table-level only, with triggers outside the table; single-table forms can't use them | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-19 | [23-form-builder](checklists/23-form-builder.md) | Medium | Open (external) | Builder modals stack: Auto-Attach opens on top of the Conditions modal | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-20 | [23-form-builder](checklists/23-form-builder.md) | Medium | Open (external) | Builder modals ignore Esc and outside clicks; Esc closes the Safety picker only | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-21 | [23-form-builder](checklists/23-form-builder.md) | Medium | Open (external) | Validation errors use a generic popup that closes the Create modal (2 round trips) (see also POP-08) | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-22 | [07-flight-details](checklists/07-flight-details.md) | Low | Open (external) | Flight Delete Form confirm uses "Stay on Page" instead of "Cancel" | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-23 | [23-form-builder](checklists/23-form-builder.md) | Low | Open (external) | Delete confirm wording differs per module | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-24 | [23-form-builder](checklists/23-form-builder.md) | Low | Open (external) | Option editors accept duplicates and malformed key-value lines silently | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-25 | [23-form-builder](checklists/23-form-builder.md) | Low | Open (external) | Save Form Template asks for group + name every time | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-26 | [23-form-builder](checklists/23-form-builder.md) | Low | Open (external) | Builder buttons are text glyphs with no tooltips (− + × ▲ ▼ C ↻ ☰) (see also VIS-21) | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-27 | [23-form-builder](checklists/23-form-builder.md) | Low | Open (external) | Default labels inconsistent ("Date:" vs "Text Field", "Textarea label") | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-28 | [23-form-builder](checklists/23-form-builder.md) | Low | Open (external) | Required marker differs: red * in builder, orange ★ in preview, none in Viewer | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-29 | [23-form-builder](checklists/23-form-builder.md) | Low | Open (external) | Monospace font in inputs, option editors and template name | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-30 | [24-form-browser](checklists/24-form-browser.md) | Low | Open (external) | Viewer is read-only but List Box × buttons still look active | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-31 | [23-form-builder](checklists/23-form-builder.md) | Low | Open (external) | Date widget stores a time component (date-only field) | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-32 | [23-form-builder](checklists/23-form-builder.md) | Low | Open (external) | Key-Value value box is empty in preview; shows italic in Viewer | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-33 | [23-form-builder](checklists/23-form-builder.md) | Low | Open (external) | Two checkbox styles in one form | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-34 | [23-form-builder](checklists/23-form-builder.md) | Low | Open (external) | Expand icon differs (expand_less vs expand_more) between modules | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-35 | [23-form-builder](checklists/23-form-builder.md) | Low | Open (external) | Picker title "Add Form Template" adds an instance, not a template; preview modal is titled "Rendered Form" but the button says "View Form" | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-36 | [23-form-builder](checklists/23-form-builder.md) | Low | Open (external) | Delete Form Template / Reset are red and enabled with no template selected (see also FUNC-04) | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-37 | [12-personnel-details](checklists/12-personnel-details.md) | Low | Open (external) | Personnel instance delete button has no tooltip; Archive has one | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-38 | [26-reports](checklists/26-reports.md) | Info | Info | Reports help text mentions renewals, but Form Browser has no Renewals folder | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| FORM-39 | [24-form-browser](checklists/24-form-browser.md) | Info | Info | Hidden empty "Error" modal in Form Viewer DOM (opacity 0, not visible) | [DataHangar_Forms_Audit.md](external-audits/DataHangar_Forms_Audit.md) |
| POP-01 | [91-xc-popups](checklists/91-xc-popups.md) | High | Fixed (retested 17/10) | Popup closed when you click inside and drag out. All 18 retestable popups fixed on 17/10/2026 (see section 13); Chat Error no longer appears | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| POP-02 | [91-xc-popups](checklists/91-xc-popups.md) | Medium | Open (external) | Esc doesn't close any popup | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| POP-03 | [91-xc-popups](checklists/91-xc-popups.md) | Medium | Open (external) | Outside click closes some popups but not others. After the POP-01 fix, Risk Matrix Delete Matrix no longer closes on an outside click or Esc, while the other fixed popups still close on an outside click | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| POP-04 | [91-xc-popups](checklists/91-xc-popups.md) | Medium | Open (external) | The same kind of popup behaves differently on different pages (History, Delete confirms) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| POP-05 | [91-xc-popups](checklists/91-xc-popups.md) | Low | Open (external) | About 6 different popup implementations/classes are in use | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| POP-06 | [91-xc-popups](checklists/91-xc-popups.md) | Low | Open (external) | Close button wording varies (Got it / OK / Close / Cancel / x) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| POP-07 | [91-xc-popups](checklists/91-xc-popups.md) | Medium | Open (external) | Scroll Wheel date picker only closes via "Set" (no Cancel, outside click or Esc) and covers the fields below it | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| POP-08 | [91-xc-popups](checklists/91-xc-popups.md) | Medium | Open (external) | Validation errors appear in a generic "Error" popup, not inline (Exam Instances Send, Safety Report Create Action) (see also FORM-21) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATE-01 | [26-reports](checklists/26-reports.md) | High | Open (external) | Reports Last Run shows "16 10M 2026" with DD MMM YYYY; Reports time ignores 12-hour setting | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATE-02 | [92-xc-dates-timezones](checklists/92-xc-dates-timezones.md) | High | Open (external) | Dates ignore the date setting: Dashboard, Flight Schedule, Resources, Activity Log, W&B Configs, Exam Builder | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATE-03 | [92-xc-dates-timezones](checklists/92-xc-dates-timezones.md) | Medium | Open (external) | Scroll Wheel picker fields always show "Oct 16, 2026 6:00 AM", whatever the format setting | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATE-04 | [92-xc-dates-timezones](checklists/92-xc-dates-timezones.md) | High | Open (external) | Empty date fields show today's date (Personnel Birth Date, SMS Review Date), in all picker modes | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATE-05 | [09-daily-flight-record](checklists/09-daily-flight-record.md) | Medium | Open (external) | DFR filter dates are lost in Scroll Wheel and Native modes | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATE-06 | [08-active-flights](checklists/08-active-flights.md) | Medium | Open (external) | Active Flights falls back to DD/MM/YYYY for text-month formats | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATE-07 | [08-active-flights](checklists/08-active-flights.md) | Medium | Open (external) | Active Flights shows 01/01/1970 for an empty SAR time | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATE-08 | [47-settings-activitylog](checklists/47-settings-activitylog.md) | Low | Open (external) | Activity Log uses lowercase "am" and 12-hour time even when 24-hour is set | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATE-09 | [20-hazard-register](checklists/20-hazard-register.md) | Low | Open (external) | Hazard Register date has no leading zero ("8 Jan 2026") | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATE-10 | [92-xc-dates-timezones](checklists/92-xc-dates-timezones.md) | Medium | Open (external) | Native mode: header and inputs show different formats; seconds dropped despite HH:mm:ss | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATE-11 | [92-xc-dates-timezones](checklists/92-xc-dates-timezones.md) | Low | Open (external) | Header UTC/Local clocks don't update until page reload | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATE-12 | [33-settings-timezone](checklists/33-settings-timezone.md) | Low | Open (external) | Time Zone settings: greyed-out formats with no explanation | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATE-13 | [33-settings-timezone](checklists/33-settings-timezone.md) | Low | Open (external) | Time Zone save: banner and toast both show; page reload required | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATE-14 | [08-active-flights](checklists/08-active-flights.md) | Info | Info | Flight #8795 SAR time is before the booking start (may be expected) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| FUNC-01 | [28-chat](checklists/28-chat.md) | n/a | Fixed (retested 17/10) | Chat failed to load. Re-tested 17 Oct: fixed, Chat now loads and works | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| FUNC-02 | [07-flight-details](checklists/07-flight-details.md) | Medium | Open (external) | PDF Summary "Generate PDF" gives no visible result or feedback | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| FUNC-03 | [06-flight-schedule](checklists/06-flight-schedule.md) | Low | Open (external) | Flight Schedule toolbar buttons disappear after toggling sticky notes | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| FUNC-04 | [23-form-builder](checklists/23-form-builder.md) | Medium | Open (external) | Form Builder Delete/Reset buttons enabled with no template selected (see also FORM-36) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| FUNC-05 | [29-exams](checklists/29-exams.md) | Low | Open (external) | Exam editor says "Read Only" but still shows Add Question and Add Group | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-01 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Medium | Open (external) | Page title size, weight and tag differ between modules | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-02 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Medium | Open (external) | Page header icons differ, are missing, or use a different icon font | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-03 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Sidebar and module icons come from different icon sets | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-04 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Medium | Open (external) | Page titles don't match menu names (Staff Roster, Projects, Comms, Timezone Settings, Resource Management, Lesson Plan Configuration) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-05 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Subtitle line present on some pages, missing on others | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-06 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Medium | Open (external) | Help (?) button missing on most modules; position and icon vary | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-07 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Corner radius differs (tables, cards, popups; some square) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-08 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Some buttons are unstyled browser defaults | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-09 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Medium | Open (external) | Different fonts: wide letter-spaced font in Notice Details, Support popup, Exam editor | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-10 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Notes and comment boxes use a monospace font | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-11 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Type-in date field is pill-shaped, unlike the other inputs | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-12 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Search box width and icon size vary | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-13 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Add buttons differ in wording and size; some are icon-only | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-14 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Table sort arrows differ | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-15 | [18-recency-renewals](checklists/18-recency-renewals.md) | Low | Open (external) | Recency table header styled differently | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-16 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Empty values shown as "-", "--" or "–" | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-17 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Edit pencil icon size varies | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-18 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Badge/pill colours differ per module | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-19 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Tab styles differ (pill tabs, icon-only tabs, underline tabs) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-20 | [13-roster-viewer](checklists/13-roster-viewer.md) | Low | Open (external) | Text "< >" arrows used in Roster Viewer, Roster Builder and date picker; "today" vs "Today" | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-21 | [23-form-builder](checklists/23-form-builder.md) | Low | Open (external) | Form Builder uses text-symbol buttons instead of icons (see also FORM-26) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-22 | [22-file-browser](checklists/22-file-browser.md) | Low | Open (external) | Files Upload button uses a sync-style icon; dark navy buttons differ from app blue | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-23 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Popup title icons inconsistent (orange PDF / ticket icons, others none) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-24 | [14-roster-builder](checklists/14-roster-builder.md) | Low | Open (external) | Roster Builder: only orange primary button; dashed-border trash button | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-25 | [29-exams](checklists/29-exams.md) | Low | Open (external) | Disabled button styles differ (Exam editor) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-26 | [07-flight-details](checklists/07-flight-details.md) | Low | Open (external) | Flight Details card heading and checkbox sizes vary | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-27 | [07-flight-details](checklists/07-flight-details.md) | Low | Open (external) | Weight unit wording "KG/Lbs" vs "kg/lbs" | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| VIS-28 | [25-task-tracker](checklists/25-task-tracker.md) | Low | Open (external) | Task Tracker header card narrower than other pages | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| UX-01 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Medium | Open (external) | Detail pages have different toolbars (PDF, History, Help, Back present or missing) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| UX-02 | [12-personnel-details](checklists/12-personnel-details.md) | Medium | Open (external) | Personnel Details has no name/title and no back button | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| UX-03 | [02-shell-navigation](checklists/02-shell-navigation.md) | Low | Open (external) | Detail page URLs inconsistent (index.pl vs ?action=) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| UX-04 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Empty-state messages worded differently | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| UX-05 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Medium | Open (external) | Row actions inconsistent (pencil vs click row; Recency pencil says "View Details"; Form Browser none) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| UX-06 | [29-exams](checklists/29-exams.md) | Low | Open (external) | Exam Builder action icons misaligned between rows; wrong icon for Download Paper | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| UX-07 | [25-task-tracker](checklists/25-task-tracker.md) | Low | Open (external) | Task Tracker icon button with no label/tooltip; Post Comment shown with no projects | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| UX-08 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | "Save" vs "Save Changes" wording | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| UX-09 | [07-flight-details](checklists/07-flight-details.md) | Low | Open (external) | Flight Details: two Add Leg buttons, empty "Secondary Status" label, no units on Crew Recency inputs | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| UX-10 | [11-personnel-list](checklists/11-personnel-list.md) | Low | Open (external) | Personnel menu has an "Administration" group, the same name as the main section | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| UX-11 | [21-settings-hub](checklists/21-settings-hub.md) | Low | Open (external) | Settings hub "Notices" card has no links (see also seed HUB-004) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| UX-12 | [29-exams](checklists/29-exams.md) | Low | Open (external) | Exam editor uses a text "Back" button; other pages use an icon | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATA-01 | [08-active-flights](checklists/08-active-flights.md) | Low | Open (external) | Active Flights overdue rows: follower "Unknown", empty route | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATA-02 | [11-personnel-list](checklists/11-personnel-list.md) | Low | Open (external) | Person with a blank name in All Personnel / Access Manager | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| DATA-03 | [18-recency-renewals](checklists/18-recency-renewals.md) | Low | Open (external) | Recency status "Expired" while Next Expiry says "74 days" | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| INFO-01 | [95-xc-performance-errors](checklists/95-xc-performance-errors.md) | Info | Info | Version tag (?v=) missing on about half the modules (see section 5). Seen in the POP-01 retest: without ?v= the browser kept serving old JS, so the drag-out fixes only appeared after clearing the cache. Users may not get fixes until their cache expires | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| INFO-02 | [95-xc-performance-errors](checklists/95-xc-performance-errors.md) | Info | Info | Performance popup shows on 9 modules and covers content (see section 6) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-01 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | High | Open (external) | Icons come from 3 external sources: Google Fonts Material Icons Sharp (shell), api.iconify.design SVGs (sidebar), Google Fonts Material Symbols Sharp (modules). If a site has no internet or blocks these, icons show as words like "delete" (see also seed NAV-021) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-02 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Medium | Open (external) | Sidebar uses the Rounded/Outline style while modules use Sharp, so the same icon looks different in the menu and on the page | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-03 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Medium | Open (external) | The older "Material Icons" font is still used in Flight Schedule, Active Flights, DFR, Support, FRMS Settings and the header | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-04 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Medium | Open (external) | Delete uses 6 icons: delete, × text, close (Safety Report detail), cancel (Exam Builder), old delete and delete_sweep (FRMS) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-05 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Medium | Open (external) | Close popup uses 4 icons: close, × text (7 pages), old close (Dashboard, DFR, Support), inline SVG (Task Tracker) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-06 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Medium | Open (external) | Edit uses 4+ icons: edit, edit_note (Personnel detail, Exam Builder, Exam Instances, Timesheets), old edit (Flight Schedule, FRMS), inline SVG (Roster Builder) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-07 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Medium | Open (external) | Add/New uses 9+ icons: add, add_circle, add_circle_outline, person_add, playlist_add, note_add, inline SVG plus, old add, text "+" | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-08 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Medium | Open (external) | Help uses help, info, help_outline (Exam Builder), old help/info (Active Flights) and an inline SVG (Task Tracker); "info" is used for both help buttons and hints | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-09 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Medium | Open (external) | Upload/attach uses inline SVG, attach_file, upload_file, upload and old attach_file (Support); Flight Files "Upload" button has an unrelated glyph | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-10 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Download/export: download vs inline SVG (Roster Builder); "description" icon used for Download Paper Exam | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-11 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Back: arrow_back on most pages; none on Personnel detail; text button in Exam editor; « in Roster Builder | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-12 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Prev/Next: text < > (Dashboard, Roster Viewer, Roster Builder, Timesheets, Personnel, date picker) vs chevron icons (Reports, Exam Instances, Timesheets, Flight Schedule old set) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-13 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Search icon: new set on most pages, old set on DFR, Flight Schedule, FRMS, Support, inline SVG on Task Tracker | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-14 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Filter icon: old set (DFR, Flight Schedule, Support) vs new set (DFR settings) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-15 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Copy: content_copy vs inline SVG (Roster Builder) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-16 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Settings gear: Symbols settings vs sidebar tune/settings images vs inline SVG gear (Settings hub) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-17 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | No icon size scale: close 16-28px, edit 13-24px, help 13-28px, description 13-40px | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| ICON-18 | [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | Low | Open (external) | Same icon means different things: description (file / view / download paper), check_circle (acknowledge / close report / deactivate), history (Legacy Duty Browser), edit ("Configure") | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| CHAT-01 | [28-chat](checklists/28-chat.md) | Medium | Open (external) | Message times show 12-hour "01:53 PM" although the time format is set to HH:mm | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| CHAT-02 | [28-chat](checklists/28-chat.md) | Low | Open (external) | Delete message uses an × (close) icon but Delete channel uses a trash icon; the two confirm popups use different title icons (delete vs delete_forever) | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| CHAT-03 | [28-chat](checklists/28-chat.md) | Low | Open (external) | Page title is "Comms" but the header button is "Chat" | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| CHAT-04 | [28-chat](checklists/28-chat.md) | Low | Open (external) | Chat uses the wider font and only the old Material Icons font | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| CHAT-05 | [28-chat](checklists/28-chat.md) | Low | Open (external) | Create Channel with an empty name does nothing and shows no message | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| CHAT-06 | [28-chat](checklists/28-chat.md) | Low | Open (external) | Esc and outside click don't close Chat popups, but Esc does close the Login Message popup | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| CHAT-07 | [28-chat](checklists/28-chat.md) | Low | Open (external) | Web addresses in messages aren't turned into links | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
| CHAT-08 | [28-chat](checklists/28-chat.md) | Low | Open (external) | Channel list is on the right (lists are on the left elsewhere); delete buttons only appear on hover, so they're hard to find and don't work on touch screens | [DataHangar_UI_UX_Audit_v2.md](external-audits/DataHangar_UI_UX_Audit_v2.md) |
<!-- /keep:external -->

## Background notes

<!-- keep:background -->
### External audits merged (17/10/2026)

- [Forms audit](external-audits/DataHangar_Forms_Audit.md) and [UI/UX audit v2](external-audits/DataHangar_UI_UX_Audit_v2.md) imported: 137 issues, 130 open, 2 fixed (POP-01 drag-out, FUNC-01 Chat load), rest Info. Listed in the External audit issues section and under *Known issues* in each checklist. "Ext. open" column above counts them.
- Already covered by the audits (retest only, don't re-audit from scratch): popup drag-out (18 popups fixed), date settings cycled through 4 configs, icon inventory (ICON-01..18, recommendation: self-hosted Material Symbols Sharp), forms widgets.
- Audit settings restored: DD/MM/YYYY, HH:mm, Type-In Fields, Pacific/Auckland.
- Not reachable for Service Account: Maintenance Portal, Leave Requests, WhatsApp, Location Planner.
- Not tested by the audits: Waypoints row delete, Google Calendar connect, full Exam Instances send flow, PDF output file, real mouse drag in Form Builder, Renewals/Waypoint forms, Flight Auto-Attach, forms with Scroll Wheel/Native pickers.

### Test data left by the audits

| Record | Where | Notes |
|---|---|---|
| Exam draft "Air Law & Regulations" (group Aviation Theory) | Exam Builder | Delete Draft |
| AUDIT_TEST_upload.txt | Flight #8795 > Files | |
| AUDIT form instance 192 (archived) | Personnel 274 | Unreachable until FORM-03 fixed |
| Group "AUDIT Forms" | Form Builder | No group delete in UI |
| Form Builder image id 1 | Form Builder | No delete in UI |
<!-- /keep:background -->

