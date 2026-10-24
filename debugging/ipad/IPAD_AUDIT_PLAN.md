# DataHangar Flight (iPad app) audit plan

How the iPad app joins the DataHangar audit. Read this together with `../DEBUGGING_GUIDE.md`. Those rules (`BETA TEST ONLY` data, the guide is the spec, cache clearing, restoring settings, evidence) apply here as well.

## 1. What is being audited

| Item | Value |
|---|---|
| App | **DataHangar Flight**: a React app (one `index.js` bundle, about 1.58 MB) wrapped in a WKWebView in an Xcode project |
| Web build under test | https://stresstest.datahangar.net/ipad/ (same origin as the DataHangar frontend) |
| Backend | The DataHangar frontend's own `index.pl?action=…` endpoints, using the session cookie from `action=Login` |
| Local storage | `localStorage` (settings, credentials, `*_backup` copies) and IndexedDB `DataHangarApp` v1, store `appData` (`aircraft`, `aerodromes`, `localPersonnel`, `flights`, `flightActivities`, `flightCategories`, `extraFlightInfoFields`, `globalFormTemplates`, `globalFormGroups`) |
| Native bridge | `webkit.messageHandlers.dhApi`, `pdfHandler`, `jsonHandler`, `fileInputHandler`, `flightFileHandler`. These only exist in the Xcode wrapper. In Chrome they are missing, and the app shows "Native App Required". |
| Version | Configuration shows **App Version / Build** only when the native wrapper supplies it. In Chrome, record the `index.js` size and its Last-Modified date instead. |

### Module map (from the live app and the bundle)

| Area | Screens and actions | DataHangar endpoints | Frontend counterpart (checklist) |
|---|---|---|---|
| First run | "Welcome to DataHangar Flight" modal (Go to Configuration / Maybe Later) | – | – |
| Configuration › General Info | Theme (Dark/Midtone/Light), Automatic Time Offsets, Configuration PIN (keypad), Aerodrome Proximity (NM), Coordinate Format (DD/DDM/DMS), Personnel Weight Unit, Time Format (24h/12h), API Debug Mode and Log, Open Source Acknowledgements, Import/Export/Copy Configuration | – | 33-settings-timezone (date/time formats) |
| Configuration › Aircraft | List grouped by type ("DataHangar Linked"), add (+), edit, duplicate, delete; W&B: empty weight & balance, cockpit/cabin stations, removable seats/equipment, equipment profiles, fuel stations and burn sequence, meters, external load, cabin layout, graphs | `settings_resources_json`, `settings_wabconfigs_download_master` | 34-settings-resources, 35-settings-wab |
| Configuration › Personnel | Crew list with weight (read-only once synced) | `personnellist_json&personnel_type=crew` | 11-personnel-list, 12-personnel-details |
| Configuration › Waypoints | List, edit, "Name Waypoint" | `settings_waypoints_json`, `flightdetails_addwaypoint` | 38-settings-waypoints |
| Configuration › Datahangar | URL, Username, Password, Test Authentication, Sync All Data, Live Tracking toggle, Clear All Data | `Login`, plus all of the above, `settings_flighttypes_json`, `flightdetails_forms_json` | 01-login-auth |
| Flights | List, search, Download Flights (week picker, Download / Downloaded / Unlink), New Flight, Delete Flight, Pull from Server, Push to Server, "Server Flight Has Changed" overwrite prompt, "Already Downloaded" | `flightschedule_json&flightsonly=1`, `flightdetails_json`, POST `index.pl` (flight save, legs `leg[n][…]`, `extra-field-*`) | 06-flight-schedule, 07-flight-details |
| Flight › Legs | Add/Delete leg, Route & Times, Local/UTC times, Nearby Aerodromes ("Now"), Time Totals and Breakdown, Meter Totals, Engine/Flight Time, Fuel, Takeoff Weight | same | 07-flight-details, 92-xc-dates-timezones |
| Flight › Crew & W&B | Left/Right Seat, Seat n, Passenger Manifest, Passengers (Unseated), Personnel & Baggage, W&B Sheet, Cabin Layout Change | same | 07-flight-details, 35-settings-wab |
| Flight › Forms / Files / Details | Attach Form, Delete/Remove Form, Add/Remove File, Image Quality (Original / Max 1600 / Max 800), PDF viewer (PDF.js), Details / Flight Identity / Additional Info | `flightdetails_forms_json`, `flightdetails_uploadfile`, `flightdetails_deletefile`, `flightdetails_servefile` | 23/24 form builder/browser, 96-xc-attachments |
| Safety Reports | List, Download Safety Reports, New Safety Report (Location & Date, Narrative, Initial/Final Risk Assessment, Hazard Register, Confidential, Submit Anonymously), detail (Report Information, Extra Info, Actions, Complete Action, Change Status, Comments, Documents, Forms, Activity Log, Final Report Summary), Delete Report | `smsreports_list_json`, `smsreports_json`, `smsreports_create`, `smsreportdetails_*` (addcomment, addpersonnel, createaction, saveextrainfo, savefinalreport, saveforms, uploaddocument, deletedocument, downloaddocument) | 19-safety-reports, 20-hazard-register, 43/44 risk matrix and SMS settings |
| Calculator | Standard, Unit Converter, True Airspeed, Density/Pressure Altitude, Wind Correction, Crosswind Component, Speed/Distance/Time, Fuel Calculator, Descent Planner, Sunrise/Sunset, Weight & Balance | – (offline maths) | – (compare against known reference values) |
| Comms | Channel picker, messages, Load older messages, send, delete, image, Create Channel | `chat_channels_json`, `chat_messages_json`, `chat_new_messages_json`, `chat_send_message`, `chat_delete_message`, `chat_create_channel`, `chat_serve_image`, `chat_is_admin_json` | 28-chat |
| Live Tracking | Start Live Tracking, Ping Interval, Device ID, Simulate / Stop Sim, Live Tracking Resumed/Error | native `dhApi` | 08-active-flights |

