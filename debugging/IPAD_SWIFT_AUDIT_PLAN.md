# DataHangar W&B iPad app (Swift): full bug audit plan

**App:** native SwiftUI "DataHangar W&B" (`DataHangarWAB.xcodeproj`, bundle `datahangar.WeightAndBalance`, v0.1.0 build 1). Offline-first companion app: everything is stored locally (Core Data, Keychain, UserDefaults) and synced to DataHangar through the `index.pl?action=…` API.
**Server:** https://stresstest.datahangar.net, Service Account `datahangar`, used for both the app login and the website.
**Fits the existing audit:** `defyent/devin` → `debugging/` (same checklist format, ID rules, severities, `bugs.json` → `mkstatus.py` → `STATUS.md`, `BUG-<PREFIX>-NNN.md`, fixit handovers).

## 1. Environment
| Item | Setup |
|---|---|
| App | Built from the copied source on the macOS VM (Xcode 26.6), run in the **iPad Pro 13" (M5), iOS 26.5** Simulator. Spot checks on **iPad mini (A17 Pro)** for the smallest iPad layout. |
| Website | Chrome on the same VM, logged in as Service Account, side by side with the Simulator. Navigation via in-app menus only (no `?action=` URLs), as in the rest of the audit. |
| Orientation | Each screen checked in portrait and landscape (Simulator rotate). |
| Versions | Each record gets the app version + source commit **and** the DataHangar header version. Hard-refresh the website before verifying. |
| Unit tests | `xcodebuild test` (8 existing test suites) once at the start, to get a baseline before the UI audit. |
| GPS / network | `simctl location` for simulated positions (nearest aerodrome, live tracking). Offline tests by blocking the server host on the VM. |
| Test data | Name every record `BETA TEST ONLY iPad …` and list it in each checklist's *Test data created* table plus the cleanup list. |
| Credentials | Typed into the app/Chrome at runtime only. Never written to the repo or notes. |

## 2. Method: every feature both directions
For every feature that touches DataHangar data:
1. **App → website:** create or edit in the app, push or sync, then find it on the website through the menus and compare **every field** (values, units, times/time zone, rounding, attachments, forms, W&B numbers).
2. **Website → app:** change the same record on the website. Check the app's out-of-sync badge (5-minute poll) and pull, then compare again.
3. **Both sides changed:** confirm conflict/stale-data detection and that no data is lost silently.
4. **Offline:** make the change with no network, then reconnect and push. Check nothing is lost or duplicated.

Local-only features (Calculator, app settings, aircraft editor for local aircraft) get hand calculations and reference values instead.

Standard traps on every screen: custom popups only (never system alerts), toast on successful post, empty/too-long input, `' " < > &`, emoji, macrons (ā), double-tap Save, Cancel with unsaved changes, rotation mid-edit, app kill/relaunch mid-edit (persistence).

