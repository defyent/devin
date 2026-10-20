# Form Builder

- **Checklist ID prefix:** `FBLD`
- **Guide section:** §11.3
- **Where:** Settings and Tools > Forms > Form Builder
- **Permission:** Form Builder = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FBLD-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| FBLD-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| FBLD-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| FBLD-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| FBLD-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| FBLD-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FBLD-001 | New Form Template (group + name) BETA TEST ONLY | Created | TODO | | |
| FBLD-002 | Add Table, rows/columns, span cells | Works | TODO | | |
| FBLD-003 | Drag every widget type from Toolbox | Header, Text Field, Textarea, Text Block, Date, Time, Dropdown, Radio, Checkbox, Toggle, List Box, Key-Value, Scribble, Image, Separator | TODO | | |
| FBLD-004 | Edit label, star required, Edit Options | Works | TODO | | |
| FBLD-005 | Condition (C): show/hide on equal/not equal | Works in View Form preview | TODO | | |
| FBLD-006 | Size, Allow Confidential | Saved | TODO | | |
| FBLD-007 | Flight Auto-Attach categories/activities > Save | Form auto-attaches on Flight Details; required on copy | TODO | | |
| FBLD-008 | Save Form Template / Reset / Delete | Work with confirmation | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
