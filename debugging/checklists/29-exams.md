# Exam Builder, Exam Editor, Exam Instances

- **Checklist ID prefix:** `EXM`
- **Guide section:** §11.9, §12.15
- **Where:** Settings and Tools > Training
- **Permission:** Exam Builder = A; settings_examinstances = A
- **Tester:** Devin
- **Date / DataHangar version:** 2026-10-21 / v2.0.111
- **Account / level used:** Service Account (datahangar); betatest_low for S06/010

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| EXM-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Training > Exam Builder loads (1 group 'Aviation Theory', 10 exams), no console errors |
| EXM-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-EXM-001 | No page Help (?) on Exam Builder. Add Group: Escape does nothing; outside click closes |
| EXM-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Add Group popup stays open after mousedown in the name box and release outside |
| EXM-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-EXM-002 | Created column shows 'Oct 22, 2026' / 'May 11, 2026' |
| EXM-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | FAIL | BUG-EXM-005 | At 390px the exam table is squeezed and the pills, icons and dates overlap |
| EXM-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Settings and Tools shows 'Error Access Denied: ... System Settings feature', so Exam Builder can't be reached |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| EXM-001 | Add Exam Group / Exam; delete | Works | FAIL | BUG-EXM-008 | Add Group and Add Exam work. Delete exam and Delete Group (after the exam had a graded instance) both fail with no message; error only in the console. |
| EXM-002 | Create Draft > Approve; delete draft; revision history | Works | PASS |  | Create Draft confirms and adds a DRAFT row; Approve Draft confirms (optional revision notes) -> 'Draft approved and promoted to master', Rev 1 -> Rev 2; Revision History lists Rev 2 / datahangar / date; Delete Draft confirms, master unchanged |
| EXM-003 | Link/unlink user groups | Works | FAIL | BUG-EXM-004 | No User Groups row / Add User Group button on any exam group; createUsergroupBadges() is never called |
| EXM-004 | Add Question of every type (10 types) | Each saves and previews | PASS | BUG-EXM-003 | All 10 types (Multiple Choice, Multi-Response, Sequence, True/False, Short Answer, Essay, Fill in Blank, Matching, Select from Lists, Hotspot) save ('Question saved successfully') and open in the editor/read-only view. Hotspot saves with no image and no warning. Read Only view still shows edit controls (BUG-EXM-003) |
| EXM-005 | Question Groups add/edit/delete; Question Settings | Works | PASS |  | Question group: Add ('Group added successfully'), rename ('Group updated'), move a question in via Question Settings (Enabled / Points / Group, 'Question settings saved'), delete asks 'delete ... and move its 1 question(s) to ungrouped?' and Ungrouped goes back to 10. Escape doesn't close Add Group (BUG-EXM-001) |
| EXM-006 | Reorder questions drag | Persists | PASS |  | Dragged question 2 above question 1: 'Question reordered successfully'; new order kept after leaving and reopening the draft |
| EXM-007 | Exam Configuration: Pass Rate, selection mode, Save | Saved | PASS |  | Configure Exam: Pass Rate 70->80, selection modes All / Random from entire exam / Random from each group, per-question enable list. 'Exam configuration saved'; 80 kept on reopen |
| EXM-008 | Assign Exam: All / Random (entire / per group), Unique / Same, Individual / Usergroup | Confirmation; instances created | PASS |  | All questions, Individual to BETA TEST ONLY Lowperm: confirm text 'Assign "BETA TEST ONLY Exam" to BETA TEST ONLY Lowperm using all question selection?', success, instance and batch created. Random modes and Usergroup assign not run (would assign to real users). |
| EXM-009 | Browse Instances / Batches; remove/delete; add person to batch | Works | FAIL | BUG-EXM-007 | Browse Instances shows per-person counts (Lowperm: 1 exam, 1 Failed after grading). Batch view shows totals, progress, per-person rows. Add person (Service Account): 'Person added to batch successfully'. Delete unstarted instance: confirm 'Only unstarted instances can be deleted' > OK > success toast, but the row stays until reload. Batch dates show '10/22/2026 01:46 AM' (BUG-EXM-002). |
| EXM-010 | Assigned exam on Personnel > Exams and Dashboard > Exams | Appears; take and score | PASS | BUG-EXM-006, BUG-EXM-010, BUG-EXM-011 | betatest_low: My Account > Exams lists 'BETA TEST ONLY Exam' as Assigned 22/10/2026. Clicking the row opens the exam (10 questions, Previous/Next, navigator, Review shows answered/remaining). Submitted with 7 of 10 answered: 'Exam Submitted', row now Graded 18.00% Fail. Dashboard > Exams not checked: betatest_low has no Dashboard access. Retest 23/10/2026: BUG-EXM-006 fixed on v2.0.121 (Lowperm, new attempt, Review matches ticks). Found BUG-EXM-010 (group-level user got Access Denied on save/submit, buttons hidden) and BUG-EXM-011 (answered counter stale); both fixed on v2.0.122 (Grpuser took and submitted his exam). |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`STATUS.md`](../STATUS.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| FUNC-05 | Low | Open (external) | Exam editor says "Read Only" but still shows Add Question and Add Group |
| VIS-25 | Low | Open (external) | Disabled button styles differ (Exam editor) |
| UX-06 | Low | Open (external) | Exam Builder action icons misaligned between rows; wrong icon for Download Paper |
| UX-12 | Low | Open (external) | Exam editor uses a text "Back" button; other pages use an icon |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Exam group 'BETA TEST ONLY Exams', exam 'BETA TEST ONLY Exam' (10 questions, Rev 2), its instance/batch for BETA TEST ONLY Lowperm | Exam Builder / Exam Instances | No - delete fails once taken (BUG-EXM-008) |

### Retest v2.0.121 / v2.0.122 (23/10/2026)
- BUG-EXM-006 fixed (v2.0.121): box, text, empty row and Space each toggle once, one save each; kept across Next/Previous and close/reopen; Review matches.
- BUG-EXM-010 fixed (v2.0.122): Grpuser (read-only Personnel Details) can answer, go back, close, reopen and submit his own exam; submitting another user's instance is refused. Not tested: progress save on another user's unstarted attempt.
- BUG-EXM-011 fixed (v2.0.122): the answered counter updates as soon as an answer changes (Multi-Response, Multiple Choice).
- To confirm with Jon: personneldetails_getexaminstance lets Grpuser read the answers and score of attempts that aren't his (6164, 6166).
- Still open, not retested: BUG-EXM-001, -002, -003, -004, -005, -007, -008, -009.
