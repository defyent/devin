# BUG-SUP-002: Support New Ticket: Ctrl+V doesn't paste a screenshot, though the error message tells you to use Ctrl+V

| Field | Value |
|---|---|
| Checklist row | `SUP-003` in `checklists/27-support.md` |
| Module | Support |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > Support > New Ticket
2. Copy a screenshot, click in the Description box and press Ctrl+V
3. Also click Paste Screenshot without clipboard permission

## Expected
Ctrl+V adds the screenshot to Attachments (as the clipboard error message says).

## Actual
Nothing is attached on Ctrl+V. The page has no paste listener; only the Paste Screenshot button (navigator.clipboard.read) works, and its error says 'use Ctrl+V to paste'.

## Evidence
- Screenshot: `screenshots/BUG-SUP-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
sup_index.js has no 'paste' event handler.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
