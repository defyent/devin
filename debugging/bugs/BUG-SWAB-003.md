# BUG-SWAB-003: Weight & Balance Configs shows a debug "Performance" timing panel to users

| Field | Value |
|---|---|
| Checklist row | `SWAB-S01` in `checklists/35-settings-wab.md` |
| Module | Settings: Weight and Balance |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Configuration > Weight and Balance Configs.
2. Look at the page.

## Expected
No developer timing panel.

## Actual
A visible 176x394 px "Performance" panel shows "settings_wabconfigs_json Permission Check 0.8ms ... Server Wait 177.0ms ... response kb 1", with a × to close it.

## Evidence
- Screenshot: `screenshots/BUG-SWAB-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
A debug/perf overlay is left switched on in the production template.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
