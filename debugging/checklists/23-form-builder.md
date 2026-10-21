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

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| FORM-05 | High | Open (external) | Invalid/cleared Date or Time keeps the old hidden value, so it saves something the user can't see |
| FORM-06 | Medium | Open (external) | Time widget defaults to current UTC time, not local time |
| FORM-12 | Medium | Open (external) | Three save models: Flight = manual Save, Personnel = auto-save on add, Safety = add only |
| FORM-13 | Medium | Open (external) | Three different Add Form pickers (Flight, Personnel, Safety) |
| FORM-14 | Medium | Open (external) | Add Form lists every template everywhere (Personnel forms on flights, etc.) |
| FORM-15 | Medium | Open (external) | Add Form search: template name only, no group names, no punctuation-tolerant match |
| FORM-16 | Medium | Open (external) | Toggle shows as a plain checkbox in attached forms and Viewer |
| FORM-17 | Medium | Open (external) | Rendered Form preview: List Box, Scribble and Checkbox don't work; no validation test |
| FORM-18 | Medium | Open (external) | Conditions are table-level only, with triggers outside the table; single-table forms can't use them |
| FORM-19 | Medium | Open (external) | Builder modals stack: Auto-Attach opens on top of the Conditions modal |
| FORM-20 | Medium | Open (external) | Builder modals ignore Esc and outside clicks; Esc closes the Safety picker only |
| FORM-21 | Medium | Open (external) | Validation errors use a generic popup that closes the Create modal (2 round trips) (see also POP-08) |
| FORM-23 | Low | Open (external) | Delete confirm wording differs per module |
| FORM-24 | Low | Open (external) | Option editors accept duplicates and malformed key-value lines silently |
| FORM-25 | Low | Open (external) | Save Form Template asks for group + name every time |
| FORM-26 | Low | Open (external) | Builder buttons are text glyphs with no tooltips (− + × ▲ ▼ C ↻ ☰) (see also VIS-21) |
| FORM-27 | Low | Open (external) | Default labels inconsistent ("Date:" vs "Text Field", "Textarea label") |
| FORM-28 | Low | Open (external) | Required marker differs: red * in builder, orange ★ in preview, none in Viewer |
| FORM-29 | Low | Open (external) | Monospace font in inputs, option editors and template name |
| FORM-31 | Low | Open (external) | Date widget stores a time component (date-only field) |
| FORM-32 | Low | Open (external) | Key-Value value box is empty in preview; shows italic in Viewer |
| FORM-33 | Low | Open (external) | Two checkbox styles in one form |
| FORM-34 | Low | Open (external) | Expand icon differs (expand_less vs expand_more) between modules |
| FORM-35 | Low | Open (external) | Picker title "Add Form Template" adds an instance, not a template; preview modal is titled "Rendered Form" but the button says "View Form" |
| FORM-36 | Low | Open (external) | Delete Form Template / Reset are red and enabled with no template selected (see also FUNC-04) |
| FUNC-04 | Medium | Open (external) | Form Builder Delete/Reset buttons enabled with no template selected (see also FORM-36) |
| VIS-21 | Low | Open (external) | Form Builder uses text-symbol buttons instead of icons (see also FORM-26) |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
