# BUG-SINS-003: Inspection Notifications: trigger date shows as 2026-10-01, Add Inspection defaults to the UTC date, and the overdue day count is one day short

| Field | Value |
|---|---|
| Checklist row | `SINS-S04` in `checklists/45-settings-inspections.md` |
| Module | Settings: Inspection Notifications |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Time Zone settings: Pacific/Auckland, DD/MM/YYYY.
2. Early in the local day (22/10 here, 21/10 in UTC), open Add Inspection and pick the Date trigger.
3. Save with date 01/10/2026 and look at the Trigger column.

## Expected
The date picker starts on the local date, 22/10/2026. The trigger shows "01/10/2026 (21 days overdue)".

## Actual
The date picker starts on 21/10/2026, the UTC date. A past date shows "2026-10-01 (20 days overdue)" when it is 21 days locally, and the date format ignores the setting. Future dates count correctly ("2026-12-31 (70 days)").

## Evidence
- Screenshot: `screenshots/BUG-SINS-003-1.png`, `screenshots/BUG-SINS-003-2.png`
- Console / network errors: none

## Suspected cause (optional)
The server writes the trigger text with an ISO date. Its overdue count is one short, probably because it uses the UTC date or truncates the part day. The client defaults the date picker with new Date() and does not use the configured timezone.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
