# BUG-PERM-001: Sidebar lists modules the user has no permission for (all lead to Access Denied)

| Field | Value |
|---|---|
| Checklist row | `PERM-007` in `checklists/90-xc-permissions.md` |
| Module | Shell (main) sidebar |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Open (confirmed 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Access Manager: create user, give 0 roles / 0 permissions, set credentials, Activate
2. Log in as that user
3. Open the sidebar and click each item

## Expected
Links to modules the user has no permission for are hidden from the sidebar (Jon confirmed 22/10/2026). Only modules the user can open are listed (Roster Builder, Timesheets etc. are already hidden, so filtering exists).

## Actual
17 items listed (Dashboard, Flight Schedule, Active Flights, DFR, Roster Viewer, All Personnel, Flight and Duty, Notices, Recency and Renewals, Safety Reports, Hazard Register, Settings and Tools, File Browser, Form Browser, Task Tracker, Reports, Support); every one shows 'Access Denied'. The landing page (Dashboard) is also Access Denied. Retest 22/10/2026 (v2.0.112): unchanged. betatest_low still sees all 17 module links and each gives Access Denied, including the Dashboard landing page. Still needs a product decision (NAV-019 expects visible links). Retest 22/10/2026 (v2.0.113, accessmanager/index.js?v=2.0.113): unchanged. betatest_low still sees every module link in the sidebar (Dashboard, Flight Schedule, Active Flights, Daily Flight Record, Roster Viewer, All Personnel, Flight and Duty, Notices, Recency and Renewals, Safety Reports, Hazard Register, Settings and Tools, File Browser, Form Browser, Task Tracker, Reports, Support), and the Dashboard landing page shows Access Denied. Still needs a product decision. Product decision 22/10/2026 (Jon): links the user can't open must be hidden, so this is a confirmed bug and NAV-019 now expects hidden links.

## Evidence
- Screenshot: `screenshots/BUG-PERM-001-1.png`, `screenshots/BUG-PERM-001-2.png`, `screenshots/BUG-PERM-001-3.png`, `screenshots/BUG-PERM-001-4.png`
- Console / network errors: none

## Suspected cause (optional)
Sidebar build in main/index.pl does not check the permission types used by each module's own access check. Note: checklist NAV-019 (from the user guide) expects the link to stay visible and show Access Denied, so this may be by design - needs a product decision.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
