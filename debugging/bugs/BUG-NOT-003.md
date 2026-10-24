# BUG-NOT-003: Settings and Tools hub: 'Notices' card has no links

| Field | Value |
|---|---|
| Checklist row | `NOT-010` in `checklists/17-notices.md` |
| Module | Notices |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Administration > Settings and Tools
2. Find the 'Notices' card

## Expected
Card links to a Notices setting, or no card at all.

## Actual
The card says 'Manage system-wide notices and announcements.' but has no links or buttons. Every other card has at least one link.

## Evidence
- Screenshot: `screenshots/BUG-NOT-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
Confirm whether this card is meant to be there.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
