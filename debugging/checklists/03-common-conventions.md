# Common screen conventions (apply on every page)

- **Checklist ID prefix:** `CON`
- **Guide section:** §4, §15.3
- **Where:** Every page
- **Permission:** n/a
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| CON-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Every module in checklists 04 to 47 was opened by clicking through the sidebar or Settings and Tools. No ?action= URLs were used. Maintenance has no menu path, so it is BLOCKED (checklist 30). |
| CON-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS |  | Checked on Flight Details: Got it! / x / backdrop click / Esc all close Help |
| CON-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | See POP-001: every popup tested stayed open after a drag-out. |
| CON-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-SLOG-001 | See DATE-001: many pages ignore the date and time format setting. |
| CON-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | FAIL | BUG-SWP-004 | See MOB-002: 15 pages are cut off or overlap at 390 px. |
| CON-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | See PERM-007: Lowperm gets "Access Denied" on modules it has no permission for, and the server refuses direct requests (PERM-009). |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| CON-001 | Help (?) button top right | Opens page help; closes with Got it/Close, ×, click outside, Esc | PASS |  | Flight Details Help (?) top right opens page help; closes with Got it!, x, backdrop click, Esc. Note: Dashboard and Flight Schedule have no Help button (VIS-06) |
| CON-002 | Pill navigation | Pills switch sections; narrow screen shows a dropdown | PASS |  | On narrow screens the settings pills turn into a dropdown (SFS-S05), and Activity Log tabs fit at 390 px. |
| CON-003 | Toast on save/add/delete | Bottom-right toast, disappears after ~3 s | PASS |  | Saves, adds and deletes show a toast, e.g. "Updated flight #42903 time.", "Permissions updated for Service Account (0 permissions)", "Project deleted successfully!". |
| CON-004 | Server error / Access Denied | Popup modal with OK; if already in a popup, that popup closes first | PASS |  | Access Manager: delete in-use group > confirm popup closes first, then 'Cannot Delete Group' error modal with OK |
| CON-005 | Destructive actions | Always a Cancel/Delete confirmation; NEVER a native browser alert/confirm | PASS |  | Deletes ask first, e.g. Flight Details delete (FD-038), Extra Flight Info (names the field), Reset Colors. The Cancellation Reason confirm does not name the reason (checklist 31). |
| CON-006 | Dirty-state buttons | Save/Cancel enable or change colour only after a change; revert when change undone | PASS |  | Flight Details Save Changes stays disabled until something changes, and an aircraft change warns about meter readings before it is applied. |
| CON-007 | Search boxes | Filter as you type; × clear button works | PASS |  | Search boxes filter as you type in Waypoints, Resources, Inspections, Support, Flight Types and Personnel. |
| CON-008 | Date/time pickers | Shared DateTimePicker; style follows Settings > Time Zone picker type | PASS |  | See DATE-003: the saved picker type is used everywhere. Known picker defects are in BUG-SINS-003 and BUG-FBLD-002. |
| CON-009 | File upload areas | Choose/Browse then Upload; list shows Name, Uploaded, Uploaded By, Size, Actions; preview modal has Download | PASS |  | Uploads work in Personnel Files (PD-025), Support, Notices, Safety Reports and File Browser. Opening .txt files fails (BUG-FB-003, BUG-PD-012). |
| CON-010 | Attached Forms | Add Form > search template > fill; Confidential forms only visible to owner + author | PASS |  | Attached forms can be added, archived, unarchived and deleted on Personnel Details (PD-024). Flight auto-attach is BLOCKED (FBLD-007). |
| CON-011 | History buttons/tabs | Show who changed what and when | PASS |  | Personnel History and Safety Report History list the changes. Activity Log logs every change from this run (checklist 47). |
| CON-012 | PDF export | Choose sections; generates PDF | PASS |  | PDF export works on Personnel Details, Roster Builder and Reports. |
| CON-013 | Field help icons (?) | Explain the field (Notify, Confidential, Anonymous...) | FAIL | BUG-SMS-001 | Field (?) icons open their hint, but Escape on the Confidential/Anonymous (?) closes the whole New Report form (BUG-SMS-001). |
| CON-014 | POPUP DRAG-OUT BUG: in every popup, mousedown inside (e.g. in a text field), drag and release outside | Popup must NOT close | PASS |  | Drag-out keeps popups open so far (Access Manager, Flight Schedule details popup) |
| CON-015 | Esc in any modal | Closes it (and does not lose unsaved data without a prompt) | FAIL | BUG-POP-001 | Esc does not close the error modal (BUG-POP-001); Esc on dirty Groups popup closes without prompt and keeps stale ticks (BUG-POP-003) |
| CON-016 | Icon consistency | Same icon for the same action (add/edit/delete/help/save) across modules — record mismatches in ui-icons checklist | FAIL | ICON-04 | See UI-001: the same action uses different icons on different pages. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
