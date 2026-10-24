# BUG-FD-012: Flight Details Files: .txt shows its text in a "Required Information" alert; empty .txt and .html show error messages

| Field | Value |
|---|---|
| Checklist row | `ATT-002` in `checklists/96-xc-attachments.md` |
| Module | Flight Details |
| Severity | Medium |
| DataHangar version | v2.0.123 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome desktop, 1600 px |
| Status | New |
| Found / session | 24/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Details #42903 > Files: upload BETA_TEST_ONLY_notes.txt, BETA_TEST_ONLY_empty.txt and BETA_TEST_ONLY_page.html
2. Click each file

## Expected
A preview of the text or the "cannot be previewed, use Download" box with a working Download button.

## Actual
notes.txt: a "Required Information" alert whose message is the file's own text ("BETA TEST ONLY text file - please ignore Line 2"). empty.txt: "File not accessible". page.html: "An unexpected server error occurred while accessing the file." No preview or Download is offered for any of them, although the files download fine with flightdetails_downloadfile.

## Evidence
- Screenshot: `screenshots/BUG-FD-012-1.png` (notes.txt alert)
- Screenshot: `screenshots/BUG-FD-012-2.png` (page.html error)
- Raw results: file-type campaign, checklist `checklists/96-xc-attachments.md`

## Suspected cause (optional)
handleFilePreview() fetches the file and treats any text/plain or text/html response as an error message. Same pattern as BUG-PD-012, BUG-NOT-002, BUG-FB-003 and BUG-SUP-003.

## Suggested fix
Have the servefile endpoint return errors with a non-2xx status (or a JSON error), and decide preview from the status code, not the content type. Show text files in a <pre> or offer Download.

## Test data involved
BETA TEST ONLY files from the attachment campaign, all deleted on 24/10/2026.

## Related
BUG-ATT-001, BUG-ATT-002, BUG-ATT-003, BUG-NOT-002, BUG-PD-012, BUG-FB-003, BUG-SUP-003

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
