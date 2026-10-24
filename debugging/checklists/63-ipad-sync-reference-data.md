# iPad sync reference data

- **Checklist ID prefix:** `IPREF`
- **Guide section:** `debugging/IPAD_SWIFT_AUDIT_PLAN.md` §3
- **Where:** iPad app — Aircraft/resources, crew list, waypoints, flight types, form templates, master W&B config
- **Permission:** Admin / Service Account unless a different permission level is identified in the row notes
- **Tester:** Devin
- **Date / DataHangar version:** 24/10/2026 / iPad DataHangar Flight 1.0.13 (46) on iOS 26.5 Simulator; stresstest v2.0.123
- **Account / level used:** Service Account unless a different account is identified in the row notes

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPREF-001 | Aircraft: app 21 regos (HEL JST RTB RTN SKY SLK SUN WAX WLD SIG SIM HLO DIA JET BTO FLY AIR WAR RAV RVN JRA) = website 21 active. PASS (pending visual rego check) | TBD (not recorded) | PASS |  | L17: Aircraft: app 21 regos (HEL JST RTB RTN SKY SLK SUN WAX WLD SIG SIM HLO DIA JET BTO FLY AIR WAR RAV RVN JRA) = website 21 active. PASS (pending visual rego check) |
| IPREF-002 | Meters: ZK-JET website Flight/Engine 3567.8, Cycles 0.0 = app startValue 3567.8/3567.8/0, cumulative, 1dp. PASS. App stores no call sign (website has Call Sign B206 etc.) -> product decis… | TBD (not recorded) | PASS |  | L18: Meters: ZK-JET website Flight/Engine 3567.8, Cycles 0.0 = app startValue 3567.8/3567.8/0, cumulative, 1dp. PASS. App stores no call sign (website has Call Sign B206 etc.) -> product decision? (app lists by rego) |
| IPREF-002b | Meters all visible aircraft (JET JRA JST BTO FLY AIR SKY SLK SUN SIG SIM DIA WAR WAX): app startValue / previous readings = website values. PASS | TBD (not recorded) | PASS |  | L20: Meters all visible aircraft (JET JRA JST BTO FLY AIR SKY SLK SUN SIG SIM DIA WAR WAX): app startValue / previous readings = website values. PASS |
| IPREF-003 | Personnel: app 44 (crew=Y), names alphabetical by last name, includes BETA Grpuser/Lowperm/Second; weights all 0 (website Weight column blank). Website Crew group list visually matches na… | TBD (not recorded) | PASS |  | L22: Personnel: app 44 (crew=Y), names alphabetical by last name, includes BETA Grpuser/Lowperm/Second; weights all 0 (website Weight column blank). Website Crew group list visually matches names (Atkinson..White). PASS (exact count pending via Role filter) |
| IPREF-004 | Waypoints: app 15; duplicate NZAA (one with coords, one blank); BTQA, BTQC, NZWR, ZZZQ have blank lat/lon -> compare website | TBD (not recorded) | PASS |  | L23: Waypoints: app 15; duplicate NZAA (one with coords, one blank); BTQA, BTQC, NZWR, ZZZQ have blank lat/lon -> compare website<br>L26: result: website Waypoints list = app (NZAA Auckland, BTQA/BTQC name-only no coords, NZCH, NZDN, NZHN, NZNS, NZAA(name-only dup), NZWR, NZPM, NZQN, NZRO, NZTG, ...) coords identical to 6dp. PASS. Website test data has a name-only "NZAA" duplicate (Scan Duplicates exists) - data, not app. |
| IPREF-005 | Flight types: categories Dual/PIC/PICUS/Solo; activities 10 (Charter..Training) -> compare website | TBD (not recorded) | TODO |  | L24: Flight types: categories Dual/PIC/PICUS/Solo; activities 10 (Charter..Training) -> compare website<br>L28: detail: categories ids Dual1 Solo2 PIC3 PICUS4; activities Training1 Charter2 Scenic3 MaintTest4 Ferry5 Private6 CommercialOp7 CheckRide8 CrossCountry9 Night10 |
| IPREF-006 | Forms: 7 templates (AUDIT All Widgets, BETA TEST ONLY Form, QA Post-Flight Report, QA Pre-Flight Checklist, QA Annual Line Check, QA Equipment Issue, QA Hazard Observation); 5 groups | TBD (not recorded) | TODO |  | L25: Forms: 7 templates (AUDIT All Widgets, BETA TEST ONLY Form, QA Post-Flight Report, QA Pre-Flight Checklist, QA Annual Line Check, QA Equipment Issue, QA Hazard Observation); 5 groups<br>L27: detail: app form groups: AUDIT Forms[23 AUDIT All Widgets], BETA TEST ONLY Forms[24], QA Flight Forms[19 Post-Flight,18 Pre-Flight], QA Personnel Forms[21 Annual Line Check,22 Equipment Issue], QA Safety Forms[20 Hazard Observation] -> compare Form Builder<br>L31: Forms: website Form Builder template dropdown shows AUDIT Forms and BETA TEST ONLY Forms groups EMPTY (only 5 QA templates selectable) but app synced 7 incl. 23 AUDIT All Widgets, 24 BETA TEST ONLY Form. Investigating (Form Browser / template status).<br>L33: Form Builder empty AUDIT/BETA groups -> recheck via Flight Details "add form" in IPFORM (possible website-side issue, not app) |
| IPREF-005a | Flight categories: website 4 (Dual1 PIC3 PICUS4 Solo2) = app ids/names. PASS | TBD (not recorded) | PASS |  | L29: Flight categories: website 4 (Dual1 PIC3 PICUS4 Solo2) = app ids/names. PASS |
| IPREF-005b | Flight activities: website 10 ids/names = app exactly. PASS | TBD (not recorded) | PASS |  | L30: Flight activities: website 10 ids/names = app exactly. PASS |
| IPREF-007 | W&B config: website Active Master = Revision 3 (1 aircraft, approved 14 Oct 2026 by Service Account); Revs 4-6 approved but not master. App wabConfigRevision=3, id 3, approvedBy Service A… | TBD (not recorded) | PASS |  | L32: W&B config: website Active Master = Revision 3 (1 aircraft, approved 14 Oct 2026 by Service Account); Revs 4-6 approved but not master. App wabConfigRevision=3, id 3, approvedBy Service Account. PASS. Only dh-1 ZK-HEL carries full W&B config (others are shells). |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
