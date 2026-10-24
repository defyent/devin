# BUG-IPWB-001 — Leg summary card rounds equipment to whole kg and disagrees with the W&B sheet

- **Severity:** Low
- **Area:** iPad app — Flights > Leg > summary card / W&B
- **Found:** 2026-10-24, iPad Pro 13-inch (M5) Simulator, iOS 26.5, DataHangar Flight 1.0.13 (46), stresstest v2.0.123

## Steps
1. ZK-HEL leg with Survival kit 3 kg onboard and Dual controls -1.2 kg removed.
2. Compare the leg summary card, the app W&B sheet and the website leg W&B.

## Expected
Net equipment 1.8 kg (the website shows 1.80 with the onboard/removed breakdown).

## Actual
Summary card shows 'Equipment 2 kg' (rounded net) while the W&B section shows 'Equipment 3 kg' (onboard only). ZFW/TOW/CG totals are correct and match the website exactly; this is display only.

## Cause
Integer rounding and different definitions (net vs onboard) in the two views.

## Evidence
- `screenshots/IPWB-001_app_leg_wb.png`
- `screenshots/IPWB-006_web_42914_wb_totals.png`
