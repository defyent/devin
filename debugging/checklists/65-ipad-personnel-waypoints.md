# iPad personnel and waypoints

- **Checklist ID prefix:** `IPPW`
- **Guide section:** `debugging/IPAD_SWIFT_AUDIT_PLAN.md` §3
- **Where:** iPad app — Personnel list/search/weights, waypoint list/edit, coordinate formats
- **Permission:** Admin / Service Account unless a different permission level is identified in the row notes
- **Tester:** Devin
- **Date / DataHangar version:** 24/10/2026 / iPad DataHangar Flight 1.0.13 (46) on iOS 26.5 Simulator; stresstest v2.0.123
- **Account / level used:** Service Account unless a different account is identified in the row notes

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPWPT-001 | Waypoint count reconciled: local `aerodromes` = 16 records = 10 with coordinates + 6 name-only entries with blank lat/lon (BTQA, BTQC, NZAA, NZCH, NZWR, ZZZQ). Earlier "15" was before ZZZ… | TBD (not recorded) | N/A |  | Candidate: L295: Waypoint count reconciled: local `aerodromes` = 16 records = 10 with coordinates + 6 name-only entries with blank lat/lon (BTQA, BTQC, NZAA, NZCH, NZWR, ZZZQ). Earlier "15" was before ZZZQ appeared (name-only entry, likely from a website flight route). NZAA/NZCH exist twice (proper airport + blank-coord duplicate) -> candidate data-quality/UX issue: picker may offer coordinate-less duplicate. Verify vs website Waypoints page. |
| IPPER-001 | localPersonnel = 44 (matches website count); all weights 0 in synced crew roster. | TBD (not recorded) | TODO |  | L296: localPersonnel = 44 (matches website count); all weights 0 in synced crew roster. |
| IPPER-002 | Personnel list: alphabetical 'Surname, First', search field, every row subtitle '—' (no weight). Evidence IPPER-002_personnel_list.png | TBD (not recorded) | TODO |  | L307: Personnel list: alphabetical 'Surname, First', search field, every row subtitle '—' (no weight). Evidence [IPPER-002_personnel_list.png](../bugs/screenshots/IPPER-002_personnel_list.png) |
| IPPER-003 | Personnel screen is read-only by design (source comment); rows not tappable -> PASS. Weight column '—' for all 44 (weight nil/0). Need website check whether personnel weights exist server… | TBD (not recorded) | PASS |  | L308: Personnel screen is read-only by design (source comment); rows not tappable -> PASS. Weight column '—' for all 44 (weight nil/0). Need website check whether personnel weights exist server-side (if yes -> sync drops weights). |
| IPWPT-002 | Waypoints UI: 16 rows; 6 coordinate-less entries (BTQA, BTQC, NZAA, NZCH, NZWR, ZZZQ) sort first with blank title (code only as subtitle, no coords). NZAA/NZCH appear twice (blank + prope… | TBD (not recorded) | PASS |  | L309: Waypoints UI: 16 rows; 6 coordinate-less entries (BTQA, BTQC, NZAA, NZCH, NZWR, ZZZQ) sort first with blank title (code only as subtitle, no coords). NZAA/NZCH appear twice (blank + proper airport). Coords shown in DDM per setting (e.g. NZAA 37 00.48S 174 47.50E) -> format PASS. Evidence [IPWPT-002_waypoints_list.png](../bugs/screenshots/IPWPT-002_waypoints_list.png) |
| IPWPT-003 | Coordinate-less entries are server waypoints with EMPTY code and name=ICAO (e.g. Code '', Name 'NZAA'); edit sheet shows coords 0 0.0000 N / 0 0.0000 E (blank shown as 0/0 - saving would… | TBD (not recorded) | TODO |  | L310: Coordinate-less entries are server waypoints with EMPTY code and name=ICAO (e.g. Code '', Name 'NZAA'); edit sheet shows coords 0 0.0000 N / 0 0.0000 E (blank shown as 0/0 - saving would store 0,0). List shows blank title because title=code. Evidence [IPWPT-003_blank_code_nzaa.png](../bugs/screenshots/IPWPT-003_blank_code_nzaa.png) |
| IPWPT-004 | Waypoint edit sheet saves locally only (no server API call); blank coords become 0.000000/0.000000 on Save in DDM/DMS mode. -> BUG-IPWPT-001 (Low/Medium). Website Waypoints comparison pen… | TBD (not recorded) | FAIL | BUG-IPWPT-001 | L311: Waypoint edit sheet saves locally only (no server API call); blank coords become 0.000000/0.000000 on Save in DDM/DMS mode. -> BUG-IPWPT-001 (Low/Medium). Website Waypoints comparison pending. |
| IPWPT-005 | Website Settings and Tools > Waypoint Locations: server holds name-only entries BTQA (1 flight), BTQC (0), NZAA (3), NZCH (2), NZWR (1) with blank code/lat/lon - app mirrors server data c… | TBD (not recorded) | FAIL | BUG-IPWPT-001 | L312: Website Settings and Tools > Waypoint Locations: server holds name-only entries BTQA (1 flight), BTQC (0), NZAA (3), NZCH (2), NZWR (1) with blank code/lat/lon - app mirrors server data correctly (PASS for sync). Website lists by Name so they are readable; app titles by Code -> blank rows (BUG-IPWPT-001 is app display/edit issue; underlying duplicates are server data quality - website has 'Scan Duplicates'). Coordinates for coded airports match app (NZAA -37.008056/174.791667 = 37 00.48S 174 47.50E). Evidence [IPWPT-005_website_waypoints.png](../bugs/screenshots/IPWPT-005_website_waypoints.png) |
| IPWPT-006 | Website waypoint total = 16 (10 coded airports + BTQA, BTQC, NZAA, NZCH, NZWR, ZZZQ name-only) = app 16; coords for all 10 coded airports match app -> PASS. Evidence IPWPT-006_website_way… | TBD (not recorded) | PASS |  | L313: Website waypoint total = 16 (10 coded airports + BTQA, BTQC, NZAA, NZCH, NZWR, ZZZQ name-only) = app 16; coords for all 10 coded airports match app -> PASS. Evidence [IPWPT-006_website_waypoints_full.png](../bugs/screenshots/IPWPT-006_website_waypoints_full.png) |
| IPPER-004 | Website People > Crew: Weight column blank for all crew (e.g. Cody Crawford) -> app '—' matches; names/order match app (Atkinson C/M/P, Blake, Booth, Crawford, Duncan, Elliott D/L, Ellis,… | TBD (not recorded) | PASS |  | L315: Website People > Crew: Weight column blank for all crew (e.g. Cody Crawford) -> app '—' matches; names/order match app (Atkinson C/M/P, Blake, Booth, Crawford, Duncan, Elliott D/L, Ellis, Fisher V, Foster A) -> row 65 personnel PASS. Evidence [IPPER-004_website_crew_weights.png](../bugs/screenshots/IPPER-004_website_crew_weights.png) |
| IPPER-005 | Website personnel detail (Blake Ellis) Weight field blank (KG/Lbs) - confirms server has no weights; app '—' correct. | TBD (not recorded) | TODO |  | L317: Website personnel detail (Blake Ellis) Weight field blank (KG/Lbs) - confirms server has no weights; app '—' correct. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
