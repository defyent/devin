# BUG-NAV-001: Leaving a page with unsaved changes gives no warning; edits are lost

| Field | Value |
|---|---|
| Checklist row | `NAV-015` in `checklists/02-shell-navigation.md` |
| Module | Shell (main) / Personnel Details |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Click Service Account (top bar) to open My Personnel Details
2. Type in Middle Name: Save Changes becomes enabled
3. Hover Flight Operations in the sidebar and click Dashboard

## Expected
Guide §3: 'The current page has unsaved changes...' modal with Cancel (stay) and Continue (leave).

## Actual
Dashboard opens immediately, no modal; the typed change is discarded. Retest 22/10/2026 (v2.0.112): still fails. The shell side now works: main/index.js has checkIframeDirtyState() (window.isDirty() or window.parent.setDirty()), and with setDirty(true) forced the Unsaved Changes modal shows, Cancel stays with the edit kept and Continue leaves. But personneldetails never reports dirty: after typing in Middle Name (Save Changes enabled) it has no window.isDirty and never calls parent.setDirty, so the sidebar and top-bar still leave with no prompt and the edit is lost. Retest 2 22/10/2026 after the personneldetails update: fixed. personneldetails now exposes window.isDirty() (false when clean, true after typing). With an unsaved edit, the sidebar and top-bar both show the Unsaved Changes modal. Cancel stays with the edit kept, Continue leaves without saving, and reload triggers the beforeunload prompt. A clean page or a just-saved page leaves with no prompt.

## Evidence
- Screenshot: `screenshots/BUG-NAV-001-1.png`, `screenshots/BUG-NAV-001-2.png`, `screenshots/BUG-NAV-001-3.png`
- Console / network errors: none

## Suspected cause (optional)
Shell is fixed; personneldetails/index.js has to expose window.isDirty() or call window.parent.setDirty(true/false) when its form changes and after save.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
