# BUG-EXM-002: Exam dates ignore the org format: 'Oct 22, 2026' in Exam Builder and '10/22/2026 01:46 AM' in Exam Instances batches

| Field | Value |
|---|---|
| Checklist row | `EXM-S04` in `checklists/29-exams.md` |
| Module | Exams |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Training > Exam Builder
2. Read the Created column (e.g. new 'BETA TEST ONLY Exam')

## Expected
22/10/2026 (DD/MM/YYYY as set in Settings > Time Zone).

## Actual
'Oct 22, 2026' (existing exams show 'May 11, 2026'). Exam Instances > Browse Batches shows '10/22/2026 01:46 AM' (US MM/DD, 12-hour).

## Evidence
- Screenshot: `screenshots/BUG-EXM-002-1.png`, `screenshots/BUG-EXM-002-2.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
