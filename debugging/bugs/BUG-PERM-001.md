# BUG-PERM-001: Sidebar lists modules the user has no permission for (all lead to Access Denied)

| Field | Value |
|---|---|
| Checklist row | `PERM-007` in `checklists/90-permissions.md` |
| Module | Shell (main) sidebar |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Access Manager: create user, give 0 roles / 0 permissions, set credentials, Activate
2. Log in as that user
3. Open the sidebar and click each item

## Expected
Only modules the user can open are listed (Roster Builder, Timesheets etc. are already hidden, so filtering exists).

## Actual
17 items listed (Dashboard, Flight Schedule, Active Flights, DFR, Roster Viewer, All Personnel, Flight and Duty, Notices, Recency and Renewals, Safety Reports, Hazard Register, Settings and Tools, File Browser, Form Browser, Task Tracker, Reports, Support); every one shows 'Access Denied'. The landing page (Dashboard) is also Access Denied.

## Evidence
- Screenshot: `screenshots/BUG-PERM-001-1.png`, `screenshots/BUG-PERM-001-2.png`
- Console / network errors: none

## Suspected cause (optional)
Sidebar build in main/index.pl does not check the permission types used by each module's own access check.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
