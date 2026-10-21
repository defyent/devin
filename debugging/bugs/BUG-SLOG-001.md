# BUG-SLOG-001: Activity Log: no page Help (?), and dates show as "22 Oct 2026, 02:51 am"

| Field | Value |
|---|---|
| Checklist row | `SLOG-S04` in `checklists/47-settings-activitylog.md` |
| Module | Settings: Activity Log |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Time Zone settings: DD/MM/YYYY, 24-hour.
2. Settings and Tools > Logs > Activity Log.
3. Look for a Help (?) button, and read the Date/Time column.

## Expected
There is a page Help (?). Dates follow the settings, e.g. "22/10/2026 02:51" and "21/10/2026 22:35".

## Actual
There is no Help (?). Dates show as "22 Oct 2026, 02:51 am" and "21 Oct 2026, 10:35 pm" (12-hour, month names). The local time itself is correct.

## Evidence
- Screenshot: `screenshots/BUG-SLOG-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
The activity log formats the date itself (with a locale date string) and ignores the Time Zone date and time format settings.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
