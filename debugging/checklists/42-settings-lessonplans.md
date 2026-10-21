# Settings – Lesson Plans

- **Checklist ID prefix:** `SLP`
- **Guide section:** §12.12
- **Where:** Settings and Tools > Training > Lesson Plans
- **Permission:** settings_lessonplans = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SLP-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Lesson Plans opens settings_lessonplans (tabs: Lesson Plans, Lessons, Exercises; "No lesson plans configured"), with no console errors. |
| SLP-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-SLP-001 | No page Help (?), and Escape does not close Add Exercise. |
| SLP-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside Add Exercise to outside it: it stays open. |
| SLP-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SLP-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SLP-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SLP-001 | Exercises CRUD | Saved | FAIL | BUG-SLP-002 | Empty name gives "Please enter an exercise name" (good). But exercises are never sent to the server (code has "TODO: Implement API integration"): edit makes a duplicate, and everything is gone after leaving the page. |
| SLP-002 | Lesson Plans CRUD; delete in use | Set Inactive instead | TODO | | |
| SLP-003 | Lessons: hours, notes, check flight, Exercise Configuration dual/solo, filter | Saved; Lesson tab on flights reflects | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
