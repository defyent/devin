# DataHangar UI/UX Consistency Audit (v2: full coverage)

**Environment:** stresstest.datahangar.net, v2.0.111, logged in as Service Account. **Date:** 16-17 Oct 2026.
**Method:** Every module was reached by clicking through the sidebar and Settings and Tools, never by typing `?action=` URLs. Computed styles were read from each module iframe, every reachable popup was drag-tested (drag-out retested after fixes on 17/10/2026, section 13), and the date settings were cycled through 4 configurations.
**Settings restored:** Date format DD/MM/YYYY, time format 24-hour HH:mm, picker Type-In Fields, timezone Pacific/Auckland (confirmed after save).

**v2 adds:** detail pages and all their tabs, row/edit/delete/confirm popups, builder internals, date fields inside forms in all 3 picker modes, upload/PDF/history/field help, and a reachability check. Phase 2 findings are in section 8.

## 0. Issue register

| ID | Severity | Issue |
|---|---|---|
| POP-01 | FIXED (was High) | Popup closed when you click inside and drag out. All 18 retestable popups fixed on 17/10/2026 (see section 13); Chat Error no longer appears |
| POP-02 | Medium | Esc doesn't close any popup |
| POP-03 | Medium | Outside click closes some popups but not others. After the POP-01 fix, Risk Matrix Delete Matrix no longer closes on an outside click or Esc, while the other fixed popups still close on an outside click |
| POP-04 | Medium | The same kind of popup behaves differently on different pages (History, Delete confirms) |
| POP-05 | Low | About 6 different popup implementations/classes are in use |
| POP-06 | Low | Close button wording varies (Got it / OK / Close / Cancel / x) |
| POP-07 | Medium | Scroll Wheel date picker only closes via "Set" (no Cancel, outside click or Esc) and covers the fields below it |
| POP-08 | Medium | Validation errors appear in a generic "Error" popup, not inline (Exam Instances Send, Safety Report Create Action) |
| DATE-01 | High | Reports Last Run shows "16 10M 2026" with DD MMM YYYY; Reports time ignores 12-hour setting |
| DATE-02 | High | Dates ignore the date setting: Dashboard, Flight Schedule, Resources, Activity Log, W&B Configs, Exam Builder |
| DATE-03 | Medium | Scroll Wheel picker fields always show "Oct 16, 2026 6:00 AM", whatever the format setting |
| DATE-04 | High | Empty date fields show today's date (Personnel Birth Date, SMS Review Date), in all picker modes |
| DATE-05 | Medium | DFR filter dates are lost in Scroll Wheel and Native modes |
| DATE-06 | Medium | Active Flights falls back to DD/MM/YYYY for text-month formats |
| DATE-07 | Medium | Active Flights shows 01/01/1970 for an empty SAR time |
| DATE-08 | Low | Activity Log uses lowercase "am" and 12-hour time even when 24-hour is set |
| DATE-09 | Low | Hazard Register date has no leading zero ("8 Jan 2026") |
| DATE-10 | Medium | Native mode: header and inputs show different formats; seconds dropped despite HH:mm:ss |
| DATE-11 | Low | Header UTC/Local clocks don't update until page reload |
| DATE-12 | Low | Time Zone settings: greyed-out formats with no explanation |
| DATE-13 | Low | Time Zone save: banner and toast both show; page reload required |
| DATE-14 | Info | Flight #8795 SAR time is before the booking start (may be expected) |
| FUNC-01 | Fixed | Chat failed to load. Re-tested 17 Oct: fixed, Chat now loads and works |
| FUNC-02 | Medium | PDF Summary "Generate PDF" gives no visible result or feedback |
| FUNC-03 | Low | Flight Schedule toolbar buttons disappear after toggling sticky notes |
| FUNC-04 | Medium | Form Builder Delete/Reset buttons enabled with no template selected |
| FUNC-05 | Low | Exam editor says "Read Only" but still shows Add Question and Add Group |
| VIS-01 | Medium | Page title size, weight and tag differ between modules |
| VIS-02 | Medium | Page header icons differ, are missing, or use a different icon font |
| VIS-03 | Low | Sidebar and module icons come from different icon sets |
| VIS-04 | Medium | Page titles don't match menu names (Staff Roster, Projects, Comms, Timezone Settings, Resource Management, Lesson Plan Configuration) |
| VIS-05 | Low | Subtitle line present on some pages, missing on others |
| VIS-06 | Medium | Help (?) button missing on most modules; position and icon vary |
| VIS-07 | Low | Corner radius differs (tables, cards, popups; some square) |
| VIS-08 | Low | Some buttons are unstyled browser defaults |
| VIS-09 | Medium | Different fonts: wide letter-spaced font in Notice Details, Support popup, Exam editor |
| VIS-10 | Low | Notes and comment boxes use a monospace font |
| VIS-11 | Low | Type-in date field is pill-shaped, unlike the other inputs |
| VIS-12 | Low | Search box width and icon size vary |
| VIS-13 | Low | Add buttons differ in wording and size; some are icon-only |
| VIS-14 | Low | Table sort arrows differ |
| VIS-15 | Low | Recency table header styled differently |
| VIS-16 | Low | Empty values shown as "-", "--" or "–" |
| VIS-17 | Low | Edit pencil icon size varies |
| VIS-18 | Low | Badge/pill colours differ per module |
| VIS-19 | Low | Tab styles differ (pill tabs, icon-only tabs, underline tabs) |
| VIS-20 | Low | Text "< >" arrows used in Roster Viewer, Roster Builder and date picker; "today" vs "Today" |
| VIS-21 | Low | Form Builder uses text-symbol buttons instead of icons |
| VIS-22 | Low | Files Upload button uses a sync-style icon; dark navy buttons differ from app blue |
| VIS-23 | Low | Popup title icons inconsistent (orange PDF / ticket icons, others none) |
| VIS-24 | Low | Roster Builder: only orange primary button; dashed-border trash button |
| VIS-25 | Low | Disabled button styles differ (Exam editor) |
| VIS-26 | Low | Flight Details card heading and checkbox sizes vary |
| VIS-27 | Low | Weight unit wording "KG/Lbs" vs "kg/lbs" |
| VIS-28 | Low | Task Tracker header card narrower than other pages |
| UX-01 | Medium | Detail pages have different toolbars (PDF, History, Help, Back present or missing) |
| UX-02 | Medium | Personnel Details has no name/title and no back button |
| UX-03 | Low | Detail page URLs inconsistent (index.pl vs ?action=) |
| UX-04 | Low | Empty-state messages worded differently |
| UX-05 | Medium | Row actions inconsistent (pencil vs click row; Recency pencil says "View Details"; Form Browser none) |
| UX-06 | Low | Exam Builder action icons misaligned between rows; wrong icon for Download Paper |
| UX-07 | Low | Task Tracker icon button with no label/tooltip; Post Comment shown with no projects |
| UX-08 | Low | "Save" vs "Save Changes" wording |
| UX-09 | Low | Flight Details: two Add Leg buttons, empty "Secondary Status" label, no units on Crew Recency inputs |
| UX-10 | Low | Personnel menu has an "Administration" group, the same name as the main section |
| UX-11 | Low | Settings hub "Notices" card has no links |
| UX-12 | Low | Exam editor uses a text "Back" button; other pages use an icon |
| DATA-01 | Low | Active Flights overdue rows: follower "Unknown", empty route |
| DATA-02 | Low | Person with a blank name in All Personnel / Access Manager |
| DATA-03 | Low | Recency status "Expired" while Next Expiry says "74 days" |
| INFO-01 | Info | Version tag (?v=) missing on about half the modules (see section 5). Seen in the POP-01 retest: without ?v= the browser kept serving old JS, so the drag-out fixes only appeared after clearing the cache. Users may not get fixes until their cache expires |
| INFO-02 | Info | Performance popup shows on 9 modules and covers content (see section 6) |
| ICON-01 | High | Icons come from 3 external sources: Google Fonts Material Icons Sharp (shell), api.iconify.design SVGs (sidebar), Google Fonts Material Symbols Sharp (modules). If a site has no internet or blocks these, icons show as words like "delete" |
| ICON-02 | Medium | Sidebar uses the Rounded/Outline style while modules use Sharp, so the same icon looks different in the menu and on the page |
| ICON-03 | Medium | The older "Material Icons" font is still used in Flight Schedule, Active Flights, DFR, Support, FRMS Settings and the header |
| ICON-04 | Medium | Delete uses 6 icons: delete, × text, close (Safety Report detail), cancel (Exam Builder), old delete and delete_sweep (FRMS) |
| ICON-05 | Medium | Close popup uses 4 icons: close, × text (7 pages), old close (Dashboard, DFR, Support), inline SVG (Task Tracker) |
| ICON-06 | Medium | Edit uses 4+ icons: edit, edit_note (Personnel detail, Exam Builder, Exam Instances, Timesheets), old edit (Flight Schedule, FRMS), inline SVG (Roster Builder) |
| ICON-07 | Medium | Add/New uses 9+ icons: add, add_circle, add_circle_outline, person_add, playlist_add, note_add, inline SVG plus, old add, text "+" |
| ICON-08 | Medium | Help uses help, info, help_outline (Exam Builder), old help/info (Active Flights) and an inline SVG (Task Tracker); "info" is used for both help buttons and hints |
| ICON-09 | Medium | Upload/attach uses inline SVG, attach_file, upload_file, upload and old attach_file (Support); Flight Files "Upload" button has an unrelated glyph |
| ICON-10 | Low | Download/export: download vs inline SVG (Roster Builder); "description" icon used for Download Paper Exam |
| ICON-11 | Low | Back: arrow_back on most pages; none on Personnel detail; text button in Exam editor; « in Roster Builder |
| ICON-12 | Low | Prev/Next: text < > (Dashboard, Roster Viewer, Roster Builder, Timesheets, Personnel, date picker) vs chevron icons (Reports, Exam Instances, Timesheets, Flight Schedule old set) |
| ICON-13 | Low | Search icon: new set on most pages, old set on DFR, Flight Schedule, FRMS, Support, inline SVG on Task Tracker |
| ICON-14 | Low | Filter icon: old set (DFR, Flight Schedule, Support) vs new set (DFR settings) |
| ICON-15 | Low | Copy: content_copy vs inline SVG (Roster Builder) |
| ICON-16 | Low | Settings gear: Symbols settings vs sidebar tune/settings images vs inline SVG gear (Settings hub) |
| ICON-17 | Low | No icon size scale: close 16-28px, edit 13-24px, help 13-28px, description 13-40px |
| ICON-18 | Low | Same icon means different things: description (file / view / download paper), check_circle (acknowledge / close report / deactivate), history (Legacy Duty Browser), edit ("Configure") |
| CHAT-01 | Medium | Message times show 12-hour "01:53 PM" although the time format is set to HH:mm |
| CHAT-02 | Low | Delete message uses an × (close) icon but Delete channel uses a trash icon; the two confirm popups use different title icons (delete vs delete_forever) |
| CHAT-03 | Low | Page title is "Comms" but the header button is "Chat" |
| CHAT-04 | Low | Chat uses the wider font and only the old Material Icons font |
| CHAT-05 | Low | Create Channel with an empty name does nothing and shows no message |
| CHAT-06 | Low | Esc and outside click don't close Chat popups, but Esc does close the Login Message popup |
| CHAT-07 | Low | Web addresses in messages aren't turned into links |
| CHAT-08 | Low | Channel list is on the right (lists are on the left elsewhere); delete buttons only appear on hover, so they're hard to find and don't work on touch screens |

