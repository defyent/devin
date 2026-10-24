# Dashboard

- **Checklist ID prefix:** `DSH`
- **Guide section:** §8.1
- **Where:** Flight Operations > Dashboard (default landing)
- **Permission:** Dashboard = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| DSH-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Opened via sidebar; no console errors (only iframe sandbox warning) |
| DSH-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS |  | Retest 22/10/2026 (fresh browser, Service Account and BETA TEST ONLY Second): Help (?) opens the Dashboard Help popup; x, Close, Escape and clicking outside each close it. VIS-06 fixed. |
| DSH-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | No popups on Dashboard (clicks navigate to other modules) |
| DSH-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | PASS | re_dsh004_two | Retest 22/10/2026: My Flights / On Duty headers show "Thu 22/10/2026" (DD/MM/YYYY) (DATE-02 fixed on Dashboard). |
| DSH-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | 390 px: single column, no horizontal scroll, calendar usable. Performance panel covers content (BUG-PERF-001) |
| DSH-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | See DSH-001 |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| DSH-001 | Load without Dashboard permission | Every widget shows 'Access Denied' | PASS |  | 0-permission user: whole Dashboard replaced by one 'Access Denied: You do not have permission to access the Dashboard feature' card (not per-widget, but no data leak / no JS error) |
| DSH-002 | My Roster calendar: < > Today | Month changes; shifts in shift colours; Today returns | PASS |  | > Nov 2026, < Oct, < Sep, Today back to Oct 2026; today (21) highlighted |
| DSH-003 | Click another day | On Duty / My Flights headers change to that date; 'Not viewing today' tag | PASS |  | Click 15: 'On Duty for Thu, Oct 15, 2026' + 'My Flights for Thu, Oct 15, 2026', both tagged 'Not viewing today' |
| DSH-004 | On Duty list | Matches published roster for that day, grouped by shift | PASS |  | On Duty grouped by shift with shift colours and times (Sick Leave, Office Hours, Morning 06:00-18:00, Afternoon 14:00-02:00). Cross-check vs Roster Viewer in 13 |
| DSH-005 | My Flights list; click a flight | Opens Flight Details; Back returns to Dashboard | PASS |  | Retest 3 22/10/2026 as BETA TEST ONLY Second (fresh browser): My Flights opens on Thu 22/10/2026 (BUG-DSH-004 fixed). Canceled #42910 badge now says 'Canceled' (#8b4513) (BUG-DSH-006 fixed). Click opens Flight Details #42910 showing Canceled; Back returns to Dashboard. Dashboard JS/CSS now load with ?v=2.0.111. |
| DSH-006 | Tab: Recency and Renewals | Grouped by status; click opens Recency tab in own Personnel Details | PASS | re_dsh003_open | Retest 22/10/2026 as BETA TEST ONLY Grpuser: clicking "Day Landings" opens own Personnel Details on the Recency and Renewals tab, no page errors. BUG-DSH-003 fixed. |
| DSH-007 | Tab: Unread Notices (badge) | Badge matches header bell; click opens notice | PASS |  | Unread Notices tab badge 99+ = header bell 99+; clicking 'Fuel Price Adjustment' opens Notice Details (notice_id=30) |
| DSH-008 | Tab: Unsigned Timesheets | Click opens Timesheets tab on that day | PASS | dsh008_open | As BETA TEST ONLY Second, the Dashboard Unsigned Timesheets tab (assignment_late badge 1) lists "OC 21/10/2026 Not signed". Clicking it opens Personnel Details on the Timesheets tab (roster_id=108409). |
| DSH-009 | Tab: Safety Actions | Click opens the report | PASS | dsh009_two_open | On report #2063, admin created action "BETA TEST ONLY action for DSH-009" assigned to BETA TEST ONLY Second. Logged in as Second, the Dashboard Safety Actions tab has badge 1 and lists the action. Clicking it opens SMS Report Details for #2063. |
| DSH-010 | Tab: Exams | Click opens Exams tab | PASS | dsh010_two_open | Assigned "BETA TEST ONLY Exam" to BETA TEST ONLY Second in Exam Instances. As Second, the Dashboard Exams tab has badge 1 and lists the exam as Assigned 22/10/2026. Clicking it opens Personnel Details on the Exams tab (person_id=278&tab=exams). |
| DSH-011 | Tab: Project Tasks | Click opens the project | PASS |  | Retest 2 22/10/2026 (after Task Tracker update): new project #16 (group BETA TEST ONLY Group). As Grpuser, clicking the task in Project Tasks opens ?action=tasktracker&project_id=16&task_id=470 with the project shown and the task marked task-item-linked. As Second (no Task Tracker permission), the click also opens the project with their task linked (no Access Denied). Admin direct URL opens the project. BUG-DSH-005 fixed. |
| DSH-012 | Tab icons have tooltips/labels | Tabs identifiable (staging shows icon-only tabs) — UI finding if not | PASS | re_dsh001_hover | Retest 22/10/2026: all 6 tabs have title and aria-label (Recency and Renewals, Unread Notices, Unsigned Timesheets, Safety Actions, Exams, Project Tasks). BUG-DSH-001 fixed. |
| DSH-013 | Recency items for Service Account show 'No Expiry' | Check whether 'No Expiry' is correct vs empty status | PASS |  | All 8 Service Account items (Dangerous Goods ... Type Rating Renewal) show grey dot + 'No Expiry'. Consistent, but question for Jon: should items with no record say 'Not recorded' instead? |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