## 2. Test environment

- **Browser:** the visible Chrome on the Devin desktop, with DevTools-equivalent capture over CDP (console errors, page exceptions, HTTP ≥ 400).
- **Account:** Service Account (username `datahangar`, admin), entered in Configuration › Datahangar. Credentials are **never** written to this repo. For permission tests, use the accounts in checklist 00 (Lowperm, Grpuser, Second).
- **Viewport emulation** (CDP `Emulation.setDeviceMetricsOverride`, `mobile: true`, DPR 2, touch on, iPad Safari UA). This is the matrix for every UX row:

| Code | Device | Portrait (CSS px) | Landscape (CSS px) | Use |
|---|---|---|---|---|
| **P** / **L** | iPad 10th gen / iPad Air 11" (primary) | 820 × 1180 | 1180 × 820 | every screen |
| P-mini / L-mini | iPad mini 6 | 744 × 1133 | 1133 × 744 | smallest layout |
| P-pro / L-pro | iPad Pro 12.9" | 1024 × 1366 | 1366 × 1024 | largest layout |
| Split | Split View, 1/2 and 1/3 width | 507 / 320 × 1180 | – | spot checks |

- **Chrome cannot cover:** native bridge features (PDF export, JSON share, file picker via `fileInputHandler`, Live Tracking GPS, App Version/Build), WKWebView storage eviction, background/foreground transitions, real touch keyboards and safe-area insets. These rows are marked `BLOCKED (native)` and go into a separate **Xcode/iPad session** (simulator or device, macOS needed).

## 3. IDs and files

- Checklists `60-ipad-*` to `79-ipad-*` in `../checklists/`, rolled up by `mkstatus.py` like every other checklist.
- Checklist prefixes all start with `IP` (`IPSET`, `IPCFG`, `IPAC`, `IPPER`, `IPSYN`, `IPFL`, `IPLEG`, `IPWB`, `IPFF`, `IPPP`, `IPSMS`, `IPCAL`, `IPCOM`, `IPLT`, `IPOFF`, `IPSEC`, `IPUX`, `IPE2E`), and bug IDs follow them: `BUG-IPSYN-001` and so on.
- **Cross-reference column:** every sync row names the frontend screen and record checked (e.g. `FD #8893 Legs tab`). If the fault is on the server or frontend side (the iPad app only exposes it), log it under the frontend prefix and link it from the iPad row.
- Module name in `bugs.json` is `iPad: <area>`.

## 4. Approach and order

1. **Baseline (60):** app build, account, frontend version, settings snapshot, empty-device state, CDP capture on.
2. **Configuration (61–63):** each setting, persistence over reload, the PIN gate, import/export round trip, Clear All Data.
3. **Connection and reference sync (64):** auth success/failure, Sync All Data, record counts **compared with the frontend** for aircraft, personnel (weights), waypoints, flight types, forms and W&B master.
4. **Flights (65–69):** download, view, edit, create, push and pull, plus conflicts. Each case is a round trip: change on the iPad, then check the frontend; change on the frontend, then pull and check the iPad.
5. **Safety reports (70), Calculator (71), Comms (72), Live Tracking (73).**
6. **Offline and lifecycle (74), security and data handling (75).**
7. **UX/UI audit (76–77)** for every screen, at P and L first, then mini/pro/split.
8. **End-to-end (79):** a full field day, from pre-flight W&B through post-flight push, safety report and chat, verified on the frontend.
9. **Native session:** rerun every `BLOCKED (native)` row in Xcode/iPad.

### Sync cross-reference matrix (what "matches" means)

