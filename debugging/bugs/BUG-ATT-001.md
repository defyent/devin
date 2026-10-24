# BUG-ATT-001: Uploaded .html and .svg files are served inline from the DataHangar site (stored XSS risk)

| Field | Value |
|---|---|
| Checklist row | `ATT-033` in `checklists/96-xc-attachments.md` |
| Module | Attachments (all modules) |
| Severity | High |
| DataHangar version | v2.0.123 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome desktop, 1600 px |
| Status | New |
| Found / session | 24/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Details #42903 > Files: upload BETA_TEST_ONLY_page.html and BETA_TEST_ONLY_drawing.svg
2. Open /index.pl?action=flightdetails_servefile&file_id=<id> for each one

## Expected
Uploaded HTML/SVG is never rendered as a page on the DataHangar site: send it as a download (Content-Disposition: attachment, X-Content-Type-Options: nosniff), or block these types, or sanitise SVG.

## Actual
flightdetails_servefile, personneldetails_servefile, settings_waypoints_servefile and noticedetails_servefile return .html as text/html and .svg as image/svg+xml with Content-Disposition: inline, on the same site as the app. filebrowser_servefile returns .html as text/html inline. smsreportdetails_downloaddocument shows .svg inline in a new tab. Any user who can upload a file could put script in an HTML/SVG file that runs with the viewer's DataHangar login. Not exploited: the test files had no script in them. Support (support_serve_file) serves .html as application/octet-stream, which is safe.

## Evidence
- Screenshot: none (see Actual)
- Raw results: file-type campaign, checklist `checklists/96-xc-attachments.md`

## Suspected cause (optional)
The serve endpoints set Content-Type from the file extension and always use inline. No type allow-list on upload (see BUG-ATT-002).

## Suggested fix
Serve user uploads with Content-Disposition: attachment unless the type is on a safe inline list (png, jpg, gif, webp, pdf); add X-Content-Type-Options: nosniff and Content-Security-Policy: sandbox on file responses; never serve text/html or image/svg+xml inline.

## Test data involved
BETA TEST ONLY files from the attachment campaign, all deleted on 24/10/2026.

## Related
BUG-ATT-001, BUG-ATT-002, BUG-ATT-003, BUG-NOT-002, BUG-PD-012, BUG-FB-003, BUG-SUP-003

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
