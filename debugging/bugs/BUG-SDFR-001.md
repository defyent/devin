# BUG-SDFR-001: Daily Flight Record Settings loads a colorpicker.js that does not exist (404 in the console)

| Field | Value |
|---|---|
| Checklist row | `SDFR-S01` in `checklists/32-settings-dfr.md` |
| Module | Settings: Daily Flight Record |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Operations > Daily Flight Record.
2. Open DevTools > Console.

## Expected
The page loads with no console errors.

## Actual
GET /templates2/settings_dfr/colorpicker.js returns 404, and the console logs "Failed to load resource: the server responded with a status of 404". The page has no colour controls, so this looks like a leftover script tag copied from Flight Schedule Settings.

## Evidence
- Screenshot: `screenshots/BUG-SDFR-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
The settings_dfr template has a <script src="colorpicker.js"> but that file is not in templates2/settings_dfr/. Remove the tag.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
