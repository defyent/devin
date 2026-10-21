# BUG-SWAB-005: W&B Configs: two revisions show the same number ("Rev 5") until another import renumbers them

| Field | Value |
|---|---|
| Checklist row | `SWAB-003` in `checklists/35-settings-wab.md` |
| Module | Settings: Weight and Balance |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Weight and Balance Configs (iPad App).
2. Import an exported config (.json) to make a new draft, approve it and set it as Master.
3. Keep working on the drafts in Revision History (review, Copy To) without reloading.
4. Look at Revision History, then Import another file.

## Expected
Each revision has its own number, and numbers don't change.

## Actual
Revision History showed two rows labelled "Rev 5": the Master (config #12) and a Pending draft (config #13). They held different aircraft (1 and 2). After the next Import, the Pending one was relabelled "Rev 6" and the new import became "Rev 7". It's easy to approve or set the wrong draft as Master.

## Evidence
- Screenshot: `screenshots/BUG-SWAB-005-1.png`, `screenshots/BUG-SWAB-005-2.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
