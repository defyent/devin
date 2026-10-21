# BUG-NAV-001: Leaving a page with unsaved changes gives no warning; edits are lost

| Field | Value |
|---|---|
| Checklist row | `NAV-015` in `checklists/02-shell-navigation.md` |
| Module | Shell (main) / Personnel Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Click Service Account (top bar) to open My Personnel Details
2. Type in Middle Name: Save Changes becomes enabled
3. Hover Flight Operations in the sidebar and click Dashboard

## Expected
Guide §3: 'The current page has unsaved changes...' modal with Cancel (stay) and Continue (leave).

## Actual
Dashboard opens immediately, no modal; the typed change is discarded.

## Evidence
- Screenshot: `screenshots/BUG-NAV-001-1.png`
- Console / network errors: none

## Suspected cause (optional)
Dirty-state check in `main/index.js` menu click handler is not wired to Personnel Details (or not at all).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
