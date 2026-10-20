# Dashboard

- **Checklist ID prefix:** `DSH`
- **Guide section:** §8.1
- **Where:** Flight Operations > Dashboard (default landing)
- **Permission:** Dashboard = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| DSH-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| DSH-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| DSH-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| DSH-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| DSH-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| DSH-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| DSH-001 | Load without Dashboard permission | Every widget shows 'Access Denied' | TODO | | |
| DSH-002 | My Roster calendar: < > Today | Month changes; shifts in shift colours; Today returns | TODO | | |
| DSH-003 | Click another day | On Duty / My Flights headers change to that date; 'Not viewing today' tag | TODO | | |
| DSH-004 | On Duty list | Matches published roster for that day, grouped by shift | TODO | | |
| DSH-005 | My Flights list; click a flight | Opens Flight Details; Back returns to Dashboard | TODO | | |
| DSH-006 | Tab: Recency and Renewals | Grouped by status; click opens Recency tab in own Personnel Details | TODO | | |
| DSH-007 | Tab: Unread Notices (badge) | Badge matches header bell; click opens notice | TODO | | |
| DSH-008 | Tab: Unsigned Timesheets | Click opens Timesheets tab on that day | TODO | | |
| DSH-009 | Tab: Safety Actions | Click opens the report | TODO | | |
| DSH-010 | Tab: Exams | Click opens Exams tab | TODO | | |
| DSH-011 | Tab: Project Tasks | Click opens the project | TODO | | |
| DSH-012 | Tab icons have tooltips/labels | Tabs identifiable (staging shows icon-only tabs) — UI finding if not | TODO | | |
| DSH-013 | Recency items for Service Account show 'No Expiry' | Check whether 'No Expiry' is correct vs empty status | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
