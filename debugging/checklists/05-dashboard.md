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
| DSH-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Opened via sidebar; no console errors (only iframe sandbox warning) |
| DSH-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| DSH-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| DSH-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | DATE-02 | Headers show 'Wed, Oct 21, 2026' (US month-first) although Time Zone is DD/MM/YYYY; already known as DATE-02 |
| DSH-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| DSH-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| DSH-001 | Load without Dashboard permission | Every widget shows 'Access Denied' | PASS |  | 0-permission user: whole Dashboard replaced by one 'Access Denied: You do not have permission to access the Dashboard feature' card (not per-widget, but no data leak / no JS error) |
| DSH-002 | My Roster calendar: < > Today | Month changes; shifts in shift colours; Today returns | PASS |  | > Nov 2026, < Oct, < Sep, Today back to Oct 2026; today (21) highlighted |
| DSH-003 | Click another day | On Duty / My Flights headers change to that date; 'Not viewing today' tag | PASS |  | Click 15: 'On Duty for Thu, Oct 15, 2026' + 'My Flights for Thu, Oct 15, 2026', both tagged 'Not viewing today' |
| DSH-004 | On Duty list | Matches published roster for that day, grouped by shift | PASS |  | On Duty grouped by shift with shift colours and times (Sick Leave, Office Hours, Morning 06:00-18:00, Afternoon 14:00-02:00). Cross-check vs Roster Viewer in 13 |
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