## 1. Summary

| # | Issue | Severity |
|---|---|---|
| 1 | ~~Popups close when you click inside and drag out~~ FIXED 17/10/2026 (section 13) | ~~High~~ Fixed |
| 2 | ~~Chat (Comms) fails to load~~ FIXED (section 12) | ~~High~~ Fixed |
| 3 | Reports "Last Run" date garbled with DD MMM YYYY ("16 10M 2026") | High |
| 4 | Several modules ignore the system date/time format (Dashboard, Flight Schedule, Resources, Activity Log, W&B Configs) | High |
| 5 | Active Flights falls back to DD/MM/YYYY when a text-month format is chosen | Medium |
| 6 | DFR Advanced Filter dates are lost in Scroll Wheel and Native picker modes | Medium |
| 7 | Birth Date shows today's date when empty (My Account / Personnel Details) | Medium |
| 8 | Popups behave differently on outside click and Esc | Medium |
| 9 | Page headers inconsistent (tag, size, icon, colour, subtitle, title vs menu name) | Medium |
| 10 | Help (?) button missing on most modules, different styles where present | Medium |
| 11 | Radius, search box, button, sort icon and placeholder inconsistencies | Low |
| 12 | Version (?v=) asset tags and Performance popup only on some modules (matrix below) | Info |

## 2. Popup drag-out bug (click inside, drag outside, release)

> **Status 17/10/2026: FIXED.** All popups below now stay open on drag-out (retest in section 13). The tables show the original results.

Cause, found in code: the overlay closes on `click` with `if (e.target === overlay)`. If the mouse goes down inside the popup and comes up on the overlay, the browser fires the click on the overlay, so the popup closes. Found in `templates2/main/index.js` (shared shell popups) and several module scripts. Modules that also check `mousedown` (Flight Schedule, Safety Reports, Hazard Register, Support, Inspections) behaved correctly.
**Fix:** record `mousedown` target on the overlay and only close on click if mousedown also started on the overlay.

**Live test results**

