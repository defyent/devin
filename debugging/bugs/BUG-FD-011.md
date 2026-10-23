# BUG-FD-011: History labels lock and unlock differently ("Locked: No > Yes" vs "Status: Locked > Unlocked")

| Field | Value |
|---|---|
| Checklist row | `FD-037` in `checklists/07-flight-details.md` |
| Module | Flight Details |
| Severity | Low |
| DataHangar version | v2.0.121 |
| Account / permission level | Service Account (datahangar), Flight Details A and temporary WL |
| Browser / width | Chrome desktop (UTC time zone), 1600 px |
| Status | New |
| Found / session | 23/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. As a WL user lock a Complete flight, then unlock it
2. Open History

## Expected
Both changes use the same label, e.g. "Status: Complete > Complete & Locked" and "Status: Complete & Locked > Complete".

## Actual
23/10/2026 v2.0.121, #42909: locking logs "Locked: No > Yes" (#753), unlocking logs "Status: Locked > Unlocked" (#754). Cosmetic. Not retested since.

## Evidence
- Screenshot: n/a
- Console / network errors: none

## Suspected cause (optional)
Lock and unlock are logged by different code paths with different field names.

## Test data involved
Flight #42909 (BETA TEST ONLY, ZK-BTO)

## Related
BUG-FD-006

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|

