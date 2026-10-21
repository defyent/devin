# BUG-SINS-002: Inspection Notifications: a meter inspection on an aircraft at 0.0 hours is never Overdue, and negative meter values are accepted

| Field | Value |
|---|---|
| Checklist row | `SINS-002` in `checklists/45-settings-inspections.md` |
| Module | Settings: Inspection Notifications |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Maintenance > Inspection Notifications > Add Inspection.
2. Resource: BETA TEST ONLY R (meter 0.0). Trigger: Flight Hours. Meter: -5. Save.
3. Look at the new row.

## Expected
Meter values below 0 are rejected. If the trigger text says the inspection is overdue, the Status says Overdue too.

## Actual
-5 is saved. The row then says "0.0 / -5.0 (5.0 overdue)" but the Status is PENDING. Any aircraft whose current meter reading is 0 can never show Overdue.

## Evidence
- Screenshot: `screenshots/BUG-SINS-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
In calculateOverdueStatus() (templates2/settings_inspections/index.js), `if (!record.meter || !record.current_meter_reading) return false;` treats a 0 reading (and a 0 meter value) as missing. #inspectionMeter has no min, and the server does not range-check the value.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
