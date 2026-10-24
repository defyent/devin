# Maintenance Portal

- **Checklist ID prefix:** `MX`
- **Guide section:** §11.10
- **Where:** Only via direct/admin link — record if no UI path
- **Permission:** Maintenance = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| MX-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | BLOCKED |  | Blocked by MX-001 (no UI path). |
| MX-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | BLOCKED |  | Blocked by MX-001 (no UI path). |
| MX-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | BLOCKED |  | Blocked by MX-001 (no UI path). |
| MX-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | BLOCKED |  | Blocked by MX-001 (no UI path). |
| MX-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | BLOCKED |  | Blocked by MX-001 (no UI path). |
| MX-S06 | Low-permission account | Access Denied or read-only as per permission | BLOCKED |  | Blocked by MX-001 (no UI path). |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| MX-001 | UI path exists? | If not, BLOCKED (no ?action=) and ask Jon | BLOCKED |  | No UI path: no Maintenance link in the sidebar or in Settings and Tools (Service Account). Not opened via ?action= per the rules; asked Jon. |
| MX-002 | Fleet Status carousel/grid; aircraft page tabs | Inspections, Defects & MEL, Work Orders, Components, ADs & SBs, Logbook | BLOCKED |  | Blocked by MX-001 (no UI path). |
| MX-003 | Planning & Forecast Due List filters/horizons; Fleet Utilisation | Correct | BLOCKED |  | Blocked by MX-001 (no UI path). |
| MX-004 | Work Orders kanban/table, statuses, RII sign-off, labour/parts, release, draft invoice | Works | BLOCKED |  | Blocked by MX-001 (no UI path). |
| MX-005 | Defects & MEL, Airworthiness, Store & Purchasing, Build & Templates, Tooling, Personnel, Commercial, Reports | Each area loads and core create/edit works | BLOCKED |  | Blocked by MX-001 (no UI path). |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