## 3. Checklists (prefixes `IP…`, bugs `BUG-IP<AREA>-NNN`)
| # | File | Prefix | Covers | Website cross-check |
|---|---|---|---|---|
| 60 | `60-ipad-setup-install` | IPSET | Install, first launch, welcome modal, auto-sync overlay + Skip, icons/display name, unit-test baseline | — |
| 61 | `61-ipad-config-general` | IPCFG | PIN gate (set/change/wrong PIN), theme light/dark/midtone, time format/offset, proximity, coord format, weight unit, device ID, debug mode | Settings > Time Zone formats |
| 62 | `62-ipad-datahangar-login` | IPDH | URL validation, login good/bad password, 2FA account, Test Connection, expired session, Sync All progress/errors, last sync, API debug log (password redacted) | Login/2FA behaviour |
| 63 | `63-ipad-sync-reference-data` | IPREF | Aircraft/resources (meters, time settings), crew list (Crew role), waypoints, flight types, form templates, master W&B config | Counts and field-by-field vs Settings – Resources, W&B Configs, Waypoints, Flight Types, Form Builder, Access Manager |
| 64 | `64-ipad-aircraft-editor` | IPAC | 5 tabs (General, Equipment, Profiles, Graphs, Meters), seat grid, fuel burn, external load, unit-system conversion, duplicate/copy config, server vs local aircraft read-only rules | Settings – W&B Configs |
| 65 | `65-ipad-personnel-waypoints` | IPPW | Personnel list/search/badges/weights, waypoint add/edit, DD/DDM/DMS, auto-create waypoint on push | All Personnel, Settings – Waypoints |
| 66 | `66-ipad-flights-list` | IPFL | Create flight, search, sync badges (4 states), swipe-delete, JSON import, Download Flights (week paging) | Flight Schedule list |
| 67 | `67-ipad-flight-legs` | IPLEG | Flight details editor, legs add/edit/delete, aerodrome picker + nearest, times validation, PIC/copilot/crew, manual names, passengers/manifest, baggage, fuel, seat map, remove/restore seats, equipment per leg | Flight Details (legs, crew & pax, manifest, Leg Info) |
| 68 | `68-ipad-weight-balance` | IPWB | W&B items, ZFW/TOW, arms/moments, fuel burn, external load, profile overrides, warnings (MTOW, seat max, CG), envelope graph, imperial/metric/metric-mm, kg/lb/L/USG | Hand calculations **and** the same flight's W&B in website Flight Details (must match exactly) |
| 69 | `69-ipad-flight-times-meters` | IPFT | Clock vs meter sources, cumulative/summed meters, previous-value carry-forward, validation warnings, odometer input widget | Flight Details times, Daily Flight Record, Resources meters |
| 70 | `70-ipad-flight-forms` | IPFORM | Attach template, every widget type (text…scribble), conditions, required/completion badge, edit/delete, sync | Flight Details → Forms, Form Browser |
| 71 | `71-ipad-flight-files` | IPFILE | Photo library + Files app, thumbnails, image/PDF preview, file types (reuse 96-xc-attachments list), delete, upload/download | Flight Details → Files, File Browser |
| 72 | `72-ipad-push-pull-sync` | IPSYNC | Create/update push (`Ok:ID`), pull, out-of-sync detection, conflicts, offline queue, delete semantics, generated PDF upload (old PDF replaced), duplicate-push on double tap | Flight Schedule, Flight Details, DFR, Activity Log |
| 73 | `73-ipad-pdf-json-export` | IPPDF | Flight/manifest PDF (title, manifest, W&B, graph pages), share sheet, JSON export → import round-trip | PDF numbers vs website Flight Details |
| 74 | `74-ipad-safety-reports` | IPSMS | List/download, create (required fields, confidential, anonymous, on behalf of), risk matrix, status changes, actions create/complete, final report, investigators/reviewers, forms, files, comments, extra info, hazard | Safety Reports module + Dashboard Safety Actions + Hazard Register |
| 75 | `75-ipad-comms-chat` | IPCHAT | Channels list/create, send/receive, images, delete, mark read, load older, unread, admin-only actions | Chat module, both directions in real time |
| 76 | `76-ipad-calculator` | IPCALC | All 12 calculators: standard, fuel, pressure alt, density alt, TAS, wind correction, crosswind, speed/distance/time, descent planner, unit converter, sunrise/sunset | Hand/reference calculations (no website side) |
| 77 | `77-ipad-live-tracking` | IPTRK | Enable + interval, start/stop on a server flight, background location, simulated route, offline ping queue, resume after relaunch | Active Flights map/SAR watch |
| 78 | `78-ipad-cross-cutting` | IPXC | Portrait/landscape, iPad mini vs 13", themes, Dynamic Type/VoiceOver basics, popup/toast conventions, errors (server down, timeout 60s, bad JSON), date/time vs Settings > Time Zone, performance with stresstest volume (flight list, big forms, images) | — |
| 79 | `79-ipad-permissions-e2e` | IPE2E | Low-permission accounts (new test accounts via Access Manager templates: RO / WO / WG / no Flight Details / no SMS), then full E2E: day of ops (download → fly legs → W&B → forms/files → push → verify DFR/F&D) | Access Manager, Flight and Duty, DFR |

Estimated size is 350–450 checks. Order: 60 → 63 (all later checks need synced data) → 66–73 (core flight flow) → 74 → 75 → 77 → 64/65 → 76 → 78 → 79 last as the regression pass.

## 4. Reporting
- Checklists in `debugging/checklists/60-79-ipad-*.md` and bugs in `debugging/bugs/BUG-IP*.md` with Simulator + Chrome screenshots. `bugs.json`/`STATUS.md` regenerated after each checklist, with the new IP prefixes added to `mkstatus.py`.
- Bug files show **both** sides (app screen and website screen), the device, the orientation, and the app and DataHangar versions. Each item is marked BUG or NEEDS PRODUCT DECISION. Nothing ambiguous gets called a bug without asking you first.
- Fixit handovers: `FIX_HANDOFF_ipad-v<appversion>_dh-v<dhversion>_<module>.md`, one per module. Because the iPad fixit agent will have the Swift source, these can name the Swift files involved. If the root cause is server-side, the bug goes into the normal web handover instead.
- Progress % (current checklist and overall) in every update. Test-data cleanup list at the end.

## 5. Questions before starting
1. **Spec:** there's no user guide for the app. I propose using `CONVERSION_CHECKLIST.md`, website behaviour and the React app's behaviour as "expected". Calculator/Comms are marked "define scope" in the checklist. Should I treat what's built as the intended scope?
2. **Source location:** can I commit the Swift source to a private repo (or a folder/branch of `defyent/devin`)? Bug files and handovers can then link to it, and future sessions won't need the copy step.
3. **Pushes from the app:** OK to create, update and delete real flights, SMS reports and chat messages on stresstest from the app (all named BETA TEST ONLY)?
4. **2FA / permissions:** is there an existing 2FA-enabled test account, or should I create test accounts in Access Manager as needed?
