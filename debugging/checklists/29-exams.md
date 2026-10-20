# Exam Builder, Exam Editor, Exam Instances

- **Checklist ID prefix:** `EXM`
- **Guide section:** §11.9, §12.15
- **Where:** Settings and Tools > Training
- **Permission:** Exam Builder = A; settings_examinstances = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| EXM-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| EXM-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| EXM-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| EXM-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| EXM-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| EXM-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| EXM-001 | Add Exam Group / Exam; delete | Works | TODO | | |
| EXM-002 | Create Draft > Approve; delete draft; revision history | Works | TODO | | |
| EXM-003 | Link/unlink user groups | Works | TODO | | |
| EXM-004 | Add Question of every type (10 types) | Each saves and previews | TODO | | |
| EXM-005 | Question Groups add/edit/delete; Question Settings | Works | TODO | | |
| EXM-006 | Reorder questions drag | Persists | TODO | | |
| EXM-007 | Exam Configuration: Pass Rate, selection mode, Save | Saved | TODO | | |
| EXM-008 | Assign Exam: All / Random (entire / per group), Unique / Same, Individual / Usergroup | Confirmation; instances created | TODO | | |
| EXM-009 | Browse Instances / Batches; remove/delete; add person to batch | Works | TODO | | |
| EXM-010 | Assigned exam on Personnel > Exams and Dashboard > Exams | Appears; take and score | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
