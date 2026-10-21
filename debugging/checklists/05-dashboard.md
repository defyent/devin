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
| DSH-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | VIS-06 | Dashboard has no Help (?) button - already tracked as external VIS-06 |
| DSH-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | No popups on Dashboard (clicks navigate to other modules) |
| DSH-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | DATE-02 | Headers show 'Wed, Oct 21, 2026' (US month-first) although Time Zone is DD/MM/YYYY; already known as DATE-02 |
| DSH-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | 390 px: single column, no horizontal scroll, calendar usable. Performance panel covers content (BUG-PERF-001) |
| DSH-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | See DSH-001 |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| DSH-001 | Load without Dashboard permission | Every widget shows 'Access Denied' | PASS |  | 0-permission user: whole Dashboard replaced by one 'Access Denied: You do not have permission to access the Dashboard feature' card (not per-widget, but no data leak / no JS error) |
| DSH-002 | My Roster calendar: < > Today | Month changes; shifts in shift colours; Today returns | PASS |  | > Nov 2026, < Oct, < Sep, Today back to Oct 2026; today (21) highlighted |
| DSH-003 | Click another day | On Duty / My Flights headers change to that date; 'Not viewing today' tag | PASS |  | Click 15: 'On Duty for Thu, Oct 15, 2026' + 'My Flights for Thu, Oct 15, 2026', both tagged 'Not viewing today' |
| DSH-004 | On Duty list | Matches published roster for that day, grouped by shift | PASS |  | On Duty grouped by shift with shift colours and times (Sick Leave, Office Hours, Morning 06:00-18:00, Afternoon 14:00-02:00). Cross-check vs Roster Viewer in 13 |
| DSH-005 | My Flights list; click a flight | Opens Flight Details; Back returns to Dashboard | FAIL | dsh005_list | BUG-DSH-004: As BETA TEST ONLY Second (PIC of #42910 on 22/10), at local 10:38 on 22/10 the Dashboard opened My Flights on "Wed, Oct 21, 2026" with "No flights scheduled", and Today kept it on 21/10. After clicking 22 in My Roster, it showed "Not viewing today" with #42910 (13:00-14:00, ZK-BTO, Role PIC). Clicking the flight opens Flight Details 42910, and Back goes to the Dashboard. |
| DSH-006 | Tab: Recency and Renewals | Grouped by status; click opens Recency tab in own Personnel Details | FAIL | BUG-DSH-003 | Recency tab lists items under 'PILOT LICENSES RENEWALS' group; clicking 'Flight Review' opens own Personnel Details (alertname_id=3) but on the Personal Details tab, not Recency and Renewals. Also throws getPickerMod error (BUG-PD-001) |
| DSH-007 | Tab: Unread Notices (badge) | Badge matches header bell; click opens notice | PASS |  | Unread Notices tab badge 99+ = header bell 99+; clicking 'Fuel Price Adjustment' opens Notice Details (notice_id=30) |
| DSH-008 | Tab: Unsigned Timesheets | Click opens Timesheets tab on that day | PASS | dsh008_open | As BETA TEST ONLY Second, the Dashboard Unsigned Timesheets tab (assignment_late badge 1) lists "OC 21/10/2026 Not signed". Clicking it opens Personnel Details on the Timesheets tab (roster_id=108409). |
| DSH-009 | Tab: Safety Actions | Click opens the report | PASS | dsh009_two_open | On report #2063, admin created action "BETA TEST ONLY action for DSH-009" assigned to BETA TEST ONLY Second. Logged in as Second, the Dashboard Safety Actions tab has badge 1 and lists the action. Clicking it opens SMS Report Details for #2063. |
| DSH-010 | Tab: Exams | Click opens Exams tab | PASS | dsh010_two_open | Assigned "BETA TEST ONLY Exam" to BETA TEST ONLY Second in Exam Instances. As Second, the Dashboard Exams tab has badge 1 and lists the exam as Assigned 22/10/2026. Clicking it opens Personnel Details on the Exams tab (person_id=278&tab=exams). |
| DSH-011 | Tab: Project Tasks | Click opens the project | FAIL | dsh011_grp_two_open | BUG-DSH-005: task in project BETA TEST ONLY TT DSH shows in the assignee's Project Tasks tab (badge 1). Clicking it as Grpuser (Task Tracker WG, in the project group) opens project_id=14 but shows "No projects yet". As Second (no Task Tracker permission) it gives Access Denied. |
| DSH-012 | Tab icons have tooltips/labels | Tabs identifiable (staging shows icon-only tabs) — UI finding if not | FAIL | BUG-DSH-001 | 6 tabs are icon-only (update, notifications, assignment_late, assignment, quiz, checklist) with no title / aria-label / tooltip |
| DSH-013 | Recency items for Service Account show 'No Expiry' | Check whether 'No Expiry' is correct vs empty status | PASS |  | All 8 Service Account items (Dangerous Goods ... Type Rating Renewal) show grey dot + 'No Expiry'. Consistent, but question for Jon: should items with no record say 'Not recorded' instead? |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
