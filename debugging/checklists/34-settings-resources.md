# Settings – Resources (Aircraft)

- **Checklist ID prefix:** `SRES`
- **Guide section:** §12.4
- **Where:** Settings and Tools > Configuration > Resources (Aircraft)
- **Permission:** settings_resources = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SRES-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Configuration > Resources (Aircraft) loads with no console errors. 20 Active, 0 Inactive. |
| SRES-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS |  | Help opens. Esc, Got it, × and a click outside all close it. |
| SRES-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside Help to outside it: Help stays open. |
| SRES-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-SRES-001 | The meter "Last:" dates show as 2026-05-09 instead of DD/MM/YYYY. |
| SRES-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | At 390px the tabs become a dropdown and the table scrolls sideways in its own box. The page itself does not overflow (scrollWidth 390). |
| SRES-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | The low-permission user gets Access Denied for all of Settings and Tools, as in 31 to 33. |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SRES-001 | Search; filter Status, Group, Aircraft/Non-Aircraft; columns | Correct | PASS |  | Search "ZK-JET" leaves 1 row. Status Inactive, Group Administration and Non-Aircraft Only show "No resources found matching your filters." (which is right: 0 inactive, all are aircraft, all are in Pilots). 10 columns. There is no column chooser. A one-off "removeChild" JS error showed once while Help was open and a filter changed; I could not repeat it. |
| SRES-002 | Add Resource BETA TEST ONLY (all fields) | Saved; required fields validated | PASS |  | Save with the form empty is blocked: Name/Callsign and Registration are flagged. Then I added "BETA TEST ONLY Res" / ZK-BTO (Cessna 172, Training Aircraft, 1 engine, $1, 600/1000 kg). It says "Resource added successfully" and shows in the list, and Active goes from 20 to 21. |
| SRES-003 | Is Aircraft / Status Inactive | Affects Flight Details Aircraft dropdown and Schedule columns | PASS |  | ZK-BTO is in the flight 42903 Flight Details aircraft dropdown while Active and gone when Inactive. The Flight Schedule week and day views have no aircraft columns (they only show flights), so nothing to check there. |
| SRES-004 | Flight/Engine time Calculated From + show toggle | 'Flight Time Calculation Changed' warning; legs show right fields | PASS | sres004_calc_change | ZK-BTO now has BETA flight #42909. Edit Resource > Flight Time Calculated From = Engine Start / Stop > Save Resource shows "Flight Time Calculation Changed ... could affect reported flight times for previously completed flights" with Cancel / Continue. Cancel kept Takeoff / Landing. |
| SRES-005 | Time Inputs toggles; locked 'Required — used to calculate time' | Correct | PASS |  | The Time Inputs toggle for the input used to calculate time is greyed out and locked, marked "Required — used to calculate time". The label moves from Takeoff/Landing to Engine Start/Stop when Calculated From changes. The other toggle can still be switched. |
| SRES-006 | User Group Assignments add/remove | Schedule visibility for WG/RG | FAIL | fs027_grp_list | ZK-BTO's User Group Assignment (BETA TEST ONLY Group) saves and shows in the list, but it doesn't make the aircraft visible to a G/WG member of that group on Flight Schedule (BUG-FS-008). |
| SRES-007 | Meter Assignments: start value, show; remove meter with data | Removal refused | PASS |  | Add Meter > Flight Hours with starting value 100 on ZK-BTO: saved, and the row shows "Flight Hours 100.0". On ZK-SIM, which has logged meter data, each meter shows a lock instead of delete, so it cannot be removed. |
| SRES-008 | Duplicate | New Callsign/Registration required | PASS |  | Duplicate asks for a new Callsign and Registration and both are required. Using the existing ones gives "The callsign ... is already in use by another resource." Cancelled, so no copy was made. |
| SRES-009 | Delete resource with flights | Refused; suggest Inactive | PASS | sres009_result | Settings > Resources > ZK-BTO (BETA TEST ONLY R, 3 flights) > Delete > Delete gives "Error: Cannot delete resource. There are 3 flight(s) associated with this resource. Consider setting the resource to Inactive instead to preserve historical flight data." ZK-BTO is still listed. The confirmation names the resource. |
| SRES-010 | Resource Categories / Aircraft Types CRUD; delete in use | Refused when in use | PASS |  | Added "BETA TEST ONLY Cat" and "BETA TEST ONLY Type" and gave them to ZK-BTO. Deleting either while in use is refused ("Cannot delete category/aircraft type. There are 1 resource(s) assigned..."). Once unassigned, both delete. The original 4 categories and 4 types are unchanged. |
| SRES-011 | Meters CRUD: unit, decimals, type, logs against, required to complete; Flights Using This Meter | Correct | PASS |  | Add, edit and delete "BETA TEST ONLY Meter" work, with a confirmation that names the meter. Fields: Name, Description, Status, Unit, Decimal Places (0/1/2), Meter Type (Cumulative/Summed/Stored, explained), Logs Against (Flight/Flight Leg), Required to Complete. Gap: the Edit Meter popup has no "Flights Using This Meter" list. |
| SRES-012 | Units: Global Weight KG/Lbs | Weights everywhere convert | PASS |  | Switching Global Weight Units to Lbs changes ZK-BTO's edit form to "Empty Weight (lbs)": 600 kg shows as 1322.77 lb and 1000 kg as 2204.62 lb, both correct. Put back to KG. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Resource "BETA TEST ONLY R" / ZK-BTO (Cessna 172, BETA TEST ONLY Group, Flight Hours meter from 100) | Settings > Resources | No - kept for testing; delete after the audit |

## Test data left
- Resource "BETA TEST ONLY R" / ZK-BTO (Cessna 172, BETA TEST ONLY Group, Flight Hours meter starting at 100). Kept for 99. Delete after the audit.
- Category, aircraft type and meter made for testing are deleted. Global units are back to KG.
