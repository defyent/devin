# BUG-STZ-003: Time Zone settings: the Example preview shows MM/DD/YYYY for every date format except DD/MM/YYYY

| Field | Value |
|---|---|
| Checklist row | `STZ-002` in `checklists/33-settings-timezone.md` |
| Module | Settings: Time Zone |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings and Tools > Configuration > Time Zone.
2. In "Choose a date format", pick YYYY-MM-DD, then DD.MM.YYYY.
3. Look at the Example preview.

## Expected
The preview follows the chosen format: 2026-10-21, then 21.10.2026.

## Actual
Both show "10/21/2026" (US order). Picking DD/MM/YYYY again shows 21/10/2026. Also, 4 of the 10 date formats (DD MMM YYYY, MMM DD, YYYY, DD MMMM YYYY, MMMM DD, YYYY) and 3 of the 5 time formats (all the 12-hour ones) are listed but greyed out, with no explanation of why. The time preview also ignores the choice: with HH:mm:ss picked it still shows "13:20". Once saved, the format itself does work: the header clocks show "02:20:15 (2026-10-22)" and Daily Flight Record shows "2026-10-21 08:30:00".

## Evidence
- Screenshot: `screenshots/BUG-STZ-003-1.png`
- Console / network errors: none

## Suspected cause (optional)
The preview picker seems to fall back to the browser locale for any format it does not know. The disabled options look deliberate (the type-in picker can't parse them?), but the page doesn't say so.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
