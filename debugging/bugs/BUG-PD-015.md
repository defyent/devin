# BUG-PD-015: Flight & Duty Analysis popup: title date is YYYY-MM-DD and Escape doesn't close it

| Field | Value |
|---|---|
| Checklist row | `PD-016` in `checklists/12-personnel-details.md` |
| Module | Personnel Details |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. All Personnel > Ethan Abbott > Timesheets (October 2026)
2. On 01 Thu click the Flight & Duty Info (F&D) icon
3. Read the popup title, then press Escape

## Expected
Title date follows Settings > Time Zone (DD/MM/YYYY, e.g. 01/10/2026). Escape closes the popup.

## Actual
Title reads 'Flight & Duty Analysis for 2026-10-01'. Escape does nothing; only the x closes it. The rest-advice text also uses a different style ('6:00 AM on Friday, October 2, 2026') from the 24-hour setting.

## Evidence
- Screenshot: `screenshots/BUG-PD-015-1.png`
- Console / network errors: none

## Suspected cause (optional)
Popup builds the title from the raw ISO data-date and the rest text with a hard-coded en-US format instead of the shared date/time formatter.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
