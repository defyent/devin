# BUG-SWP-005: Waypoint Files list shows the Uploaded date as MM/DD/YYYY and Size N/A for every file

| Field | Value |
|---|---|
| Checklist row | `ATT-027` in `checklists/96-xc-attachments.md` |
| Module | Settings: Waypoints |
| Severity | Low |
| DataHangar version | v2.0.123 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome desktop, 1600 px |
| Status | New |
| Found / session | 24/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings > Waypoints > ZZZQ > Files
2. Upload any file and look at the Uploaded and Size columns

## Expected
Uploaded in the org date format (24/10/2026) and the real file size.

## Actual
Uploaded shows 10/24/2026 for every file and Size shows N/A for all 18 files, including a 40 KB PDF.

## Evidence
- Screenshot: `screenshots/BUG-SWP-005-1.png` (Waypoint files list)
- Raw results: file-type campaign, checklist `checklists/96-xc-attachments.md`

## Suspected cause (optional)
The list uses a fixed US date format and the list_files rows don't give a usable size.

## Suggested fix
Format the date with the org date setting and return/display the file size (KB/MB).

## Test data involved
BETA TEST ONLY files from the attachment campaign, all deleted on 24/10/2026.

## Related
BUG-ATT-001, BUG-ATT-002, BUG-ATT-003, BUG-NOT-002, BUG-PD-012, BUG-FB-003, BUG-SUP-003

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