| Module | Popup | Drag-out | Outside click | Esc |
|---|---|---|---|---|
| Reports | New Report Template (button and + icon) | ~~CLOSES (bug)~~ fixed | closes | - |
| File Browser | Create New Folder | ~~CLOSES (bug)~~ fixed | closes | - |
| File Browser | Upload Files | ~~CLOSES (bug)~~ fixed | closes | - |
| File Browser | Configure Folder (edit) | ~~CLOSES (bug)~~ fixed | closes | - |
| Access Manager | Help | ~~CLOSES (bug)~~ fixed | closes | - |
| Lesson Plans | Add Lesson Plan | ~~CLOSES (bug)~~ fixed | closes | - |
| Exam Instances | Error popup (Send with nothing selected) | ~~CLOSES (bug)~~ fixed | closes | - |
| Chat (header) | Error popup (shared error-modal) | ~~CLOSES (bug)~~ fixed | closes | - |
| Notices | Create New Notice | ok | closes | - |
| Access Manager | Add New User | ok | closes | - |
| Resources | Add Resource | ok | closes | - |
| Safety Reports | Create New Safety Report, Help | ok | closes | - |
| Hazard Register | Help | ok | closes | - |
| Settings and Tools | System Settings Help | ok | closes | - |
| DFR | Manage Columns | ok | closes | - |
| Exam Builder | Add Exam Group | ok | closes | - |
| Inspection Notifications | Add Inspection | ok | closes | - |
| Task Tracker | Add New Project | ok | does NOT close | does NOT close |
| Active Flights | About Live Tracking | ok | does NOT close | does NOT close |
| Form Builder | Help, Create New Form Template | ok | does NOT close | does NOT close |
| Google Calendar Sync | Setup Instructions | ok | does NOT close | does NOT close |
| Roster Shifts | Deleted Items | ok | does NOT close | does NOT close |
| Waypoints | Coordinate Format, Scan for Duplicates | ok | does NOT close | does NOT close |
| Risk Matrix | Add New Matrix | ok | does NOT close | does NOT close |
| Extra Flight Info | Add New Field | ok | does NOT close | does NOT close |
| FRMS Settings | AC119-2 Rule Import Wizard | ok | does NOT close | does NOT close |

**Other popup observations**
- Esc did not close any popup tested.
- Outside-click behaviour is split about 50/50 between modules. Pick one rule, for example: forms do not close on outside click, info/help popups do.
- Popup class names differ (`modal-overlay`, `modal-backdrop`, `modal`, `help-modal`, `help-modal-overlay`, `error-modal`), so there are several popup implementations.
- Exam Instances "Send" with nothing selected shows a generic "Error" popup. The button should be disabled or show a validation message.

## 3. Date format and date input testing

Configurations tested (Settings and Tools > Time Zone), each followed by a scan of 20 modules:
1. DD/MM/YYYY, HH:mm, Type-In (original)
2. MM/DD/YYYY, HH:mm, Type-In
3. DD MMM YYYY, hh:mm A, Scroll Wheel Picker
4. YYYY-MM-DD, HH:mm:ss, Native Browser

| Module | Follows date setting | Follows time setting | Notes |
|---|---|---|---|
| Active Flights | numeric only | yes | Text-month formats fall back to 27/06/2026. Also shows 01/01/1970 (empty date shown as epoch) |
| Daily Flight Record | yes | yes | Filter dates lost in Scroll Wheel / Native mode ("Select...", empty) |
| Notices | yes | - | |
| Safety Reports | yes | yes | |
| Hazard Register | partly | yes | "8 Jan 2026" has no leading zero, unlike "09 May 2026" elsewhere |
| Reports | numeric only | **no** | DD MMM YYYY renders "16 10M 2026 16:11"; time stays 24h |
| My Account / Personnel Details | partly | - | Scroll Wheel widget shows "Oct 16, 2026" whatever the setting; empty Birth Date shows today |
| Dashboard | **no** | yes | Always "Oct 16, 2026" (US style) |
| Flight Schedule | **no** | yes | Always "18 October 2026" |
| Resources (Aircraft) | **no** | - | Meter dates always ISO "2026-05-09" |
| Activity Log | **no** | **no** | Always "17 Oct 2026" and lowercase "12:04 am" even in 24h |
| Weight and Balance Configs | **no** | - | Always "29 Sept 2026" (browser locale) |
| Header UTC/Local clocks | after reload | - | Do not update until page reload |

**Time Zone settings page UX**
- With Type-In or Native picker, text-month date formats and all 12-hour time formats are greyed out with no explanation.
- Saving shows a confirm popup, then an inline green banner and a toast (duplicate feedback), and asks you to reload the page for changes to take effect.

## 4. Visual consistency findings

**Page headers**
- Title tag and size differ: Dashboard and Support use h2 24px; Active Flights h1 24px; DFR, Roster Viewer and Task Tracker h1 21px bold 700; most others h1 21px 600; Recency h2.
- Header icon differs: most are blue 42px. DFR's is grey. Notices uses a small megaphone (sidebar uses a bell). Recency uses a "dashboard" grid icon. Roster Viewer, Task Tracker and the Settings hub have none. FRMS uses Material Icons Sharp while others use Material Symbols Sharp.
- Sidebar icons are iconify images, module icons are Material font glyphs, so the same item shows different glyphs.
- Title does not match the menu name: Roster Viewer is "Staff Roster", Task Tracker is "Projects", Chat is "Comms", Time Zone is "Timezone Settings", Resources is "Resource Management".
- Subtitle line present on some modules (Flight and Duty, Notices, SMS, Hazard, Settings pages, Task Tracker) and missing on others (Dashboard, DFR, Personnel, File/Form Browser, Reports, Support, Recency).
- Header extras vary: stat cards (Access Manager, Resources, Safety Reports), back arrow (Resources only), Task Tracker header card is inset narrower than other modules.

**Help button**
- Present: Active Flights (inside a card, not the header), Safety Reports, Hazard Register, Settings hub, Task Tracker, Personnel Details, and the Flight Schedule / DFR / Access Manager / Form Builder / Resources / Google Calendar settings pages. Exam Builder uses a different help_outline icon.
- Missing: Dashboard, DFR, Roster Viewer, All Personnel, Flight and Duty, Notices, Recency, File Browser, Form Browser, Reports, Support and most settings pages.
- Position varies (far right vs before the primary button).

**Radius and sizing**
- Dashboard uses 4/6/8px radii. Flight Schedule uses rem-scaled 3.5/5.25/7px (14px root) and 12px popups. Some table wrappers are square (0px).
- Some buttons fall back to unstyled browser defaults (13.33px font).
- Font stacks differ between modules (system-ui...Noto Sans vs ...Oxygen, Ubuntu, Cantarell).
- The type-in date field is pill-shaped with centred text, unlike the rectangular text inputs next to it.

