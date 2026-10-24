# BUG-PD-018: Request Leave: Start and End Date default to the UTC date, not today's local date

| Field | Value |
|---|---|
| Checklist row | `PD-015` in `checklists/12-personnel-details.md` |
| Module | Personnel Details |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Time zone is Pacific/Auckland. Do this when the UTC date is still the day before (local 00:00-13:00 in NZDT).
2. Log in as a user with Timesheets own access (BETA TEST ONLY Second).
3. My Account > Timesheets > Request Leave.

## Expected
Start Date and End Date default to today's local date (22/10/2026).

## Actual
At local 10:21 on 22/10/2026 (UTC 21:21 on 21/10), both dates showed 21/10/2026. The hidden values were '2026-10-21 21:21:23' (UTC time). Unless you change them, the leave is requested for the wrong day. It's the same UTC-default problem as BUG-FD-007 and BUG-SMS-002.

## Evidence
- Screenshot: `screenshots/BUG-PD-018-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
