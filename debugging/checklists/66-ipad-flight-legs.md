# iPad: Flight: legs, times, meters, fuel

- **Checklist ID prefix:** `IPLEG`
- **Guide section:** `ipad/IPAD_AUDIT_PLAN.md`
- **Where:** Flight > Legs / Details
- **Frontend cross-reference:** 07-flight-details, 92-xc-dates-timezones
- **Viewport:** P 820x1180 and L 1180x820 unless stated
- **Tester:**  
- **Date / app build / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID. Sync rows: put the frontend record checked in Notes.

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPLEG-001 | Downloaded legs = frontend Legs tab (dep/dest, scheduled and actual times, meters, fuel) | Match | TODO |  |  |
| IPLEG-002 | New Flight: Select Aircraft, date, activity, category; 'Required Field Missing' | Validated | TODO |  |  |
| IPLEG-003 | Add Leg / Delete Leg / Delete Flight Leg confirm | Works | TODO |  |  |
| IPLEG-004 | Route & Times: Standard Time Picker HH:MM and HHMM entry, invalid times rejected | Validated | TODO |  |  |
| IPLEG-005 | Local vs UTC display; site TZ Pacific/Auckland incl. DST change days (27/09, 05/04) | Correct | TODO |  |  |
| IPLEG-006 | Nearby Aerodromes 'Now' / Detect nearby departure/destination (needs GPS: native) | Suggests within proximity | TODO |  |  |
| IPLEG-007 | Time Totals / Time Breakdown / Flight Total: correct sums across legs and midnight | Correct | TODO |  |  |
| IPLEG-008 | Meter Totals: previous readings = list_previous_meter_readings from frontend | Correct | TODO |  |  |
| IPLEG-009 | Missing Scheduled Times warning | Shown | TODO |  |  |
| IPLEG-010 | Extra Flight Info fields (e.g. BETA TEST ONLY EFI) shown and editable | Shown | TODO |  |  |
| IPLEG-011 | Flight Identity / Details: customer, authorised by, followers, lesson plans | Match frontend | TODO |  |  |
| IPLEG-012 | Special characters, emoji, very long notes | Saved intact | TODO |  |  |

## Test data created

| Record | Where | Cleaned up |
|---|---|---|
