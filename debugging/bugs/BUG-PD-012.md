# BUG-PD-012: Personnel Details > Files: opening a file shows 'File Access Error' with the file's contents as the message

| Field | Value |
|---|---|
| Checklist row | `PD-025` in `checklists/12-personnel-details.md` |
| Module | Personnel Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Not fixed (retested 24/10/2026 v2.0.123) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. All Personnel > BETA TEST ONLY Lowperm > Files tab
2. Browse > BETA_TEST_ONLY_pd.txt (30 B) > Upload
3. Click the file name in the list

## Expected
The file opens in a preview (or a new tab).

## Actual
An error popup 'File Access Error' appears whose message is the text inside the file ('BETA TEST ONLY personnel file'). No preview opens. After pressing OK on that error, the Delete file button does nothing: the confirm popup is set active but stays hidden (display:none), so nothing appears until the page is reloaded. The page also has two buttons with id confirm-modal-ok-btn (#alert-modal and #confirm-modal).

## Evidence
- Screenshot: `screenshots/BUG-PD-012-1.png`, `screenshots/BUG-PD-012-2.png`
- Console / network errors: none

## Suspected cause (optional)
The preview call probably expects JSON and treats the raw file response as an error message.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
| 24/10/2026 | v2.0.123 | Not fixed | BETA_TEST_ONLY_notes.txt (person 277) still shows "File Access Error" with the file's text. Images preview, PDF opens one tab, empty .txt/.html/others show "cannot be previewed". Downloads byte-identical. See checklist 96-xc-attachments. Screenshot `screenshots/BUG-PD-012-rt123-files.png`. |
