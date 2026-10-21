# BUG-DSH-003: Dashboard recency item opens Personnel Details on the wrong tab (Personal Details instead of Recency and Renewals)

| Field | Value |
|---|---|
| Checklist row | `DSH-006` in `checklists/05-dashboard.md` |
| Module | Dashboard / Personnel Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Open Dashboard from the sidebar
2. Recency and Renewals tab (first tab) is shown
3. Click 'Flight Review'

## Expected
Own Personnel Details opens on the Recency and Renewals tab with Flight Review highlighted.

## Actual
Personnel Details opens (URL has alertname_id=3) but the Personal Details tab is active; user has to find the Recency tab manually. Page also throws 'getPickerMod is not defined' (BUG-PD-001), which may be what stops the tab switch.

## Evidence
- Screenshot: `screenshots/BUG-DSH-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
alertname_id param not used to select the Recency tab, or the tab-switch code never runs because index.js is truncated (BUG-PD-001). Retest after BUG-PD-001 is fixed.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
