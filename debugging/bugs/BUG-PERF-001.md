# BUG-PERF-001: 'Performance' debug timing panel shown on every page, including to non-admin users

| Field | Value |
|---|---|
| Checklist row | `PERF-001` in `checklists/95-performance.md` |
| Module | All modules (debug panel) |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Log in as any user (also BETA TEST ONLY Lowperm with one permission)
2. Open My Account or Access Manager

## Expected
Debug timing panel hidden for normal users (only when debug is switched on for an admin), or at least off by default.

## Actual
Bottom-right 'Performance' panel lists internal step timings (Permission Check, Load People, Load Permissions, Total Time...). Covers content and toasts, exposes internals.

## Evidence
- Screenshot: `screenshots/BUG-PERF-001-1.png`, `screenshots/BUG-PERF-001-2.png`
- Console / network errors: none

## Suspected cause (optional)
Debug config ('Check Debug Config') is enabled site-wide on stresstest, or the check does not consider the user's role. Confirm with Jon whether this is intentional on staging.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
