# BUG-IPFL-002: Flights with a Student PIC cannot be pushed from the app

| Field | Value |
|---|---|
| Checklist row | `IPFL-002` |
| Module | Flight sync / personnel |
| Severity | High |
| Environment | Simulator iPad Pro 13" M5, iOS 26.5 |
| App version | 1.0.13 (Build 46) |
| DataHangar version | v2.0.123 (`https://stresstest.datahangar.net`) |
| Status | Open |
| Found / session | 2026-10-24, https://app.devin.ai/sessions/8b79cff4b7ea4af2989164dd937fd4e4 |

## Steps to reproduce
1. Create web flight `#42915` with Aaron Fisher as PIC; Aaron Fisher is a Student and is accepted as a PIC on the website.
2. Add a leg on the website with Aaron Fisher as PIC and a valid weight, then pull the flight into the app.
3. Push the flight from the app.

## Expected
The app pushes the leg successfully and preserves Aaron Fisher as the PIC.

## Actual
The push fails with `Leg 1: the PIC must be a crew member or student. Please choose a crew member, then save again.` The app's local leg represents Aaron Fisher as `MANUAL_ENTRY`, so the server rejects the PIC even though the website accepts this Student as a PIC.

## Evidence
- `screenshots/IPFL-002_42915_details.png`
- `screenshots/IPFL-002_42915_push_rejected_pic.png`
- `screenshots/IPFL-002_web_aaron_fisher_student.png`

## Suspected cause (optional)
`SyncService.syncPersonnel` requests crew personnel and filters to `crew == 'Y'`, excluding Student personnel. On pull, `FlightSyncService.resolveCockpit` resolves the PIC through the manifest and `pic_pax_name` fallback; when the person is absent from the synced personnel, the app represents the PIC as `MANUAL_ENTRY`, which the server rejects on push.

## Test data involved
Flight `#42915`; PIC Aaron Fisher (Student).

## Related
None.
