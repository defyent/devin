# DataHangar Forms System Audit

Site: stresstest.datahangar.net (v2.0.111), account Service Account, 17/10/2026. Settings during test: Pacific/Auckland, DD/MM/YYYY, HH:mm, Type-In Fields (unchanged).
Scope: Form Builder (all 15 widgets), Rendered Form preview, attached forms on Flights, Personnel, Safety Reports, Form Browser / Form Viewer, Reports (Forms data source). Separate from the general UI/UX audit.

## 0. Issue list (reply with ID + change)

| ID | Sev | Summary |
|---|---|---|
| FORM-01 | High | Flight Details saves a form with 9 empty required fields, no warning |
| FORM-02 | High | Safety Report form edits are lost: Save Changes never enables, values gone after reopening |
| FORM-03 | High | Personnel "Archived Forms" section won't expand, so archived forms can't be viewed or unarchived |
| FORM-04 | High | Form Viewer shows no value for Date and Time widgets |
| FORM-05 | High | Invalid/cleared Date or Time keeps the old hidden value, so it saves something the user can't see |
| FORM-06 | Med | Time widget defaults to current UTC time, not local time |
| FORM-07 | Med | Safety Report instance dates use MM/DD/YYYY and switch between UTC and local |
| FORM-08 | Med | Form Browser dates ignore the date setting ("Oct 17, 2026") |
| FORM-09 | Med | Form Browser shows incomplete forms as "Submitted"; no Draft/Incomplete status |
| FORM-10 | Med | Field count differs: Viewer 8/11 vs Flight Details 11/11; defaults count as filled |
| FORM-11 | Med | "Updated" time doesn't change after a later save of a flight form |
| FORM-12 | Med | Three save models: Flight = manual Save, Personnel = auto-save on add, Safety = add only |
| FORM-13 | Med | Three different Add Form pickers (Flight, Personnel, Safety) |
| FORM-14 | Med | Add Form lists every template everywhere (Personnel forms on flights, etc.) |
| FORM-15 | Med | Add Form search: template name only, no group names, no punctuation-tolerant match |
| FORM-16 | Med | Toggle shows as a plain checkbox in attached forms and Viewer |
| FORM-17 | Med | Rendered Form preview: List Box, Scribble and Checkbox don't work; no validation test |
| FORM-18 | Med | Conditions are table-level only, with triggers outside the table; single-table forms can't use them |
| FORM-19 | Med | Builder modals stack: Auto-Attach opens on top of the Conditions modal |
| FORM-20 | Med | Builder modals ignore Esc and outside clicks; Esc closes the Safety picker only |
| FORM-21 | Med | Validation errors use a generic popup that closes the Create modal (2 round trips) |
| FORM-22 | Low | Flight Delete Form confirm uses "Stay on Page" instead of "Cancel" |
| FORM-23 | Low | Delete confirm wording differs per module |
| FORM-24 | Low | Option editors accept duplicates and malformed key-value lines silently |
| FORM-25 | Low | Save Form Template asks for group + name every time |
| FORM-26 | Low | Builder buttons are text glyphs with no tooltips (− + × ▲ ▼ C ↻ ☰) |
| FORM-27 | Low | Default labels inconsistent ("Date:" vs "Text Field", "Textarea label") |
| FORM-28 | Low | Required marker differs: red * in builder, orange ★ in preview, none in Viewer |
| FORM-29 | Low | Monospace font in inputs, option editors and template name |
| FORM-30 | Low | Viewer is read-only but List Box × buttons still look active |
| FORM-31 | Low | Date widget stores a time component (date-only field) |
| FORM-32 | Low | Key-Value value box is empty in preview; shows italic in Viewer |
| FORM-33 | Low | Two checkbox styles in one form |
| FORM-34 | Low | Expand icon differs (expand_less vs expand_more) between modules |
| FORM-35 | Low | Picker title "Add Form Template" adds an instance, not a template; preview modal is titled "Rendered Form" but the button says "View Form" |
| FORM-36 | Low | Delete Form Template / Reset are red and enabled with no template selected |
| FORM-37 | Low | Personnel instance delete button has no tooltip; Archive has one |
| FORM-38 | Info | Reports help text mentions renewals, but Form Browser has no Renewals folder |
| FORM-39 | Info | Hidden empty "Error" modal in Form Viewer DOM (opacity 0, not visible) |

Good: drag-out does not close any forms popup tested (builder edit modals, Rendered Form, Conditions, Auto-Attach, Personnel Archive confirm, Safety picker). Values persist on Flights for all 11 input widgets. Reports Forms source lists all input fields as columns.

## 1. Details

