# BUG-IPFL-003 — Leg times pulled from DataHangar ("HH:MM:SS") display as the current time; editing overwrites them

- **Module:** iPad app — Flights > Leg Detail > Route & Times (also time engine)
- **Severity:** High (wrong times shown; one tap overwrites real times with "now"; flight/engine durations not computed)
- **App:** DataHangar Flight 1.0.13 (46), iPad Pro 13" Simulator iOS 26.5; website v2.0.123

## Steps
1. Push a flight with leg times from the app (or create one on the website), then Pull / download it so the app stores the server copy.
2. Open the flight > Leg 1.

## Expected
Start/Takeoff/Landing/Stop show the server times (#42914: 23:07, 23:08, 00:07, 01:07).

## Actual
All four show the current device time (02:13 AM in 12h mode / 02:14 in 24h mode). The local store still holds "23:07:00" etc.

## Cause
`FlightSyncService` maps `engineStart`/`flightStart`/`flightStop`/`engineStop` verbatim; the server returns `HH:MM:SS`.
`TimeUtils.parseHHMM` accepts only `HH:MM` (2 parts) or `HHMM`; 3 parts -> nil. `TimeUtils.dateFromHHMM` then returns `Date()`, which the leg DatePicker binds to, so the picker shows "now" and any interaction commits "now" via `phase.onCommit(hhmmFromDate(...))`.
`TimeUtils.durationMinutes` (used by FlightTimeEngine / upload clockHours) relies on the same parser.

## Fix direction
Accept `HH:MM:SS` in `parseHHMM` (use first two parts), and/or normalise to `HH:MM` in `FlightSyncService` when mapping legs. Treat `00:00:00` from the server as blank where the website does.

## Evidence
- screenshots/IPCFG-004_12h_leg_times_now.png
- screenshots/IPFL-010_leg_times_show_now_24h.png
