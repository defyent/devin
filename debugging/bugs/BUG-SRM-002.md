# BUG-SRM-002: Risk Matrix Settings on a phone: the page scrolls sideways and "+ Add Level" is cut off

| Field | Value |
|---|---|
| Checklist row | `SRM-S05` in `checklists/43-settings-riskmatrix.md` |
| Module | Settings: Risk Matrix |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Risk Matrix.
2. Make the window 390 px wide.

## Expected
No sideways page scrolling. The matrix list wraps or stacks, and the Add Level buttons are fully visible.

## Actual
The page is 419 px wide (there is a horizontal scrollbar). The matrix list row (.matrix-nav) is 774 px wide, and "+ Add Level" is cut off at the right edge. The grid itself scrolls inside its own box, which is fine.

## Evidence
- Screenshot: `screenshots/BUG-SRM-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
.matrix-nav lays matrix items out in one non-wrapping row, and the level section headers don't wrap below 768 px.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
