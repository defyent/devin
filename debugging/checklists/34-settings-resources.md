# Settings – Resources (Aircraft)

- **Checklist ID prefix:** `SRES`
- **Guide section:** §12.4
- **Where:** Settings and Tools > Configuration > Resources (Aircraft)
- **Permission:** settings_resources = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SRES-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SRES-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SRES-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SRES-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SRES-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SRES-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SRES-001 | Search; filter Status, Group, Aircraft/Non-Aircraft; columns | Correct | TODO | | |
| SRES-002 | Add Resource BETA TEST ONLY (all fields) | Saved; required fields validated | TODO | | |
| SRES-003 | Is Aircraft / Status Inactive | Affects Flight Details Aircraft dropdown and Schedule columns | TODO | | |
| SRES-004 | Flight/Engine time Calculated From + show toggle | 'Flight Time Calculation Changed' warning; legs show right fields | TODO | | |
| SRES-005 | Time Inputs toggles; locked 'Required — used to calculate time' | Correct | TODO | | |
| SRES-006 | User Group Assignments add/remove | Schedule visibility for WG/RG | TODO | | |
| SRES-007 | Meter Assignments: start value, show; remove meter with data | Removal refused | TODO | | |
| SRES-008 | Duplicate | New Callsign/Registration required | TODO | | |
| SRES-009 | Delete resource with flights | Refused; suggest Inactive | TODO | | |
| SRES-010 | Resource Categories / Aircraft Types CRUD; delete in use | Refused when in use | TODO | | |
| SRES-011 | Meters CRUD: unit, decimals, type, logs against, required to complete; Flights Using This Meter | Correct | TODO | | |
| SRES-012 | Units: Global Weight KG/Lbs | Weights everywhere convert | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
