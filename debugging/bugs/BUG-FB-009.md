# BUG-FB-009: File Browser: clicking an .svg shows an error popup with the raw SVG code

| Field | Value |
|---|---|
| Checklist row | `ATT-029` in `checklists/96-xc-attachments.md` |
| Module | File Browser |
| Severity | Low |
| DataHangar version | v2.0.123 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome desktop, 1600 px |
| Status | New |
| Found / session | 24/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. File Browser > BETA TEST ONLY Folder: upload BETA_TEST_ONLY_drawing.svg
2. Click it

## Expected
An image preview (like .png) or the "cannot be previewed" box with Download.

## Actual
An error popup whose message is the file's SVG markup (<svg xmlns=... <rect ...>). The preview image also fails to load (naturalWidth 0).

## Evidence
- Screenshot: none (see Actual)
- Raw results: file-type campaign, checklist `checklists/96-xc-attachments.md`

## Suspected cause (optional)
filebrowser_servefile sends .svg as application/octet-stream and the preview code shows text replies as errors (same pattern as BUG-FB-003).

## Suggested fix
Fix together with BUG-FB-003; if SVG preview is wanted, serve it safely (see BUG-ATT-001).

## Test data involved
BETA TEST ONLY files from the attachment campaign, all deleted on 24/10/2026.

## Related
BUG-ATT-001, BUG-ATT-002, BUG-ATT-003, BUG-NOT-002, BUG-PD-012, BUG-FB-003, BUG-SUP-003

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
