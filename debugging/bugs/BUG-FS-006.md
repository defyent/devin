# BUG-FS-006: Flight Schedule month view is slow: flightschedule_json takes ~1.6 s and rendering 2,500 events ~4.5 s

| Field | Value |
|---|---|
| Checklist row | `FS-034` in `checklists/06-flight-schedule.md` |
| Module | Flight Schedule |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Flight Schedule > Schedule Only
2. Click Month (October 2026, range 28/09-08/11)
3. Measure in DevTools Network: index.pl?action=flightschedule_json&start=2026-09-28&end=2026-11-09

## Expected
Server response < 500 ms; month view usable in about 1-2 s.

## Actual
Request 1,590 ms (first byte 844 ms); 2,493 events take 4.5 s from click to render. Page freezes while rendering. Retest 22/10/2026 (v2.0.114, assets ?v=2.0.114): improved but still over target. Schedule Only > Month (October 2026): flightschedule_json&start=2026-09-28&end=2026-11-09 took 1,072-1,369 ms total (first byte 365-384 ms, 511,679 bytes), 2,497 events rendered, no errors. Was 1,590 ms (first byte 844 ms). Server time is still over the 500 ms target. Second retest 22/10/2026 (v2.0.114): month JSON 1,286-1,344 ms total, first byte 576-633 ms, 511,380 bytes, 2,497 events, no Content-Encoding (not gzipped). Still over 500 ms. Third retest 22/10/2026 (v2.0.115): partly fixed. JSON is now gzipped and 465,003 bytes (was 511,380). Direct repeat requests take 364-373 ms (under 500 ms), but the first request took 835 ms, and in the browser the month load took 777 ms with the first byte at 635 ms. Fourth retest 22/10/2026 (v2.0.117): unchanged since v2.0.115. Gzipped, 465,003 bytes; repeat requests 367-370 ms, first request 866 ms; in the browser 777 ms total, first byte 635 ms.

## Evidence
- Screenshot: `screenshots/BUG-FS-006-1.png`, `screenshots/BUG-FS-006-2.png`, `screenshots/BUG-FS-006-3.png`, `screenshots/BUG-FS-006-4.png`
- Console / network errors: none

## Suspected cause (optional)
Whole 6-week range returned with full event details in one JSON call and every event rendered; consider a summary per day for month view, indexes on flight start/end, or lazy loading of 'more' events.

## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
