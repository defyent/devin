# BUG-SRES-001: Resources: the meter "Last:" dates show as YYYY-MM-DD instead of the Time Zone date format

| Field | Value |
|---|---|
| Checklist row | `SRES-S04` in `checklists/34-settings-resources.md` |
| Module | Settings: Resources (Aircraft) |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings > Time Zone date format is DD/MM/YYYY.
2. Settings and Tools > Configuration > Resources (Aircraft).
3. Look at the Meters column for C172-02 (ZK-AIR).

## Expected
Flight Hours Last: 3102.7 (09/05/2026)

## Actual
Flight Hours Last: 3102.7 (2026-05-09). Every "Last:" meter date on the page is in ISO format.

## Evidence
- Screenshot: `screenshots/BUG-SRES-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
The raw database date is shown without going through the shared date formatter.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
