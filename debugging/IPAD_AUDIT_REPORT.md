# iPad app (native Swift) audit report

DataHangar Flight iPad companion app, audited against the DataHangar website (stresstest). Date: 24/10/2026. Tester: Devin.

**Result:** 33 bugs (9 High, 13 Medium, 11 Low). 258 checks across 20 checklists (60-79): 165 PASS, 66 FAIL, 27 N/A (decisions, candidates, info and not-tested items).

Contents: [1 Summary](#1-summary) · [2 Scope and environment](#2-scope-and-environment) · [3 How it was tested](#3-how-it-was-tested) · [4 Results by checklist](#4-results-by-checklist) · [5 Bug list](#5-bug-list) · [6 Bug details](#6-bug-details) · [7 What works](#7-what-works) · [8 Not tested](#8-not-tested) · [9 Decisions needed](#9-decisions-needed) · [10 Other observations](#10-other-observations-candidates-and-info) · [11 Test data and cleanup](#11-test-data-and-cleanup) · [12 Files](#12-files)

## 1. Summary

The iPad app is a local-first companion to DataHangar: it stores flights, Safety Reports and reference data on the iPad and syncs with the website by Pull/Push. Every feature with a website counterpart was changed in the app and checked on the website, and changed on the website and checked in the app after Pull. Offline, stale-data, conflict, relaunch and permission behaviour were also tested.

**Most important problems**

- **[BUG-IPCALC-001](bugs/BUG-IPCALC-001.md) (High):** Unit Converter: NM <-> Statute Miles conversion inverted; large values shown in scientific notation
- **[BUG-IPFL-002](bugs/BUG-IPFL-002.md) (High):** Flights with a Student PIC cannot be pushed from the app
- **[BUG-IPFL-003](bugs/BUG-IPFL-003.md) (High):** Leg times pulled from DataHangar ("HH:MM:SS") display as the current time; editing overwrites them
- **[BUG-IPFORM-001](bugs/BUG-IPFORM-001.md) (High):** Pushed form uses the wrong template and loses widget data
- **[BUG-IPFORM-002](bugs/BUG-IPFORM-002.md) (High):** Pull creates phantom form instances and pushed updates are ignored
- **[BUG-IPFORM-003](bugs/BUG-IPFORM-003.md) (High):** Form Date/Time widgets ignore website values and show (and can save) the current date/time
- **[BUG-IPSMS-001](bugs/BUG-IPSMS-001.md) (High):** Safety Report form attached in iPad app is silently lost on push
- **[BUG-WEBCHAT-001](bugs/BUG-WEBCHAT-001.md) (High):** Chat API used by the iPad app ignores the Chat permission (permission bypass)
- **[BUG-WEBTRK-001](bugs/BUG-WEBTRK-001.md) (High):** Live tracking pings fail on stresstest - live_tracking table missing

**Main themes**

- **Sync integrity:** several paths lose or corrupt data without warning - wrong form template on push, Safety Report forms lost after a 'successful' push, pulled leg times shown as the current time, stale Push overwriting website edits, Pull not applying website Notes and marking unsent edits as synced, flights whose aircraft never re-links.
- **Errors swallowed / unclear:** Safety Report push ignores form, file and status errors; raw server text ('Error block Error', HTML pages, '(nil)') reaches the user; offline actions wait ~60 s before failing.
- **Permissions:** the server Chat API ignores the Chat permission (security). The app shows full edit controls to read-only users and relies on the server to reject the push.
- **Server (stresstest):** the `live_tracking` table is missing, so no positions can be saved, and the error page exposes SQL and server paths.
- **UI/accessibility:** keyboard input leaks into fields behind sheets, Light-theme contrast, sparse VoiceOver labels and partial Dynamic Type.

## 2. Scope and environment

| Item | Value |
|---|---|
| App | DataHangar Flight 1.0.13 (build 46), bundle `datahangar.WeightAndBalance`, Xcode project `DataHangarWAB.xcodeproj` (SwiftUI) |
| Source | Copied from the user's Windows machine to the audit VM (`~/repos/datahangar-ipad/`). Not on GitHub and not in this repo. |
| Build | Xcode 26.6, Debug, ad-hoc signed (an unsigned build makes Keychain saves fail silently - see BUG-IPDH-001) |
| Devices | iPad Pro 13-inch (M5) Simulator and iPad mini (A17 Pro) Simulator, iOS 26.5. No physical iPad. |
| Website | https://stresstest.datahangar.net, v2.0.123, used through the visible Chrome UI and in-app menus only |
| Accounts | Service Account (`datahangar`, admin) on both website and app; temporary `betalowperm` ('BETA TEST ONLY LowPerm') for permission tests. Passwords are not recorded anywhere. |
| Time zones | VM/Simulator clock US Pacific; DataHangar server NZ time. Time-zone handling recorded as a decision (section 9). |
| Test data | All records named 'BETA TEST ONLY' (section 11) |

Features covered: setup and unit tests, Configuration (theme, time format, time offsets, PIN, aerodrome proximity, coordinates, weight units, device ID, debug), DataHangar login and Sync All, reference data (aircraft, personnel, waypoints, flight types, forms, W&B master config), aircraft editor, personnel and waypoints, Flights (list, download, legs, crew and seats, W&B, times and meters, forms, files, Push/Pull, PDF and JSON export), Safety Reports (details, comments, actions, status, files, forms, final report), Comms/Chat, Live Tracking, all 11 calculators, layouts/orientation/themes/accessibility, offline and conflict behaviour, and permissions.

## 3. How it was tested

- **App -> website:** create or edit in the app, Push, then compare every field on the website.
- **Website -> app:** edit on the website, Pull/Download in the app, then compare every field again.
- **Conflicts:** edit the same record on both sides and check whether the app detects the clash or loses data.
- **Offline:** block only the stresstest host with a blackhole route (the VM stays online), edit, force-quit, relaunch, reconnect and push.
- **W&B and calculators:** every result checked by hand calculation and against the website's Flight Details.
- **Permissions:** a temporary user with 0 permissions, then Safety Reports Write Own, Flight Schedule / Flight Details Read Only All, Resources and W&B Config Download, then Safety Report Investigator and per-report investigator assignment, then revocation.
- **Source review:** where behaviour needed explaining, the Swift source was read to find the cause (file/function noted in each bug).
- Evidence: screenshots are in `bugs/screenshots/` and linked from each bug and checklist row.

## 4. Results by checklist

| Checklist | Checks | PASS | FAIL | N/A | Bugs |
|---|---:|---:|---:|---:|---|
| [iPad setup and install](checklists/60-ipad-setup-install.md) | 3 | 2 | 1 | 0 | [BUG-IPSET-001](bugs/BUG-IPSET-001.md) |
| [iPad configuration — general](checklists/61-ipad-config-general.md) | 8 | 3 | 5 | 0 | [BUG-IPCFG-001](bugs/BUG-IPCFG-001.md), [BUG-IPUI-002](bugs/BUG-IPUI-002.md) |
| [iPad DataHangar login and sync](checklists/62-ipad-datahangar-login.md) | 8 | 6 | 2 | 0 | [BUG-IPDH-001](bugs/BUG-IPDH-001.md), [BUG-IPDH-002](bugs/BUG-IPDH-002.md) |
| [iPad sync reference data](checklists/63-ipad-sync-reference-data.md) | 10 | 9 | 0 | 1 | - |
| [iPad aircraft editor](checklists/64-ipad-aircraft-editor.md) | 10 | 7 | 2 | 1 | [BUG-IPAC-001](bugs/BUG-IPAC-001.md) |
| [iPad personnel and waypoints](checklists/65-ipad-personnel-waypoints.md) | 11 | 7 | 3 | 1 | [BUG-IPWPT-001](bugs/BUG-IPWPT-001.md) |
| [iPad flights list](checklists/66-ipad-flights-list.md) | 14 | 6 | 6 | 2 | [BUG-IPFL-001](bugs/BUG-IPFL-001.md), [BUG-IPFL-002](bugs/BUG-IPFL-002.md), [BUG-IPFL-003](bugs/BUG-IPFL-003.md) |
| [iPad flight legs](checklists/67-ipad-flight-legs.md) | 8 | 7 | 1 | 0 | - |
| [iPad weight and balance](checklists/68-ipad-weight-balance.md) | 6 | 3 | 3 | 0 | [BUG-IPWB-001](bugs/BUG-IPWB-001.md), [BUG-IPWB-002](bugs/BUG-IPWB-002.md) |
| [iPad flight times and meters](checklists/69-ipad-flight-times-meters.md) | 9 | 7 | 1 | 1 | [BUG-IPREF-001](bugs/BUG-IPREF-001.md) |
| [iPad flight forms](checklists/70-ipad-flight-forms.md) | 7 | 4 | 3 | 0 | [BUG-IPFORM-001](bugs/BUG-IPFORM-001.md), [BUG-IPFORM-002](bugs/BUG-IPFORM-002.md) |
| [iPad flight files](checklists/71-ipad-flight-files.md) | 8 | 8 | 0 | 0 | - |
| [iPad push/pull sync](checklists/72-ipad-push-pull-sync.md) | 7 | 3 | 3 | 1 | - |
| [iPad PDF/JSON export](checklists/73-ipad-pdf-json-export.md) | 3 | 3 | 0 | 0 | - |
| [iPad safety reports](checklists/74-ipad-safety-reports.md) | 18 | 10 | 7 | 1 | [BUG-IPFORM-003](bugs/BUG-IPFORM-003.md), [BUG-IPSMS-001](bugs/BUG-IPSMS-001.md), [BUG-IPSMS-002](bugs/BUG-IPSMS-002.md), [BUG-IPSMS-003](bugs/BUG-IPSMS-003.md), [BUG-IPSMS-004](bugs/BUG-IPSMS-004.md) |
| [iPad communications and chat](checklists/75-ipad-comms-chat.md) | 12 | 9 | 1 | 2 | [BUG-IPCHAT-001](bugs/BUG-IPCHAT-001.md) |
| [iPad calculator](checklists/76-ipad-calculator.md) | 12 | 11 | 1 | 0 | [BUG-IPCALC-001](bugs/BUG-IPCALC-001.md) |
| [iPad live tracking](checklists/77-ipad-live-tracking.md) | 5 | 3 | 2 | 0 | [BUG-IPTRK-001](bugs/BUG-IPTRK-001.md), [BUG-IPTRK-002](bugs/BUG-IPTRK-002.md), [BUG-WEBTRK-001](bugs/BUG-WEBTRK-001.md) |
| [iPad cross-cutting checks](checklists/78-ipad-cross-cutting.md) | 23 | 14 | 8 | 1 | [BUG-IPOFF-001](bugs/BUG-IPOFF-001.md), [BUG-IPSYNC-001](bugs/BUG-IPSYNC-001.md), [BUG-IPUI-001](bugs/BUG-IPUI-001.md), [BUG-IPUI-003](bugs/BUG-IPUI-003.md) |
| [iPad permissions and end-to-end](checklists/79-ipad-permissions-e2e.md) | 76 | 43 | 17 | 16 | [BUG-IPFL-004](bugs/BUG-IPFL-004.md), [BUG-IPPERM-001](bugs/BUG-IPPERM-001.md), [BUG-IPSYNC-002](bugs/BUG-IPSYNC-002.md), [BUG-WEBCHAT-001](bugs/BUG-WEBCHAT-001.md) |
| **Total** | **258** | **165** | **66** | **27** | **33** |

## 5. Bug list

| Bug | Severity | Area | Title | Checklist row |
|---|---|---|---|---|
| [BUG-IPCALC-001](bugs/BUG-IPCALC-001.md) | High | iPad app — Calculator > Unit Converter (Distance) | Unit Converter: NM <-> Statute Miles conversion inverted; large values shown in scientific notation | [IPCALC-010](checklists/76-ipad-calculator.md) |
| [BUG-IPFL-002](bugs/BUG-IPFL-002.md) | High | Flight sync / personnel | Flights with a Student PIC cannot be pushed from the app | [IPFL-002f](checklists/66-ipad-flights-list.md) |
| [BUG-IPFL-003](bugs/BUG-IPFL-003.md) | High | iPad app — Flights > Leg Detail > Route & Times (also time engine) | Leg times pulled from DataHangar ("HH:MM:SS") display as the current time; editing overwrites them | [IPFL-010](checklists/66-ipad-flights-list.md) |
| [BUG-IPFORM-001](bugs/BUG-IPFORM-001.md) | High | Flight forms / upload | Pushed form uses the wrong template and loses widget data | [IPFORM-003](checklists/70-ipad-flight-forms.md) |
| [BUG-IPFORM-002](bugs/BUG-IPFORM-002.md) | High | Flight forms / sync | Pull creates phantom form instances and pushed updates are ignored | [IPFORM-004](checklists/70-ipad-flight-forms.md) |
| [BUG-IPFORM-003](bugs/BUG-IPFORM-003.md) | High | iPad app — Forms engine (Safety Report forms and Flight forms), checklist 70/74 | Form Date/Time widgets ignore website values and show (and can save) the current date/time | [IPSMS-014](checklists/74-ipad-safety-reports.md) |
| [BUG-IPSMS-001](bugs/BUG-IPSMS-001.md) | High | iPad app — Safety Reports > Forms (checklist 74) | Safety Report form attached in iPad app is silently lost on push | [IPSMS-013](checklists/74-ipad-safety-reports.md) |
| [BUG-WEBCHAT-001](bugs/BUG-WEBCHAT-001.md) | High | Website / Chat API | Chat API used by the iPad app ignores the Chat permission (permission bypass) | [IPPERM-024](checklists/79-ipad-permissions-e2e.md) |
| [BUG-WEBTRK-001](bugs/BUG-WEBTRK-001.md) | High | Website / Live Tracking API | Live tracking pings fail on stresstest - live_tracking table missing | [IPTRK-003](checklists/77-ipad-live-tracking.md) |
| [BUG-IPAC-001](bugs/BUG-IPAC-001.md) | Medium | iPad app — Configuration > Aircraft > editor; SyncService.syncAircraft | Aircraft editor edits to server aircraft are local-only and silently reverted by Sync All | [IPAC-006](checklists/64-ipad-aircraft-editor.md) |
| [BUG-IPCFG-001](bugs/BUG-IPCFG-001.md) | Medium | iPad app — Configuration > Configuration PIN / PinPadView | Configuration PIN saves non-4-digit values, permanently locking Configuration | [IPCFG-009](checklists/61-ipad-config-general.md) |
| [BUG-IPCHAT-001](bugs/BUG-IPCHAT-001.md) | Medium | - | Chat message typed while offline is discarded on send | [IPCHAT-010](checklists/75-ipad-comms-chat.md) |
| [BUG-IPFL-004](bugs/BUG-IPFL-004.md) | Medium | iPad app, Flights (download/pull/push) | Flight downloaded before aircraft sync keeps aircraft "None" forever; Pull never re-links; push fails with "(nil)" | [IPPERM-067](checklists/79-ipad-permissions-e2e.md) |
| [BUG-IPPERM-001](bugs/BUG-IPPERM-001.md) | Medium | iPad app, Flights, permissions | App lets read-only users edit and push flights and only fails at the server, showing a raw "Error block Error" message | [IPPERM-049](checklists/79-ipad-permissions-e2e.md) |
| [BUG-IPSET-001](bugs/BUG-IPSET-001.md) | Medium | Unit tests | Unit-test target does not compile | [IPSET-001](checklists/60-ipad-setup-install.md) |
| [BUG-IPSMS-002](bugs/BUG-IPSMS-002.md) | Medium | iPad app — Safety Reports > Final Report | Final Report tab shows stale values after Pull (overwrite risk) | [IPSMS-016](checklists/74-ipad-safety-reports.md) |
| [BUG-IPSMS-004](bugs/BUG-IPSMS-004.md) | Medium | iPad app — Safety Reports > Push (SMSReportUploadService) | Safety Report push says 'Successfully pushed' even if saving forms, deleting files or changing status fails | [IPSMS-009](checklists/74-ipad-safety-reports.md) |
| [BUG-IPSYNC-001](bugs/BUG-IPSYNC-001.md) | Medium | Flight sync / conflict handling | Push silently overwrites website-side Notes edits | [IPOFF-005](checklists/78-ipad-cross-cutting.md) |
| [BUG-IPSYNC-002](bugs/BUG-IPSYNC-002.md) | Medium | Flight sync / pull | Pull from Server doesn't apply website Notes and can mark an unpushed local edit as synced | [IPPERM-063](checklists/79-ipad-permissions-e2e.md) |
| [BUG-IPTRK-002](bugs/BUG-IPTRK-002.md) | Medium | iPad app — Live Tracking | Live Tracking queue stores duplicate/stale pings; rejected pings are dropped | [IPTRK-006](checklists/77-ipad-live-tracking.md) |
| [BUG-IPUI-001](bugs/BUG-IPUI-001.md) | Medium | iPad UI / keyboard focus | Hardware-keyboard focus leaks through sheets and keypads | [IPXC-002](checklists/78-ipad-cross-cutting.md) |
| [BUG-IPWPT-001](bugs/BUG-IPWPT-001.md) | Medium | iPad app — Configuration > Waypoints | Code-less server waypoints show blank titles; editing them stores 0,0 coordinates; edits are local-only | [IPWPT-004](checklists/65-ipad-personnel-waypoints.md) |
| [BUG-IPDH-001](bugs/BUG-IPDH-001.md) | Low | DataHangar configuration / credentials | Keychain save failure is silent | [IPDH-007](checklists/62-ipad-datahangar-login.md) |
| [BUG-IPDH-002](bugs/BUG-IPDH-002.md) | Low | DataHangar configuration / button states | Empty-field authentication and sync buttons look enabled | [IPDH-001](checklists/62-ipad-datahangar-login.md) |
| [BUG-IPFL-001](bugs/BUG-IPFL-001.md) | Low | Flights / flight ID display | Flight ID badges and labels add thousands separators | [IPFL-003](checklists/66-ipad-flights-list.md) |
| [BUG-IPOFF-001](bugs/BUG-IPOFF-001.md) | Low | Offline handling | Offline launch and push block for about a minute before timing out | [IPOFF-003](checklists/78-ipad-cross-cutting.md) |
| [BUG-IPREF-001](bugs/BUG-IPREF-001.md) | Low | iPad app — Configuration > DataHangar > Sync All (Flight Custom Fields) | Sync All reports 'Flight Custom Fields: 0' although a custom field is synced and used | [IPFT-006](checklists/69-ipad-flight-times-meters.md) |
| [BUG-IPSMS-003](bugs/BUG-IPSMS-003.md) | Low | iPad app — Safety Reports > Actions > New Action | Safety Report action 'Assign To' picker shows a blank person row | [IPSMS-007](checklists/74-ipad-safety-reports.md) |
| [BUG-IPTRK-001](bugs/BUG-IPTRK-001.md) | Low | iPad app — Live Tracking | Live Tracking UI/state issues (raw HTML error, stale/global menu, no offline indicator) | [IPTRK-003](checklists/77-ipad-live-tracking.md) |
| [BUG-IPUI-002](bugs/BUG-IPUI-002.md) | Low | iPad app — Configuration > General | Light theme: Configuration values/toggles unreadable (white on white) | [IPCFG-003](checklists/61-ipad-config-general.md) |
| [BUG-IPUI-003](bugs/BUG-IPUI-003.md) | Low | iPad app — cross-cutting accessibility | Sparse VoiceOver labels and partial Dynamic Type support | [IPUI-013](checklists/78-ipad-cross-cutting.md) |
| [BUG-IPWB-001](bugs/BUG-IPWB-001.md) | Low | iPad app — Flights > Leg > summary card / W&B | Leg summary card rounds equipment to whole kg and disagrees with the W&B sheet | [IPWB-002](checklists/68-ipad-weight-balance.md) |
| [BUG-IPWB-002](bugs/BUG-IPWB-002.md) | Low | iPad app — Flights > Leg > W&B cabin | Cabin header counts hidden seats ('0/4 occupied' with only 2 seats shown) | [IPWB-003](checklists/68-ipad-weight-balance.md) |

## 6. Bug details

Grouped by checklist. Each bug also has its own file in `bugs/` with the full write-up.

### iPad setup and install

#### [BUG-IPSET-001](bugs/BUG-IPSET-001.md) — Unit-test target does not compile

- **Severity:** Medium · **Status:** Open · **Area:** Unit tests · **Checklist row:** [IPSET-001](checklists/60-ipad-setup-install.md)

**Steps**

1. On the macOS VM: xcodebuild test -project 'DataHangar WAB Swift/DataHangarWAB.xcodeproj' -scheme DataHangarWAB -destination 'platform=iOS Simulator,name=iPad Pro 13-inch (M5)' (or Product > Test in Xcode).
2. Read the compile errors for the test target.

**Expected:** The unit-test target compiles.

**Actual:** Compilation fails due to duplicate FlightTimeEngineTests declarations and stale call signatures, including missing pic, copilot, crew, passengers, takeoffFuel, and decimalPlaces arguments. Renaming the duplicate still leaves about 12 compile errors.

**Cause:** Duplicate test-class declaration and test calls that have not been updated to current signatures.

### iPad configuration — general

#### [BUG-IPCFG-001](bugs/BUG-IPCFG-001.md) — Configuration PIN saves non-4-digit values, permanently locking Configuration

- **Severity:** Medium · **Status:** Open · **Area:** iPad app — Configuration > Configuration PIN / PinPadView · **Checklist row:** [IPCFG-009](checklists/61-ipad-config-general.md)

**Steps**

1. Configuration > Configuration PIN, enter `12`, tap Done. Field shows `12` (saved).
2. Close Configuration, tap the gear again.

**Expected:** PIN must be exactly 4 digits (reject/confirm before saving), or the gate accepts PINs of the saved length.

**Actual:** `12` is saved to the Keychain immediately. The PIN gate (`PinPadView`) has 4 dots and only compares once 4 digits are entered, so `12` can never match -> Configuration unreachable. Wipe Data lives inside Configuration, so the only recovery is reinstalling the app.

**Cause:** `ConfigView` binds `NumberPadField` directly to `KeychainStore.shared.configPin` (every keystroke persisted, no length/digit validation). The field's keypad also offers `.` and `+/-`. `PinPadView` `guard enteredPin.count < 4` / `if enteredPin.count == 4` compare.

**Screenshots:** [IPCFG-007_pin_gate.png](bugs/screenshots/IPCFG-007_pin_gate.png) · [IPCFG-008_pin_correct_opens.png](bugs/screenshots/IPCFG-008_pin_correct_opens.png) · [IPCFG-009_pin_2digit_saved.png](bugs/screenshots/IPCFG-009_pin_2digit_saved.png)

#### [BUG-IPUI-002](bugs/BUG-IPUI-002.md) — Light theme: Configuration values/toggles unreadable (white on white)

- **Severity:** Low · **Status:** Open · **Area:** iPad app — Configuration > General · **Checklist row:** [IPCFG-003](checklists/61-ipad-config-general.md)

**Steps**

1. Configuration > Theme = Light.
2. Look at Device Identifier and Automatic Time Offsets.

**Expected:** Values and controls legible (WCAG AA contrast), as in Dark/Midtone.

**Actual:** Device Identifier value `iPad-F6EC` is white text on a white card (unreadable). The OFF state of the Automatic Time Offsets toggle is a near-white track on white, barely visible.

**Screenshots:** [IPCFG-001_config_general.png](bugs/screenshots/IPCFG-001_config_general.png) · [IPCFG-002_light_theme.png](bugs/screenshots/IPCFG-002_light_theme.png) · [IPCFG-003_light_contrast.png](bugs/screenshots/IPCFG-003_light_contrast.png)

### iPad DataHangar login and sync

#### [BUG-IPDH-001](bugs/BUG-IPDH-001.md) — Keychain save failure is silent

- **Severity:** Low · **Status:** Open · **Area:** DataHangar configuration / credentials · **Checklist row:** [IPDH-007](checklists/62-ipad-datahangar-login.md)

**Steps**

1. Run an unsigned Simulator build with CODE_SIGNING_ALLOWED=NO.
2. Enter the DataHangar URL, username, and password, then save/use the credentials.
3. Attempt authentication.

**Expected:** The app reports a Keychain save failure, or credentials are saved successfully before authentication is attempted.

**Actual:** The Keychain write failure is not surfaced. The fields remain filled, but authentication reports Error: notConfigured. An ad-hoc-signed rebuild avoided the unsigned-build condition.

**Cause:** The app ignores the SecItemAdd status returned from the Keychain save operation.

#### [BUG-IPDH-002](bugs/BUG-IPDH-002.md) — Empty-field authentication and sync buttons look enabled

- **Severity:** Low · **Status:** Open · **Area:** DataHangar configuration / button states · **Checklist row:** [IPDH-001](checklists/62-ipad-datahangar-login.md)

**Steps**

1. Open DataHangar configuration with the URL, username, and password fields empty.
2. Observe and tap Test Authentication and Sync All.

**Expected:** Buttons unavailable because required fields are empty are visibly disabled.

**Actual:** Test Authentication and Sync All look enabled although the fields are empty. Tapping them does nothing and provides no feedback.

**Cause:** The disabled and enabled states use the same visual style.

### iPad aircraft editor

#### [BUG-IPAC-001](bugs/BUG-IPAC-001.md) — Aircraft editor edits to server aircraft are local-only and silently reverted by Sync All

- **Severity:** Medium · **Status:** Open · **Area:** iPad app — Configuration > Aircraft > editor; SyncService.syncAircraft · **Checklist row:** [IPAC-006](checklists/64-ipad-aircraft-editor.md)

**Steps**

1. Configuration > Aircraft > ZK-FLY (tagged "Server"). Set Empty Weight 600, Save. List shows "BEW 600 kg".
2. Configuration > DataHangar > Sync All Data.
3. Re-open Aircraft list.

**Expected:** Either the edit is pushed to DataHangar, or the editor marks server-owned fields read-only / warns that changes are device-only and will be overwritten on sync.

**Actual:** Sync All replaces Empty Weight with the server value (0); "BEW 600 kg" disappears with no message. Nothing is sent to the website (`AircraftEditorView.save()` -> `aircraftStore.upsert` only).

`SyncService` re-sync keeps the local W&B config (seats, arms, equipment, profiles, graphs) but overwrites emptyWeight, MTOW, type, registration, meters and time settings - so a single aircraft ends up as a mix of server and local values, and the iPad's W&B for that aircraft can differ from the website's with no indication.

**Screenshots:** [IPAC-005_zkfly_bew600_saved.png](bugs/screenshots/IPAC-005_zkfly_bew600_saved.png) · [IPAC-006_zkfly_ew_reverted_after_sync.png](bugs/screenshots/IPAC-006_zkfly_ew_reverted_after_sync.png)

### iPad personnel and waypoints

#### [BUG-IPWPT-001](bugs/BUG-IPWPT-001.md) — Code-less server waypoints show blank titles; editing them stores 0,0 coordinates; edits are local-only

- **Severity:** Medium · **Status:** Open · **Area:** iPad app — Configuration > Waypoints · **Checklist row:** [IPWPT-004](checklists/65-ipad-personnel-waypoints.md)

**Steps**

1. Sync All. Configuration > Waypoints.
2. Tap the first entry whose title is blank (subtitle `NZAA`).

**Expected:** Fall back to name when code is empty; keep blank coordinates blank; tell the user edits are device-only (or push them).

**Actual:** - 6 synced entries (BTQA, BTQC, NZAA, NZCH, NZWR, ZZZQ) have empty `code` and no lat/lon; the list uses code as the title, so rows are blank and sort first. NZAA/NZCH therefore appear twice.

- Edit sheet shows Code empty, Name `NZAA`, coordinates `0 0.0000 N / 0 0.0000 E`. Saving in DDM/DMS writes `0.000000, 0.000000` (Gulf of Guinea) instead of leaving blank.

- `save()` only updates the local `WaypointStore`; nothing is sent to DataHangar, and the next Sync All may replace it (no warning that edits are local).

**Screenshots:** [IPWPT-002_waypoints_list.png](bugs/screenshots/IPWPT-002_waypoints_list.png) · [IPWPT-003_blank_code_nzaa.png](bugs/screenshots/IPWPT-003_blank_code_nzaa.png) · [IPWPT-005_website_waypoints.png](bugs/screenshots/IPWPT-005_website_waypoints.png)

### iPad flights list

#### [BUG-IPFL-002](bugs/BUG-IPFL-002.md) — Flights with a Student PIC cannot be pushed from the app

- **Severity:** High · **Status:** Open · **Area:** Flight sync / personnel · **Checklist row:** [IPFL-002f](checklists/66-ipad-flights-list.md)

**Steps**

1. Create web flight #42915 with Aaron Fisher as PIC; Aaron Fisher is a Student accepted as a PIC on the website.
2. Add a leg on the website with Aaron Fisher as PIC and a valid weight, then pull the flight into the app.
3. Push the flight from the app.

**Expected:** The app pushes the leg successfully and preserves Aaron Fisher as the PIC.

**Actual:** The push fails with 'Leg 1: the PIC must be a crew member or student. Please choose a crew member, then save again.' The app represents Aaron Fisher as MANUAL_ENTRY, so the server rejects the PIC.

**Cause:** SyncService.syncPersonnel filters personnel to crew == 'Y', excluding Student personnel. When the PIC is absent from synced personnel, FlightSyncService.resolveCockpit falls back to a manual-entry representation.

**Screenshots:** [IPFL-002_42915_details.png](bugs/screenshots/IPFL-002_42915_details.png) · [IPFL-002_42915_push_rejected_pic.png](bugs/screenshots/IPFL-002_42915_push_rejected_pic.png) · [IPFL-002_web_aaron_fisher_student.png](bugs/screenshots/IPFL-002_web_aaron_fisher_student.png)

#### [BUG-IPFL-003](bugs/BUG-IPFL-003.md) — Leg times pulled from DataHangar ("HH:MM:SS") display as the current time; editing overwrites them

- **Severity:** High · **Status:** Open · **Area:** iPad app — Flights > Leg Detail > Route & Times (also time engine) · **Checklist row:** [IPFL-010](checklists/66-ipad-flights-list.md)

**Steps**

1. Push a flight with leg times from the app (or create one on the website), then Pull / download it so the app stores the server copy.
2. Open the flight > Leg 1.

**Expected:** Start/Takeoff/Landing/Stop show the server times (#42914: 23:07, 23:08, 00:07, 01:07).

**Actual:** All four show the current device time (02:13 AM in 12h mode / 02:14 in 24h mode). The local store still holds "23:07:00" etc.

**Cause:** `FlightSyncService` maps `engineStart`/`flightStart`/`flightStop`/`engineStop` verbatim; the server returns `HH:MM:SS`.
`TimeUtils.parseHHMM` accepts only `HH:MM` (2 parts) or `HHMM`; 3 parts -> nil. `TimeUtils.dateFromHHMM` then returns `Date()`, which the leg DatePicker binds to, so the picker shows "now" and any interaction commits "now" via `phase.onCommit(hhmmFromDate(...))`.
`TimeUtils.durationMinutes` (used by FlightTimeEngine / upload clockHours) relies on the same parser.

**Screenshots:** [IPCFG-004_12h_leg_times_now.png](bugs/screenshots/IPCFG-004_12h_leg_times_now.png) · [IPFL-010_leg_times_show_now_24h.png](bugs/screenshots/IPFL-010_leg_times_show_now_24h.png)

#### [BUG-IPFL-001](bugs/BUG-IPFL-001.md) — Flight ID badges and labels add thousands separators

- **Severity:** Low · **Status:** Open · **Area:** Flights / flight ID display · **Checklist row:** [IPFL-003](checklists/66-ipad-flights-list.md)

**Steps**

1. Open Download Flights and inspect the flight ID badges.
2. Inspect flight ID labels in the flight list, flight details, and communications views.

**Expected:** Flight IDs display as ungrouped identifiers, without locale-dependent numeric formatting.

**Actual:** Some badges and labels apply thousands separators (for example, #8,893 and #43,913), while adjacent text shows the same IDs without separators.

**Cause:** SwiftUI interpolation of an Int in a localized Text/Label string applies numeric grouping.

**Screenshots:** [IPDL-download_list_week.png](bugs/screenshots/IPDL-download_list_week.png)

### iPad weight and balance

#### [BUG-IPWB-001](bugs/BUG-IPWB-001.md) — Leg summary card rounds equipment to whole kg and disagrees with the W&B sheet

- **Severity:** Low · **Status:** Open · **Area:** iPad app — Flights > Leg > summary card / W&B · **Checklist row:** [IPWB-002](checklists/68-ipad-weight-balance.md)

**Steps**

1. ZK-HEL leg with Survival kit 3 kg onboard and Dual controls -1.2 kg removed.
2. Compare the leg summary card, the app W&B sheet and the website leg W&B.

**Expected:** Net equipment 1.8 kg (the website shows 1.80 with the onboard/removed breakdown).

**Actual:** Summary card shows 'Equipment 2 kg' (rounded net) while the W&B section shows 'Equipment 3 kg' (onboard only). ZFW/TOW/CG totals are correct and match the website exactly; this is display only.

**Cause:** Integer rounding and different definitions (net vs onboard) in the two views.

**Screenshots:** [IPWB-001_app_leg_wb.png](bugs/screenshots/IPWB-001_app_leg_wb.png) · [IPWB-006_web_42914_wb_totals.png](bugs/screenshots/IPWB-006_web_42914_wb_totals.png)

#### [BUG-IPWB-002](bugs/BUG-IPWB-002.md) — Cabin header counts hidden seats ('0/4 occupied' with only 2 seats shown)

- **Severity:** Low · **Status:** Open · **Area:** iPad app — Flights > Leg > W&B cabin · **Checklist row:** [IPWB-003](checklists/68-ipad-weight-balance.md)

**Steps**

1. Open a ZK-HEL leg > cabin / seat layout.

**Expected:** The occupancy count matches the seats shown, or the hidden row-2 seats are shown.

**Actual:** Header says '0/4 occupied' but only Rear Left / Rear Right are shown. ZK-HEL's config has seats R2C1/R2C2 (row 2, arm 330) while seatRows = 1, so 2 seats are counted but can't be used.

**Cause:** Likely: occupancy counts every config seat while the grid renders only seatRows rows (not confirmed in source).

### iPad flight times and meters

#### [BUG-IPREF-001](bugs/BUG-IPREF-001.md) — Sync All reports 'Flight Custom Fields: 0' although a custom field is synced and used

- **Severity:** Low · **Status:** Open · **Area:** iPad app — Configuration > DataHangar > Sync All (Flight Custom Fields) · **Checklist row:** [IPFT-006](checklists/69-ipad-flight-times-meters.md)

**Steps**

1. Website: Settings > Extra Flight Info has the field 'BETA TEST ONLY EFI'.
2. iPad app: Configuration > DataHangar > Sync All Data and read the results summary.
3. Open flight #42914 > Details tab.

**Expected:** The Sync All summary shows 1 Flight Custom Field.

**Actual:** The summary says 'Flight Custom Fields: 0', yet the field is stored locally (extraFlightInfoFields), shown on the flight Details tab, and its value 'BETA TEST ONLY EFI audit value' pushed to the website correctly. Only the count is wrong/misleading.

**Cause:** Not traced in source (summary count vs stored data).

### iPad flight forms

#### [BUG-IPFORM-001](bugs/BUG-IPFORM-001.md) — Pushed form uses the wrong template and loses widget data

- **Severity:** High · **Status:** Open · **Area:** Flight forms / upload · **Checklist row:** [IPFORM-003](checklists/70-ipad-flight-forms.md)

**Steps**

1. In the app, attach BETA TEST ONLY Form to flight #42914.
2. Fill 8 of the form's 12 fields and save the form.
3. Push the flight and inspect the attached form on the website.

**Expected:** The website shows BETA TEST ONLY Form with the values entered in the app.

**Actual:** The app pushes BETA TEST ONLY Form, but the website shows QA Post-Flight Report with only 1 of 11 fields populated (the automatically populated Flight Date). The app-entered widget values are absent.

**Cause:** Suspected (not fully traced): the template IDs the app syncs and sends don't match the server's form_template_id values, so the server attaches a different template (the app's 'BETA TEST ONLY Form' became 'QA Post-Flight Report' on the website) and the widget data doesn't fit it.

**Screenshots:** [IPFORM-003_web_wrong_form.png](bugs/screenshots/IPFORM-003_web_wrong_form.png) · [IPJSON-001_export.json](bugs/screenshots/IPJSON-001_export.json)

#### [BUG-IPFORM-002](bugs/BUG-IPFORM-002.md) — Pull creates phantom form instances and pushed updates are ignored

- **Severity:** High · **Status:** Open · **Area:** Flight forms / sync · **Checklist row:** [IPFORM-004](checklists/70-ipad-flight-forms.md)

**Steps**

1. On flight #42914, pull the server's attached form data into the app.
2. Compare the app's Forms tab with the website's Forms tab.
3. Push the flight again and compare the website form's update state.

**Expected:** The app shows the single form instance present on the website, and a pushed update to that instance is reflected on the website.

**Actual:** The app shows three local instances (IDs 198, 199, and 200), while the website has one QA Post-Flight Report. The app's later 'updated' entries are silently ignored by the website.

**Cause:** The app never stores the server instance ID returned for a pushed form, so each push re-sends the form as new, and each Pull adds server instances alongside the local copies (the app ended up with 3 instances 198/199/200 while the website showed 1).

**Screenshots:** [IPFORM-004_app_3_phantom_forms.png](bugs/screenshots/IPFORM-004_app_3_phantom_forms.png) · [IPFORM-dup_web_forms_tab.png](bugs/screenshots/IPFORM-dup_web_forms_tab.png)

### iPad safety reports

#### [BUG-IPFORM-003](bugs/BUG-IPFORM-003.md) — Form Date/Time widgets ignore website values and show (and can save) the current date/time

- **Severity:** High · **Status:** Open · **Area:** iPad app — Forms engine (Safety Report forms and Flight forms), checklist 70/74 · **Checklist row:** [IPSMS-014](checklists/74-ipad-safety-reports.md)

**Steps**

1. Website: Safety Report #2064 > Forms > Add Form > QA Hazard Observation; Observed Time 01:25, fill others, Save Changes.
2. App: open #2064, Pull, Forms > QA Hazard Observation.
3. Close, wait one minute, reopen.

**Expected:** Observed Time shows 01:25 (the saved value).

**Actual:** Shows 01:26, then 01:27 after reopening — always the current time. Local stored value is still `"2026-10-24 01:25:00"`. Observed Date shows today (coincidentally correct here; a value from any other day would display as today).

**Cause:** `Views/Forms/FormWidgetViews.swift`: `FormDateField` parses `yyyy-MM-dd`, `FormTimeField` uses `TimeUtils.dateFromHHMM` (`HH:mm`). The website stores date and time widgets as `yyyy-MM-dd HH:mm:ss`. Both getters fall back to `Date()` on parse failure, so the picker shows now; any edit/Save writes the wrong value back.

**Screenshots:** [IPSMS-014_app_form_time_now.png](bugs/screenshots/IPSMS-014_app_form_time_now.png) · [IPSMS-014_app_form_values.png](bugs/screenshots/IPSMS-014_app_form_values.png) · [IPSMS-014_web_form_saved.png](bugs/screenshots/IPSMS-014_web_form_saved.png)

#### [BUG-IPSMS-001](bugs/BUG-IPSMS-001.md) — Safety Report form attached in iPad app is silently lost on push

- **Severity:** High · **Status:** Open · **Area:** iPad app — Safety Reports > Forms (checklist 74) · **Checklist row:** [IPSMS-013](checklists/74-ipad-safety-reports.md)

**Steps**

1. In the app open Safety Report #2064 (BETA TEST ONLY iPad SMS report) > Forms > Attach Form > QA Hazard Observation.
2. Fill Risk Level=Medium, Location, Description, Hazard Category=Maintenance, Reported to Supervisor=on; Save (shows 5/8 fields, "#2064 needs push").
3. Tap Push > confirm.

**Expected:** Form instance is created on the server with the entered values and appears in the website Forms tab and stays in the app.

**Actual:** - App shows "Report Synced — Successfully pushed to DataHangar Report #2064."

- Website #2064 Forms tab: "No forms have been attached."

- App Forms tab after the post-push refresh: "No forms attached" (local `attachedForms` = []). The user's entered form data is gone on both sides.

**Cause:** - `SMSReportSyncService.addForm` (`smsreportdetails_addform`) has no callers anywhere in the project.
- `SMSReportUploadService` step 9 calls `saveForms`, which sends `instance_id = form.localId` for forms without a server instance; the server does not create an instance from it.
- The call is `try? await smsSync.saveForms(...)` — any error is swallowed and the push still reports success; step 11 then refreshes from server and overwrites the local form list.

**Screenshots:** [IPSMS-013_app_attach_form_list.png](bugs/screenshots/IPSMS-013_app_attach_form_list.png) · [IPSMS-013_app_form_blank.png](bugs/screenshots/IPSMS-013_app_form_blank.png) · [IPSMS-013_app_form_push_ok_but_empty.png](bugs/screenshots/IPSMS-013_app_form_push_ok_but_empty.png) · [IPSMS-013_app_form_saved_local.png](bugs/screenshots/IPSMS-013_app_form_saved_local.png) · [IPSMS-013_web_no_forms.png](bugs/screenshots/IPSMS-013_web_no_forms.png)

#### [BUG-IPSMS-002](bugs/BUG-IPSMS-002.md) — Final Report tab shows stale values after Pull (overwrite risk)

- **Severity:** Medium · **Status:** Open · **Area:** iPad app — Safety Reports > Final Report · **Checklist row:** [IPSMS-016](checklists/74-ipad-safety-reports.md)

**Steps**

1. Report #2064 open in the app on the Final tab (summary "BETA TEST ONLY final summary from iPad").
2. On the website, change the Final Report summary to "...edited on website" and Save.
3. In the app, Pull while staying on the Final tab.

**Expected:** Final tab shows the website summary.

**Actual:** The local model gets the new value (SQLite closedDescription = "edited on website"), but the text box still shows the old "from iPad" text until you switch tabs and come back. Editing the stale box autosaves the old text over the website value.

**Cause:** `SafetyFinalReportSection.loadState()` runs on `.onAppear` and is guarded by `isLoaded`, so later report changes from Pull never reach the `@State` fields (closedDescription, final likelihood/consequence, hazard fields).

**Screenshots:** [IPSMS-016_app_final_after_tabswitch.png](bugs/screenshots/IPSMS-016_app_final_after_tabswitch.png) · [IPSMS-016_app_final_pulled.png](bugs/screenshots/IPSMS-016_app_final_pulled.png) · [IPSMS-016_web_final_after_reload.png](bugs/screenshots/IPSMS-016_web_final_after_reload.png)

#### [BUG-IPSMS-004](bugs/BUG-IPSMS-004.md) — Safety Report push says 'Successfully pushed' even if saving forms, deleting files or changing status fails

- **Severity:** Medium · **Status:** Open · **Area:** iPad app — Safety Reports > Push (SMSReportUploadService) · **Checklist row:** [IPSMS-009](checklists/74-ipad-safety-reports.md)

**Steps**

1. Source review of SMSReportUploadService.swift push path (about lines 156-178).
2. To reproduce live: push a report whose status change or form save the server rejects (for example a user without investigator access on that report).

**Expected:** Push reports which part failed and keeps that change pending for retry.

**Actual:** deleteDocument (file deletions), saveForms (form save/removal) and changeStatus are all called with `try?`, so server errors are discarded and the app still shows 'Successfully pushed to DataHangar Report #N'. The 'Step 11: Refresh from server' comment has no call behind it. This is part of why BUG-IPSMS-001 (forms lost) shows a success message. Found in source; the happy path works (file delete IPFILE-006, form removal IPFORM-006, status change IPPERM-080) - a live server-side failure was not reproduced.

**Cause:** SMSReportUploadService.swift: `try? await smsSync.deleteDocument`, `try? await smsSync.saveForms`, `try? await smsSync.changeStatus`.

#### [BUG-IPSMS-003](bugs/BUG-IPSMS-003.md) — Safety Report action 'Assign To' picker shows a blank person row

- **Severity:** Low · **Status:** Open · **Area:** iPad app — Safety Reports > Actions > New Action · **Checklist row:** [IPSMS-007](checklists/74-ipad-safety-reports.md)

**Steps**

1. Safety Reports > report #2064 > Actions > + New Action.
2. Open the Assign To picker.

**Expected:** Only named people are listed; records with no name are hidden or labelled.

**Actual:** A blank row appears under 'Unassigned' (report options people[0] = id 274 with an empty name). The same nameless person also appears in the website's personnel pickers, so the record itself is probably a server data-quality issue; the app should still filter or label it.

**Cause:** The picker lists every person from the report options without filtering empty names.

**Screenshots:** [IPSMS-007_app_action_assignee_picker.png](bugs/screenshots/IPSMS-007_app_action_assignee_picker.png)

### iPad communications and chat

#### [BUG-IPCHAT-001](bugs/BUG-IPCHAT-001.md) — Chat message typed while offline is discarded on send

- **Severity:** Medium · **Status:** Open · **Area:** - · **Checklist row:** [IPCHAT-010](checklists/75-ipad-comms-chat.md)

**Steps**

1. Comms > select a channel.
2. Make stresstest unreachable (host blackhole route; device otherwise online).
3. Type "BETA TEST ONLY offline message" and tap Send.

**Expected:** Message kept (pending bubble / outbox with retry), or input left intact with a quick "offline" error.

**Actual:** Input clears immediately; no pending bubble or offline indicator. About 60-70 s later: "Error Sending Message - The request timed out." The text is gone and must be retyped. The message never reached the server.

**Cause:** `CommsView.handleSend()` clears `messageText` and the pending image before `chatService.sendMessage`; the catch block only shows a popup. `DataHangarAPI` uses a 60 s request timeout.

**Screenshots:** [IPCHAT-010_app_offline_65s.png](bugs/screenshots/IPCHAT-010_app_offline_65s.png) · [IPCHAT-010_app_offline_after_send.png](bugs/screenshots/IPCHAT-010_app_offline_after_send.png) · [IPCHAT-010_app_offline_timeout_error.png](bugs/screenshots/IPCHAT-010_app_offline_timeout_error.png) · [IPCHAT-010_app_resend_online.png](bugs/screenshots/IPCHAT-010_app_resend_online.png)

### iPad calculator

#### [BUG-IPCALC-001](bugs/BUG-IPCALC-001.md) — Unit Converter: NM <-> Statute Miles conversion inverted; large values shown in scientific notation

- **Severity:** High · **Status:** Open · **Area:** iPad app — Calculator > Unit Converter (Distance) · **Checklist row:** [IPCALC-010](checklists/76-ipad-calculator.md)

**Steps**

1. Calculator > Unit Converter > Distance, Convert From = Nautical Miles (NM).
2. Enter 100.

**Expected:** Statute Miles = 115.08 mi (1 NM = 1.15078 mi). Meters 185,200 m; Feet 607,612 ft shown as plain numbers.

**Actual:** Statute Miles = **86.8974 mi** (that is the mi->NM figure). Meters shows `1.852e+05 m`, Feet `6.076e+05 ft`.

Reverse direction (100 mi -> NM) is also inverted per source (gives 115.08 NM instead of 86.90 NM).

**Cause:** `Views/Calculator/UnitConverterView.swift`, distance units:
```swift
ConvUnit(name: "Statute Miles", abbrev: "mi", toBase: { $0 * 1.852 / 1.60934 }, fromBase: { $0 * 1.60934 / 1.852 }),
```
Base unit is NM; the factors are swapped. Fix: `toBase: { $0 * 1.60934 / 1.852 }, fromBase: { $0 * 1.852 / 1.60934 }`.
Scientific notation comes from the result formatter (likely `%g`); use a grouped decimal format for large values.

**Screenshots:** [IPCALC-010_unit_nm_to_mi_wrong.png](bugs/screenshots/IPCALC-010_unit_nm_to_mi_wrong.png)

### iPad live tracking

#### [BUG-WEBTRK-001](bugs/BUG-WEBTRK-001.md) — Live tracking pings fail on stresstest - live_tracking table missing

- **Severity:** High · **Status:** Open · **Area:** Website / Live Tracking API · **Checklist row:** [IPTRK-003](checklists/77-ipad-live-tracking.md)

**Steps**

1. iPad app: Config > DataHangar > Live Tracking ON, interval 30s.
2. Open pushed flight #42914 > menu > Start Tracking (Simulator location Auckland, moving).
3. Leg toolbar tracking icon turns red; tap it.

**Expected:** Ping saved; aircraft appears on Active Flights > Live Tracking map.

**Actual:** Every ping gets an HTML "Error" page:

`exec_sql: Can't execute (INSERT INTO live_tracking (session_id, flight_id, person_id, lat, lng, altitude_m, speed_ms, heading_deg, accuracy_m, device_id, recorded_at) ...): DBD::mysql::st execute failed: Table 'stresstest.live_tracking' doesn't exist at /var/www/datahangar/DHLib/DHMysql.pm line 363.`

The map shows nothing. The error page shows SQL text, parameters and a server path to the client.

**Screenshots:** [IPTRK-003_app_tracking_error.png](bugs/screenshots/IPTRK-003_app_tracking_error.png) · [IPTRK-003_web_active_flights.png](bugs/screenshots/IPTRK-003_web_active_flights.png)

#### [BUG-IPTRK-002](bugs/BUG-IPTRK-002.md) — Live Tracking queue stores duplicate/stale pings; rejected pings are dropped

- **Severity:** Medium · **Status:** Open · **Area:** iPad app — Live Tracking · **Checklist row:** [IPTRK-006](checklists/77-ipad-live-tracking.md)

**Steps**

1. Start tracking on #42914 (30 s interval) with the device stationary.
2. Make stresstest unreachable (host blackhole route) for about 75 s.
3. Inspect UserDefaults lt_pendingPings.

**Expected:** One point per new fix, no stale fixes carried from an earlier session, and server-rejected pings either retried or reported.

**Actual:** - The queue holds 6–7 entries. Most are identical (same recorded_at 08:56:37.677Z, same lat/lng), because each timer tick re-sends lastKnownLocation even when there is no new fix.

- One queued entry is a fix from 08:52:55, taken in the previous session (before Stop and relaunch), and it now carries the new session_id.

- The queue drains only after a successful "Ok" ping. A non-"Ok" server response is never queued, so that position is lost.

- Stop Tracking does not clear lt_pendingPings (7 remained after Stop); they would be sent later under the stopped session id.

#### [BUG-IPTRK-001](bugs/BUG-IPTRK-001.md) — Live Tracking UI/state issues (raw HTML error, stale/global menu, no offline indicator)

- **Severity:** Low · **Status:** Open · **Area:** iPad app — Live Tracking · **Checklist row:** [IPTRK-003](checklists/77-ipad-live-tracking.md)

**Steps**


**Expected:** Server errors are shown as a short readable message (no raw HTML); while tracking is on, the flight menu shows Stop Tracking (not Start Tracking again) and the tracking state belongs to that flight; starting tracking asks for confirmation; the app shows when pings can't be sent (offline).

**Actual:** 1. Error modal shows the server's raw HTML ("Server returned: <!DOCTYPE html>..."). (LiveTrackingService.sendPing sets lastError to the first 200 chars of the response.)

2. After Start Tracking, the flight detail menu still says "Start Tracking" (FlightDetailView reads LiveTrackingService.shared.isActive without observing it). Tapping it again starts a new session ID.

3. The menu shows the global session state: flight #8884, which was not being tracked, showed "Stop Tracking" while #42914 was tracked. Tapping it would stop the other flight's session.

4. While offline, the toolbar icon stays green/active; network errors only set lastError.

5. No confirmation or toast after Start Tracking from the flight menu.

**Screenshots:** [IPTRK-002_menu_still_start.png](bugs/screenshots/IPTRK-002_menu_still_start.png) · [IPTRK-003_app_tracking_error.png](bugs/screenshots/IPTRK-003_app_tracking_error.png) · [IPTRK-006_offline_icon_green.png](bugs/screenshots/IPTRK-006_offline_icon_green.png) · [IPTRK-006_other_flight_shows_stop.png](bugs/screenshots/IPTRK-006_other_flight_shows_stop.png)

### iPad cross-cutting checks

#### [BUG-IPSYNC-001](bugs/BUG-IPSYNC-001.md) — Push silently overwrites website-side Notes edits

- **Severity:** Medium · **Status:** Open · **Area:** Flight sync / conflict handling · **Checklist row:** [IPOFF-005](checklists/78-ipad-cross-cutting.md)

**Steps**

1. On flight #42914, edit Notes on the website to WEBEDIT.
2. Make an offline Notes edit in the app.
3. Reconnect and push the app's flight changes.

**Expected:** The app detects the website edit and presents a conflict or otherwise prevents silently replacing the website value.

**Actual:** The push succeeds and replaces WEBEDIT with the app's offline Notes edit. No conflict is detected; the result is last-write-wins behavior.

**Cause:** No conflict detection during push; the stale local copy is sent as the latest value.

**Screenshots:** [IPOFF-005_push_after_reconnect.png](bugs/screenshots/IPOFF-005_push_after_reconnect.png) · [IPOFF-005_web_details_after_push.png](bugs/screenshots/IPOFF-005_web_details_after_push.png)

#### [BUG-IPUI-001](bugs/BUG-IPUI-001.md) — Hardware-keyboard focus leaks through sheets and keypads

- **Severity:** Medium · **Status:** Open · **Area:** iPad UI / keyboard focus · **Checklist row:** [IPXC-002](checklists/78-ipad-cross-cutting.md)

**Steps**

1. In a flight leg, enter NZAA in Departure and open the seat-assignment sheet.
2. Open Override Weight's custom numeric keypad and type 85 using a hardware keyboard.
3. Open the meter keypad and type while Notes had previously been active.
4. In a form, focus the textarea, tap a key-value field, and type using the hardware keyboard.

**Expected:** Hardware-keyboard input is directed only to the field or control in the active sheet, keypad, or form widget.

**Actual:** Typing goes into a field behind the sheet/keypad: Departure became NZAA8585, meter input was appended to Notes, and key-value field input was appended to the form textarea.

**Cause:** Results note that custom keypads do not resign the previous first responder.

**Screenshots:** [IPLEG-005_focus_leak_departure.png](bugs/screenshots/IPLEG-005_focus_leak_departure.png) · [IPXC-002_focus_leak_notes.png](bugs/screenshots/IPXC-002_focus_leak_notes.png) · [IPJSON-001_export.json](bugs/screenshots/IPJSON-001_export.json)

#### [BUG-IPOFF-001](bugs/BUG-IPOFF-001.md) — Offline launch and push block for about a minute before timing out

- **Severity:** Low · **Status:** Open · **Area:** Offline handling · **Checklist row:** [IPOFF-003](checklists/78-ipad-cross-cutting.md)

**Steps**

1. Make the DataHangar host unreachable while leaving the Simulator online.
2. Launch the app and wait for the sync attempt to finish.
3. While still offline, attempt to push a flight.

**Expected:** The app detects that it is offline and promptly explains that launch sync or push cannot proceed.

**Actual:** Launch displays a blocking Syncing Data screen for about 60 seconds before Authentication Error / The request timed out. A push displays Authenticating… for about 60 seconds before Push Failed / The request timed out.

**Cause:** No up-front reachability/offline check; launch auto-sync and push wait for the default ~60 s URLSession timeout before failing with 'The request timed out'.

**Screenshots:** [IPOFF-001_authenticating_spinner.png](bugs/screenshots/IPOFF-001_authenticating_spinner.png) · [IPOFF-001_push_timeout.png](bugs/screenshots/IPOFF-001_push_timeout.png) · [IPOFF-003_launch_sync_blocking.png](bugs/screenshots/IPOFF-003_launch_sync_blocking.png) · [IPOFF-003_launch_auth_error.png](bugs/screenshots/IPOFF-003_launch_auth_error.png)

#### [BUG-IPUI-003](bugs/BUG-IPUI-003.md) — Sparse VoiceOver labels and partial Dynamic Type support

- **Severity:** Low · **Status:** Open · **Area:** iPad app — cross-cutting accessibility · **Checklist row:** [IPUI-013](checklists/78-ipad-cross-cutting.md)

**Steps**


**Expected:** Every icon-only button and control has a VoiceOver label (and hint/value where useful), and all text, including segmented controls, titles, headers and buttons, scales with Dynamic Type and layouts use the extra width.

**Actual:** - Source: 23 `accessibilityLabel` uses vs 151 `Image(systemName:)`; no `accessibilityHint/Value/Hidden`. Icon-only toolbar buttons (settings gear, download, tracking, +, ⋯) will mostly be read by SF Symbol name or not at all.

- 87 fixed `.font(.system(size:))` uses. At Accessibility XXL text size, row titles/descriptions scale, but segmented controls (Theme, Time Format, Legs/Forms/Files/Details), section headers, nav titles, Done and Add Leg stay tiny; leg cards keep a fixed ~300pt width so text wraps heavily on a 13" screen.

- Live VoiceOver could not be exercised (simulator AX tree not reachable in this harness).

**Screenshots:** [IPUI-014_dyntype_axxxl_config.png](bugs/screenshots/IPUI-014_dyntype_axxxl_config.png) · [IPUI-015_dyntype_flight_list.png](bugs/screenshots/IPUI-015_dyntype_flight_list.png) · [IPUI-016_dyntype_flight_detail.png](bugs/screenshots/IPUI-016_dyntype_flight_detail.png)

### iPad permissions and end-to-end

#### [BUG-WEBCHAT-001](bugs/BUG-WEBCHAT-001.md) — Chat API used by the iPad app ignores the Chat permission (permission bypass)

- **Severity:** High · **Status:** Open · **Area:** Website / Chat API · **Checklist row:** [IPPERM-024](checklists/79-ipad-permissions-e2e.md)

**Steps**

1. Website, Settings and Tools > Access Manager > New User: "BETA TEST ONLY LowPerm" (username betalowperm), no permissions/roles/groups. Activate Login Access.
2. Website (incognito) log in as betalowperm > header Chat icon -> Access Denied (correct).
3. iPad app (fresh install) > Configuration > DataHangar: log in as betalowperm. Test Authentication succeeds; Sync All -> 6x "Access denied" (correct).
4. Comms tab -> channel `#beta-test-only-ipad-chat` listed with 17 unread; open it -> Service Account messages and image visible.
5. Send "BETA TEST ONLY lowperm message" -> delivered, attributed to BETA TEST ONLY LowPerm.

**Expected:** Chat API endpoints (channels list, messages, send, poll, image fetch, read tracking) return Access Denied for users without Chat permission, matching the website; app shows the same "Access denied" state it shows for Flights/Safety Reports.

**Actual:** Full read and write access to chat through the API.

**Screenshots:** [IPPERM-011_lowperm_sync_denied.png](bugs/screenshots/IPPERM-011_lowperm_sync_denied.png) · [IPPERM-016_lowperm_comms_channel_visible.png](bugs/screenshots/IPPERM-016_lowperm_comms_channel_visible.png) · [IPPERM-017_lowperm_comms_read.png](bugs/screenshots/IPPERM-017_lowperm_comms_read.png) · [IPPERM-018_lowperm_send_ok.png](bugs/screenshots/IPPERM-018_lowperm_send_ok.png) · [IPPERM-024_web_lowperm_chat_denied.png](bugs/screenshots/IPPERM-024_web_lowperm_chat_denied.png) · [IPPERM-025_web_shows_lowperm_message.png](bugs/screenshots/IPPERM-025_web_shows_lowperm_message.png)

#### [BUG-IPFL-004](bugs/BUG-IPFL-004.md) — Flight downloaded before aircraft sync keeps aircraft "None" forever; Pull never re-links; push fails with "(nil)"

- **Severity:** Medium · **Status:** Open · **Area:** iPad app, Flights (download/pull/push) · **Checklist row:** [IPPERM-067](checklists/79-ipad-permissions-e2e.md)

**Steps**

1. Log the app in as a user who cannot sync aircraft yet (no Resources permission), or download a flight before running Sync All.
2. Download BETA flight #42914 (ZK-HEL on the website).
3. Grant the user aircraft access (Resources + W&B Config Download) and run Sync All. Aircraft now sync.
4. Open #42914 and run Pull from Server.
5. Push the flight.

**Expected:** Pull (or Sync All) re-links the flight to ZK-HEL (`dh-<resourceId>`), and push works. If it can't, the message should say the aircraft isn't available on this iPad and how to fix it.

**Actual:** - The Aircraft field stays "None" and Category/Activity stay blank after Sync All and after Pull.

- Every push fails with "Push Failed: Could not push flight data to DataHangar. Aircraft configuration (nil) not found for this flight."

- The website still has ZK-HEL. Nothing was sent, so no server data was lost.

**Cause:** - `FlightSyncService.swift:129/142` sets `flight.aircraftId` from `aircraftStore.aircraft(id: "dh-\(serverFlight.resourceId)")` only on the first download.
- Pull (`~line 195`) reuses `localFlight.aircraftId` and never re-resolves it.
- `FlightUploadService.swift:41` and `FlightPayloadBuilder.swift:132` show the Swift `nil` text in the user-facing message.

**Screenshots:** [IPPERM-050_readonly_flight_details_missing_ref.png](bugs/screenshots/IPPERM-050_readonly_flight_details_missing_ref.png) · [IPPERM-052_readonly_push_nil_config.png](bugs/screenshots/IPPERM-052_readonly_push_nil_config.png) · [IPPERM-057_5perm_sync_3_denied.png](bugs/screenshots/IPPERM-057_5perm_sync_3_denied.png) · [IPPERM-066_push_nil_config_after_aircraft_sync.png](bugs/screenshots/IPPERM-066_push_nil_config_after_aircraft_sync.png)

#### [BUG-IPPERM-001](bugs/BUG-IPPERM-001.md) — App lets read-only users edit and push flights and only fails at the server, showing a raw "Error block Error" message

- **Severity:** Medium · **Status:** Open · **Area:** iPad app, Flights, permissions · **Checklist row:** [IPPERM-049](checklists/79-ipad-permissions-e2e.md)

**Steps**

1. Log in to the app as the read-only user and download flight #42914.
2. Edit Notes (Add Leg and all the fields are enabled too).
3. Set the aircraft if needed (see BUG-IPFL-004), then choose ... > Push to Server > Push.

**Expected:** The app should see that the user can't edit flights (the server already exposes per-user permissions, as Safety Reports do). It should then show the flight read-only, hide Add Leg and Push, or warn before any edits are made.

**Actual:** - Every edit control and Push stays enabled.

- The confirmation dialog appears, then the push fails with: "Push Failed - Could not push flight data to DataHangar. Error block Error Access Denied: You do not have permission to create or modify flights."

- The message includes raw markup text ("Error block Error").

- The local edit stays "needs push" forever. After a Pull it is silently kept and marked synced (BUG-IPSYNC-002).

**Screenshots:** [IPPERM-049_readonly_flight_editable.png](bugs/screenshots/IPPERM-049_readonly_flight_editable.png) · [IPPERM-068_readonly_push_confirm_zkhel.png](bugs/screenshots/IPPERM-068_readonly_push_confirm_zkhel.png) · [IPPERM-069_readonly_push_server_denied.png](bugs/screenshots/IPPERM-069_readonly_push_server_denied.png)

#### [BUG-IPSYNC-002](bugs/BUG-IPSYNC-002.md) — Pull from Server doesn't apply website Notes and can mark an unpushed local edit as synced

- **Severity:** Medium · **Status:** Open · **Area:** Flight sync / pull · **Checklist row:** [IPPERM-063](checklists/79-ipad-permissions-e2e.md)

**Steps**

1. Edit the Notes on website flight #42914 to WEBEDIT.
2. In the app, use Already Downloaded > Pull from Server (overwrites local changes).
3. Check the flight's Notes in the app.

**Expected:** The app replaces its stale Notes value with the website value WEBEDIT.

**Actual:** Pull from Server leaves the app's Notes unchanged. Retest 24/10/2026 (IPPERM-061/063): website #42914 Notes = 'BETA TEST ONLY OFFLINE EDIT'; the app had an unpushed local edit 'BETA TEST ONLY OFFLINE EDIT RO' (its push had failed). After Pull from Server the app still showed the local text but the badge changed to '#42,914 synced' and the needs-push flag was cleared, so the edit will never be sent and the app silently disagrees with the website. Pull is labelled 'overwrites local changes' but does not.

**Cause:** Not fully traced; Pull path in FlightSyncService.swift updates sync timestamps without replacing local flight-level fields.

**Screenshots:** [IPPERM-063_web_42914_notes_server.png](bugs/screenshots/IPPERM-063_web_42914_notes_server.png) · [IPPERM-064_app_42914_notes_RO_synced.png](bugs/screenshots/IPPERM-064_app_42914_notes_RO_synced.png)

## 7. What works

- Login, wrong-password handling and password masking in the debug log; Sync All of 21 aircraft, 44 personnel, 16 waypoints, 4 categories, 10 activities, 7 form templates and W&B master config Rev 3 - all matching the website.
- Flight created in the app and pushed as #42914: aircraft, route, PIC, times, notes, legs, meters, passengers, baggage and the auto-uploaded PDF all match the website.
- Weight and balance matches hand calculations and the website exactly (ZFW 733.8 kg @ 258.62/2.70, TOW 833.8 kg @ 259.70/-0.56, Within Limits).
- Midnight-crossing leg times, PDF export and JSON export.
- Offline edits are kept through force-quit and relaunch and push correctly after reconnecting.
- Safety Reports: list and details match (278 then 280 reports); report created in the app pushed as #2064; comments, actions, status changes, files and final report sync in both directions; file deletion and form removal work in both directions.
- Comms: channels, text messages, images and deletion sync both ways; new website messages appear in the app within about 3 seconds and new channels within about 30 seconds; per-user read tracking works.
- Live Tracking start/stop, interval setting and resume-after-relaunch prompt (server storage blocked, see BUG-WEBTRK-001).
- 10 of 11 calculators match hand calculations.
- Configuration: theme and 12/24-hour switching, 4-digit PIN gate (wrong PIN rejected, right PIN opens), aircraft Meters tab read-only and matching the website, personnel read-only and matching, waypoint coordinates matching.
- Layouts: iPad Pro 13-inch landscape, iPad mini portrait and landscape, empty states for Flights, Safety Reports and Comms.
- Permissions: the server denies Sync All, Flights and Safety Reports to a 0-permission user and the app shows 'Access denied' clearly; Write Own users see only their own reports and can create and push them; read-only flight pushes are rejected by the server and the website is unchanged; investigator access granted and removed per report flows to the app after Pull; revoking access gives 'Access denied' on Pull.

## 8. Not tested

- **Live Tracking positions reaching the website** (map, Active Flights, timestamps, altitude/speed/course, queue drain on success): blocked because stresstest has no `live_tracking` table (BUG-WEBTRK-001). Needs the table created, then a retest. Not checked whether production has the table.
- **Comms with a second non-admin website user** (unread counts on the website side, deleting your own message on the website): the test user has no Chat permission on the website. App side: unread counts and read tracking work for the second user.
- **Safety Report form surviving force-quit and relaunch:** not re-run separately; flight edits survived (same local store).
- **Physical iPad, real GPS, real network loss, Magic Keyboard:** Simulator only. The keyboard-leak bug was found with the Mac keyboard and is expected to affect hardware keyboards on iPad.
- **2FA accounts:** none available.
- **Unit tests:** the test target does not compile (BUG-IPSET-001), so no automated tests were run.

## 9. Decisions needed

- **Time zones:** flight and Safety Report times are saved as the iPad's local clock time with no time zone, and the server reads them as NZ time. Correct for iPads set to NZ time; an iPad set to another time zone records shifted times. Sunrise/Sunset in the Calculator also uses the iPad's time zone. Is NZ-only acceptable?
- **Deleting chat messages:** in the app only admins can delete messages, so users can't delete their own. Should non-admins be able to delete their own messages (and what does the website allow)?
- **Permission levels:** Resources and W&B Config Download only offer 'All Access' on the website, so a pilot who needs aircraft data in the app must be given full edit rights. Add read-only levels?
- **Aircraft and waypoint edits are device-only:** the app lets you edit server aircraft and waypoints, but changes never reach the website and Sync All silently reverts aircraft edits (BUG-IPAC-001, BUG-IPWPT-001). Make server fields read-only in the app, or sync them?
- **Cached data after access is revoked:** a user whose permission is removed keeps the reports already on the iPad, with no indication. Should the app clear or flag them?
- **Read-only users:** should the app hide or disable editing for users with read-only flight permission (BUG-IPPERM-001)?
- **Scope for Calculator and Comms:** treated what is built as the intended scope (no spec exists).

## 10. Other observations, candidates and info

Checklist rows marked N/A that are not bugs: candidates (possible issues not raised as bugs), info, decisions and not-tested notes.

| Row | Checklist | Note |
|---|---|---|
| IPREF-006 | [63](checklists/63-ipad-sync-reference-data.md) | Candidate: AUDIT All Widgets / BETA TEST ONLY Form sit under empty groups on website and app. Forms: 7 templates (AUDIT All Widgets, BETA TEST ONLY Form, QA Post-Flight Report, QA Pre-Flight Checklist, QA Annual Line Check, QA Equipment Issue, QA Hazard Observation); 5 groups detail: app form groups: AUDIT Forms[23 AUDIT All Widgets], BETA TEST ONLY Forms[24], QA Flight Forms[19 Post-Flight,18 Pre… |
| IPAC-008 | [64](checklists/64-ipad-aircraft-editor.md) | Candidate: untouched new-aircraft Cancel still asks Discard Changes. New Aircraft opened, nothing typed (only Save tapped -> validation), Cancel -> 'Discard Changes: You have unsaved changes' prompt even though form untouched -> minor UX note (false-positive dirty state; draft likely differs from initial). Discard confirms. Evidence [IPAC-008_discard_prompt_no_edits.png](../bugs/screenshots/IPAC-0… |
| IPWPT-001 | [65](checklists/65-ipad-personnel-waypoints.md) | Candidate: Waypoint count reconciled: local `aerodromes` = 16 records = 10 with coordinates + 6 name-only entries with blank lat/lon (BTQA, BTQC, NZAA, NZCH, NZWR, ZZZQ). Earlier "15" was before ZZZQ appeared (name-only entry, likely from a website flight route). NZAA/NZCH exist twice (proper airport + blank-coord duplicate) -> candidate data-quality/UX issue: picker may offer coordinate-less dupl… |
| IPFL-006 | [66](checklists/66-ipad-flights-list.md) | Candidate: Sync All reports Flight Custom Fields 0 while 1 field is stored and used. Website shows flight custom field "BETA TEST ONLY EFI" (Extra Information); Sync All said Flight Custom Fields 0 but app stored extraFlightInfoFields [id24 BETA TEST ONLY EFI] after download -> recheck Sync All count. Details tab: Flight Identity (Flight Name, Flight No 'Assigned by server' (empty though server id… |
| IPFL-002d | [66](checklists/66-ipad-flights-list.md) | Info: website behaviour (PIC added with 0 kg; website blocks save at 0 kg). Web Add Leg on #42915: leg auto-PIC Aaron Fisher, Personnel&Baggage 0.0 kg (PIC weight not applied), TOW 782 'Out of Limits'. Web obs: PIC added with 0 kg. - web Save blocked: 'Leg 1: Aaron Fisher has a seat weight of 0. Please enter a valid weight.' (good validation) - web: #42915 saved with leg NZAA->NZCH, PIC Aaron Fish… |
| IPFT-005 | [69](checklists/69-ipad-flight-times-meters.md) | Candidate: (candidate Low) Meter field: label 'Previous: 2,450.5' but validation error 'Value (0.1) < previous (2,450.7)' - inconsistent previous value (probably label uses aircraft startValue, validator adds flightPreviousReadings). Check DB. resolved: 'Previous' label actually 2,450.7 (matches aircraft.previousMeterReadings, last reading from downloaded flights), startValue 2450.5 is older basel… |
| IPSYNC-006 | [72](checklists/72-ipad-push-pull-sync.md) | Candidate: one-off empty Category/Activity/EFI after push #2, not reproduced. Earlier 'Category/Activity/EFI empty after push#2' not reproduced on push#3 (Solo/Charter/EFI persisted both directions). Probably push#2's update POST partially failed (forms_json die -> rollback on server). Keep as 'observed once'. |
| IPSMS-020 | [74](checklists/74-ipad-safety-reports.md) | Candidate: Source finding (SMSReportUploadService.swift ~L157-178): file deletions (deleteDocument), form save/remove (saveForms) and pending status change (changeStatus) are all called with try? — server errors are swallowed and the app still shows 'Successfully pushed'. Same root as BUG-IPSMS-001 (forms); also means a denied status change / file delete would report success. Verifying file delete… |
| IPCHAT-011 | [75](checklists/75-ipad-comms-chat.md) | Not tested: N/A Not tested: Comms unread counts / own-message delete with a second non-admin user. betalowperm has no Chat permission on the website (Access Denied) and is now inactive, so a website-side second user was not available; app-side source shows delete only for admins (CommsView contextMenu isAdmin). Decision: should non-admins delete their own messages? |
| IPCHAT-012 | [75](checklists/75-ipad-comms-chat.md) | Decision: N/A Decision: 'Load older messages' pagination — app loads latest page and offers older on demand; treated as expected pagination, not a defect. |
| IPUI-023 | [78](checklists/78-ipad-cross-cutting.md) | Decision: iPad mini fresh Flights empty state: 'No Flights' + Download button; toolbar (+, download, tracking) hidden until data exists -> note: cannot create a local flight before first sync/aircraft setup (likely by design; welcome popup points to Configuration). Evidence [IPUI-023_mini_flights_empty.png](../bugs/screenshots/IPUI-023_mini_flights_empty.png) |
| IPPERM-001 | [79](checklists/79-ipad-permissions-e2e.md) | Corrected by IPPERM-073..082: SafetyReportDetailView / SafetyFinalReportSection do use these flags. Source: SMSReportSyncService parses report permissions (investigator_access, reviewer_access, user_permission) into report.permissions, but no View reads them (grep Views: 0 uses) -> app shows edit/status/final-report controls regardless of user permission; enforcement relies on server rejecting. Li… |
| IPPERM-007 | [79](checklists/79-ipad-permissions-e2e.md) | Candidate (website): create dialog doesn't say new users start with Login Access Inactive. Cause: new user created with Login Access 'Inactive' (0 roles, 0 groups). Expected behaviour; minor website UX note - create dialog/toast doesn't say login is inactive. App's 'Invalid username or password' for inactive account is same as server - OK. Activating. Evidence [IPPERM-007_lowperm_inactive.png](../… |
| IPPERM-020 | [79](checklists/79-ipad-permissions-e2e.md) | Candidate: New Safety Report form opens before failing with Access denied (website blocks up front). Low-perm: '+' New Safety Report opens form but 'Load Failed: Could not load report options... Access denied.'; Report Type empty so required field cannot be filled. Form/Submit still shown (no upfront permission state). Checking website: can a 0-permission user file a safety report there? Evidence… |
| IPPERM-022 | [79](checklists/79-ipad-permissions-e2e.md) | Candidate (website): menus list all modules for a 0-permission user. Website as 0-perm: landing Dashboard -> 'Access Denied: You do not have permission to access the Dashboard feature'; menus still list all items (website-side UX: menus not filtered by permission). Evidence [IPPERM-022_web_lowperm_dashboard_denied.png](../bugs/screenshots/IPPERM-022_web_lowperm_dashboard_denied.png) |
| IPPERM-033 | [79](checklists/79-ipad-permissions-e2e.md) | Candidate: Local report detail: header 'Report #0' for unpushed report (minor - should say Local/Draft). Date Reported '24 Oct 2026, 09:49' appears to be UTC while Occurrence '02:48' is device-local (VM Pacific) - mixed timezones on same card (adds to SMS timezone candidate). Tabs Files/Comments/Actions/Final/Forms/History all shown to non-investigator. Pushing. Evidence [IPPERM-033_writeown_repor… |
| IPPERM-034 | [79](checklists/79-ipad-permissions-e2e.md) | Candidate: Write Own user push -> 'Successfully pushed to DataHangar Report #2065'. Submitted By now 'BETA TEST ONLY LowPerm'. Date Reported changed 09:49 (local copy, UTC) -> 22:50 (server, NZ) after push: app shows different timezone for same field before/after push (Low, add to SMS timezone candidate). Evidence [IPPERM-034_writeown_push_2065.png](../bugs/screenshots/IPPERM-034_writeown_push_206… |
| IPPERM-043 | [79](checklists/79-ipad-permissions-e2e.md) | Info: endpoint-to-permission mapping. App flight endpoints: download list = flightschedule_json (perm Flight Schedule #209); detail/push = flightdetails_json/addwaypoint/uploadfile/deletefile (perm Flight Details #214). Flight Details levels include 'Write and Locking'. Granting betalowperm Flight Schedule + Flight Details = Read Only All to test whether app lets a read-only user edit/push and how… |
| IPPERM-044 | [79](checklists/79-ipad-permissions-e2e.md) | Info: Flight Schedule permission levels (website model). Flight Schedule level list offers only All Access/Read Only All/Write Group/Read Only Group (no Own levels), unlike Flight Details. Selected Read Only All for both; saving. |
| IPPERM-053 | [79](checklists/79-ipad-permissions-e2e.md) | Candidate (website): Manage User Permissions modal closes on Escape/outside click without unsaved warning. Harness note: Escape / click outside closes Manage User Permissions modal without saving (no unsaved-change warning, nothing pending at the time). Re-opening to add aircraft resources read permission. |
| IPPERM-054 | [79](checklists/79-ipad-permissions-e2e.md) | Decision: Resources / W&B Config Download only offer All Access (no read-only level). Settings & Tools - Resources (#237) only offers 'All Access' level (no read-only option) - website permission-model note: a pilot needing aircraft data for the iPad app must be given full write on Resources. Granting All Access to betalowperm (test account) so the app can sync aircraft. |
| IPPERM-060 | [79](checklists/79-ipad-permissions-e2e.md) | Candidate: Website candidate (Low): Flight Schedule day view for 23 Oct 2026 shows banner 'You are viewing a future date' while server Local is 23:03 24/10/2026 (23 Oct is in the past). Evidence [IPPERM-059_web_future_date_banner_past_day.png](../bugs/screenshots/IPPERM-059_web_future_date_banner_past_day.png) |
| IPPERM-073 | [79](checklists/79-ipad-permissions-e2e.md) | Info: investigator/reviewer access is per-report assignment, not the global permission. After granting global Safety Report Investigator R/W All + app relaunch + report Pull: server still returns permissions investigator_access=false (local store {'investigatorAccess': False, 'reviewerAccess': False, 'userPermission':'WO'}); no 'Investigate' button. Hypothesis: investigator_access is per-report (a… |
| IPPERM-075 | [79](checklists/79-ipad-permissions-e2e.md) | Candidate (website data): case-variant duplicate person 'BETA TEST ONLY Lowperm'/'LowPerm'. Website Add Investigator picker lists both 'BETA TEST ONLY Lowperm' and 'BETA TEST ONLY LowPerm' (case-variant duplicate person; likely earlier test artifact - note for cleanup). Selecting 'LowPerm' (matches betalowperm display name). Evidence [IPPERM-075_web_investigator_picker_dup_lowperm.png](../bugs/scr… |
| IPPERM-076 | [79](checklists/79-ipad-permissions-e2e.md) | Candidate (website, Low): Add Investigator toast says 'Reviewer added successfully!'. Website: assigned BETA TEST ONLY LowPerm as Investigator on #2065; shown under Investigators, but toast says 'Reviewer added successfully!' (website wording bug, Low). Evidence [IPPERM-076_web_investigator_added_toast_says_reviewer.png](../bugs/screenshots/IPPERM-076_web_investigator_added_toast_says_reviewer.png… |
| IPPERM-085 | [79](checklists/79-ipad-permissions-e2e.md) | Decision: After revocation, app Safety Reports list still shows cached #2065 'synced' with no indication access was revoked (Low/product note). Evidence [IPPERM-085_app_revoked_cached_list.png](../bugs/screenshots/IPPERM-085_app_revoked_cached_list.png). Cleanup: deactivating betalowperm. Process note: Cleanup: betalowperm Login Access set Inactive (4 permissions remain: Flight Schedule RO, Flight… |
| IPE2E-001 | [79](checklists/79-ipad-permissions-e2e.md) | Candidate: N/A Not separately re-run: Safety Report form persistence across force-quit (flight offline edits survived force-quit in IPOFF; SMS uses the same Core Data store). |

## 11. Test data and cleanup

| Record | Where | State |
|---|---|---|
| Flight #42914 'BETA TEST ONLY NZAA-NZCH' (ZK-HEL) | Website + iPad Pro app | Kept for retests |
| Flight #42915 (website-created, Student PIC Aaron Fisher) | Website + app | Kept for retests (BUG-IPFL-002) |
| Safety Report #2064 'BETA TEST ONLY iPad SMS report' | Website + app | Closed; files and forms deleted during deletion tests |
| Safety Report #2065 'BETA TEST ONLY low perm report' | Website + iPad mini app | Under Investigation; investigator removed |
| Chat channel #beta-test-only-ipad-chat and BETA messages | Website + app | Kept |
| User betalowperm 'BETA TEST ONLY LowPerm' | Access Manager | Login Access set Inactive; 4 permissions remain (Flight Schedule RO, Flight Details RO, Resources, W&B Config Download) |
| Duplicate person 'BETA TEST ONLY Lowperm' (case variant) | Personnel | Pre-existing from an earlier session; not removed |
| Aircraft ZK-FLY empty weight 600 kg edit | iPad app only | Reverted by Sync All (BUG-IPAC-001) |
| Configuration PIN | iPad app | Cleared after testing |

## 12. Files

- Plan: [IPAD_SWIFT_AUDIT_PLAN.md](IPAD_SWIFT_AUDIT_PLAN.md)
- Checklists: `checklists/60-ipad-*.md` to `checklists/79-ipad-*.md` (every check, result and notes)
- Bugs: `bugs/BUG-IP*.md`, `bugs/BUG-WEBCHAT-001.md`, `bugs/BUG-WEBTRK-001.md`; screenshots in `bugs/screenshots/`
- All bugs (website and iPad): [STATUS.md](STATUS.md) and `bugs.json`
- This report is generated from bugs.json and the checklists; regenerate after retests.
