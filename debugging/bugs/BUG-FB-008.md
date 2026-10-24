# BUG-FB-008: Files attached to a waypoint also appear in the File Browser Home folder

| Field | Value |
|---|---|
| Checklist row | `ATT-030` in `checklists/96-xc-attachments.md` |
| Module | File Browser |
| Severity | Medium |
| DataHangar version | v2.0.123 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome desktop, 1600 px |
| Status | New |
| Found / session | 24/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings > Waypoints > ZZZQ > Files: upload some files
2. Open File Browser > Home

## Expected
Waypoint attachments only appear on the waypoint (or in a clearly named Waypoints folder, with the waypoint's access rules).

## Actual
All 18 files uploaded to waypoint ZZZQ were listed in File Browser Home (file_513 to file_530, group Internal, no folder). Deleting them from the waypoint removed them from File Browser as well. Anyone with File Browser access can see, download or edit waypoint files.

## Evidence
- Screenshot: `screenshots/BUG-FB-008-1.png` (File Browser Home showing the waypoint files)
- Raw results: file-type campaign, checklist `checklists/96-xc-attachments.md`

## Suspected cause (optional)
Waypoint uploads are stored in the File Browser table with no folder and aren't filtered out of filebrowser_json.

## Suggested fix
Filter waypoint (and any other module) attachments out of File Browser, or put them in a dedicated folder with the right permissions.

## Test data involved
BETA TEST ONLY files from the attachment campaign, all deleted on 24/10/2026.

## Related
BUG-ATT-001, BUG-ATT-002, BUG-ATT-003, BUG-NOT-002, BUG-PD-012, BUG-FB-003, BUG-SUP-003

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
