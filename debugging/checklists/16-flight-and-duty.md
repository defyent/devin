# Flight and Duty

- **Checklist ID prefix:** `FAD`
- **Guide section:** §10.1
- **Where:** Flight Safety > Flight and Duty
- **Permission:** Flight and Duty A/RG/RO
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FAD-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| FAD-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| FAD-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| FAD-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| FAD-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| FAD-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FAD-001 | Rows | One per person in groups with Show Group in Flight and Duty | TODO | | |
| FAD-002 | Columns | One per FRMS flight-time and duty-time rule period; OK/Caution/Warning colours vs thresholds | TODO | | |
| FAD-003 | View Date | Figures recalculated as at date | TODO | | |
| FAD-004 | Search / Filter by Group | Work | TODO | | |
| FAD-005 | Click flight time value | Contributing flights list with all columns | TODO | | |
| FAD-006 | Click duty value | Duty Time Details | TODO | | |
| FAD-007 | Seeded violations | Resolutions Required / Roster Violations shown | TODO | | |
| FAD-008 | Performance (150 staff, FRMS calc) | < 500 ms server time | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
