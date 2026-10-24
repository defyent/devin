# iPad: Calculator

- **Checklist ID prefix:** `IPCAL`
- **Guide section:** `ipad/IPAD_AUDIT_PLAN.md`
- **Where:** Calculator tab
- **Frontend cross-reference:** -
- **Viewport:** P 820x1180 and L 1180x820 unless stated
- **Tester:**  
- **Date / app build / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID. Sync rows: put the frontend record checked in Notes.

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPCAL-001 | Standard Calculator: operations, divide by zero, chaining | Correct | TODO |  |  |
| IPCAL-002 | Unit Converter: every unit pair vs reference | Correct | TODO |  |  |
| IPCAL-003 | True Airspeed vs E6B reference | Within 1 kt | TODO |  |  |
| IPCAL-004 | Density Altitude / Pressure Altitude vs ICAO formula | Within 10 ft | TODO |  |  |
| IPCAL-005 | Wind Correction / Crosswind Component / Steady Wind / Gust vs reference | Correct | TODO |  |  |
| IPCAL-006 | Speed / Distance / Time: 'Enter any two values', 'Leave one field empty to solve for it' | Solves | TODO |  |  |
| IPCAL-007 | Fuel Calculator and Descent Planner vs reference | Correct | TODO |  |  |
| IPCAL-008 | Sunrise / Sunset for NZAA and NZQN on a known date | Within 1 min | TODO |  |  |
| IPCAL-009 | Weight & Balance calculator matches flight W&B | Match | TODO |  |  |
| IPCAL-010 | Invalid input (letters, negatives, empty) handled | No NaN shown | TODO |  |  |

## Test data created

| Record | Where | Cleaned up |
|---|---|---|
