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
| SLP-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SLP-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SLP-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SLP-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SLP-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SLP-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SLP-001 | Exercises CRUD | Saved | TODO | | |
| SLP-002 | Lesson Plans CRUD; delete in use | Set Inactive instead | TODO | | |
| SLP-003 | Lessons: hours, notes, check flight, Exercise Configuration dual/solo, filter | Saved; Lesson tab on flights reflects | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
