# BUG-ATT-002: No file-type check on any upload: .exe, .html and anything else is accepted; Notices "Supported formats" isn't enforced

| Field | Value |
|---|---|
| Checklist row | `ATT-034` in `checklists/96-xc-attachments.md` |
| Module | Attachments (all modules) |
| Severity | Medium |
| DataHangar version | v2.0.123 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome desktop, 1600 px |
| Status | New |
| Found / session | 24/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Upload BETA_TEST_ONLY_program.exe (fake, MZ header) and BETA_TEST_ONLY_page.html in Flight Details, Personnel Details, Notices, Safety Reports, Support, File Browser and Waypoints
2. In Notices > Edit, read the note under Attachment

## Expected
Either a clear allow-list (with a message when a file is refused) or a documented "any type" policy. Notices should only accept the formats it lists.

## Actual
All 7 systems accept every one of the 18 test types, including .exe, .html, .heic, .mp4 and a zero-byte .txt. Notices says "Supported formats: PDF, DOC, DOCX, TXT, JPG, JPEG, PNG" but accepted and saved .exe, .zip, .html, .svg, .mp4, .heic, .xlsx etc. without a message.

## Evidence
- Screenshot: `screenshots/BUG-ATT-002-1.png` (Notices edit after saving the .exe)
- Raw results: file-type campaign, checklist `checklists/96-xc-attachments.md`

## Suspected cause (optional)
No server-side extension/MIME check; the Notices file input has no accept list and the label is text only.

## Suggested fix
Decide the policy. If restricted: check extension and content on the server, refuse with a clear message, and set accept= on the inputs. If not: remove the misleading Notices label. Either way see BUG-ATT-001 for safe serving.

## Test data involved
BETA TEST ONLY files from the attachment campaign, all deleted on 24/10/2026.

## Related
BUG-ATT-001, BUG-ATT-002, BUG-ATT-003, BUG-NOT-002, BUG-PD-012, BUG-FB-003, BUG-SUP-003

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
