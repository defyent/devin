# Cross-cutting: popups/modals

- **Checklist ID prefix:** `POP`
- **Guide section:** §4
- **Where:** Every popup in every module
- **Permission:** n/a
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| POP-001 | Drag-out: mousedown inside popup, release outside | Popup stays open (recurring bug — check EVERY popup) | TODO | | |
| POP-002 | Click on backdrop (true outside click) | Closes only where documented; never loses unsaved input silently | TODO | | |
| POP-003 | Esc | Closes | TODO | | |
| POP-004 | × and Cancel | Close; unsaved changes prompt where applicable | TODO | | |
| POP-005 | Error while inside popup | Popup closes first, error modal readable | TODO | | |
| POP-006 | Stacked popups (popup opens popup) | Correct z-order; closing child keeps parent | TODO | | |
| POP-007 | Long content | Scrolls inside popup; buttons reachable | TODO | | |
| POP-008 | Mobile width | Popup fits screen | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
