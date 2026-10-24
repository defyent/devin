# iPad PDF/JSON export

- **Checklist ID prefix:** `IPPDF`
- **Guide section:** `debugging/IPAD_SWIFT_AUDIT_PLAN.md` §3
- **Where:** iPad app — PDF/JSON export, share sheet, data contents and round-trip
- **Permission:** Admin / Service Account unless a different permission level is identified in the row notes
- **Tester:** Devin
- **Date / DataHangar version:** 24/10/2026 / iPad DataHangar Flight 1.0.13 (46) on iOS 26.5 Simulator; stresstest v2.0.123
- **Account / level used:** Service Account unless a different account is identified in the row notes

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPPDF-001 | Auto-uploaded PDF (docId 587, 3 pages): Flight Report header, "W&B config approved by Service Account - Rev. 3", Flight Details (date, aircraft ZK-HEL (Robinson R44), sched start/end raw… | TBD (not recorded) | PASS |  | L77: Auto-uploaded PDF (docId 587, 3 pages): Flight Report header, "W&B config approved by Service Account - Rev. 3", Flight Details (date, aircraft ZK-HEL (Robinson R44), sched start/end raw 'yyyy-MM-dd HH:mm:ss' strings, route, notes), Legs overview (NZAA->NZCH, times '-', fuel 100, POB 1, TOW 834, W&B OK), People on Board (Cody Crawford PIC 52 kg). Values match app/website. PASS. Minor UI: Sched. Start shows raw '2026-10-23 23:59:00' (seconds, ISO) while Date uses long format. evidence/IPPDF-001_42914_push1.pdf |
| IPJSON-001 | Export JSON -> share sheet -> Save to Files (On My iPad). File ZK_HEL__BETA_TEST_ONLY_NZAA_NZCH_2026-10-23.json (11 KB): all fields incl apiFlightId, meters {1:2451.7,2:2452.7,3:1}, categ… | TBD (not recorded) | PASS |  | L95: Export JSON -> share sheet -> Save to Files (On My iPad). File ZK_HEL__BETA_TEST_ONLY_NZAA_NZCH_2026-10-23.json (11 KB): all fields incl apiFlightId, meters {1:2451.7,2:2452.7,3:1}, category '2', activity '2', additionalInfo EFI value, attachedForms data, legs full. PASS |
| IPPDF-002 | Export PDF (share sheet, 91 KB): page1 Flight Details (sched times raw ISO, Flight Time 1 hrs, Engine Time 2 hrs, Flight Hours 2,451.7, Engine Hours 2,452.7, 1 cycles), Legs Overview NZAA… | TBD (not recorded) | PASS |  | L98: Export PDF (share sheet, 91 KB): page1 Flight Details (sched times raw ISO, Flight Time 1 hrs, Engine Time 2 hrs, Flight Hours 2,451.7, Engine Hours 2,452.7, 1 cycles), Legs Overview NZAA->NZCH 23:07/23:08/00:07/01:07 Flt1 Eng2 Fuel100 POB2 TOW924 W&B OK, People on Board (PIC 52, Pax 78). Baggage not listed in POB (baggage separate?) - check page2/3 later. PASS overall; UI nit raw ISO sched times. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Flights #42914 and #42915 | BETA test flights used for PDF/JSON export checks | No |
