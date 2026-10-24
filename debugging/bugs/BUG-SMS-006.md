# BUG-SMS-006: Safety Report document link for a deleted file shows the server's file path

| Field | Value |
|---|---|
| Checklist row | `ATT-016` in `checklists/96-xc-attachments.md` |
| Module | Safety Reports |
| Severity | Low |
| DataHangar version | v2.0.123 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome desktop, 1600 px |
| Status | New |
| Found / session | 24/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Safety Report #2060 > Files: upload a file and note its id
2. Delete it, then open /index.pl?action=smsreportdetails_downloaddocument&doc_id=<id>

## Expected
A plain "Document not found" message.

## Actual
"Error: Document not found at /var/www/datahangar/D..." - the reply includes the server's install path. Other modules say "File not found" or "Invalid file ID".

## Evidence
- Screenshot: none (see Actual)
- Raw results: file-type campaign, checklist `checklists/96-xc-attachments.md`

## Suspected cause (optional)
A Perl die message (with "at <file> line N") is returned to the browser.

## Suggested fix
Catch the error and return a plain message with a 404 status.

## Test data involved
BETA TEST ONLY files from the attachment campaign, all deleted on 24/10/2026.

## Related
BUG-ATT-001, BUG-ATT-002, BUG-ATT-003, BUG-NOT-002, BUG-PD-012, BUG-FB-003, BUG-SUP-003

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
