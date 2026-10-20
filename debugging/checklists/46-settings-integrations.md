# Settings – Google Calendar, WhatsApp

- **Checklist ID prefix:** `SINT`
- **Guide section:** §12.17, §12.18
- **Where:** Settings and Tools > Configuration > Google Calendar Sync (WhatsApp not linked on staging)
- **Permission:** settings_googlecalendar / settings_whatsapp = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SINT-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| SINT-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| SINT-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| SINT-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| SINT-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| SINT-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SINT-001 | Add Calendar > Authorize (popup) > Select > Enable > Save | Likely BLOCKED without Google account — note | TODO | | |
| SINT-002 | Sync Status: search, refresh, sync now, test connection | Works or clear error | TODO | | |
| SINT-003 | Setup Instructions | Readable | TODO | | |
| SINT-004 | WhatsApp page reachability via UI | Not on hub — record | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
