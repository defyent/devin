# BUG-IPFORM-001: Pushed form uses the wrong template and loses widget data

| Field | Value |
|---|---|
| Checklist row | `IPFORM-001` |
| Module | Flight forms / upload |
| Severity | High |
| Environment | Simulator iPad Pro 13" M5, iOS 26.5 |
| App version | 1.0.13 (Build 46) |
| DataHangar version | v2.0.123 (`https://stresstest.datahangar.net`) |
| Status | Open |
| Found / session | 2026-10-24, https://app.devin.ai/sessions/8b79cff4b7ea4af2989164dd937fd4e4 |

## Steps to reproduce
1. In the app, attach `BETA TEST ONLY Form` to flight `#42914`.
2. Fill 8 of the form's 12 fields and save the form.
3. Push the flight and inspect the attached form on the website.

## Expected
The website shows the `BETA TEST ONLY Form` with the values entered in the app.

## Actual
The app pushes `BETA TEST ONLY Form`, but the website shows `QA Post-Flight Report` with only 1 of 11 fields populated (the automatically populated Flight Date). The app-entered widget values are absent.

## Evidence
- `screenshots/IPFORM-003_web_wrong_form.png`
- `IPJSON-001_export.json`

## Suspected cause (optional)
Suspected (not fully traced): the template IDs the app syncs and sends don't match the server's form_template_id values, so the server attaches a different template (the app's 'BETA TEST ONLY Form' became 'QA Post-Flight Report' on the website) and the widget data doesn't fit it.

## Code pointer
`FlightUploadService`, `forms_json`.

## Test data involved
Flight `#42914`; `BETA TEST ONLY Form`; 8 fields filled.

## Related
BUG-IPFORM-002 (duplicate/phantom forms), BUG-IPSMS-001 (Safety Report forms lost).
