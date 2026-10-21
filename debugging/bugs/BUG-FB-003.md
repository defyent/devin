# BUG-FB-003: File Browser: clicking a .txt file shows 'File Access Error' with the file's own text

| Field | Value |
|---|---|
| Checklist row | `FB-006` in `checklists/22-file-browser.md` |
| Module | File Browser |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > File Browser
2. Search 'BETA_TEST_ONLY'
3. Click BETA_TEST_ONLY_notice-GCKLCWJK.txt

## Expected
The file opens in the preview (or downloads).

## Actual
An error popup titled 'File Access Error' shows the file content ('BETA TEST ONLY notice attachment - please ignore'). No preview opens. Same cause as BUG-NOT-002 and BUG-PD-012.

## Evidence
- Screenshot: `screenshots/BUG-FB-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
filebrowser/index.js handleFilePreview(): any text/plain response that is not 'Ok' is treated as an error message, so every real .txt file is shown as an error.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
