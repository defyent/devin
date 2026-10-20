# Session setup, accounts and baseline

- **Checklist ID prefix:** `SET`
- **Guide section:** §1, §7, §15.1
- **Where:** n/a
- **Permission:** n/a
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SET-001 | Record DataHangar version from the top bar (e.g. v2.0.111) in TRACKER.md | Version noted | TODO | | |
| SET-002 | Clear browser cache / hard reload before starting (modules without ?v= on assets serve stale JS) | Fresh assets loaded | TODO | | |
| SET-003 | Record the test account name, roles (Admin/Customer/Crew/Staff/Student) and groups | Recorded in TRACKER.md | TODO | | |
| SET-004 | Confirm with Jon which extra test accounts exist per permission level (A, RA, WG, RG, WO, RO, WL) | Account-to-level map recorded; missing levels listed as BLOCKED | TODO | | |
| SET-005 | Record current Settings > Time Zone values (zone, date format, time format, picker type) before changing anything | Original values recorded so they can be restored | TODO | | |
| SET-006 | Record the staging aircraft (expected ZK-HDY/HLO/HQO/JET/NFL) and whether each is Active / Is Aircraft | Fleet baseline recorded | TODO | | |
| SET-007 | Open DevTools Console + Network tabs and keep them open for the run | JS errors and failed requests are visible | TODO | | |
| SET-008 | Agree the test-data naming prefix: every created record starts with `BETA TEST ONLY` | All test data is identifiable for cleanup | TODO | | |
| SET-009 | Note the Performance timing panel (bottom right); record any server timing > 500 ms as a PERF finding | Timings captured | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
