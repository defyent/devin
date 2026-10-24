# iPad weight and balance

- **Checklist ID prefix:** `IPWB`
- **Guide section:** `debugging/IPAD_SWIFT_AUDIT_PLAN.md` §3
- **Where:** iPad app — W&B items, calculations, equipment/fuel/personnel, seat display, website comparison
- **Permission:** Admin / Service Account unless a different permission level is identified in the row notes
- **Tester:** Devin
- **Date / DataHangar version:** 24/10/2026 / iPad DataHangar Flight 1.0.13 (46) on iOS 26.5 Simulator; stresstest v2.0.123
- **Account / level used:** Service Account unless a different account is identified in the row notes

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPWB-001 | ZK-HEL leg (PIC Cody Crawford 52 kg override, fuel 100 kg, profile Standard): app W&B sheet BEW 680@269.20/0.50, Removed Dual controls -1.2@125.7/-26.4, PIC 52@125.7/31.0, Survival kit 3@… | Behaves correctly / matches website | PASS |  | L59: ZK-HEL leg (PIC Cody Crawford 52 kg override, fuel 100 kg, profile Standard): app W&B sheet BEW 680@269.20/0.50, Removed Dual controls -1.2@125.7/-26.4, PIC 52@125.7/31.0, Survival kit 3@112, Fuel 100@267.58/-24.47; ZFW 734 @258.62/2.70 mom 189.8; TOW 834 @259.70/-0.56 mom 216.5. Hand calc ZFW 733.8@258.62/2.70 PASS. (fuel see below)<br>L64: fuel: engine linearly interpolates arms between sorted burn stations (80@269.2/-34.3, 127@265.4/-11.2): factor (100-80)/47=0.4255 -> 267.58/-24.47; TOW 833.8 @259.70/-0.56. App output matches its algorithm PASS (website comparison pending). |
| IPWB-002 | (UI) Summary card "Equipment 2 kg" (net incl. removed -1.2) vs W&B section "Equipment 3 kg" -> inconsistent labels. Candidate BUG-IPWB-001 UI. | No defect (see Bug ID) | FAIL | BUG-IPWB-001 | L60: (UI) Summary card "Equipment 2 kg" (net incl. removed -1.2) vs W&B section "Equipment 3 kg" -> inconsistent labels. Candidate BUG-IPWB-001 UI. |
| IPWB-003 | Cabin header '0/4 occupied' but grid shows only Rear Left/Rear Right; aircraft config has seats R2C1/R2C2 (row 2, arm 330) while seatRows=1 -> hidden seats counted. Candidate BUG-IPWB-002… | No defect (see Bug ID) | FAIL | BUG-IPWB-002 | L61: Cabin header '0/4 occupied' but grid shows only Rear Left/Rear Right; aircraft config has seats R2C1/R2C2 (row 2, arm 330) while seatRows=1 -> hidden seats counted. Candidate BUG-IPWB-002 (Low) - compare website W&B config. |
| IPWB-004 | Website #42914 Times&Weights: BEW 680.0, Equipment(net) 1.8, Fuel 100.0, Personnel&Baggage 52.0, Leg1 TOW 833.8 kg; leg NZAA->NZCH PIC Cody Crawford SFC -, TOW 834 kg Within Limits. Meter… | Behaves correctly / matches website | PASS |  | L69: Website #42914 Times&Weights: BEW 680.0, Equipment(net) 1.8, Fuel 100.0, Personnel&Baggage 52.0, Leg1 TOW 833.8 kg; leg NZAA->NZCH PIC Cody Crawford SFC -, TOW 834 kg Within Limits. Meters ZK-HEL start 2450.5. Matches app (app summary rounds equipment to 2). PASS |
| IPWB-005 | Website leg W&B: Rev 3, Equipment Profile Standard, envelope plot ZFW ~258.6@734, TOW ~259.7@834 inside boundary - matches app graph. PASS | Behaves correctly / matches website | PASS |  | L71: Website leg W&B: Rev 3, Equipment Profile Standard, envelope plot ZFW ~258.6@734, TOW ~259.7@834 inside boundary - matches app graph. PASS |
| IPWB-006 | Website leg W&B totals: Equipment 1.80 (3.00 onboard, -1.20 removed from BEW), Fuel 100.00, Pers&Bag 52.00, ZFW 733.80 @ 258.62/2.70, TOW 833.80 @ 259.70/-0.56, BEW 680.00@269.2 mom 183.1… | No defect (see Bug ID) | FAIL | BUG-IPWB-001 | L72: Website leg W&B totals: Equipment 1.80 (3.00 onboard, -1.20 removed from BEW), Fuel 100.00, Pers&Bag 52.00, ZFW 733.80 @ 258.62/2.70, TOW 833.80 @ 259.70/-0.56, BEW 680.00@269.2 mom 183.1. EXACT match with app W&B sheet and hand calc. PASS<br>L73: -> BUG-IPWB-001 downgraded: app card "Equipment 2 kg" = rounded net 1.8; website shows 1.80 with breakdown. UI-only (rounding to integer kg hides 0.2 kg). |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Flight #42914 | BETA test flight used for W&B checks | No |
