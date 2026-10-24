# BUG-IPSET-001: Unit-test target does not compile

| Field | Value |
|---|---|
| Checklist row | `IPSET-001` |
| Module | Unit tests |
| Severity | Medium |
| Environment | Simulator iPad Pro 13" M5, iOS 26.5 |
| App version | 1.0.13 (Build 46) |
| DataHangar version | v2.0.123 (`https://stresstest.datahangar.net`) |
| Status | Open |
| Found / session | 2026-10-24, https://app.devin.ai/sessions/8b79cff4b7ea4af2989164dd937fd4e4 |

## Steps to reproduce
1. Attempt to compile the app's unit-test target.
2. TBD: exact build command and target invocation.

## Expected
The unit-test target compiles.

## Actual
Compilation fails due to duplicate `FlightTimeEngineTests` declarations (`WeightBalanceEngineTests.swift:196` and `FlightTimeEngineTests.swift`) and stale call signatures, including missing `pic`, `copilot`, `crew`, `passengers`, `takeoffFuel`, and `decimalPlaces` arguments. Renaming the duplicate still leaves about 12 compile errors.

## Evidence
- TBD — test output is recorded outside `evidence/`; no matching evidence file is present.

## Suspected cause (optional)
Duplicate test-class declaration and test calls that have not been updated to current signatures.

## Test data involved
Unit-test target; exact build command TBD.

## Related
TBD
