# iPad flight legs

- **Checklist ID prefix:** `IPLEG`
- **Guide section:** `debugging/IPAD_SWIFT_AUDIT_PLAN.md` §3
- **Where:** iPad app — Flight detail and leg editor, aerodromes, crew, passengers, baggage, fuel, seats
- **Permission:** Admin / Service Account unless a different permission level is identified in the row notes
- **Tester:** Devin
- **Date / DataHangar version:** 24/10/2026 / iPad DataHangar Flight 1.0.13 (46) on iOS 26.5 Simulator; stresstest v2.0.123
- **Account / level used:** Service Account unless a different account is identified in the row notes

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPLEG-001 | Add Leg on ZK-HEL opens leg editor: CG envelope graph, summary Equipment 2kg / Fuel 100kg / Pers&Bag 0 / ZFW 682 / TOW 782, "Out of Balance" with empty seats (aft CG without pilot - plaus… | Behaves correctly / matches website | PASS |  | L52: Add Leg on ZK-HEL opens leg editor: CG envelope graph, summary Equipment 2kg / Fuel 100kg / Pers&Bag 0 / ZFW 682 / TOW 782, "Out of Balance" with empty seats (aft CG without pilot - plausible). Cockpit: "Copilot - Left Seat", "PIC - Right Seat" (R44 picSeatPosition right) PASS. Default takeoff fuel 100 kg of max 127 kg. Cabin Rear Left/Rear Right, 0/4 occupied. Equipment profile "Standard". |
| IPLEG-002 | Departure field: typing gives no suggestions; magnifier opens 'Select Aerodrome' sheet listing 15 synced waypoints (NZAA Auckland Airport, BTQA, BTQC, NZCH...). Duplicate 'NZAA / NZAA' (n… | Behaves correctly / matches website | PASS |  | L53: Departure field: typing gives no suggestions; magnifier opens 'Select Aerodrome' sheet listing 15 synced waypoints (NZAA Auckland Airport, BTQA, BTQC, NZCH...). Duplicate 'NZAA / NZAA' (name-only) entry also listed -> ambiguous choice (data issue). PASS |
| IPLEG-003 | Selecting NZAA/NZCH via picker updates header 'NZAA -> NZCH'. PASS | Behaves correctly / matches website | PASS |  | L54: Selecting NZAA/NZCH via picker updates header 'NZAA -> NZCH'. PASS |
| IPLEG-004 | Seat assign sheet 'PIC (Right Seat)': Passenger/Crew/Baggage tabs, Crew Member picker (44 crew alphabetical), Override Weight (kg, optional). Assigning Cody Crawford override 85 kg. | Behaves correctly / matches website | PASS |  | L55: Seat assign sheet 'PIC (Right Seat)': Passenger/Crew/Baggage tabs, Crew Member picker (44 crew alphabetical), Override Weight (kg, optional). Assigning Cody Crawford override 85 kg. |
| IPLEG-005 | ? (Low) With seat-assign sheet open, tapping Override Weight did not focus it; typed '85' went into Departure field behind the sheet (now 'NZAA85', header 'NZAA85 -> NZCH'). Keyboard focu… | No defect (see Bug ID) | FAIL |  | L56: FAIL? (Low) With seat-assign sheet open, tapping Override Weight did not focus it; typed '85' went into Departure field behind the sheet (now 'NZAA85', header 'NZAA85 -> NZCH'). Keyboard focus leaks to background field (hardware keyboard in Simulator; possible with iPad Magic Keyboard). evidence/IPLEG-005_*<br>L57: confirmed: Override Weight opens custom numeric keypad popover; hardware-keyboard digits still go to Departure ('NZAA8585'). Keypad buttons must be tapped. |
| IPLEG-006 | enger 'BETA TEST ONLY Pax' 78 kg assigned to Rear Left (Name+Weight keypad; seat max 136). Cabin 1/4 occupied. App: Pers&Bag 130, ZFW 812 @253.17/-0.54, TOW 912 @254.75/-3.16, W&B sheet 6… | Behaves correctly / matches website | PASS |  | L82: Passenger 'BETA TEST ONLY Pax' 78 kg assigned to Rear Left (Name+Weight keypad; seat max 136). Cabin 1/4 occupied. App: Pers&Bag 130, ZFW 812 @253.17/-0.54, TOW 912 @254.75/-3.16, W&B sheet 6 items. Hand calc below. Leg Meters section hidden for ZK-HEL because all meters logsAgainst=flight (expected).<br>L83: hand calc: ZFW 811.8 @253.17/-0.54, TOW 911.8 @254.75/-3.16 -> exact match PASS |
| IPLEG-007 | Baggage 12.5 kg on Rear Right via Baggage tab: Cabin 2/4, seat label 'Baggage 13 kg' (rounded), Pers&Bag 143, ZFW 824 @252.40/-0.06, TOW 924 @254.04/-2.70, sheet 7 items. Hand calc ZFW 82… | Behaves correctly / matches website | PASS |  | L84: Baggage 12.5 kg on Rear Right via Baggage tab: Cabin 2/4, seat label 'Baggage 13 kg' (rounded), Pers&Bag 143, ZFW 824 @252.40/-0.06, TOW 924 @254.04/-2.70, sheet 7 items. Hand calc ZFW 824.3 @252.40/-0.06, TOW 924.3 @254.04/-2.70 PASS. |
| IPLEG-008 | Website Crew&Pax: Copilot empty, PIC Cody Crawford 52.00, Rear Left 'BETA TEST ONLY Pax' 78.00kg, Rear Right Baggage 12.50 - exact match PASS. Leg Category empty on website; app has no le… | Behaves correctly / matches website | PASS |  | L103: Website Crew&Pax: Copilot empty, PIC Cody Crawford 52.00, Rear Left 'BETA TEST ONLY Pax' 78.00kg, Rear Right Baggage 12.50 - exact match PASS. Leg Category empty on website; app has no leg-category control (feature gap, PD-IP-02) |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Flights #42914 and #42915 | DataHangar flights used for leg/crew checks | No |
