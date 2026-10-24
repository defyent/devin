# BUG-LOG-002: Logout throws JS error removeChild; Esc doesn't close the Log Out confirm

| Field | Value |
|---|---|
| Checklist row | `LOG-016` in `checklists/01-login-auth.md` |
| Module | Shell (main) |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Click Logout in the top bar
2. Press Esc (nothing happens)
3. Click Log Out

## Expected
Esc closes the confirm (CON-015); no console errors.

## Actual
Esc ignored (see POP-02). On Log Out the console logs `Failed to execute 'removeChild' on 'Node': The node to be removed is not a child of this node.` Logout itself works. Retest 22/10/2026 (v2.0.112): fixed. Esc closes the Log Out confirm, and Log Out completes with no console errors.

## Evidence
- Screenshot: n/a
- Console / network errors: pageerror removeChild

## Suspected cause (optional)


## Test data involved
none

## Related
POP-02

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
