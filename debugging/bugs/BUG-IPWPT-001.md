# BUG-IPWPT-001 — Code-less server waypoints show blank titles; editing them stores 0,0 coordinates; edits are local-only

- **Module:** iPad app — Configuration > Waypoints
- **Severity:** Low/Medium (confusing duplicates; risk of 0,0 navigation point)
- **App:** DataHangar Flight 1.0.13 (46), iPad Pro 13" Simulator iOS 26.5

## Steps
1. Sync All. Configuration > Waypoints.
2. Tap the first entry whose title is blank (subtitle `NZAA`).

## Actual
- 6 synced entries (BTQA, BTQC, NZAA, NZCH, NZWR, ZZZQ) have empty `code` and no lat/lon; the list uses code as the title, so rows are blank and sort first. NZAA/NZCH therefore appear twice.
- Edit sheet shows Code empty, Name `NZAA`, coordinates `0 0.0000 N / 0 0.0000 E`. Saving in DDM/DMS writes `0.000000, 0.000000` (Gulf of Guinea) instead of leaving blank.
- `save()` only updates the local `WaypointStore`; nothing is sent to DataHangar, and the next Sync All may replace it (no warning that edits are local).

## Expected
Fall back to name when code is empty; keep blank coordinates blank; tell the user edits are device-only (or push them).

## Website comparison
The website (Settings and Tools > Waypoint Locations) holds these same name-only waypoints (BTQA 1 flight, BTQC 0, NZAA 3, NZCH 2, NZWR 1) and lists them by Name, so they are readable there. The app syncs them correctly; the defect is the app's Code-as-title display and the 0,0 save. The duplicates themselves are server data quality (website offers Scan Duplicates).

## Evidence
- evidence/IPWPT-005_website_waypoints.png
- evidence/IPWPT-002_waypoints_list.png
- evidence/IPWPT-003_blank_code_nzaa.png
