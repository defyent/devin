# Form Builder

- **Checklist ID prefix:** `FBLD`
- **Guide section:** §11.3
- **Where:** Settings and Tools > Forms > Form Builder
- **Permission:** Form Builder = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FBLD-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Forms > Form Builder loads (template list QA Post-Flight Report ... QA Hazard Observation, toolbox, default Table 1), no page errors |
| FBLD-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-FBLD-001 | Help opens and closes with x and Close (no 'Got it'). Escape and outside click do nothing (FORM-20) |
| FBLD-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag-out from Help content keeps Help open |
| FBLD-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-FBLD-002 | Preview Date shows DD/MM/YYYY and Time HH:MM, but both default to UTC (21/10/2026 12:07) while local is 22/10/2026 01:07 (FORM-06) |
| FBLD-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | FAIL | BUG-FBLD-004 | At 390px the page is 644px wide and scrolls sideways; Toolbox overlays the form and header controls are cut off |
| FBLD-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | Form Builder is only linked from Settings and Tools; betatest_low gets Access Denied on Settings and Tools (HUB-S06) |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FBLD-001 | New Form Template (group + name) BETA TEST ONLY | Created | PASS |  | New Form Template with '+ New Group...' 'BETA TEST ONLY Forms' and name 'BETA TEST ONLY Form' creates it and selects it. Create with an empty name shows 'Validation Error: Please enter a template name' and closes the Create popup (FORM-21) |
| FBLD-002 | Add Table, rows/columns, span cells | Works | PASS |  | Table 1: +Row x6 gives 8x2 cells, +Col/-Col add and remove a column, span Col+ on R1C1 spans both columns ('Col 2') and Col- undoes it |
| FBLD-003 | Drag every widget type from Toolbox | Header, Text Field, Textarea, Text Block, Date, Time, Dropdown, Radio, Checkbox, Toggle, List Box, Key-Value, Scribble, Image, Separator | PASS |  | All 15 toolbox widgets dragged into cells and created: Header, Separator, Text Block, Text Field, Date, Time, Textarea, Dropdown, Radio Group, Checkbox, Toggle, Scribble, Key-Value Pair, List Box, Image |
| FBLD-004 | Edit label, star required, Edit Options | Works | PASS | BUG-FBLD-001 | Text Field label edited to 'BETA TEST ONLY Name'; star toggles required (red * on label); Dropdown Edit Options replaced First/Second/Third with BETA A/B/C. Esc doesn't close Edit Options (BUG-FBLD-001) |
| FBLD-005 | Condition (C): show/hide on equal/not equal | Works in View Form preview | FAIL | BUG-FBLD-003 | Table 2 condition 'Choose an option is BETA A > show' saved, but in View Form Table 2 always shows (none/BETA A/BETA B), even after Save Form Template |
| FBLD-006 | Size, Allow Confidential | Saved | PASS |  | Size 16px and Allow Confidential on, Save Form Template (group/name prefilled) shows 'Template saved successfully.'; after switching template and back: 15 widgets, edited label, required star, BETA A/B/C options, 16px, Confidential on all kept |
| FBLD-007 | Flight Auto-Attach categories/activities > Save | Form auto-attaches on Flight Details; required on copy | PASS | fbld007_copy | "QA Equipment Issue" set to Auto-Attach on activity Maintenance Test. On a new ZK-BTO flight, picking that activity shows 'Form "QA Equipment Issue" auto-attached', and saved flight #42910 lists the form on its Forms tab. Copying #42910 (Ctrl+C, click a slot, Ctrl+V) opens Copy Flight Options with "Forms 1 — Required by flight type", ticked and locked on. |
| FBLD-008 | Save Form Template / Reset / Delete | Work with confirmation | PASS |  | Save Form Template works (toast shown twice). Reset asks 'Confirm Reset ... grid will be reset to a 2x2 layout', Cancel keeps all widgets. Delete asks 'Are you sure you want to delete BETA TEST ONLY Form?' and removes it; Delete is then disabled |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`STATUS.md`](../STATUS.md)). Retest each one while working this checklist and note the result.

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
| Form group 'BETA TEST ONLY Forms' (template 'BETA TEST ONLY Form' deleted, auto-attach unticked) | Settings and Tools > Form Builder | No - empty group stays, no way to delete groups |
