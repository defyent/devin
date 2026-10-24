# iPad setup and install

- **Checklist ID prefix:** `IPSET`
- **Guide section:** `debugging/IPAD_SWIFT_AUDIT_PLAN.md` §3
- **Where:** iPad app — Install, first launch, welcome modal, auto-sync overlay + Skip, icons/display name, unit-test baseline
- **Permission:** Admin / Service Account unless a different permission level is identified in the row notes
- **Tester:** Devin
- **Date / DataHangar version:** 24/10/2026 / iPad DataHangar Flight 1.0.13 (46) on iOS 26.5 Simulator; stresstest v2.0.123
- **Account / level used:** Service Account unless a different account is identified in the row notes

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPSET-001 | Unit tests: FAIL BUG-IPSET-001 test target doesn't compile (dup class FlightTimeEngineTests in WeightBalanceEngineTests.swift:196 + FlightTimeEngineTests.swift; stale signatures: missing… | TBD (not recorded) | FAIL | BUG-IPSET-001 | L3: Unit tests: FAIL BUG-IPSET-001 test target doesn't compile (dup class FlightTimeEngineTests in WeightBalanceEngineTests.swift:196 + FlightTimeEngineTests.swift; stale signatures: missing pic/copilot/crew/passengers/takeoffFuel, decimalPlaces). Renaming dup still leaves ~12 compile errors. |
| IPSET-002 | First launch welcome modal Go to Configuration / Maybe Later: PASS | TBD (not recorded) | PASS |  | L4: First launch welcome modal Go to Configuration / Maybe Later: PASS |
| IPSET-003 | Version shown in Config footer: "Version 1.0.13 (Build 46)" PASS | TBD (not recorded) | PASS |  | L5: Version shown in Config footer: "Version 1.0.13 (Build 46)" PASS |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
