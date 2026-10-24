# BUG-IPWB-002 — Cabin header counts hidden seats ('0/4 occupied' with only 2 seats shown)

- **Severity:** Low
- **Area:** iPad app — Flights > Leg > W&B cabin
- **Found:** 2026-10-24, iPad Pro 13-inch (M5) Simulator, iOS 26.5, DataHangar Flight 1.0.13 (46), stresstest v2.0.123

## Steps
1. Open a ZK-HEL leg > cabin / seat layout.

## Expected
The occupancy count matches the seats shown, or the hidden row-2 seats are shown.

## Actual
Header says '0/4 occupied' but only Rear Left / Rear Right are shown. ZK-HEL's config has seats R2C1/R2C2 (row 2, arm 330) while seatRows = 1, so 2 seats are counted but can't be used.

## Cause
Likely: occupancy counts every config seat while the grid renders only seatRows rows (not confirmed in source).

## Evidence
- Source review / audit log only (see checklist row).
