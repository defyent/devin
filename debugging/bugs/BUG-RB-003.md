# BUG-RB-003: Roster Builder: copy/paste still works with violation checking ON

| Field | Value |
|---|---|
| Checklist row | `RB-006` in `checklists/14-roster-builder.md` |
| Module | Roster Builder |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Roster Builder, select a draft
2. Turn the violations toggle ON (badge VIOLATIONS FOUND)
3. Click a cell with a shift, Ctrl+C
4. Click an empty cell, Ctrl+V

## Expected
Copy/paste is not allowed while violation checking is on (documented behaviour), with a message saying why.

## Actual
'Copied 1 cell(s)' then 'Successfully pasted 1 shift(s)' - the shift is pasted with no warning, even onto a day that then shows a violation.

## Evidence
- Screenshot: `screenshots/BUG-RB-003-1.png`, `screenshots/BUG-RB-003-2.png`
- Console / network errors: none

## Suspected cause (optional)
rosterbuilder/index.js copy handler (around line 4528-4555) and paste never check violationsEnabled; only an empty selection is rejected.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
