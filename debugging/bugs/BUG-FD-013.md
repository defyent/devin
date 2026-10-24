# BUG-FD-013: Flight Details Files: clicking a PDF opens it in two new tabs

| Field | Value |
|---|---|
| Checklist row | `ATT-002` in `checklists/96-xc-attachments.md` |
| Module | Flight Details |
| Severity | Low |
| DataHangar version | v2.0.123 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome desktop, 1600 px |
| Status | New |
| Found / session | 24/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Details #42903 > Files
2. Click BETA_TEST_ONLY_scan.pdf once

## Expected
One new tab (or an in-page preview).

## Actual
Two new tabs open with flightdetails_servefile for the same PDF, every click. Seen for both test PDFs. Personnel Details, Notices, Support and File Browser open one tab.

## Evidence
- Screenshot: none (see Actual)
- Raw results: file-type campaign, checklist `checklists/96-xc-attachments.md`

## Suspected cause (optional)
Probably both the row click handler and handleFilePreview() call window.top.open() (not confirmed in the code).

## Suggested fix
Open the PDF once, from one handler, or preview it in an iframe like Waypoints.

## Test data involved
BETA TEST ONLY files from the attachment campaign, all deleted on 24/10/2026.

## Related
BUG-ATT-001, BUG-ATT-002, BUG-ATT-003, BUG-NOT-002, BUG-PD-012, BUG-FB-003, BUG-SUP-003

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
