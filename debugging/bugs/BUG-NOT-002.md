# BUG-NOT-002: Notice Details: clicking a .txt attachment does nothing (no preview, no download)

| Field | Value |
|---|---|
| Checklist row | `NOT-006` in `checklists/17-notices.md` |
| Module | Notices |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Not fixed (retested 24/10/2026 v2.0.123) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Safety > Notices > open 'BETA TEST ONLY Notice' (#1189)
2. Click the attached file BETA_TEST_ONLY_notice.txt

## Expected
Preview popup (or download) for the attachment.

## Actual
Nothing appears. The browser sends HEAD and GET to noticedetails_servefile&doc_id=453, but no preview, error or download is shown.

## Evidence
- Screenshot: `screenshots/BUG-NOT-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
handleFilePreview() in notices/noticedetails.js treats any text/plain response that isn't 'Ok' as an error message (showErrorModal('File Access Error', text)), so a real .txt file's content is taken as an error and the preview never opens. Same pattern as BUG-PD-012.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
| 24/10/2026 | v2.0.123 | Not fixed | Clicking BETA_TEST_ONLY_notes.txt on notice #1189 still does nothing (no popup, tab or download). Other types now tested: images (png/jpg/gif/webp/svg) preview, PDFs open in a new tab, empty .txt/.html/office/zip/exe/mp4 show "cannot be previewed" + Download. All 18 types serve byte-identical. See checklist 96-xc-attachments. Screenshot `screenshots/BUG-NOT-002-rt123-files.png`. |
