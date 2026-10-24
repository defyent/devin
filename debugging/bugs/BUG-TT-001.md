# BUG-TT-001: Task Tracker: Escape doesn't close Help or Add Project

| Field | Value |
|---|---|
| Checklist row | `TT-S02` in `checklists/25-task-tracker.md` |
| Module | Task Tracker |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > Task Tracker
2. Click the (?) Help icon, press Escape
3. Click Add Project, press Escape

## Expected
Escape closes the popup, like x, Got it! and clicking outside do.

## Actual
Both popups stay open. tasktracker/index.js has no Escape/keydown handler for the modal.

## Evidence
- Screenshot: `screenshots/BUG-TT-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
No keydown listener in tasktracker/index.js closeModal/openModal.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
