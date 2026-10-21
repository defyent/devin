# BUG-STZ-001: Time Zone settings: the Example preview shows UTC, not the selected time zone

| Field | Value |
|---|---|
| Checklist row | `STZ-S04` in `checklists/33-settings-timezone.md` |
| Module | Settings: Time Zone |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Configuration > Time Zone (time zone is Pacific/Auckland).
2. Look at the Example preview (Date & Time, Date Only, Time Only).

## Expected
The preview shows the current Pacific/Auckland date and time (22/10/2026 02:16, the same as the header's Local clock).

## Actual
The preview shows 21/10/2026 13:16, which is UTC (the same as the header's UTC clock). So the page that sets the time zone shows the wrong local time. This is the same UTC default problem as BUG-FS-001, BUG-SMS-002 and BUG-FBLD-002.

## Evidence
- Screenshot: `screenshots/BUG-STZ-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
The preview pickers are given new Date() (the browser's time, which is UTC here) instead of the time in the configured zone.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
