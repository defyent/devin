# BUG-FAD-005: Flight and Duty 'View as Date' defaults to the UTC date instead of the local date

| Field | Value |
|---|---|
| Checklist row | `FAD-003` in `checklists/16-flight-and-duty.md` |
| Module | Flight and Duty |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Do this when the local date differs from UTC (e.g. after 00:00 NZ time)
2. Flight Safety > Flight and Duty > View as Date

## Expected
Date box shows today's local date (22/10/2026 at Local 00:19 22/10/2026).

## Actual
Date box shows 21/10/2026 (the UTC date); the hidden value is '2026-10-21 11:19:37', i.e. UTC time.

## Evidence
- Screenshot: `screenshots/BUG-FAD-005-1.png`
- Console / network errors: none

## Suspected cause (optional)
The View as Date picker is initialised from the server/UTC time rather than the Settings > Time Zone local time.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
