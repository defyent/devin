# BUG-DSH-001: Dashboard side tabs are icon-only with no tooltip or label

| Field | Value |
|---|---|
| Checklist row | `DSH-012` in `checklists/05-dashboard.md` |
| Module | Dashboard |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open Dashboard from the sidebar
2. Hover each of the 6 tabs above the right-hand panel

## Expected
Each tab has a tooltip/label (Recency and Renewals, Unread Notices, Unsigned Timesheets, Safety Actions, Exams, Project Tasks).

## Actual
Tabs show only Material icons (update, notifications, assignment_late, assignment, quiz, checklist); no title, aria-label or tooltip. Users must click each to find out what it is; screen readers read the icon ligature names. Retest 22/10/2026 (v2.0.111): fixed.

## Evidence
- Screenshot: `screenshots/BUG-DSH-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
Tab buttons render the icon only; add title + aria-label (or a short text label).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
