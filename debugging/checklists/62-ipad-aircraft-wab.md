# iPad: Configuration: Aircraft and W&B

- **Checklist ID prefix:** `IPAC`
- **Guide section:** `ipad/IPAD_AUDIT_PLAN.md`
- **Where:** Config > Aircraft
- **Frontend cross-reference:** 34-settings-resources, 35-settings-wab
- **Viewport:** P 820x1180 and L 1180x820 unless stated
- **Tester:**  
- **Date / app build / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID. Sync rows: put the frontend record checked in Notes.

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPAC-001 | Synced aircraft list = frontend Settings > Resources active aircraft (count, regos, types) | Same set | TODO |  |  |
| IPAC-002 | Linked aircraft fields (empty weight, max weight, arms) = frontend W&B config | Same values | TODO |  |  |
| IPAC-003 | Add aircraft (+) locally: required fields, Save, appears in list | Created | TODO |  |  |
| IPAC-004 | Edit / Duplicate Aircraft / Delete Aircraft (confirm) | Works | TODO |  |  |
| IPAC-005 | Empty Weight & Balance, Cockpit Stations, Cabin, Removable Seats, Removable Equipment (in BEW) | Values saved, moments recomputed | TODO |  |  |
| IPAC-006 | Equipment profiles: Add New Profile, Set as Default, Reorder Profiles, Override Values, Clear Overrides | Works | TODO |  |  |
| IPAC-007 | Fuel stations, Fuel Burn Sequence, Fuel Weight Unit (L / US Gal), 'Exceeds max fuel' | Correct | TODO |  |  |
| IPAC-008 | Meters: Meter Type, Start Value, Decimal Places, Logs Against, Summed/Cumulative | Correct | TODO |  |  |
| IPAC-009 | External Load slots, Allow External Load | Correct | TODO |  |  |
| IPAC-010 | W&B graphs (Add New Graph) render envelope; CG point inside/outside flagged | Correct | TODO |  |  |
| IPAC-011 | Re-sync after changing aircraft on frontend: updates, no duplicate aircraft | Updated, no dupes | TODO |  |  |
| IPAC-012 | Local edits to a linked aircraft vs next Sync All Data (overwritten? warned?) | Defined behaviour, user warned | TODO |  |  |
| IPAC-013 | wabMasterOutOfSync / revision change on frontend detected on iPad | Detected | TODO |  |  |

## Test data created

| Record | Where | Cleaned up |
|---|---|---|
