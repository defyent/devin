# BUG-SMS-002: New Safety Report: Event Date/Time defaults to the UTC date and time, not local

| Field | Value |
|---|---|
| Checklist row | `SMS-S04` in `checklists/19-safety-reports.md` |
| Module | Safety Reports |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. At a time when UTC and local dates differ (e.g. local 00:37 22/10/2026, UTC 11:37 21/10/2026)
2. Flight Safety > Safety Reports > New Report
3. Look at Event Date/Time

## Expected
Defaults to the local date and time (22/10/2026 00:37), as set in Settings > Time Zone.

## Actual
Defaults to 21/10/2026 11:37, the UTC date and time. A report saved without changing it is dated 13 hours early. Same issue as BUG-FS-001 and BUG-FAD-005.

## Evidence
- Screenshot: `screenshots/BUG-SMS-002-1.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