**FORM-01 (High) Required fields not enforced.** Flight Details > Forms > Add Form > AUDIT All Widgets > Save Changes with nothing filled. Expected: block or warn and mark fields. Actual: saved silently, no toast, page jumped back to the Details tab. Suggest inline red required markers, block save (or allow "Save draft" with status Draft). shots/fd_save_empty.png

**FORM-02 (High) Safety Report form edits lost.** Safety Reports > report 274 > Forms > Add Form > AUDIT; instance is created immediately. Typed "SMS form test" in Pilot Name. Save Changes stays disabled; leave and reopen: the value is empty. Expected: Save enables on change, or auto-save. shots/sr_form.png, sr_after_nav.png

**FORM-03 (High) Archived Forms unreachable.** Personnel record > Forms > archive a form. "Archived Forms (1)" appears, but clicking the header (twice with the mouse, plus a JS click) never expands it (content stays display:none). So Unarchive can't be reached. Before this, the expanded archived body also showed editable Clear/Add controls. shots/pd_archived.png

**FORM-04 (High) Viewer omits Date/Time.** Form Browser > search 8795 > open AUDIT instance. The Flight Date and Departure Time labels show with no value or input, though values were saved (visible in Flight Details). shots/fbr_viewer.png

**FORM-05 (High) Silent invalid date/time.** Rendered/attached Date: type 31/02/2026, 99/99/9999, "abc", or clear the field. No error is shown, and the hidden stored value stays at the last valid date. Time is the same (25:99, 7:5, cleared). The user sees blank/invalid, but the old value gets saved. Suggest validating on blur, marking the field red, and clearing the stored value when the field is cleared.

**FORM-06 (Med) Time default UTC.** Preview and attached Time widgets prefill e.g. 03:31 while the header shows Local 16:31. Expected local time (or the flight time / blank).

**FORM-07 (Med) Safety instance dates.** Meta shows "Created: 10/17/2026 03:47" right after adding (MM/DD, UTC), then "10/17/2026 16:47" after reload (local). Flight/Personnel show 17/10/2026 16:40. The "by user" is missing until reload.

**FORM-08..11** Form Browser search results show "Oct 17, 2026" regardless of format. Status is "Submitted" for a form saved with 9 empty required fields. Viewer progress is 8/11 (date/time not counted) vs 11/11 in Flight Details, and new instances count auto-defaulted date/time as filled (2/11 with nothing typed). After a second save of the flight form, values persisted but "Updated" stayed at the first save time.

**FORM-12 (Med) Save models.** Flight: select template, then Save Changes (header button, no icon). Personnel: the instance saves the moment it's added (Save disabled until edited; floating button with icon). Safety: the instance saves on add, and edits can't be saved (FORM-02). Suggest one model across all records.

**FORM-13/14/15 (Med) Add Form picker.** Flight: icon title, × top-right, plain list. Personnel: centred title, × top-left, bordered buttons. Safety (<dialog>): × inline right, dark focus ring, closes on Esc, not on outside click. All list every template group, including Personnel forms on a flight. Search "QA Personnel" or "post flight" returns nothing. Suggest one shared picker, filtering by record type (or a template "applies to" setting), and searching group names with punctuation-insensitive matching. shots/fd_addform.png, sr_addform.png

**FORM-16 (Med)** Toggle renders as a switch in builder/preview but as a small checkbox in attached forms and a greyed checkbox in Viewer.

**FORM-17 (Med) Preview incomplete.** In View Form ("Rendered Form"): List Box Add does nothing (both click and Enter), the Scribble canvas can't be drawn on, and checkbox clicks don't toggle. All of these work in attached instances. There's only a Close button, with no "test validation". Some automation interference was ruled out by retesting in attached forms; the preview failures should still be confirmed manually.

**FORM-18/19/20 (Med) Builder modals.** Conditions ("C") apply to a whole table only, and triggers must be outside the table, so a form with one table can never use conditions (the Add button stays enabled anyway). Esc doesn't close Conditions, and clicking Auto-Attach while Conditions is open stacks both modals. Suggest widget-level conditions and one modal at a time with Esc support. shots/fb_conditions.png, fb_autoattach.png

**FORM-21 (Med)** New Form Template with empty fields closes the modal and shows "Validation Error: Please enter a template name." The user must reopen it, then gets "Please select a group." Suggest inline errors in the modal. shots/fb_newtpl_empty.png

**FORM-22..37 (Low).** See the table. Key facts: the Flight delete confirm buttons are "Stay on Page / Delete", while Safety shows "Cancel / Delete" with different text. Dropdown keeps "Bravo" twice. Key-Value keeps "BadEntry" (no =) as a key and drops "=noKey" without warning. Save on an existing template reopens the Save modal (looks like Save As). Builder grid buttons have no title. The required * sits inside the editable label text, so the user can delete it while editing.

