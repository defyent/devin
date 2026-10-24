# BUG-NOT-005: Notices: only one attachment can be added per save

| Field | Value |
|---|---|
| Checklist row | `ATT-012` in `checklists/96-xc-attachments.md` |
| Module | Notices |
| Severity | Low |
| DataHangar version | v2.0.123 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome desktop, 1600 px |
| Status | New |
| Found / session | 24/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Notices > BETA TEST ONLY Notice (#1189) > Edit
2. Try to select several files in Attachment

## Expected
Several files can be selected at once (as in Flight Details, Personnel Details and Support).

## Actual
The file picker only accepts one file. Adding 18 files took 18 separate Edit > Save rounds. Create New Notice has the same single-file input.

## Evidence
- Screenshot: `screenshots/BUG-NOT-005-1.png` (Notice edit form)
- Raw results: file-type campaign, checklist `checklists/96-xc-attachments.md`

## Suspected cause (optional)
#editNoticeFile (and the new-notice input) has no multiple attribute.

## Suggested fix
Add multiple to both inputs and send each file as files[].

## Test data involved
BETA TEST ONLY files from the attachment campaign, all deleted on 24/10/2026.

## Related
BUG-ATT-001, BUG-ATT-002, BUG-ATT-003, BUG-NOT-002, BUG-PD-012, BUG-FB-003, BUG-SUP-003

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
