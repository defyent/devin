# BUG-FB-005: File Browser: Read/Write Access groups are not kept after Update Document

| Field | Value |
|---|---|
| Checklist row | `FB-007` in `checklists/22-file-browser.md` |
| Module | File Browser |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > File Browser, open edit (Configure File) on a file
2. Tick Read Access 'BETA TEST ONLY Group'
3. Update Document
4. Open edit on the same file again

## Expected
BETA TEST ONLY Group is still ticked and the file is limited to that group.

## Actual
No group is ticked. The request sent read_access with the group (id 103), but the popup shows nothing ticked when reopened. Moving the file to Root (Parent Folder) did save.

## Evidence
- Screenshot: `screenshots/BUG-FB-005-1.png`
- Console / network errors: none

## Suspected cause (optional)
Either the server does not store read_access/write_access, or handleOpenConfigModal() does not tick the saved groups. Needs a server-side check.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
