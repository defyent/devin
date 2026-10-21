# Common screen conventions (apply on every page)

- **Checklist ID prefix:** `CON`
- **Guide section:** §4, §15.3
- **Where:** Every page
- **Permission:** n/a
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| CON-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| CON-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS |  | Checked on Flight Details: Got it! / x / backdrop click / Esc all close Help |
| CON-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| CON-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| CON-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| CON-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| CON-001 | Help (?) button top right | Opens page help; closes with Got it/Close, ×, click outside, Esc | PASS |  | Flight Details Help (?) top right opens page help; closes with Got it!, x, backdrop click, Esc. Note: Dashboard and Flight Schedule have no Help button (VIS-06) |
| CON-002 | Pill navigation | Pills switch sections; narrow screen shows a dropdown | TODO | | |
| CON-003 | Toast on save/add/delete | Bottom-right toast, disappears after ~3 s | TODO | | |
| CON-004 | Server error / Access Denied | Popup modal with OK; if already in a popup, that popup closes first | PASS |  | Access Manager: delete in-use group > confirm popup closes first, then 'Cannot Delete Group' error modal with OK |
| CON-005 | Destructive actions | Always a Cancel/Delete confirmation; NEVER a native browser alert/confirm | TODO | | |
| CON-006 | Dirty-state buttons | Save/Cancel enable or change colour only after a change; revert when change undone | TODO | | |
| CON-007 | Search boxes | Filter as you type; × clear button works | TODO | | |
| CON-008 | Date/time pickers | Shared DateTimePicker; style follows Settings > Time Zone picker type | TODO | | |
| CON-009 | File upload areas | Choose/Browse then Upload; list shows Name, Uploaded, Uploaded By, Size, Actions; preview modal has Download | TODO | | |
| CON-010 | Attached Forms | Add Form > search template > fill; Confidential forms only visible to owner + author | TODO | | |
| CON-011 | History buttons/tabs | Show who changed what and when | TODO | | |
| CON-012 | PDF export | Choose sections; generates PDF | TODO | | |
| CON-013 | Field help icons (?) | Explain the field (Notify, Confidential, Anonymous...) | TODO | | |
| CON-014 | POPUP DRAG-OUT BUG: in every popup, mousedown inside (e.g. in a text field), drag and release outside | Popup must NOT close | PASS |  | Drag-out keeps popups open so far (Access Manager, Flight Schedule details popup) |
| CON-015 | Esc in any modal | Closes it (and does not lose unsaved data without a prompt) | FAIL | BUG-POP-001 | Esc does not close the error modal (BUG-POP-001); Esc on dirty Groups popup closes without prompt and keeps stale ticks (BUG-POP-003) |
| CON-016 | Icon consistency | Same icon for the same action (add/edit/delete/help/save) across modules — record mismatches in ui-icons checklist | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
