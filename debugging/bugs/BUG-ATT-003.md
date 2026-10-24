# BUG-ATT-003: File names are changed differently in each module; accents and symbols are stripped ("résumé" becomes "rsum")

| Field | Value |
|---|---|
| Checklist row | `ATT-035` in `checklists/96-xc-attachments.md` |
| Module | Attachments (all modules) |
| Severity | Low |
| DataHangar version | v2.0.123 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome desktop, 1600 px |
| Status | New |
| Found / session | 24/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Upload "BETA TEST ONLY résumé #1 (copy).pdf" in each attachment area
2. Look at the name in the file list and in the downloaded file

## Expected
The original name is kept (or at least shown) everywhere, and the same rule is used in every module.

## Actual
Flight Details: BETA_TEST_ONLY_rsum_1_copy.pdf (spaces to _, é, #, ( ) removed). Personnel Details, Safety Reports, File Browser and Waypoints: same stripping plus a random suffix, e.g. BETA_TEST_ONLY_rsum_1_copy-WSFEKWRS.pdf, BETA_TEST_ONLY_image-POHUNQIA.png. Notices and Support keep the original name exactly. Names with accents (common in NZ Māori place and person names) lose letters.

## Evidence
- Screenshot: `screenshots/BUG-ATT-003-1.png` (Flight Details list with the stripped name)
- Raw results: file-type campaign, checklist `checklists/96-xc-attachments.md`

## Suspected cause (optional)
Each upload handler has its own filename sanitiser that drops non-ASCII characters.

## Suggested fix
Store a safe internal name but keep and display the original (UTF-8) name, and use it in Content-Disposition (filename*=UTF-8''...) on download. Use one shared helper.

## Test data involved
BETA TEST ONLY files from the attachment campaign, all deleted on 24/10/2026.

## Related
BUG-ATT-001, BUG-ATT-002, BUG-ATT-003, BUG-NOT-002, BUG-PD-012, BUG-FB-003, BUG-SUP-003

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
