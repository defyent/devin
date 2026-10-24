# BUG-FD-008: Unlocking a Complete & Locked flight wipes its leg route, leg PIC, leg passengers and manifest

| Field | Value |
|---|---|
| Checklist row | `FD-030` in `checklists/07-flight-details.md` |
| Module | Flight Details |
| Severity | High |
| DataHangar version | v2.0.120 |
| Account / permission level | Service Account (datahangar), Flight Details A and temporary WL |
| Browser / width | Chrome desktop (UTC time zone), 1600 px |
| Status | Fixed (verified 23/10/2026 v2.0.121) |
| Found / session | 23/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Give a user Flight Details = WL (Access Manager, permission 214)
2. Open a Complete & Locked flight with full leg data (#42909: Wellington Airport > Wellington Airport, PIC + pax BETA TEST ONLY Grpuser, manifest Grpuser)
3. Flight Status > Complete > Save Changes
4. Reload and check the legs, manifest and History

## Expected
Only the status changes (Locked > Unlocked); all leg, manifest and meter data is kept.

## Actual
Found 23/10/2026 on v2.0.120: saved with no popup; leg depart, dest and pic_id became null, pax_ids [] and the manifest empty; only times/totals kept. History #748 logged "Leg 1 Departure Wellington Airport > (empty)", Destination and PIC likewise. Retest 23/10/2026 (v2.0.121): fixed. Lock then unlock as WL kept every leg, PIC, passenger, manifest and meter value; History #754 shows only "Status Locked > Unlocked".

## Evidence
- Screenshot: `screenshots/BUG-FD-008-1.png`, `screenshots/BUG-FD-008-2.png`
- Console / network errors: none

## Suspected cause (optional)
Locked mode disables the leg inputs (enableReadOnlyMode(..., "locked_wl")), disabled fields are not submitted, and the server rebuilt legs/manifest from the request. v2.0.121 re-enables the fields just for the submit (fd L8248-8254).

## Test data involved
Flight #42909 (BETA TEST ONLY, ZK-BTO)

## Related
BUG-FD-006

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
| 23/10/2026 | v2.0.121 | Fixed | See Actual |
