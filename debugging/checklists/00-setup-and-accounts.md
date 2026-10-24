# Session setup, accounts and baseline

- **Checklist ID prefix:** `SET`
- **Guide section:** §1, §7, §15.1
- **Where:** n/a
- **Permission:** n/a
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SET-001 | Record DataHangar version from the top bar (e.g. v2.0.111) in STATUS.md | Version noted | PASS |  | v2.0.111 (21/10/2026) |
| SET-002 | Clear browser cache / hard reload before starting (modules without ?v= on assets serve stale JS) | Fresh assets loaded | PASS |  | Reloaded before the run; cache cleared again before retests |
| SET-003 | Record the test account name, roles (Admin/Customer/Crew/Staff/Student) and groups | Recorded in STATUS.md | PASS |  | Service Account (username datahangar), group Pilots, admin |
| SET-004 | Confirm with Jon which extra test accounts exist per permission level (A, RA, WG, RG, WO, RO, WL) | Account-to-level map recorded; missing levels listed as BLOCKED | PASS | perm010_groups | Test accounts per level: Service Account = A (admin). BETA TEST ONLY Lowperm = RA/G/WG/WO/WL, set one at a time in checklist 90. BETA TEST ONLY Grpuser (#277) = group levels G/RG/WG, member of BETA TEST ONLY Group. BETA TEST ONLY Second (#278) = RO/WO plus A on Support, Time Sheets, System Settings, Active Flights and Access Manager WA. Every level now has an account. |
| SET-005 | Record current Settings > Time Zone values (zone, date format, time format, picker type) before changing anything | Original values recorded so they can be restored | PASS |  | Pacific/Auckland, DD/MM/YYYY, 24-hour HH:mm, Type-In Fields |
| SET-006 | Record the staging aircraft (expected ZK-HDY/HLO/HQO/JET/NFL) and whether each is Active / Is Aircraft | Fleet baseline recorded | PASS |  | Fleet differs from old notes: 20 active aircraft (ZK-JET/JRA/JST/FLY/AIR/SKY/SLK/SUN/SIG/SIM/DIA/WAR/WAX/WLD/HEL/HLO/RAV/RVN/RTB/RTN), 0 inactive |
| SET-007 | Open DevTools Console + Network tabs and keep them open for the run | JS errors and failed requests are visible | PASS |  | Console, page errors and HTTP >= 400 captured via CDP for the whole run |
| SET-008 | Agree the test-data naming prefix: every created record starts with `BETA TEST ONLY` | All test data is identifiable for cleanup | PASS |  | Prefix BETA TEST ONLY |
| SET-009 | Note the Performance timing panel (bottom right); record any server timing > 500 ms as a PERF finding | Timings captured | PASS |  | Panel visible; Dashboard server timings all < 100 ms |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
