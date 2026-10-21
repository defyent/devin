# BUG-DFR-002: Daily Flight Record: Clear Filters unticks every status (lists Open, Cancelled and Deleted flights), and the date fields show today's date when no date filter is applied

| Field | Value |
|---|---|
| Checklist row | `DFR-008` in `checklists/09-daily-flight-record.md` |
| Module | Daily Flight Record |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Sidebar > Flight Operations > Daily Flight Record
2. Expand Advanced Filters: Completed and Complete Locked are ticked, Date From/To both show 21/10/2026 (today) but the list has flights from other days
3. Type Rego ZK-SIM (or any filter), press Enter
4. Click Clear Filters

## Expected
Clear Filters goes back to the default view: Completed + Complete Locked, no other filters. Empty date filters show empty fields (or the dates shown are actually applied).

## Actual
Clear Filters unticks all five status pills, so the list shows every status, including Open and Deleted flights (e.g. #9476 Open, #42902 Deleted), and the filter badge disappears. The Date From/To fields show today's date on load and after clearing, yet no date filter is applied.

## Evidence
- Screenshot: `screenshots/BUG-DFR-002-1.png`, `screenshots/BUG-DFR-002-2.png`
- Console / network errors: none

## Suspected cause (optional)
Clear resets status checkboxes to unchecked instead of the defaults, and an empty status set is treated as 'all'. The date pickers display a default value that is not sent as a filter.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
