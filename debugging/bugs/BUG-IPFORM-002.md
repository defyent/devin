# BUG-IPFORM-002: Pull creates phantom form instances and pushed updates are ignored

| Field | Value |
|---|---|
| Checklist row | `IPFORM-002` |
| Module | Flight forms / sync |
| Severity | High |
| Environment | Simulator iPad Pro 13" M5, iOS 26.5 |
| App version | 1.0.13 (Build 46) |
| DataHangar version | v2.0.123 (`https://stresstest.datahangar.net`) |
| Status | Open |
| Found / session | 2026-10-24, https://app.devin.ai/sessions/8b79cff4b7ea4af2989164dd937fd4e4 |

## Steps to reproduce
1. On flight `#42914`, pull the server's attached form data into the app.
2. Compare the app's Forms tab with the website's Forms tab.
3. Push the flight again and compare the website form's update state.

## Expected
The app shows the single form instance present on the website, and a pushed update to that instance is reflected on the website.

## Actual
After pulling, the app shows three local instances (IDs 198, 199, and 200): two `BETA TEST ONLY Form` instances at 0/9 fields and one `QA Post-Flight Report` at 1/11 fields. The website has exactly one form, `QA Post-Flight Report`. On a later push, the app's `updated` entries are silently ignored; the website form was not updated by that push.

## Evidence
- `screenshots/IPFORM-004_app_3_phantom_forms.png`
- `screenshots/IPFORM-dup_web_forms_tab.png`

## Suspected cause (optional)
TBD.

## Test data involved
Flight `#42914`; local form instance IDs 198, 199, and 200.

## Related
`BUG-IPFORM-001`
