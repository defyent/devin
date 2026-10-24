# BUG-STZ-002: Time Zone settings page has no Help (?)

| Field | Value |
|---|---|
| Checklist row | `STZ-S02` in `checklists/33-settings-timezone.md` |
| Module | Settings: Time Zone |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Configuration > Time Zone.
2. Look for the Help (?) in the page header.

## Expected
A Help (?) in the header, like Flight Schedule and Daily Flight Record settings have, that explains the date format, time format and picker type options.

## Actual
There is no Help button or help icon anywhere on the page.

## Evidence
- Screenshot: `screenshots/BUG-STZ-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
The settings_timezone template has no helpBtn or help modal.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
