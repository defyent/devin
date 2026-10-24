# BUG-FB-006: File Browser: deleting a folder fails with 'Invalid Action: filebrowser_deletefolder'

| Field | Value |
|---|---|
| Checklist row | `FB-008` in `checklists/22-file-browser.md` |
| Module | File Browser |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > File Browser > Make Folder 'BETA TEST ONLY Folder'
2. Click edit on the folder, then Delete
3. Confirm

## Expected
The folder is deleted.

## Actual
Error popup 'Delete Failed: Invalid Action: filebrowser_deletefolder' and the folder stays. The confirm popup also says 'delete this file' for a folder.

## Evidence
- Screenshot: `screenshots/BUG-FB-006-1.png`
- Console / network errors: none

## Suspected cause (optional)
filebrowser/index.js performDeleteFolder() posts action filebrowser_deletefolder, which the server does not handle.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