| Data | iPad → frontend check | Frontend → iPad check |
|---|---|---|
| Flight header (aircraft, date, PIC/crew, customer, activity, category, status) | Flight Details header, and Flight Schedule tile | Edit on FD › Pull from Server › values update; "Server Flight Has Changed" fires on push |
| Legs (dep/dest, scheduled/actual times, local vs UTC, meters, fuel) | FD Legs tab, DFR, Flight & Duty recalculation (16) | Edit leg on FD › pull |
| Crew, passengers, seats, W&B | FD crew/passengers, W&B sheet totals (CG, TOW) to 0.1 | Change passengers on FD › pull › W&B recomputes |
| Extra Flight Info (`extra-field-*`) | FD › Extra info values | Edit on FD › pull |
| Forms / files | FD Forms and Files tabs; file opens; names, sizes and images at the chosen quality | Add/remove on FD › pull |
| New waypoint (`flightdetails_addwaypoint`) | Settings › Waypoints has it with coordinates | – |
| Safety report | Safety Reports list/detail: fields, risk scores, confidential/anonymous handling, actions, comments, documents | Status change / comment on frontend › Download Safety Reports |
| Chat | Chat module shows message, sender and time; image renders | Message from frontend appears (new-messages poll) |
| Aircraft / personnel / waypoints | – (read-only on iPad when linked) | Change weight/aircraft on frontend › Sync All Data › updated, no duplicates |

Every sync case is also run **twice** (no duplicates), **with the network dropped mid-push** (no partial records, a clear error, retry works), **after the session expires** (re-auth prompt) and **as a lower-permission user** (server rules respected, no silent failure).

## 5. UX/UI audit scope (checklists 76–77)

For each screen, in both orientations, check:

- **Layout:** no clipped or overlapping content, no horizontal scroll, header and tab bar fixed, safe-area/`viewport-fit=cover` padding, modals/sheets centred and scrollable, keyboard does not cover the focused input, list rows don't truncate key data (flight titles currently truncate at ~45 chars).
- **Orientation change:** state, scroll position, open sheet and unsaved input survive rotation.
- **Touch:** targets ≥ 44 × 44 pt, no hover-only affordances, swipe/scroll inertia, no accidental double-submit, pickers usable by touch.
- **Visual consistency:** the three themes (Dark/Midtone/Light) on every screen, contrast WCAG AA (4.5:1 text, 3:1 UI), consistent button styles, icons, spacing and typography, empty/loading/error states present.
- **Feedback:** toasts and modals use app UI (no native `alert/confirm`), destructive actions confirm (danger style), progress shown for sync/download/upload, errors say what to do.
- **Wording and formats:** labels match the frontend's terms (e.g. "Datahangar" vs "DataHangar" capitalisation), date/time formats follow Configuration (24h/12h) and the frontend's site time zone (Pacific/Auckland), units (kg/lb, L/US gal), coordinate format.
- **Accessibility:** buttons have accessible names, focus order is logical, text scales (Dynamic Type is native-only: BLOCKED in Chrome), screen-reader labels on icon buttons.
- **Consistency with the frontend:** the same record looks the same (names, statuses, colours, risk-matrix colours) on the iPad and the website.

## 6. Initial assessment (24/10/2026, stresstest, Chrome 137)

**Works:**
- First-run modal works.
- Test Authentication returns "Authentication Successful".
- Sync All Data pulls 21 aircraft (all "DataHangar Linked", grouped by type), 46 crew and 15 waypoints.
- Download Flights lists the current week (Oct 19 – Oct 25) and downloads #8893 ("1 leg, 0 files", shown as "#8893 synced").
- The Comms channel picker loads.
- Responsive emulation at 820 × 1180 works.

**Logged:**
- `BUG-IPSEC-001` (High): the DataHangar password is stored in plain text in `localStorage` (`datahangarPassword`, plus a `datahangarPassword_backup` copy). The web build shares an origin with the frontend, so any script on that origin can read it. Together with BUG-ATT-001 (uploaded HTML served inline), an uploaded file could read it.

**To verify against the frontend (not yet bugs):**
- Every synced crew member shows **Weight: 0.0 kg**, and every synced aircraft has `emptyWeight`/`maxWeight` 0. Is the weight missing from `personnellist_json`, or is it not mapped? This affects W&B.
- Waypoints list **NZAA twice**: one has coordinates, the other has none. Is this a duplicate in Settings › Waypoints, or a merge bug?
- `flightdetails_json` returns `lastUpdatedAt: null` for #8893. The "Server Flight Has Changed" conflict check depends on it, so conflicts may never be detected.
- `flightdetails_json` (used by the iPad) returns large global lists with every flight: 162 personal emergency contacts, 113 authorisers/followers and all aircraft. That is a payload-size and data-minimisation question for the frontend team.
- Configuration PIN help says "default: 0000", but the stored `configPin` is empty. Check whether Configuration is actually PIN-protected.
- Capitalisation is inconsistent: "Datahangar" in Configuration, "DataHangar" elsewhere.
- `favicon.ico` returns 404 under /ipad/, and `manifest.json` has `"icons": []`, so there is no home-screen icon.

## 7. Exit criteria

- Every `60–79` checklist row is PASS, FAIL (with a bug), N/A or BLOCKED (with a reason); every BLOCKED (native) row is queued for the Xcode session.
- Every sync matrix row has been checked in both directions, with frontend evidence.
- UX rows have been done at P and L for every screen, plus mini/pro spot checks.
- Bugs are in `bugs.json` and `STATUS.md` has been regenerated. iPad fix-it handovers use `../handover/FIXIT_HANDOVER_TEMPLATE.md` with module `iPad`.
