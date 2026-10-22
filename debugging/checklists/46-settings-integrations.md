# Settings – Google Calendar, WhatsApp

- **Checklist ID prefix:** `SINT`
- **Guide section:** §12.17, §12.18
- **Where:** Settings and Tools > Configuration > Google Calendar Sync (WhatsApp not linked on staging)
- **Permission:** settings_googlecalendar / settings_whatsapp = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SINT-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Configuration > Google Calendar Sync opens settings_googlecalendar ("No calendars configured", Sync Status: Pending Sync 9000, Synced 0), with no console errors. |
| SINT-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-SINT-001 | Help (?) opens Setup Instructions and closes with × / Close. Escape and an outside click do not close it, and Escape does not close Add Calendar. |
| SINT-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside Add Calendar to outside it: it stays open. |
| SINT-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-SINT-002 | Pending Sync list shows "2024-01-01 07:55" instead of DD/MM/YYYY. |
| SINT-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | 390 px: scrollWidth 375, nothing off-screen. The cards stack and the buttons are all visible. |
| SINT-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Settings and Tools shows Access Denied (System Settings). |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SINT-001 | Add Calendar > Authorize (popup) > Select > Enable > Save | Likely BLOCKED without Google account — note | BLOCKED |  | Add Calendar opens (Calendar Name, Authorize Calendar, Sync enabled). Saving with no name gives "Please enter a Calendar Name." I couldn't authorize because there is no Google account for stresstest. No calendar was created. |
| SINT-002 | Sync Status: search, refresh, sync now, test connection | Works or clear error | PASS |  | Search flights narrows the list (R66-02 only, no C172-05). Refresh reloads the status (get_status 200). Sync Now with no calendar gives a clear error: "No authorized calendars configured for sync". There is no Test Connection, because it needs a calendar. |
| SINT-003 | Setup Instructions | Readable | PASS |  | Setup Instructions (the help icon) explains How Sync Works (every 5 minutes), Adding a Calendar (step by step), and What Gets Synced. Clear and readable. |
| SINT-004 | WhatsApp page reachability via UI | Not on hub — record | BLOCKED |  | There is no WhatsApp link in the sidebar or in Settings and Tools (also noted in 21-settings-hub). I didn't open it by URL. Asked Jon whether it should be linked. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