**Search, buttons, tables**
- Search box widths vary: about 230px (Personnel, Reports, Resources), about 390px (Notices, File/Form Browser, Access Manager), full width (Flight and Duty, Support, SMS). Search icon size varies too.
- Primary "add" buttons differ in size and wording ("New Notice", "New Ticket", "Add Project", "Add Report Template", "Add Resource", "New User"). Some pages use icon-only + buttons (Reports results, Lesson Plans, Risk Matrix, Exam Builder, Extra Flight Info).
- Sort indicators differ: up/down pair (SMS, Access Manager), single down arrow (Notices, DFR), single up arrow (Personnel, Recency).
- Recency table header uses a larger font and a different background from other tables.
- Empty values shown three ways: "-" (Notices, SMS), "--" (Hazard), "–" (Recency).
- Edit pencil icon size differs (large in File Browser and Reports, small in Notices and Resources).
- Pill and badge colour sets differ per module (Access Manager has 5 colours; SMS, Hazard and Resources each use their own).
- Tabs: Reports, Access Manager, Resources and Personnel Details use pill tabs in a separate card; Dashboard uses icon-only tabs.

**Data and UX issues noticed**
- Active Flights: overdue rows show SAR time 01/01/1970 00:00, Flight Follower "Unknown" and an empty route.
- All Personnel and Access Manager: a row with a blank name (avatar "?" / gradient circle).
- Recency: status "Expired" while Next Expiry shows "74 days".
- Personnel menu has a group called "Administration", the same name as the Administration section.
- Roster Viewer uses text "<" ">" arrows and lowercase "today"; Dashboard uses "Today".
- Settings hub: the "Notices" card has no links.
- Flight Schedule toolbar buttons (note_add, flight_takeoff, ?) disappear after toggling the sticky-note view.

## 5. Version implementation (asset `?v=2.0.111` cache-busting)

The header shows v2.0.111 on every page. No module shows its own version label.

| Uses ?v= on module assets | Does NOT use ?v= |
|---|---|
| Dashboard, Flight Schedule, Active Flights, Daily Flight Record, Roster Viewer, Flight and Duty, Notices, Safety Reports, Reports, Support, Access Manager, Roster Builder, Form Builder, FRMS Settings, Waypoints, Resources, W&B Configs, Exam Instances, Exam Builder | All Personnel (and group views), Recency and Renewals, Hazard Register, Settings and Tools hub, File Browser, Form Browser, Task Tracker, Timesheets, Settings pages: Flight Schedule, DFR, Roster Shifts, Risk Matrix, Safety Reports, Recency and Renewals, Time Zone, Extra Flight Info, Flight Types, Google Calendar Sync, Lesson Plans, Activity Log, Inspection Notifications |

Example: the Time Zone page loads `templates2/settings_timezone/index.js` with no version, so browsers may cache old code after a deploy.

## 6. Debug Performance popup

| Shows Performance popup | No Performance popup |
|---|---|
| Dashboard, Active Flights, Daily Flight Record, Flight and Duty, Personnel Details / My Account, Access Manager, Roster Builder, Timesheets, W&B Configs | Flight Schedule, Roster Viewer, All Personnel, Notices, Recency and Renewals, Safety Reports, Hazard Register, Settings hub, File Browser, Form Browser, Task Tracker, Reports, Support, Chat, and all other settings pages |

On the Personnel Details and Access Manager pages it covers page content (Digital Signature button, table rows).

## 7. Limitations and test data left behind
- Not present for this account: Maintenance Portal, Leave Requests, WhatsApp, Location Planner.
- Not tested: Waypoints row delete, Google Calendar connect, the full Exam Instances send flow, and the PDF output file (Generate PDF gave no visible result).
- Test data to clean up:
  - Exam Builder: a **DRAFT** of "Air Law & Regulations" (group Aviation Theory). Remove it with Delete Draft.
  - Flight #8795 > Files: **AUDIT_TEST_upload.txt**.
  - Time Zone settings were saved several times and restored to DD/MM/YYYY, HH:mm, Type-In, Pacific/Auckland. These saves will show in the Activity Log.

## 8. Phase 2: full coverage (detail pages, row actions, builders, form dates, shared features)

### 8.1 New high-severity findings
| # | Issue | Where | Severity |
|---|---|---|---|
| P1 | ~~11 more popups close on drag-out~~ FIXED 17/10/2026 (section 13) | see 8.2 | ~~High~~ Fixed |
| P2 | Scroll Wheel picker fields ignore the date and time format. They always show "Oct 16, 2026 6:00 AM" (tested with MM/DD/YYYY, DD MMMM YYYY, hh:mm A and h:mm A). The page header on the same screen does follow the setting. | Flight Details, flight forms, SMS Final Report, Personnel Birth Date | High |
| P3 | Empty date fields fill in today's date: SMS Final Report "Review Date" and Personnel "Birth Date". Happens in all 3 picker modes, so saving the form stores a wrong date. | SMS Final Report, Personnel Details | High |
| P5 | Validation is done through a generic "Error" popup instead of inline messages (e.g. "Please enter an action request before creating"). The button looks disabled but can still be clicked. | SMS > Actions, Exam Instances | Medium |
| P6 | The Scroll Wheel picker only closes via "Set". Outside click and Esc don't close it, there is no Cancel or X, and it covers the fields below it. | All Scroll Wheel date fields | Medium |
| P7 | Native mode: header shows "2026-10-16 06:00:00" but the inputs show "10/16/2026, 06:00 AM" (browser locale). Seconds are dropped even though HH:mm:ss is selected. | Flight Details | Medium |
| P8 | SAR time (15/10 08:57) is before the flight start (16/10 06:00) | Flight #8795 (Start/End are booking times, so this may be expected) | Info |

### 8.2 Popup drag-out results (Phase 2)

