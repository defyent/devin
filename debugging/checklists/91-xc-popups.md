# Cross-cutting: popups/modals

- **Checklist ID prefix:** `POP`
- **Guide section:** §4
- **Where:** Every popup in every module
- **Permission:** n/a
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| POP-001 | Drag-out: mousedown inside popup, release outside | Popup stays open (recurring bug — check EVERY popup) | PASS |  | Every popup I tested stays open after a drag-out (mousedown inside, release outside), across checklists 04 to 47: e.g. DFR Manage Columns, F&D popups, Inspections and Google Calendar Add, Access Manager. The 17/10 fix holds. |
| POP-002 | Click on backdrop (true outside click) | Closes only where documented; never loses unsaved input silently | FAIL | BUG-POP-004 | Outside click is inconsistent. It closes Help, Flight Schedule View Details, Personnel History, Support New Ticket (wiping what you typed, BUG-SUP-001) and others. It does nothing on Form Builder, Google Calendar Add and many settings popups. See the 14 bugs that mention outside click (BUG-AF-003, BUG-FBLD-001, BUG-SINT-001...).. Retest (v2.0.117): the flightschedule Double Booking / Flight Alerts popup (#fad-modal) closes with Esc |
| POP-003 | Esc | Closes | FAIL | BUG-POP-001 | Escape closes only page Help on a few pages. It does nothing on almost every other popup: 38 bugs mention it (BUG-POP-001, BUG-POP-004, BUG-FS-002, BUG-PD-005, BUG-TS-005 ... BUG-SINS-001, BUG-SINT-001). |
| POP-004 | × and Cancel | Close; unsaved changes prompt where applicable | PASS |  | The x and Cancel buttons close the popup wherever they are shown. Personnel PDF Options has no x (BUG-PD-005). |
| POP-005 | Error while inside popup | Popup closes first, error modal readable | FAIL | BUG-TS-006 | An error inside a popup often closes the popup and loses the input: wrong colour in Add Leave Type (BUG-TS-006), wrong password on the signature (BUG-PD-014). Roster Builder error messages never show because openErrorModal throws (BUG-RB-005). |
| POP-006 | Stacked popups (popup opens popup) | Correct z-order; closing child keeps parent | FAIL | BUG-SMS-001 | Stacked popups: Escape on the Confidential/Anonymous (?) inside New Safety Report closes the whole form and loses the input (BUG-SMS-001). Error popups opened over a form need OK before the form can be used again. |
| POP-007 | Long content | Scrolls inside popup; buttons reachable | PASS |  | Long content scrolls inside the popup: DFR Notes full text, Google Calendar Setup Instructions, the Help popups and Exam Instances. |
| POP-008 | Mobile width | Popup fits screen | PASS |  | At 390 px the Flight Details Help popup fits inside the screen (left 9 px, right 366 px), scrolls inside and keeps Got it! visible (shot mob_popup). Earlier mobile checks also found the module popups usable. |

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
