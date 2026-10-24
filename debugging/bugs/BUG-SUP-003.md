# BUG-SUP-003: Support ticket: clicking a .txt attachment shows an 'Error' popup containing the file's text

| Field | Value |
|---|---|
| Checklist row | `SUP-005` in `checklists/27-support.md` |
| Module | Support |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Not fixed (retested 24/10/2026 v2.0.123) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > Support > open ticket #8
2. Click the attachment BETA_TEST_ONLY_sup.txt

## Expected
File preview shows the text, or the file downloads.

## Actual
An 'Error' popup opens whose message is the file content ('BETA TEST ONLY attachment'); the File Preview popup behind it is blocked until OK is clicked. Same pattern as BUG-FB-003.

## Evidence
- Screenshot: `screenshots/BUG-SUP-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
Text preview response is passed to showErrorModal.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
| 24/10/2026 | v2.0.123 | Not fixed | On new ticket #11, BETA_TEST_ONLY_notes.txt still shows an "Error" popup with the file text. Images show inline and preview, PDFs open a tab, empty .txt/.html/others show "cannot be previewed" + Download. Ticket deleted afterwards. See checklist 96-xc-attachments. Screenshot `screenshots/BUG-SUP-003-rt123-files.png`. |