> **Status 17/10/2026: FIXED.** All drag-out failures below are fixed (section 13). The table shows the original results.
| Popup | Drag-out | Outside click | Esc |
|---|---|---|---|
| Flight Details: PDF Summary | ~~CLOSES (bug)~~ fixed | - | - |
| Flight Details: Help | ~~CLOSES (bug)~~ fixed | - | - |
| Flight Details: History | stays | no close | no close |
| Flight Details: Delete Form (confirm) | ~~CLOSES (bug)~~ fixed | - | - |
| Flight Details: Delete Leg (confirm) | ~~CLOSES (bug)~~ fixed | - | - |
| Flight Details: Scroll Wheel date picker | stays | no close | no close |
| Personnel Details: History | ~~CLOSES (bug)~~ fixed | - | - |
| Personnel Details: PDF Options | ~~CLOSES (bug)~~ fixed | - | - |
| Personnel Details: Help | ~~CLOSES (bug)~~ fixed | - | - |
| Active Flights: Adjust SAR Time | ~~CLOSES (bug)~~ fixed | - | - |
| Active Flights: Add Note | ~~CLOSES (bug)~~ fixed | - | - |
| Safety Report: Confirm Status Change (Open Investigation) | ~~CLOSES (bug)~~ fixed | - | - |
| Safety Report: Add Investigator / Add Reviewer | stays | closes | - |
| Safety Report: Error (Create Action) | stays | closes | - |
| Risk Matrix: Delete Matrix (confirm) | ~~CLOSES (bug)~~ fixed | - | - |
| Risk Matrix: Edit Matrix | stays | no close | no close |
| Lesson Plans: Add Lesson Plan | ~~CLOSES (bug)~~ fixed (reconfirmed) | - | - |
| Notices: Edit Notice | stays | closes | - |
| Access Manager: Manage User Permissions | stays | closes | - |
| Roster Shifts: Edit Shift Type | stays | no close | no close |
| Resources: Edit Resource | stays | closes | - |
| Support: New Support Ticket | stays | closes | no close |
| Task Tracker: Help Guide | stays | no close | no close |
| Roster Builder: Copy/Paste Instructions | stays | no close | no close |
| Roster Builder: Bulk Actions | stays | closes | - |
| Exam Builder: Add Exam / Exam Configuration / Choose Question Type / Add Question Group | stays | closes | - |
| Exam Builder: Delete Group / Delete Exam / Create Draft / Approve Draft / Delete Draft / Revision History | stays | no close | no close |
| Form Builder: Confirm Reset | stays | no close | no close |

Observations:
- The same kind of action behaves differently in different places. History closes on drag in Personnel but not in Flight Details. Delete Form, Delete Leg and Delete Matrix close on drag, but Delete Group and Delete Exam don't. (Drag-out part now fixed; see section 13.)
- At least 5 overlay implementations are in use: `modal-overlay`, `modal-overlay active`, `form-modal-overlay`, `modal-backdrop`, `modal`, `help-modal-overlay`, and the Support modal, which hides with opacity:0 and pointer-events:none but stays in the layout.
- Close buttons are worded differently: "Got it" (field help), "OK", "Cancel", "Close", and "x".

### 8.3 Date fields inside forms (all picker modes)
| Field | Type-In (DD/MM/YYYY) | Scroll Wheel (MM/DD/YYYY, hh:mm A) | Scroll Wheel (DD MMMM YYYY, h:mm A) | Native (ISO, HH:mm:ss) |
|---|---|---|---|---|
| Flight start/end/SAR | 16/10/2026 — 06:00 (pill, centred) | **Oct 16, 2026 6:00 AM** | **Oct 16, 2026 6:00 AM** | datetime-local 2026-10-16T06:00 (no seconds) |
| Flight form "Flight Date" | 16/10/2026 | **Oct 16, 2026** | **Oct 16, 2026** | date 2026-10-16 |
| SMS Final Report Review Date (empty) | **17/10/2026 (today)** | **Oct 17, 2026 (today)** | **Oct 17, 2026** | **2026-10-17 (today)** |
| Personnel Birth Date (empty) | **17/10/2026 (today)** | **Oct 17, 2026** | **Oct 17, 2026** | **2026-10-17** |
| Flight Details header | follows setting | follows (10/16/2026 06:00 AM) | follows (16 October 2026) | follows (2026-10-16 06:00:00) |
| Exam Builder "Created" | May 11, 2026 (hardcoded) | same | same | same |
- The SMS details, Hazard details and Notice details dates are display-only and follow the setting. Notice Edit has no date fields.
- Native inputs lose the app's rounded styling and use the browser font.

### 8.4 Detail pages
| Page | Header | Back | PDF | History | Help | Save | Tabs |
|---|---|---|---|---|---|---|---|
| Flight Details | ~21px, plane icon, status pills | yes | yes | yes | yes | header "Save Changes" | 9 |
| Safety Report Details ("SMS Report Details") | h1 19.5px, progress stepper | yes | no | as tab | no | in-tab "Save Changes" | 7 |
| Hazard Register Details | h1 19.5px, orange warning icon | yes | no | no | no | - | 2 + "Original SMS Report" |
| Personnel Details | **no name/title shown** (blank record), h2 29px | **no** | yes | yes | yes | "Save Changes", but Customize tab says "Save" | 8 |
| Notice Details | h1 21px, small megaphone icon, **different font** | yes | no | no | no | - | none |
- Routes are inconsistent: Flight Details uses `index.pl?action=flightdetails`, while the others use `?action=...details`.
- Empty states are worded differently: "No records found.", "No items to display.", "No comments yet.", "No comments yet. Be the first to comment!", "No files have been attached to this flight."
- Notes, Comment, Debrief and form Remarks textareas use a monospace font, while all other inputs use sans-serif.
- Flight Details: two "Add Leg" buttons; card heading sizes differ (21px vs 17px); "Secondary Status" label with nothing under it; Crew Recency inputs have no units or placeholders; checkbox sizes differ inside forms; the Upload button uses a clock/sync-style icon while Browse uses an upload icon; both buttons are dark navy, unlike the app's blue.
- Weight toggle casing: "KG/Lbs" (Personnel) vs "kg/lbs" (Flight).
- Notice Details, the Support ticket modal and the Exam editor use a wider, letter-spaced font that the rest of the app doesn't use.

### 8.5 Row actions
- Notices: pencil edit per row. Recency and Renewals: pencil icon, but the tooltip says "View Details". Safety Reports, Hazard, Flight and Duty, All Personnel and DFR: no row buttons; you click the whole row. Waypoints: trash per row. File Browser: pencil on folders, but Form Browser has no actions.
- Exam Builder shows 6 icon-only actions per exam (view, create draft, download Q&A, download paper, history, delete). When an exam has a draft, the master row loses 2 icons, so the icons no longer line up in columns. The "description" glyph is used for "Download Paper Exam".
- Task Tracker has an icon button with no text or title (it opens Help Guide). There is also a "Post Comment" button on an empty project list.

### 8.6 Builders
- Form Builder: uses Unicode glyph buttons (☰ − + ▲ ▼ C ↻ ×) instead of Material icons. "Delete Form Template" and "Reset" are red and enabled even with no template selected. Toolbox items have dashed blue borders.
- Exam editor: the master opens with a "Read Only" banner but still shows Add Question and Add Group, each in a different disabled style. It uses a text "Back to Exam Builder" button, while other pages use an icon-only back button.
- Roster Builder: page title is "Staff Roster" (the menu says Roster Builder, and the Roster Viewer uses the same title). Navigation uses « < > » text buttons. Orange "Enable Live Edit" is the only orange primary button. The trash button has a dashed border. The Performance popup covers the legend.
- Lesson Plans: page title is "Lesson Plan Configuration".

### 8.7 Shared features
- File upload works. A green toast appears and the Files tab count updates.
- PDF Summary: a modal with section toggles. "Generate PDF" gave no visible feedback within 15s (no new tab and no toast).
- Field help (?) next to NOTIFY opens a "Notification Feature" modal with a "Got it" button.

