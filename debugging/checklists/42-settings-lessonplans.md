# Settings – Lesson Plans

- **Checklist ID prefix:** `SLP`
- **Guide section:** §12.12
- **Where:** Settings and Tools > Training > Lesson Plans
- **Permission:** settings_lessonplans = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SLP-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Lesson Plans opens settings_lessonplans (tabs: Lesson Plans, Lessons, Exercises; "No lesson plans configured"), with no console errors. |
| SLP-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-SLP-001 | No page Help (?), and Escape does not close Add Exercise. |
| SLP-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside Add Exercise to outside it: it stays open. |
| SLP-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | N/A |  | No dates or times on this page. |
| SLP-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | 390 px: no page overflow, tabs become a dropdown, lessons show as cards and are readable. |
| SLP-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Settings and Tools shows Access Denied (System Settings). |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SLP-001 | Exercises CRUD | Saved | FAIL | BUG-SLP-002 | Empty name gives "Please enter an exercise name" (good). But exercises are never sent to the server (code has "TODO: Implement API integration"): edit makes a duplicate, and everything is gone after leaving the page. |
| SLP-002 | Lesson Plans CRUD; delete in use | Set Inactive instead | PASS |  | Add/edit Lesson Plan saved to the server (settings_lessonplans_save "Ok:14") and still there after leaving the page. Deleting a plan that has a lesson: server replies HAS_LESSONS:1, and the app offers "Cannot Delete ... make it inactive instead?". OK sets it Inactive ("Lesson plan set to inactive"). |
| SLP-003 | Lessons: hours, notes, check flight, Exercise Configuration dual/solo, filter | Saved; Lesson tab on flights reflects | FAIL | BUG-SLP-003 | Add Lesson: empty save gives "Please fill in all required fields". Hours, notes and Check Flight are saved and load back in edit. But Solo -1 is accepted (BUG-SLP-003). Exercise Configuration can't be tested because exercises can't be saved (BUG-SLP-002). Lesson tab on flights not checked: no student/lesson flight on stresstest (see 07 blocked rows). |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |


**Cleanup (42):** test lesson (id 65) and lesson plan "BETA TEST ONLY LP2" (id 14) deleted. Test exercises were never saved to the server (BUG-SLP-002), so there was nothing to clean up. Lesson Plans, Lessons and Exercises are all empty again, as they were.
