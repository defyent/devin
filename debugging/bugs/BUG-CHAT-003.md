# BUG-CHAT-003: Chat image button: non-images are ignored with no message; SVG/TIFF/HEIC preview then fail on Send

| Field | Value |
|---|---|
| Checklist row | `ATT-032` in `checklists/96-xc-attachments.md` |
| Module | Chat |
| Severity | Low |
| DataHangar version | v2.0.123 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome desktop, 1600 px |
| Status | New |
| Found / session | 24/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Chat > channel beta-test-only-files > image button
2. Pick a .pdf, .txt or .zip; then pick .svg, .tiff or .heic and press Send

## Expected
The picker only offers supported images, and anything else gets a clear message straight away.

## Actual
PDF, ZIP, CSV, DOCX, XLSX, TXT, HTML, EXE and MP4: nothing happens, no message. SVG, TIFF and HEIC: a preview strip appears, but Send gives "Error Sending Message: Invalid image format" (SVG) or posts nothing (TIFF, HEIC). PNG, JPG, GIF and WebP send and display correctly and download byte-identical.

## Evidence
- Screenshot: none (see Actual)
- Raw results: file-type campaign, checklist `checklists/96-xc-attachments.md`

## Suspected cause (optional)
handleImageFile() silently returns when file.type isn't image/*; the server only accepts some image types, and the client doesn't know which.

## Suggested fix
Set accept="image/png,image/jpeg,image/gif,image/webp" on #chat-file-input and show a message for other files before the preview.

## Test data involved
BETA TEST ONLY files from the attachment campaign, all deleted on 24/10/2026.

## Related
BUG-ATT-001, BUG-ATT-002, BUG-ATT-003, BUG-NOT-002, BUG-PD-012, BUG-FB-003, BUG-SUP-003

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
