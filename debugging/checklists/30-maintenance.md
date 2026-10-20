# Maintenance Portal

- **Checklist ID prefix:** `MX`
- **Guide section:** §11.10
- **Where:** Only via direct/admin link — record if no UI path
- **Permission:** Maintenance = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| MX-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| MX-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| MX-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| MX-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| MX-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| MX-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| MX-001 | UI path exists? | If not, BLOCKED (no ?action=) and ask Jon | TODO | | |
| MX-002 | Fleet Status carousel/grid; aircraft page tabs | Inspections, Defects & MEL, Work Orders, Components, ADs & SBs, Logbook | TODO | | |
| MX-003 | Planning & Forecast Due List filters/horizons; Fleet Utilisation | Correct | TODO | | |
| MX-004 | Work Orders kanban/table, statuses, RII sign-off, labour/parts, release, draft invoice | Works | TODO | | |
| MX-005 | Defects & MEL, Airworthiness, Store & Purchasing, Build & Templates, Tooling, Personnel, Commercial, Reports | Each area loads and core create/edit works | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
