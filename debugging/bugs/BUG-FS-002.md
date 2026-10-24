# BUG-FS-002: Esc does not end copy/paste mode on the Flight Schedule - the next click + Ctrl+V creates another flight

| Field | Value |
|---|---|
| Checklist row | `FS-021` in `checklists/06-flight-schedule.md` |
| Module | Flight Schedule |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | Fixed (verified 22/10/2026) |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Schedule > Enable Live Edit
2. Select a flight, Ctrl+C, click an empty slot, Ctrl+V, Paste
3. Toast: '... press Escape to finish.' Press Esc
4. Click another empty slot, press Ctrl+V

## Expected
Esc ends paste mode; Ctrl+V afterwards does nothing.

## Actual
No feedback on Esc; the click shows 'Press Ctrl+V to paste the flight here' and Ctrl+V creates another flight (created #42906). Users can create unwanted live flights. Retest 22/10/2026 (v2.0.114, assets ?v=2.0.114): fixed. Live Edit > select #42909 > Ctrl+C > click 24/10 14:00 > Ctrl+V > Copy Flight Options > Paste created #42912 ('Flight pasted successfully... or press Escape to finish'). Esc now shows 'Copy/paste finished. Ctrl+V will no longer paste.' Clicking another slot and pressing Ctrl+V afterwards creates nothing (only 'Click on the schedule to choose where to paste the flight.'). #42912 deleted afterwards.

## Evidence
- Screenshot: `screenshots/BUG-FS-002-1.png`
- Console / network errors: none

## Suspected cause (optional)
Escape keydown handler does not clear the copied-flight clipboard state (or is not bound inside the schedule iframe).

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
