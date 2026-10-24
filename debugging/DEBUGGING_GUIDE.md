# DataHangar debugging guide

How to test DataHangar systematically against `DataHangar_Frontend_User_Guide.md` (the "guide") and turn failures into fixable bug reports.

## 1. Ground rules
1. **Test site:** https://stresstest.datahangar.net — throwaway data; add/edit/delete freely.
2. **Name all created records `BETA TEST ONLY …`** and list them in each checklist's *Test data created* table.
3. **Click through the UI like a user.** Never load modules with `?action=…` URLs. If something has no UI path, mark the row `BLOCKED` and say so.
4. **The guide is the spec.** Expected = what the guide says. If the app and the guide disagree, log it and note "guide or app?" — do not assume either is right.
5. **Clear cache / hard reload** before each session and before every retest (some modules don't version their assets).
6. **Restore settings** you change (especially Settings > Time Zone, Flight Schedule colours, DFR filtering).
7. **Not bugs:** flight times exceeding booking Start/End times; things the guide lists as deliberate (admin explicit level wins, users can't be deleted, copy/paste blocked with roster violations on).
8. Jon logs in through the Desktop tab; never store passwords in this repo.

## 2. Order of work
1. `00-setup-and-accounts` — version, accounts per permission level, baseline settings, DevTools open.
2. `01`–`03` — login, shell, common conventions (these find bugs that affect every module).
3. `04`–`30` — modules in menu order. Each starts with the **Standard checks** block.
4. `31`–`47` — settings pages; verify each setting's *effect* in the module it drives (see guide §6 dependency map).
5. `90`–`95` — cross-cutting sweeps (permissions per level, every popup, date formats, mobile, icons, performance).
6. `99` — end-to-end workflows last, as a regression pass.

Within a checklist: work top to bottom, fill `Result` immediately, don't batch.

## 3. Per-check method
1. Read the guide section referenced in the checklist header.
2. Perform the check; watch Console + Network + the Performance panel.
3. Compare against **Expected**.
4. Record `PASS` / `FAIL` / `BLOCKED` (say what blocks it) / `N/A` (say why).
5. For `FAIL`: screenshot (full window), create the bug file, put the Bug ID in the row.
6. Also check the **standard traps** in every popup and form:
   - drag-out: mousedown inside popup, release outside → must not close;
   - Esc / × / Cancel with unsaved changes;
   - native `alert()`/`confirm()` must never appear;
   - empty submit, too-long input, special characters (`' " < > &`, emoji, Māori macrons `ā`);
   - double-click on Save (duplicate records?);
   - dates in the org format.

## 4. IDs
- **Checklist rows:** `<PREFIX>-<NNN>` (module checks) and `<PREFIX>-S<NN>` (standard checks). Prefixes are listed in `STATUS.md` (Progress by checklist).
- **Bugs:** `BUG-<PREFIX>-<NNN>`, numbered per prefix in the order found (e.g. `BUG-FS-001`). Jon can reply per ID.
- **Screenshots:** `bugs/screenshots/BUG-<PREFIX>-<NNN>-<n>.png`.
- **External audit IDs** (`FORM-NN`, `POP-NN`, `DATE-NN`, `VIS-NN`, `UX-NN`, `ICON-NN`, `CHAT-NN`, …) from `external-audits/` are kept as-is and listed in `STATUS.md` (External audit issues); Jon can reply with either kind of ID.

## 5. Severity
| Severity | Meaning | Examples |
|---|---|---|
| **Critical** | Data loss/corruption, security/permission bypass, app unusable | RO user can save; wrong flight deleted; login broken |
| **High** | Core workflow blocked, wrong numbers in safety/ops data | Can't complete a flight; F&D totals wrong; SAR timer wrong |
| **Medium** | Feature broken with workaround; validation missing | Filter ignores a field; popup closes on drag-out |
| **Low** | Minor functional glitch | Sort wrong on one column; toast text wrong |
| **UI** | Visual/consistency/wording | Icon mismatch, typo, misaligned layout |

## 6. Evidence standard for a bug file
Steps from the menu, expected (with guide §), actual (exact on-screen text), account + level, version, width, screenshot, console/network errors, test data involved. One bug per file; link duplicates instead of merging.

## 7. Reporting cadence
- After each checklist, update `bugs.json` and run `tools/mkstatus.py` to regenerate `STATUS.md`.
- At the end of each session: attach a consolidated report (all bugs found, severity, screenshots) and a test-data cleanup list, and say clearly that the run is finished.

## 8. For the bug-fixing session
1. Read the handover file in `fixit-handovers/` and the linked bug files.
2. Code lives in `defyent/code`: modules are top-level folders with a frontend and `perl/DH<Module>.pm`; routing in `mod_perl/index.pl`; shell, menu and shared popup code in `main/` (`main/index.js`). Note there are several differing copies of `mysql.pm`.
3. Fix in priority order (Critical → UI). Keep edits minimal; bump `?v=` on changed assets.
4. Reply per Bug ID with the fix summary and PR link; set status `Fixed (deployed)` once Jon deploys.
5. The tester session then retests the linked checklist rows and marks `Verified` / `Reopened`.

## Icons

All icons in every DataHangar module must come from the self-hosted folder `/templates2/main/icons/` (SVG files). This applies to all icons, not just the sidebar.

- Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other CDN.
- If an icon you need doesn't exist, add the SVG to `/templates2/main/icons/` and use it from there. Keep the naming style: `<name>-outline-rounded.svg`, or `<name>-rounded.svg` for filled icons.
- Use the same icon for the same action everywhere (see UI-001).
- When testing, any icon loaded from somewhere else is a UI FAIL under ICON-01.

Icons in the folder on 22/10/2026:

- `badge-outline-rounded.svg`
- `bar-chart-rounded.svg`
- `calendar-month-outline-rounded.svg`
- `dashboard-outline-rounded.svg`
- `description-outline-rounded.svg`
- `dynamic-form-outline-rounded.svg`
- `event-note-outline-rounded.svg`
- `flight-rounded.svg`
- `flight-takeoff-rounded.svg`
- `folder-open-outline-rounded.svg`
- `group-outline-rounded.svg`
- `headset-mic-outline-rounded.svg`
- `health-and-safety-outline-rounded.svg`
- `notifications-outline-rounded.svg`
- `report-outline-rounded.svg`
- `schedule-outline-rounded.svg`
- `settings-outline-rounded.svg`
- `task-outline-rounded.svg`
- `tune-rounded.svg`
- `verified-outline-rounded.svg`
- `warning-outline-rounded.svg`
