# BUG-TS-002: Timesheet Approval: status filter 'Unsigned' shows 'No personnel found' although everyone has unsigned days

| Field | Value |
|---|---|
| Checklist row | `TS-001` in `checklists/15-timesheets-leave.md` |
| Module | Timesheets |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > Settings and Tools > Timesheets (October 2026)
2. Note e.g. Aaron Foster Unsigned 10
3. Set the status filter to Unsigned

## Expected
Everyone with unsigned days is listed (110 people).

## Actual
'No personnel found'. All Status lists 110 people, all with Unsigned counts above 0.

## Evidence
- Screenshot: `screenshots/BUG-TS-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
filterPersonnel() in timesheets/index.js skips days with no timesheet_id ('if (!day.timesheet_id) return false') and then compares day.status to the filter value, but unsigned days have no timesheet record, so Unsigned can never match. The counts use other status names too ('draft'/'submitted'/'denied'), so Pending/Rejected may also never match.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
