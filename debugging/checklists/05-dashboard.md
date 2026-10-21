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
| DSH-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-DSH-002 | Dashboard has no Help (?) button in the header (other modules have one) |
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
| DSH-005 | My Flights list; click a flight | Opens Flight Details; Back returns to Dashboard | BLOCKED |  | Service Account: 'No flights scheduled for this day.' (checked today and 15 Oct) |
| DSH-006 | Tab: Recency and Renewals | Grouped by status; click opens Recency tab in own Personnel Details | TODO | | |
| DSH-007 | Tab: Unread Notices (badge) | Badge matches header bell; click opens notice | PASS |  | Unread Notices tab badge 99+ = header bell 99+; clicking 'Fuel Price Adjustment' opens Notice Details (notice_id=30) |
| DSH-008 | Tab: Unsigned Timesheets | Click opens Timesheets tab on that day | BLOCKED |  | Service Account: 'All timesheets are signed!' - no unsigned timesheet to click |
| DSH-009 | Tab: Safety Actions | Click opens the report | BLOCKED |  | Service Account: 'No safety actions assigned to you.' |
| DSH-010 | Tab: Exams | Click opens Exams tab | BLOCKED |  | Service Account: 'No exams assigned to you.' |
| DSH-011 | Tab: Project Tasks | Click opens the project | BLOCKED |  | Service Account: 'No project tasks assigned to you.' |
| DSH-012 | Tab icons have tooltips/labels | Tabs identifiable (staging shows icon-only tabs) — UI finding if not | FAIL | BUG-DSH-001 | 6 tabs are icon-only (update, notifications, assignment_late, assignment, quiz, checklist) with no title / aria-label / tooltip |
| DSH-013 | Recency items for Service Account show 'No Expiry' | Check whether 'No Expiry' is correct vs empty status | PASS |  | All 8 Service Account items (Dangerous Goods ... Type Rating Renewal) show grey dot + 'No Expiry'. Consistent, but question for Jon: should items with no record say 'Not recorded' instead? |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