### 8.8 Reachability
- This account doesn't have Maintenance Portal, Leave Requests, WhatsApp or Location Planner: they aren't in the sidebar or in Settings and Tools. The Settings hub only has a "Maintenance" section, which contains Inspection Notifications.
- The Support New Ticket popup was tested (8.2).
- Not tested: Waypoints row delete; Exam Instances send flow beyond the validation popup; Google Calendar sync connect.

## 11. Icon consistency (every page, detail tab, settings page and popup scanned)

94 page/tab states were scanned and 14,651 icon elements recorded (including hidden popup icons). In the module frames, 3,255 use Material Symbols Sharp, 728 use the older Material Icons Sharp, and about 100 are hand-drawn inline SVGs; the sidebar uses iconify `<img>` SVGs.

### 11.1 Icon issues
| ID | Severity | Issue |
|---|---|---|
| ICON-01 | High | Icons come from 3 external sources: Google Fonts Material Icons Sharp (shell), api.iconify.design SVGs (sidebar), Google Fonts Material Symbols Sharp (modules). If a site has no internet or blocks these, icons show as words like "delete" |
| ICON-02 | Medium | Sidebar uses the Rounded/Outline style while modules use Sharp, so the same icon looks different in the menu and on the page |
| ICON-03 | Medium | The older "Material Icons" font is still used in Flight Schedule, Active Flights, DFR, Support, FRMS Settings and the header |
| ICON-04 | Medium | Delete uses 6 icons: delete, × text, close (Safety Report detail), cancel (Exam Builder), old delete and delete_sweep (FRMS) |
| ICON-05 | Medium | Close popup uses 4 icons: close, × text (7 pages), old close (Dashboard, DFR, Support), inline SVG (Task Tracker) |
| ICON-06 | Medium | Edit uses 4+ icons: edit, edit_note (Personnel detail, Exam Builder, Exam Instances, Timesheets), old edit (Flight Schedule, FRMS), inline SVG (Roster Builder) |
| ICON-07 | Medium | Add/New uses 9+ icons: add, add_circle, add_circle_outline, person_add, playlist_add, note_add, inline SVG plus, old add, text "+" |
| ICON-08 | Medium | Help uses help, info, help_outline (Exam Builder), old help/info (Active Flights) and an inline SVG (Task Tracker); "info" is used for both help buttons and hints |
| ICON-09 | Medium | Upload/attach uses inline SVG, attach_file, upload_file, upload and old attach_file (Support); Flight Files "Upload" button has an unrelated glyph |
| ICON-10 | Low | Download/export: download vs inline SVG (Roster Builder); "description" icon used for Download Paper Exam |
| ICON-11 | Low | Back: arrow_back on most pages; none on Personnel detail; text button in Exam editor; « in Roster Builder |
| ICON-12 | Low | Prev/Next: text < > (Dashboard, Roster Viewer, Roster Builder, Timesheets, Personnel, date picker) vs chevron icons (Reports, Exam Instances, Timesheets, Flight Schedule old set) |
| ICON-13 | Low | Search icon: new set on most pages, old set on DFR, Flight Schedule, FRMS, Support, inline SVG on Task Tracker |
| ICON-14 | Low | Filter icon: old set (DFR, Flight Schedule, Support) vs new set (DFR settings) |
| ICON-15 | Low | Copy: content_copy vs inline SVG (Roster Builder) |
| ICON-16 | Low | Settings gear: Symbols settings vs sidebar tune/settings images vs inline SVG gear (Settings hub) |
| ICON-17 | Low | No icon size scale: close 16-28px, edit 13-24px, help 13-28px, description 13-40px |
| ICON-18 | Low | Same icon means different things: description (file / view / download paper), check_circle (acknowledge / close report / deactivate), history (Legacy Duty Browser), edit ("Configure") |

