# Debugging tracker

- **DataHangar version:** v2.0.111 (stresstest.datahangar.net at pack creation)
- **Test accounts / levels:** Service Account (username datahangar, admin). No other levels available (SET-004 BLOCKED)
- **Original Time Zone settings:** Pacific/Auckland, DD/MM/YYYY, 24-hour HH:mm, Type-In Fields

Status: `TODO` · `IN PROGRESS` · `DONE` · `BLOCKED`

| Checklist | Prefix | Area | Checks | Pass | Fail | Blocked | Ext. open | Status |
|---|---|---|---|---|---|---|---|---|
| [00-setup-and-accounts](checklists/00-setup-and-accounts.md) | `SET` | Session setup, accounts and baseline | 9 | 8 | 0 | 1 | 0 | DONE |
| [01-login-auth](checklists/01-login-auth.md) | `LOG` | Login, 2FA, sessions, landing page | 25 | 14 | 3 | 0 | 0 | IN PROGRESS |
| [02-shell-navigation](checklists/02-shell-navigation.md) | `NAV` | Application shell, sidebar, header, mobile | 27 | 22 | 2 | 2 | 1 | DONE |
| [03-common-conventions](checklists/03-common-conventions.md) | `CON` | Common screen conventions (apply on every page) | 22 | 4 | 1 | 0 | 0 | IN PROGRESS |
| [04-access-manager](checklists/04-access-manager.md) | `AM` | Access Manager (users, roles, groups, permissions, templates) | 38 | 21 | 7 | 0 | 0 | IN PROGRESS |
| [05-dashboard](checklists/05-dashboard.md) | `DSH` | Dashboard | 19 | 10 | 4 | 5 | 0 | DONE |
| [06-flight-schedule](checklists/06-flight-schedule.md) | `FS` | Flight Schedule (incl. embedded Location Planner) | 40 | 30 | 7 | 1 | 1 | IN PROGRESS |
| [07-flight-details](checklists/07-flight-details.md) | `FD` | Flight Details | 44 | 24 | 5 | 2 | 8 | IN PROGRESS |
| [08-active-flights](checklists/08-active-flights.md) | `AF` | Active Flights and Live Tracking | 19 | 14 | 4 | 1 | 3 | DONE |
| [09-daily-flight-record](checklists/09-daily-flight-record.md) | `DFR` | Daily Flight Record | 16 | 12 | 2 | 2 | 1 | DONE |
| [10-location-planner](checklists/10-location-planner.md) | `LP` | Location Planner (stand-alone) | 9 | 0 | 0 | 9 | 0 | DONE |
| [11-personnel-list](checklists/11-personnel-list.md) | `PL` | All Personnel (Personnel List) | 11 | 9 | 1 | 1 | 2 | DONE |
| [12-personnel-details](checklists/12-personnel-details.md) | `PD` | Personnel Details / My Account | 36 | 8 | 6 | 0 | 3 | IN PROGRESS |
| [13-roster-viewer](checklists/13-roster-viewer.md) | `RV` | Roster Viewer | 12 | 0 | 0 | 0 | 1 | TODO |
| [14-roster-builder](checklists/14-roster-builder.md) | `RB` | Roster Builder | 21 | 0 | 0 | 0 | 1 | TODO |
| [15-timesheets-leave](checklists/15-timesheets-leave.md) | `TS` | Timesheets, Timesheet Details, Leave Requests | 17 | 0 | 0 | 0 | 0 | TODO |
| [16-flight-and-duty](checklists/16-flight-and-duty.md) | `FAD` | Flight and Duty | 14 | 0 | 0 | 0 | 0 | TODO |
| [17-notices](checklists/17-notices.md) | `NOT` | Notices | 16 | 0 | 0 | 0 | 0 | TODO |
| [18-recency-renewals](checklists/18-recency-renewals.md) | `REC` | Recency and Renewals (overview page) | 11 | 0 | 0 | 0 | 2 | TODO |
| [19-safety-reports](checklists/19-safety-reports.md) | `SMS` | Safety Reports (SMS) | 21 | 0 | 0 | 0 | 2 | TODO |
| [20-hazard-register](checklists/20-hazard-register.md) | `HAZ` | Hazard Register | 10 | 0 | 0 | 0 | 1 | TODO |
| [21-settings-hub](checklists/21-settings-hub.md) | `HUB` | Settings and Tools hub | 11 | 0 | 0 | 0 | 1 | TODO |
| [22-file-browser](checklists/22-file-browser.md) | `FB` | File Browser | 14 | 0 | 0 | 0 | 1 | TODO |
| [23-form-builder](checklists/23-form-builder.md) | `FBLD` | Form Builder | 14 | 0 | 0 | 0 | 27 | TODO |
| [24-form-browser](checklists/24-form-browser.md) | `FBR` | Form Browser / Form Viewer | 10 | 0 | 0 | 0 | 4 | TODO |
| [25-task-tracker](checklists/25-task-tracker.md) | `TT` | Task Tracker | 12 | 0 | 0 | 0 | 2 | TODO |
| [26-reports](checklists/26-reports.md) | `RPT` | Reports | 16 | 0 | 0 | 0 | 1 | TODO |
| [27-support](checklists/27-support.md) | `SUP` | Support tickets | 14 | 0 | 0 | 0 | 0 | TODO |
| [28-chat](checklists/28-chat.md) | `CHAT` | Chat | 11 | 0 | 0 | 0 | 8 | TODO |
| [29-exams](checklists/29-exams.md) | `EXM` | Exam Builder, Exam Editor, Exam Instances | 16 | 0 | 0 | 0 | 4 | TODO |
| [30-maintenance](checklists/30-maintenance.md) | `MX` | Maintenance Portal | 11 | 0 | 0 | 0 | 0 | TODO |
| [31-settings-flightschedule](checklists/31-settings-flightschedule.md) | `SFS` | Settings – Flight Schedule | 13 | 0 | 0 | 0 | 0 | TODO |
| [32-settings-dfr](checklists/32-settings-dfr.md) | `SDFR` | Settings – Daily Flight Record | 7 | 0 | 0 | 0 | 0 | TODO |
| [33-settings-timezone](checklists/33-settings-timezone.md) | `STZ` | Settings – Time Zone (date/time matrix) | 11 | 0 | 0 | 0 | 2 | TODO |
| [34-settings-resources](checklists/34-settings-resources.md) | `SRES` | Settings – Resources (Aircraft) | 18 | 0 | 0 | 0 | 0 | TODO |
| [35-settings-wab](checklists/35-settings-wab.md) | `SWAB` | Settings – Weight and Balance Configs | 13 | 0 | 0 | 0 | 0 | TODO |
| [36-settings-extraflightinfo](checklists/36-settings-extraflightinfo.md) | `SEFI` | Settings – Extra Flight Info | 9 | 0 | 0 | 0 | 0 | TODO |
| [37-settings-flighttypes](checklists/37-settings-flighttypes.md) | `SFT` | Settings – Flight Types | 8 | 0 | 0 | 0 | 0 | TODO |
| [38-settings-waypoints](checklists/38-settings-waypoints.md) | `SWP` | Settings – Waypoint Locations | 12 | 0 | 0 | 0 | 0 | TODO |
| [39-settings-shifttypes](checklists/39-settings-shifttypes.md) | `SST` | Settings – Roster Shifts | 10 | 0 | 0 | 0 | 0 | TODO |
| [40-settings-frms](checklists/40-settings-frms.md) | `SFRMS` | Settings – Fatigue Risk Management | 11 | 0 | 0 | 0 | 0 | TODO |
| [41-settings-renewals](checklists/41-settings-renewals.md) | `SREN` | Settings – Recency and Renewals | 10 | 0 | 0 | 0 | 0 | TODO |
| [42-settings-lessonplans](checklists/42-settings-lessonplans.md) | `SLP` | Settings – Lesson Plans | 9 | 0 | 0 | 0 | 0 | TODO |
| [43-settings-riskmatrix](checklists/43-settings-riskmatrix.md) | `SRM` | Settings – Risk Matrix | 9 | 0 | 0 | 0 | 0 | TODO |
| [44-settings-smsreports](checklists/44-settings-smsreports.md) | `SSMS` | Settings – Safety Reports | 9 | 0 | 0 | 0 | 0 | TODO |
| [45-settings-inspections](checklists/45-settings-inspections.md) | `SINS` | Settings – Inspection Notifications | 9 | 0 | 0 | 0 | 0 | TODO |
| [46-settings-integrations](checklists/46-settings-integrations.md) | `SINT` | Settings – Google Calendar, WhatsApp | 10 | 0 | 0 | 0 | 0 | TODO |
| [47-settings-activitylog](checklists/47-settings-activitylog.md) | `SLOG` | Settings – Activity Log | 9 | 0 | 0 | 0 | 1 | TODO |
| [90-xc-permissions](checklists/90-xc-permissions.md) | `PERM` | Cross-cutting: permission levels | 10 | 2 | 0 | 0 | 0 | IN PROGRESS |
| [91-xc-popups](checklists/91-xc-popups.md) | `POP` | Cross-cutting: popups/modals | 8 | 0 | 0 | 0 | 7 | TODO |
| [92-xc-dates-timezones](checklists/92-xc-dates-timezones.md) | `DATE` | Cross-cutting: date/time formats and pickers | 7 | 0 | 0 | 0 | 5 | TODO |
| [93-xc-mobile](checklists/93-xc-mobile.md) | `MOB` | Cross-cutting: mobile / narrow layout | 4 | 0 | 0 | 0 | 0 | TODO |
| [94-xc-ui-icons](checklists/94-xc-ui-icons.md) | `UI` | Cross-cutting: UI consistency and icon inventory | 7 | 0 | 0 | 0 | 41 | TODO |
| [95-xc-performance-errors](checklists/95-xc-performance-errors.md) | `PERF` | Cross-cutting: performance, console and network | 4 | 0 | 0 | 0 | 0 | TODO |
| [99-e2e-workflows](checklists/99-e2e-workflows.md) | `E2E` | End-to-end workflows | 8 | 0 | 0 | 0 | 0 | TODO |

## External audits merged (17/10/2026)

- [Forms audit](external-audits/DataHangar_Forms_Audit.md) and [UI/UX audit v2](external-audits/DataHangar_UI_UX_Audit_v2.md) imported: 137 issues, 130 open, 2 fixed (POP-01 drag-out, FUNC-01 Chat load), rest Info. Listed in [bugs/BUGS_INDEX.md](bugs/BUGS_INDEX.md) and under *Known issues* in each checklist. "Ext. open" column above counts them.
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

## Seed observations (from first look, not yet verified as bugs)

- NAV-021 / UI-002 (= ICON-01): menu icons load from external CDN `api.iconify.design` (Jon prefers one self-hosted pack).
- HUB-004 / NOT-010 (= UX-11): Settings and Tools "Notices" card has no links.
- HUB-005 / MX-001 / LP-001: Maintenance Portal, Location Planner (stand-alone), WhatsApp, Chat not linked from the hub or menu.
- AM-010: guide says New User accepts 6-char passwords while placeholder says 10 and Change Credentials needs 10.
- FD-033: "Required to Complete" meters not enforced (guide §14).
