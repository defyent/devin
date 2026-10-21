# BUG-SINT-002: Google Calendar Sync Status: flight dates show as 2024-01-01 07:55 instead of DD/MM/YYYY

| Field | Value |
|---|---|
| Checklist row | `SINT-S04` in `checklists/46-settings-integrations.md` |
| Module | Settings: Google Calendar Sync |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Time Zone settings: DD/MM/YYYY.
2. Settings and Tools > Configuration > Google Calendar Sync.
3. Expand Pending Sync.

## Expected
Flight times follow Settings > Time Zone, e.g. "01/01/2024 07:55".

## Actual
Each pending flight shows "2024-01-01 07:55".

## Evidence
- Screenshot: `screenshots/BUG-SINT-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
settings_googlecalendar_get_status returns start_time as "YYYY-MM-DD HH:MM", and the page shows it as it is.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