### 11.2 Icon used for each action, and where
| Action | Icon used (source): where |
|---|---|
| Delete | **delete (Symbols)**: All Personnel (detail), Daily Flight Record (detail), Reports, Reports (detail), Settings: Access Manager, Settings: Exam Builder, Settings: Flight Types, Settings: Inspection Notifications, Settings: Recency and Renewals, Settings: Resources (Aircraft), Settings: Risk Matrix, Settings: Roster Shifts, Settings: Safety Reports, Settings: Waypoint Locations<br>**× (text char)**: Daily Flight Record (detail), Settings: Flight Schedule, Settings: Form Builder<br>**close (Symbols)**: Safety Reports (detail)<br>**restore_from_trash (Symbols)**: Settings: Roster Shifts<br>**delete (Icons(old))**: Settings: Fatigue Risk Management Settings<br>**delete_sweep (Icons(old))**: Settings: Fatigue Risk Management Settings<br>**cancel (Symbols)**: Settings: Exam Builder |
| Close popup/clear | **close (Symbols)**: All Personnel (detail), Daily Flight Record (detail), File Browser, Hazard Register, Notices, Notices (detail), Safety Reports, Safety Reports (detail), Settings: Access Manager, Settings: Daily Flight Record, Settings: Flight Schedule, Settings: Resources (Aircraft), Settings: Waypoint Locations<br>**× (text char)**: Daily Flight Record (detail), Flight Schedule, Roster Viewer, Settings and Tools, Settings: Form Builder, Settings: Google Calendar Sync, Settings: Roster Builder<br>**close (Icons(old))**: Daily Flight Record, Dashboard, Support<br>**inline SVG (SVG)**: Task Tracker<br>**rate_review (Symbols)**: Safety Reports (detail)<br>**check_circle (Symbols)**: Safety Reports (detail) |
| Edit | **edit (Symbols)**: File Browser, Notices, Recency and Renewals, Recency and Renewals (detail), Reports, Reports (detail), Settings: Access Manager, Settings: Extra Flight Info, Settings: Flight Types, Settings: Inspection Notifications, Settings: Recency and Renewals, Settings: Resources (Aircraft), Settings: Risk Matrix, Settings: Roster Shifts, Settings: Safety Reports<br>**edit_note (Symbols)**: All Personnel (detail), Settings: Exam Builder, Settings: Exam Instances, Settings: Timesheets<br>**edit (Icons(old))**: Flight Schedule, Settings: Fatigue Risk Management Settings<br>**flight (Symbols)**: Settings: Form Builder, Settings: Weight and Balance Configs (iPad App)<br>**edit_location (Icons(old))**: Flight Schedule<br>**edit-mode-icon (SVG)**: Settings: Roster Builder<br>**check_circle (Symbols)**: Settings: Weight and Balance Configs (iPad App)<br>**edit_calendar (Symbols)**: Settings: Google Calendar Sync<br>**settings (Symbols)**: Settings: Exam Builder |
| Add/New | **add (Symbols)**: All Personnel (detail), Daily Flight Record (detail), Hazard Register, Notices, Reports, Reports (detail), Safety Reports, Settings: Access Manager, Settings: Exam Builder, Settings: Extra Flight Info, Settings: Flight Types, Settings: Google Calendar Sync, Settings: Inspection Notifications, Settings: Lesson Plans, Settings: Recency and Renewals, Settings: Resources (Aircraft), Settings: Risk Matrix, Settings: Roster Shifts, Settings: Safety Reports, Settings: Waypoint Locations, Settings: Weight and Balance Configs (iPad App)<br>**add_circle (Symbols)**: All Personnel (detail), Hazard Register, Safety Reports<br>**person_add (Symbols)**: Safety Reports (detail), Settings: Access Manager, Settings: Exam Instances<br>**add (Icons(old))**: Flight Schedule, Support<br>**inline SVG (SVG)**: Settings: Roster Builder, Task Tracker<br>**workspaces (Symbols)**: Reports, Reports (detail)<br>**picture_as_pdf (Symbols)**: Reports, Reports (detail)<br>**note_add (Icons(old))**: Flight Schedule<br>**flight_takeoff (Icons(old))**: Flight Schedule<br>**add_location (Icons(old))**: Flight Schedule<br>**add_location_alt (Icons(old))**: Flight Schedule<br>**send (Symbols)**: Notices<br>**add_task (Symbols)**: Safety Reports (detail)<br>**draw (Symbols)**: All Personnel (detail)<br>**add_circle (Icons(old))**: Settings: Fatigue Risk Management Settings<br>**playlist_add (Icons(old))**: Settings: Fatigue Risk Management Settings<br>**playlist_add (Symbols)**: Settings: Waypoint Locations<br>**fork_right (Symbols)**: Settings: Weight and Balance Configs (iPad App)<br>**add_circle_outline (Symbols)**: Settings: Exam Builder<br>**folder (Symbols)**: Settings: Exam Builder |
| Help/Info | **info (Symbols)**: All Personnel (detail), Daily Flight Record (detail), Hazard Register, Hazard Register (detail), Reports, Reports (detail), Safety Reports, Settings: Access Manager, Settings: Exam Builder, Settings: Extra Flight Info, Settings: Google Calendar Sync, Settings: Resources (Aircraft), Settings: Time Zone, Settings: Timesheets, Settings: Waypoint Locations<br>**help (Symbols)**: All Personnel (detail), Daily Flight Record (detail), Hazard Register, Safety Reports, Settings and Tools, Settings: Access Manager, Settings: Daily Flight Record, Settings: Flight Schedule, Settings: Form Builder, Settings: Google Calendar Sync, Settings: Resources (Aircraft), Settings: Timesheets<br>**help (Icons(old))**: Active Flights<br>**info (Icons(old))**: Active Flights<br>**inline SVG (SVG)**: Task Tracker<br>**help_outline (Symbols)**: Settings: Exam Builder |
| Upload | **inline SVG (SVG)**: All Personnel (detail), Daily Flight Record (detail), Notices, Safety Reports (detail)<br>**attach_file (Symbols)**: All Personnel (detail), Daily Flight Record (detail), Notices (detail), Settings: Waypoint Locations<br>**upload_file (Symbols)**: File Browser, Settings: Form Builder<br>**upload (Symbols)**: Settings: Waypoint Locations, Settings: Weight and Balance Configs (iPad App)<br>**folder-open-outline-rounded.svg (img)**: Dashboard<br>**dynamic-form-outline-rounded.svg (img)**: Dashboard<br>**folder_open (Symbols)**: File Browser<br>**attach_file (Icons(old))**: Support<br>**description (Symbols)**: Daily Flight Record (detail)<br>**history (Symbols)**: All Personnel (detail) |
| Download/Export | **download (Symbols)**: All Personnel (detail), Daily Flight Record (detail), Reports, Reports (detail), Settings: Exam Builder, Settings: Weight and Balance Configs (iPad App)<br>**picture_as_pdf (Symbols)**: Daily Flight Record (detail)<br>**inline SVG (SVG)**: Settings: Roster Builder<br>**description (Symbols)**: Settings: Exam Builder |
| PDF | **picture_as_pdf (Symbols)**: All Personnel (detail), Daily Flight Record (detail) |
| History | **history (Symbols)**: All Personnel (detail), Daily Flight Record (detail), Flight and Duty, Safety Reports (detail), Settings: Activity Log, Settings: Exam Builder, Settings: Form Builder<br>**history (Icons(old))**: Flight Schedule |
| Back | **arrow_back (Symbols)**: Daily Flight Record (detail), File Browser, Form Browser, Hazard Register (detail), Notices (detail), Reports, Reports (detail), Safety Reports (detail), Settings: Access Manager, Settings: Exam Builder, Settings: Resources (Aircraft), Settings: Timesheets, Settings: Waypoint Locations, Settings: Weight and Balance Configs (iPad App)<br>**refresh (Symbols)**: All Personnel (detail)<br>**« (text char)**: Settings: Roster Builder |
| Prev/Next | **< (text char)**: All Personnel (detail), Dashboard, Roster Viewer, Settings: Roster Builder, Settings: Timesheets<br>**> (text char)**: All Personnel (detail), Dashboard, Roster Viewer, Settings: Roster Builder, Settings: Timesheets<br>**chevron_right (Symbols)**: Reports (detail), Settings: Exam Instances, Settings: Timesheets<br>**chevron_left (Symbols)**: Reports (detail), Settings: Timesheets<br>**chevron_left (Icons(old))**: Flight Schedule<br>**chevron_right (Icons(old))**: Flight Schedule<br>**» (text char)**: Settings: Roster Builder |
| Search | **search (Symbols)**: All Personnel, All Personnel (detail), Crew, Engineers, File Browser, Flight and Duty, Form Browser, Hazard Register, Notices, Pilots, Recency and Renewals, Recency and Renewals (detail), Reports, Reports (detail), Safety Reports, Safety Reports (detail), Settings: Access Manager, Settings: Activity Log, Settings: Exam Builder, Settings: Exam Instances, Settings: Flight Types, Settings: Inspection Notifications, Settings: Resources (Aircraft), Settings: Waypoint Locations<br>**search (Icons(old))**: Daily Flight Record, Flight Schedule, Settings: Fatigue Risk Management Settings, Support<br>**inline SVG (SVG)**: Task Tracker |
| Filter | **filter_list (Icons(old))**: Daily Flight Record, Flight Schedule, Support<br>**clear_all (Icons(old))**: Daily Flight Record<br>**filter_list (Symbols)**: Settings: Daily Flight Record |
| Save | **save (Symbols)**: All Personnel (detail), Notices, Reports, Reports (detail), Safety Reports (detail), Settings: Access Manager, Settings: Daily Flight Record, Settings: Flight Schedule, Settings: Form Builder, Settings: Resources (Aircraft), Settings: Time Zone |
| Copy/Duplicate | **content_copy (Symbols)**: Reports, Reports (detail), Settings: Access Manager, Settings: Resources (Aircraft)<br>**inline SVG (SVG)**: Settings: Roster Builder<br>**find_replace (Symbols)**: Settings: Waypoint Locations |
| Settings | **settings (Symbols)**: Daily Flight Record (detail), File Browser, Settings and Tools, Settings: Flight Schedule, Settings: Form Builder, Settings: Resources (Aircraft), Settings: Waypoint Locations<br>**tune-rounded.svg (img)**: Dashboard<br>**settings-outline-rounded.svg (img)**: Dashboard<br>**inline SVG (SVG)**: Settings and Tools |

