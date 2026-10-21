# BUG-NOT-001: Notices has no page Help (?), and the Create New Notice popup ignores Escape

| Field | Value |
|---|---|
| Checklist row | `NOT-S02` in `checklists/17-notices.md` |
| Module | Notices |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Safety > Notices
2. Look for the (?) Help button
3. Click New Notice, press Escape

## Expected
A Help (?) button; Escape closes the New Notice popup.

## Actual
No Help button in the header. The Create New Notice popup stays open after Escape (x and Cancel work).

## Evidence
- Screenshot: `screenshots/BUG-NOT-001-1.png`, `screenshots/BUG-NOT-001-2.png`
- Console / network errors: none

## Suspected cause (optional)
notices/index.js has no Escape handler for #newNoticeModalOverlay.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
