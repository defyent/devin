# BUG-FB-004: File Browser: Escape doesn't close the Create New Folder or Configure File popups

| Field | Value |
|---|---|
| Checklist row | `FB-S03` in `checklists/22-file-browser.md` |
| Module | File Browser |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > File Browser > Make Folder (create_new_folder)
2. Type a name
3. Press Escape

## Expected
The popup closes (as on Safety Reports, Hazard Register and Settings and Tools).

## Actual
Both popups stay open on Escape (Create New Folder, Configure File).

## Evidence
- Screenshot: `screenshots/BUG-FB-004-1.png`
- Console / network errors: none

## Suspected cause (optional)
filebrowser/index.js has no keydown/Escape handler.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