### 11.3 Recommended single icon pack: Material Symbols (Sharp), self-hosted
**Why this pack**
- Most of DataHangar already uses it. Most module icons are Material Symbols Sharp, and the sidebar SVGs are also Material Symbols (Rounded style), so switching changes the fewest icons.
- It is licensed under Apache 2.0, so it is free to bundle and self-host.
- One variable font file covers about 3,000+ icons, with fill, weight and size controlled by CSS (`font-variation-settings`). The font is named "Material Symbols", but the full set covers file, flight, person, calendar and other icons.
- It replaces all three current sources (old Material Icons Sharp font, iconify SVG API, Google Fonts Symbols) and the hand-drawn inline SVGs.

**How to host it locally (no external requests)**
1. Download the Sharp variable font from Google's official repo (`google/material-design-icons`, folder `variablefont/`: `MaterialSymbolsSharp[FILL,GRAD,opsz,wght].woff2`), or from the npm package `material-symbols` (`material-symbols/sharp.css` + woff2).
2. Put it in the app's static folder, e.g. `templates2/assets/fonts/material-symbols-sharp.woff2`, and serve it with a long cache header and a `?v=` version tag.
3. Add one shared stylesheet, loaded by the shell and every module iframe:
```css
@font-face{font-family:'Material Symbols Sharp';font-style:normal;font-weight:100 700;font-display:block;
 src:url('/templates2/assets/fonts/material-symbols-sharp.woff2?v=2.0.111') format('woff2');}
.dh-icon{font-family:'Material Symbols Sharp';font-weight:400;font-style:normal;font-size:20px;line-height:1;
 letter-spacing:normal;text-transform:none;white-space:nowrap;direction:ltr;-webkit-font-smoothing:antialiased;
 font-variation-settings:'FILL' 0,'wght' 400,'GRAD' 0,'opsz' 20;}
.dh-icon.sm{font-size:16px}.dh-icon.lg{font-size:24px}
```
4. Remove the `fonts.googleapis.com/icon?family=Material+Icons+Sharp` and `fonts.googleapis.com/css2?family=Material+Symbols+Sharp` links. Replace the `api.iconify.design/...svg` sidebar images with `<span class="dh-icon">dashboard</span>` and so on.
5. Optional: if the full font (about 3-4 MB woff2) is too heavy, generate a subset containing only the glyphs DataHangar uses, using `pyftsubset` with `--text-file` listing the ligature names. Note that variable-font subsetting by ligature needs the `--layout-features=liga` option.
6. Inter (the text font) also comes from Google Fonts. Self-host it the same way so the app has no external font dependency.

**Size standard:** 16px inline/table, 20px buttons and toolbars, 24px page-header actions, 42px page-title icon. Colour: inherit from the button (`currentColor`).

## 12. Chat re-test (17 Oct, after the fix)

Chat now loads. Tested: create a channel, send messages (short, long text with a long URL, multi-line with Shift+Enter), stage an image upload, delete a message, delete a channel. Test data created during the test was all deleted.

### 12.1 What works
- Channels and messages load with no errors. Toasts confirm channel create and delete.
- Send is disabled when the message box is empty. Shift+Enter adds a new line. Long text and URLs wrap correctly.
- An image is shown as a preview with a remove (×) button before sending.
- None of the 3 Chat popups (Create Channel, Delete Message, Delete Channel) has the drag-out bug.
- The Login Message popup (shown at login/reload) also has no drag-out bug.

### 12.2 Chat issues
| ID | Severity | Issue |
|---|---|---|
| CHAT-01 | Medium | Message times show 12-hour "01:53 PM" although the time format is set to HH:mm |
| CHAT-02 | Low | Delete message uses an × (close) icon but Delete channel uses a trash icon; the two confirm popups use different title icons (delete vs delete_forever) |
| CHAT-03 | Low | Page title is "Comms" but the header button is "Chat" |
| CHAT-04 | Low | Chat uses the wider font and only the old Material Icons font |
| CHAT-05 | Low | Create Channel with an empty name does nothing and shows no message |
| CHAT-06 | Low | Esc and outside click don't close Chat popups, but Esc does close the Login Message popup |
| CHAT-07 | Low | Web addresses in messages aren't turned into links |
| CHAT-08 | Low | Channel list is on the right (lists are on the left elsewhere); delete buttons only appear on hover, so they're hard to find and don't work on touch screens |

### 12.3 Chat popup matrix
| Popup | Drag-out | Outside click | Esc |
|---|---|---|---|
| Create Channel | stays | no close | no close |
| Delete Message | stays | not tested | no close |
| Delete Channel | stays | no close | not tested |
| Login Message (shell) | stays | not tested | closes |

## 13. POP-01 retest (drag-out) - 17/10/2026 (second retest)

Method: mousedown inside the popup, drag to the overlay, mouseup. Reached through the UI only.

**Cache note:** the first run of this retest still showed the same 10 failures as before. After clearing the browser cache and reloading, all of them passed. The old JS was being served from cache. Modules without a `?v=` version tag (INFO-01) will keep serving stale files to users until their cache expires. Adding `?v=` to these modules would make fixes reach users straight away (inference).

| Popup | Result |
|---|---|
| Reports New Report Template | FIXED |
| File Browser Create New Folder | FIXED |
| File Browser Upload Files | FIXED |
| File Browser Configure Folder | FIXED |
| Access Manager Help | FIXED |
| Lesson Plans Add Lesson Plan | FIXED |
| Exam Instances Error (shared Error popup) | FIXED |
| Flight Details PDF Summary | FIXED |
| Flight Details Help | FIXED |
| Flight Details Delete Form | FIXED |
| Flight Details Delete Leg | FIXED |
| Personnel History | FIXED |
| Personnel PDF Options | FIXED |
| Personnel Details Help | FIXED |
| Active Flights Adjust SAR Time | FIXED |
| Active Flights Add Note | FIXED |
| Safety Report Confirm Status Change | FIXED |
| Risk Matrix Delete Matrix | FIXED (but it no longer closes on an outside click or Esc, unlike the others; see POP-03) |
| Chat Error | Not retestable (Chat loads, popup no longer appears). Uses the shared Error popup, which is now fixed. |

POP-01 status: **Fixed** (18/18 retested).
