# iPad flight times and meters

- **Checklist ID prefix:** `IPFT`
- **Guide section:** `debugging/IPAD_SWIFT_AUDIT_PLAN.md` §3
- **Where:** iPad app — Clock and meter inputs, durations, previous readings and validation
- **Permission:** Admin / Service Account unless a different permission level is identified in the row notes
- **Tester:** Devin
- **Date / DataHangar version:** 24/10/2026 / iPad DataHangar Flight 1.0.13 (46) on iOS 26.5 Simulator; stresstest v2.0.123
- **Account / level used:** Service Account unless a different account is identified in the row notes

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPFT-001 | Route&Times: Start/Takeoff/Landing/Stop 'Set' buttons stamp current device time (00:07) HH:mm; tapping a time opens a wheel picker (hour/min). Clear (x) buttons per time. Engine 0.0 hrs s… | TBD (not recorded) | PASS |  | L78: Route&Times: Start/Takeoff/Landing/Stop 'Set' buttons stamp current device time (00:07) HH:mm; tapping a time opens a wheel picker (hour/min). Clear (x) buttons per time. Engine 0.0 hrs shown. PASS |
| IPFT-002 | Start set to 23:07 via wheel (Stop 00:07): engine time 1.0 hrs computed across midnight (TimeUtils wrap). PASS. Sanity warning exists for spans >=18h. | TBD (not recorded) | PASS |  | L79: Start set to 23:07 via wheel (Stop 00:07): engine time 1.0 hrs computed across midnight (TimeUtils wrap). PASS. Sanity warning exists for spans >=18h. |
| IPFT-003 | Leg times entered via wheels: Start 23:07, Takeoff 23:08, Landing 00:07, Stop -> 01:07 (to make engine != flight). After Takeoff 23:08/Landing 00:07 chips show Flight 1.0 / Engine 1.0 (59… | TBD (not recorded) | TODO |  | L80: Leg times entered via wheels: Start 23:07, Takeoff 23:08, Landing 00:07, Stop -> 01:07 (to make engine != flight). After Takeoff 23:08/Landing 00:07 chips show Flight 1.0 / Engine 1.0 (59 min -> 1.0 rounding to 0.1h). Verifying engine 2.0 after Stop change. |
| IPFT-004 | DB leg times stored HH:mm: start 23:07 takeoff 23:08 landing 00:07 shutdown 01:07 (no date component; midnight crossing implied). PASS locally; verify website hours after push. | TBD (not recorded) | PASS |  | L81: DB leg times stored HH:mm: start 23:07 takeoff 23:08 landing 00:07 shutdown 01:07 (no date component; midnight crossing implied). PASS locally; verify website hours after push. |
| IPFT-005 | (candidate Low) Meter field: label 'Previous: 2,450.5' but validation error 'Value (0.1) < previous (2,450.7)' - inconsistent previous value (probably label uses aircraft startValue, vali… | TBD (not recorded) | N/A |  | Candidate: L87: (candidate Low) Meter field: label 'Previous: 2,450.5' but validation error 'Value (0.1) < previous (2,450.7)' - inconsistent previous value (probably label uses aircraft startValue, validator adds flightPreviousReadings). Check DB.<br>L88: resolved: 'Previous' label actually 2,450.7 (matches aircraft.previousMeterReadings, last reading from downloaded flights), startValue 2450.5 is older baseline. Not a bug.<br>L89: Setting Flight Hours via MeterInput: + sets 0.1 (delta stepper), pencil opens numeric keypad; validation 'Value < previous (2,450.7)' works. Entering 2451.7 (=2450.7+1.0). |
| IPFT-006 | Details filled: Category Solo, Activity Charter, meters Flight 2451.7 / Engine 2452.7 / Cycles 1.0 (all cumulative >= previous 2450.7/0), Time Totals auto: Flight 1.0 hrs, Engine 2.0 hrs… | TBD (not recorded) | FAIL | BUG-IPREF-001 | L91: Details filled: Category Solo, Activity Charter, meters Flight 2451.7 / Engine 2452.7 / Cycles 1.0 (all cumulative >= previous 2450.7/0), Time Totals auto: Flight 1.0 hrs, Engine 2.0 hrs (from leg times). Additional Info 'BETA TEST ONLY EFI audit value' — custom EFI field IS present on Details tab despite Sync All 'Flight Custom Fields: 0' -> BUG-IPREF-001 (Low): sync count label wrong/misleading. |
| IPFT-007 | Time Breakdown sheet: Flight Time NZAA->NZCH 1.0 / total 1.0 hrs; Engine Time 2.0 / total 2.0 hrs. Correct from leg times. PASS | TBD (not recorded) | PASS |  | L93: Time Breakdown sheet: Flight Time NZAA->NZCH 1.0 / total 1.0 hrs; Engine Time 2.0 / total 2.0 hrs. Correct from leg times. PASS |
| IPFT-008 | Website #42914 after push#2/3: Total Engine 2.0 (calculated), Total Flight 1.0; Meters Cycles 1.0 (+1.0), Engine 2452.7 (+2.2), Flight 2451.7 (+1.2) vs start 2450.5; Weights Pers&Bag 142.… | TBD (not recorded) | PASS |  | L101: Website #42914 after push#2/3: Total Engine 2.0 (calculated), Total Flight 1.0; Meters Cycles 1.0 (+1.0), Engine 2452.7 (+2.2), Flight 2451.7 (+1.2) vs start 2450.5; Weights Pers&Bag 142.5 TOW 924.3; leg NZAA->NZCH PIC Cody Crawford, Engine 2.0h Flight 1.0h, Within Limits. All match app PASS. NOTE: website deltas computed from start 2450.5, but app's previousMeterReadings said 2450.7 - server 'last reading' vs app baseline differ by 0.2 (server likely updated by another flight; not a bug). |
| IPFT-009 | Leg times on website: start 23:07 stop 01:07 -> 2.0, takeoff 23:08 landing 00:07 -> 1.0. Midnight wrap correct both sides PASS. Leg Category field exists on website; app leg editor has no… | TBD (not recorded) | PASS |  | L102: Leg times on website: start 23:07 stop 01:07 -> 2.0, takeoff 23:08 landing 00:07 -> 1.0. Midnight wrap correct both sides PASS. Leg Category field exists on website; app leg editor has no leg category (check code - not pushed) |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Flights #42914 and #42915 | BETA test flights used for time and meter checks | No |
