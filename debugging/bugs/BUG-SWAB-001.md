# BUG-SWAB-001: Weight & Balance Configs: no Help (?), and Escape does not close popups

| Field | Value |
|---|---|
| Checklist row | `SWAB-S02` in `checklists/35-settings-wab.md` |
| Module | Settings: Weight and Balance |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Configuration > Weight and Balance Configs.
2. Look for the Help (?) in the header.

## Expected
A Help (?) that explains the Draft > Approve > Master workflow.

## Actual
There is no Help button on the page. Also, Escape does not close the "New Draft Revision" confirmation; only Cancel closes it.

## Evidence
- Screenshot: `screenshots/BUG-SWAB-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
The template has no help button or help modal.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