## 2. Coverage matrices

**Widgets (15)** - B builder, P preview, A attached (flight), V viewer, Rq required supported

| Widget | B | P | A persist | V | Notes |
|---|---|---|---|---|---|
| Header | ok | ok | ok | ok | |
| Separator | ok | ok | ok | ok | |
| Text Block | ok | ok | ok | ok | |
| Text Field | ok Rq | ok | ok | ok | monospace |
| Date | ok Rq | invalid accepted | ok | **missing** | FORM-04/05/31 |
| Time | ok Rq | UTC default | ok | **missing** | FORM-04/05/06 |
| Textarea | ok Rq | ok | multi-line ok | ok | |
| Dropdown | ok Rq, options | ok | ok | ok | duplicates kept |
| Radio | ok Rq, options | ok | ok | ok | |
| Checkbox | ok Rq, flip | click fails | ok | ok | |
| Toggle | ok | switch | checkbox | checkbox | FORM-16 |
| Scribble | ok Rq | can't draw | ok | ok | |
| Key-Value | ok Rq, options | value empty | ok | italic | FORM-24/32 |
| List Box | ok Rq | Add fails | ok (incl Enter) | × active | FORM-30 |
| Image | upload ok (id 1) | ok | ok | ok | 5 MB, JPEG/PNG/GIF/WebP/SVG |

**Attachment locations**

| Location | Add | Save edits | Reopen persists | Delete | Archive | Notes |
|---|---|---|---|---|---|---|
| Flight 8795 | ok | manual Save | ok | ok ("Stay on Page") | n/a | FORM-01, 11 |
| Personnel 274 | auto-save | ok | ok | not tested | archive ok, unarchive blocked | FORM-03 |
| Safety Report 274 | auto-save | **lost** | instance only | ok | n/a | FORM-02, 07 |
| Renewals | not tested | | | | | no instances in Form Browser |
| Waypoints | not tested | | | | | |

**Builder**: create group/template ok; validation popups (FORM-21); required ok; labels ok; option editors ok (FORM-24); image ok; save + reload persistence ok; View Form ok (FORM-17); Conditions opened (FORM-18); Auto-Attach opened, Cancel (not saved); Delete Form Template confirm ok, template removed. Not tested: table row/col/span/border edits in depth, moving tables, font size, Allow Confidential effect, Reset.

**Form Browser / Viewer**: folders Flights/People/SMS Reports; path Flights > 2026 > October > Flight 8795 ok; search by name and flight number ok; empty result message ok; Viewer read-only inputs ok, except FORM-04/10/16/28/30.

**Reports (Forms source)**: Custom Report > Data Source Forms > template list ok; Columns tab lists submission info + 10 input fields (signature/layout excluded, fine); Filters tab has Add Filter Group. Report not saved or run.

## 3. Test data and cleanup

| Item | Status |
|---|---|
| Template "AUDIT All Widgets" | deleted |
| Flight 8795 AUDIT instance (191) | deleted |
| Safety Report 274 AUDIT instance | deleted |
| Personnel 274 AUDIT instance (192), archived | **left**: unreachable due to FORM-03 (template deletion says existing forms are kept) |
| Group "AUDIT Forms" | **left**: no group delete found in builder |
| Form Builder image id 1 | **left** (no UI to delete) |
| Earlier audit: exam draft "Air Law & Regulations", group "Aviation Theory", AUDIT_TEST_upload.txt on Flight 8795 | still left |

Date settings were not changed during this forms test.

## 4. Limitations

- Toolbox drag-and-drop was done with synthetic drag events (Playwright native drag hangs in Chrome). Real mouse drag was not verified.
- Not tested: Renewals and Waypoint forms, Flight Auto-Attach in effect (flight creation), copying flights with required forms, Allow Confidential visibility with another user, the date picker types (Scroll Wheel/Native) inside forms, table layout editing in depth, saving/running a Forms report.
- Preview widget failures (FORM-17) should be confirmed by hand.

## 5. Suggestions

1. One attached-forms component for all record types: same picker, same save model, same meta format, same archive/delete.
2. Statuses Draft / Complete based on required fields; block "Complete" until required fields are filled.
3. Validate date/time inline and honour the date/time settings everywhere (meta, Browser, Viewer, defaults in local time).
4. Widget-level conditions with triggers anywhere in the form.
5. Render Toggle, required markers and read-only states the same in builder, preview, attached and Viewer.
6. Make the preview fully interactive with a "Check required fields" button.
7. Replace text-glyph builder buttons with self-hosted Material Symbols Sharp icons plus tooltips (see general audit ICON section).
8. Filter templates by record type in Add Form; search group names, fuzzy match.
