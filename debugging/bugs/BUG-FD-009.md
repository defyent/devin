# BUG-FD-009: A user without lock rights (not WL) can lock a flight; the server accepted status complete_locked

| Field | Value |
|---|---|
| Checklist row | `FD-029` in `checklists/07-flight-details.md` |
| Module | Flight Details |
| Severity | Medium |
| DataHangar version | v2.0.120 |
| Account / permission level | Service Account (datahangar), Flight Details A and temporary WL |
| Browser / width | Chrome desktop (UTC time zone), 1600 px |
| Status | Fixed (verified 23/10/2026 v2.0.121) |
| Found / session | 23/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Log in as a Flight Details A/W user without WL (allFlightData.user_permission.can_unlock false)
2. Open a Complete flight; the Complete & Locked card is hidden
3. In the console click .status-card[data-status=complete_locked] (or post status=complete_locked) and Save Changes

## Expected
The server refuses: only WL users can lock or unlock.

## Actual
Found 23/10/2026 on v2.0.120: the server saved complete_locked, and the same user then could not undo it ("You do not have permission to modify locked flights"). Retest 23/10/2026 (v2.0.121): fixed. Refused with "Only users with lock permission can lock a flight. Please choose Complete instead of Complete & Locked."; status stayed complete.

## Evidence
- Screenshot: `screenshots/BUG-FD-009-1.png`
- Console / network errors: none

## Suspected cause (optional)
Lock rights were only enforced by hiding the status card; the save did not check can_unlock.

## Test data involved
Flight #42909 (BETA TEST ONLY, ZK-BTO)

## Related
BUG-FD-006

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
| 23/10/2026 | v2.0.121 | Fixed | See Actual |
