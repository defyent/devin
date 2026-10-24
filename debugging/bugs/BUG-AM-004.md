# BUG-AM-004: Permission level dropdown shows bare codes 'WA' and 'G' next to full labels

| Field | Value |
|---|---|
| Checklist row | `AM-020` in `checklists/04-access-manager.md` |
| Module | Access Manager > Manage User Permissions |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Access Manager > a user's 'N Permissions' badge
2. Look at the level dropdown for Personnel Details (also Flight Schedule, Dashboard, DFR)

## Expected
Every level has a readable label, e.g. 'Read/Write All - Can view and modify all data', 'Group - level defined by group membership' (as in the Help).

## Actual
Options: 'Read Only All - ...', 'WA', 'Read Only Own - ...', 'Write Own - ...', 'G'. Retest 22/10/2026 (v2.0.113, accessmanager/index.js?v=2.0.113): fixed. Every option on all 76 permission cards has a label, e.g. 'WA=Read/Write All - ...' and 'G=Group - Level defined by group membership'. No bare codes.

## Evidence
- Screenshot: `screenshots/BUG-AM-004-1.png`, `screenshots/BUG-AM-004-2.png`
- Console / network errors: none

## Suspected cause (optional)
Label map in accessmanager JS is missing WA and G (falls back to the code).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
