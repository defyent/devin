# BUG-DSH-004: Dashboard: My Flights and On Duty open on the UTC date, not today's local date

| Field | Value |
|---|---|
| Checklist row | `DSH-005` in `checklists/05-dashboard.md` |
| Module | Dashboard |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Time zone is Pacific/Auckland. Do this between local 00:00 and 13:00 (NZDT), when the UTC date is still the day before.
2. Log in as BETA TEST ONLY Second, who is PIC of flight #42910 on 22/10/2026.
3. Open Dashboard.

## Expected
My Flights and On Duty show today's local date (Thu 22/10/2026), including flight #42910.

## Actual
At local 10:38 on 22/10/2026 (UTC 21:38 on 21/10), the Dashboard showed 'My Flights for Wed, Oct 21, 2026: No flights scheduled for this day' and 'On Duty for Wed, Oct 21, 2026'. You have to click > to see today's flight. The dates are also in US format. Retest 22/10/2026 (v2.0.111): fixed.

## Evidence
- Screenshot: `screenshots/BUG-DSH-004-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
