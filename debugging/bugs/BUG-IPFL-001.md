# BUG-IPFL-001: Flight ID badges and labels add thousands separators

| Field | Value |
|---|---|
| Checklist row | `IPFL-001` |
| Module | Flights / flight ID display |
| Severity | UI |
| Environment | Simulator iPad Pro 13" M5, iOS 26.5 |
| App version | 1.0.13 (Build 46) |
| DataHangar version | v2.0.123 (`https://stresstest.datahangar.net`) |
| Status | Open |
| Found / session | 2026-10-24, https://app.devin.ai/sessions/8b79cff4b7ea4af2989164dd937fd4e4 |

## Steps to reproduce
1. Open Download Flights and inspect the flight ID badges.
2. Inspect flight ID labels in the flight list, flight details, and communications views.

## Expected
Flight IDs display as ungrouped identifiers, for example `#8893` and `#42914` without locale-dependent numeric formatting.

## Actual
Some badges and labels apply thousands separators (for example `#8,893`, `#43,913`, and `#42,914`), while adjacent text shows the same IDs without separators.

## Evidence
- `screenshots/IPDL-download_list_week.png`

## Suspected cause (optional)
SwiftUI interpolation of an `Int` in a localized `Text`/`Label` string applies numeric grouping.

## Code pointer
`DownloadFlightsSheet`, `FlightsView`, `FlightDetailView`, and `CommsView`; results note `#\(apiId)` patterns.

## Test data involved
Flight IDs including 8893, 43913, and 42914.

## Related
None (chat channel names use the same number formatting).
