# BUG-SUP-001: Support has no page Help (?); Escape doesn't close New Ticket, but a click outside closes it and wipes everything typed

| Field | Value |
|---|---|
| Checklist row | `SUP-S02` in `checklists/27-support.md` |
| Module | Support |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > Support
2. Look for a Help (?) button
3. Click New Ticket, type a Subject and Bug Report fields
4. Press Escape
5. Click once on the dark area outside the popup
6. Click New Ticket again

## Expected
Help (?) exists. Escape closes the popup (or nothing loses data). An outside click either does nothing or asks before throwing away typed text.

## Actual
No Help button. Escape does nothing. One outside click closes New Ticket, and reopening it shows every field empty (openNewTicketModal clears them), so the typed ticket is lost with no warning.

## Evidence
- Screenshot: `screenshots/BUG-SUP-001-1.png`, `screenshots/BUG-SUP-001-2.png`
- Console / network errors: none

## Suspected cause (optional)
No keydown handler; overlay click calls closeNewTicketModal without a dirty check; openNewTicketModal resets all fields.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
