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

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| POP-01 | High | Fixed (retested 17/10) | Popup closed when you click inside and drag out. All 18 retestable popups fixed on 17/10/2026 (see section 13); Chat Error no longer appears |
| POP-02 | Medium | Open (external) | Esc doesn't close any popup |
| POP-03 | Medium | Open (external) | Outside click closes some popups but not others. After the POP-01 fix, Risk Matrix Delete Matrix no longer closes on an outside click or Esc, while the other fixed popups still close on an outside click |
| POP-04 | Medium | Open (external) | The same kind of popup behaves differently on different pages (History, Delete confirms) |
| POP-05 | Low | Open (external) | About 6 different popup implementations/classes are in use |
| POP-06 | Low | Open (external) | Close button wording varies (Got it / OK / Close / Cancel / x) |
| POP-07 | Medium | Open (external) | Scroll Wheel date picker only closes via "Set" (no Cancel, outside click or Esc) and covers the fields below it |
| POP-08 | Medium | Open (external) | Validation errors appear in a generic "Error" popup, not inline (Exam Instances Send, Safety Report Create Action) (see also FORM-21) |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
