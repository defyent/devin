# BUG-PD-001: personneldetails/index.js is truncated: ReferenceError getPickerMod on every load

| Field | Value |
|---|---|
| Checklist row | `PD-S01` in `checklists/12-personnel-details.md` |
| Module | Personnel Details / My Account |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Click Service Account (top bar) or open any person from All Personnel
2. Watch the console

## Expected
No console errors.

## Actual
`ReferenceError: getPickerMod is not defined` at `templates2/personneldetails/index.js?v=2.0.111:13734`. The file's last line is `window.getPickerMode = getPickerMod` (cut off; should be `getPickerMode;`), so `window.getPickerMode` is never set and anything after it never runs.

## Evidence
- Screenshot: n/a
- Console / network errors: ReferenceError: getPickerMod is not defined (index.js:13734:24)

## Suspected cause (optional)
`personneldetails/index.js` last line truncated during build/deploy; restore `window.getPickerMode = getPickerMode;` and check nothing else is missing from the end of the file.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
