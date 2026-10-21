# Cross-cutting: UI consistency and icon inventory

- **Checklist ID prefix:** `UI`
- **Guide section:** §4
- **Where:** Whole app
- **Permission:** n/a
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| UI-001 | Per-action icon inventory (add, edit, delete, save, help, history, PDF, upload, download, close) | Same icon per action everywhere; record each variant with module | TODO | | |
| UI-002 | Icon source | Single self-hosted pack (currently api.iconify.design CDN + Material Symbols mix) | TODO | | |
| UI-003 | Button labels and colours | Consistent primary/secondary/destructive | TODO | | |
| UI-004 | Help (?) present on every page | Yes | TODO | | |
| UI-005 | Empty states | Friendly message, not blank | TODO | | |
| UI-006 | Loading states | Spinner/skeleton; no layout jump | TODO | | |
| UI-007 | Typos / wording | Record exact text | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| VIS-01 | Medium | Open (external) | Page title size, weight and tag differ between modules |
| VIS-02 | Medium | Open (external) | Page header icons differ, are missing, or use a different icon font |
| VIS-03 | Low | Open (external) | Sidebar and module icons come from different icon sets |
| VIS-04 | Medium | Open (external) | Page titles don't match menu names (Staff Roster, Projects, Comms, Timezone Settings, Resource Management, Lesson Plan Configuration) |
| VIS-05 | Low | Open (external) | Subtitle line present on some pages, missing on others |
| VIS-06 | Medium | Open (external) | Help (?) button missing on most modules; position and icon vary |
| VIS-07 | Low | Open (external) | Corner radius differs (tables, cards, popups; some square) |
| VIS-08 | Low | Open (external) | Some buttons are unstyled browser defaults |
| VIS-09 | Medium | Open (external) | Different fonts: wide letter-spaced font in Notice Details, Support popup, Exam editor |
| VIS-10 | Low | Open (external) | Notes and comment boxes use a monospace font |
| VIS-11 | Low | Open (external) | Type-in date field is pill-shaped, unlike the other inputs |
| VIS-12 | Low | Open (external) | Search box width and icon size vary |
| VIS-13 | Low | Open (external) | Add buttons differ in wording and size; some are icon-only |
| VIS-14 | Low | Open (external) | Table sort arrows differ |
| VIS-16 | Low | Open (external) | Empty values shown as "-", "--" or "–" |
| VIS-17 | Low | Open (external) | Edit pencil icon size varies |
| VIS-18 | Low | Open (external) | Badge/pill colours differ per module |
| VIS-19 | Low | Open (external) | Tab styles differ (pill tabs, icon-only tabs, underline tabs) |
| VIS-23 | Low | Open (external) | Popup title icons inconsistent (orange PDF / ticket icons, others none) |
| UX-01 | Medium | Open (external) | Detail pages have different toolbars (PDF, History, Help, Back present or missing) |
| UX-04 | Low | Open (external) | Empty-state messages worded differently |
| UX-05 | Medium | Open (external) | Row actions inconsistent (pencil vs click row; Recency pencil says "View Details"; Form Browser none) |
| UX-08 | Low | Open (external) | "Save" vs "Save Changes" wording |
| ICON-01 | High | Open (external) | Icons come from 3 external sources: Google Fonts Material Icons Sharp (shell), api.iconify.design SVGs (sidebar), Google Fonts Material Symbols Sharp (modules). If a site has no internet or blocks these, icons show as words like "delete" (see also seed NAV-021) |
| ICON-02 | Medium | Open (external) | Sidebar uses the Rounded/Outline style while modules use Sharp, so the same icon looks different in the menu and on the page |
| ICON-03 | Medium | Open (external) | The older "Material Icons" font is still used in Flight Schedule, Active Flights, DFR, Support, FRMS Settings and the header |
| ICON-04 | Medium | Open (external) | Delete uses 6 icons: delete, × text, close (Safety Report detail), cancel (Exam Builder), old delete and delete_sweep (FRMS) |
| ICON-05 | Medium | Open (external) | Close popup uses 4 icons: close, × text (7 pages), old close (Dashboard, DFR, Support), inline SVG (Task Tracker) |
| ICON-06 | Medium | Open (external) | Edit uses 4+ icons: edit, edit_note (Personnel detail, Exam Builder, Exam Instances, Timesheets), old edit (Flight Schedule, FRMS), inline SVG (Roster Builder) |
| ICON-07 | Medium | Open (external) | Add/New uses 9+ icons: add, add_circle, add_circle_outline, person_add, playlist_add, note_add, inline SVG plus, old add, text "+" |
| ICON-08 | Medium | Open (external) | Help uses help, info, help_outline (Exam Builder), old help/info (Active Flights) and an inline SVG (Task Tracker); "info" is used for both help buttons and hints |
| ICON-09 | Medium | Open (external) | Upload/attach uses inline SVG, attach_file, upload_file, upload and old attach_file (Support); Flight Files "Upload" button has an unrelated glyph |
| ICON-10 | Low | Open (external) | Download/export: download vs inline SVG (Roster Builder); "description" icon used for Download Paper Exam |
| ICON-11 | Low | Open (external) | Back: arrow_back on most pages; none on Personnel detail; text button in Exam editor; « in Roster Builder |
| ICON-12 | Low | Open (external) | Prev/Next: text < > (Dashboard, Roster Viewer, Roster Builder, Timesheets, Personnel, date picker) vs chevron icons (Reports, Exam Instances, Timesheets, Flight Schedule old set) |
| ICON-13 | Low | Open (external) | Search icon: new set on most pages, old set on DFR, Flight Schedule, FRMS, Support, inline SVG on Task Tracker |
| ICON-14 | Low | Open (external) | Filter icon: old set (DFR, Flight Schedule, Support) vs new set (DFR settings) |
| ICON-15 | Low | Open (external) | Copy: content_copy vs inline SVG (Roster Builder) |
| ICON-16 | Low | Open (external) | Settings gear: Symbols settings vs sidebar tune/settings images vs inline SVG gear (Settings hub) |
| ICON-17 | Low | Open (external) | No icon size scale: close 16-28px, edit 13-24px, help 13-28px, description 13-40px |
| ICON-18 | Low | Open (external) | Same icon means different things: description (file / view / download paper), check_circle (acknowledge / close report / deactivate), history (Legacy Duty Browser), edit ("Configure") |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
