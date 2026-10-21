# BUG-PD-007: Personnel Details > Recency: 'Days Until Expiry' and status don't match the Last Conducted date

| Field | Value |
|---|---|
| Checklist row | `PD-021` in `checklists/12-personnel-details.md` |
| Module | Personnel Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. All Personnel > Ethan Abbott > Recency and Renewals tab
2. Look at the Pilot Licenses Recencies rows (today 21/10/2026)

## Expected
Days match the dates, e.g. Day Landings last conducted 03/02/2026 with a 90-day window expired about 170 days ago (260 days since last conducted), and an expired item shows Expired.

## Actual
Day Landings: Last Conducted 03/02/2026, '462 days ago', status Caution, count 0/0 in 90 days. Instrument Approaches: 26/07/2025, '447 days ago', Caution, 0/0 in 180 days. Night Landings: 11/03/2026, '245 days ago', Caution. None of these numbers match the dates, and items long past their window show Caution, not Expired. PIC Hours / Total Flight Hours show Expired with no days value.

## Evidence
- Screenshot: `screenshots/BUG-PD-007-1.png`
- Console / network errors: none

## Suspected cause (optional)
Needs a check against the recency rules; a 0/0 requirement may be treated as Caution, and the days value may come from a different date than Last Conducted.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
