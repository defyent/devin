# Fix-it Handover: Flight Details (`flightdetails`), DataHangar v2.0.108

- **Source run:** first beta test run, 2026-09-12, against https://new.datahangar.net/?action=flightdetails (account `jonkeller`)
- **Original session:** https://app.devin.ai/sessions/a9cfbbe9fd194b11a74a69cce2d92fe3
- **Status:** Findings come from the 12 Sep run, which did not record a version. The file is labelled v2.0.108 as Jon asked; the findings have not been re-checked on stresstest v2.0.108.
- **Evidence:** `screenshots/flightdetails/` (`<TestID>_fail.png`)

---


## Severity summary

| # | ID(s) | Area | Issue | Severity |
|---|---|---|---|---|
| 1 | PDF-07 | PDF | lbs weights labeled `kg`; recency omitted; lesson exercise names blank | **High** — safety-relevant wrong weight units |
| 2 | FL-12 | Files | Download blocked by permission error for the uploading account | **High** — feature unusable |
| 3 | MB-02, MB-09, MB-10 | Mobile | PDF / History / Help header controls disappear below ~1000px | **High** — flows unreachable on mobile |
| 4 | SV-05 | Save/Discard | Discard duplicates Forms cards and badge (2→4) until real reload | **High** — duplicates land in generated PDF |
| 5 | L-13 | Legs | Engine-time picker hour wheel clipped and click-intercepted | **High** — cannot enter engine times |
| 6 | FL-13 | Files | Rapid sequential delete → `Document not found ... DHFlightdetails.pm line 3428` | Medium |
| 7 | D-21 | Extra info | Numeric field rejects decimals | Medium |
| 8 | N-05 | Navigation | Tab pills not shown at 1000px (dropdown instead) | Medium |
| 9 | W-04, WB-23 | Weights / W&B | Disabled-W&B notice wrongly says "Select an aircraft" | Medium |
| 10 | PDF-05 | PDF | Validation error opens *behind* the PDF dialog | Medium |
| 11 | S-09, H-02 | Status / History | Unlock history row has no action label | Medium |
| 12 | LS-06 | Lesson | Score 5 shows `Excellent` on desktop but `High` on mobile/PDF | Low |
| 13 | HM-03 | Help | Help text uses obsolete tab names | Low |
| 14 | P-05 | Passenger List | Wrong error popup when no crew member is selected | Low |
| 15 | N-08 | Navigation | Back arrow shown without return context | Low |

---

## Details

### 1. PDF-07 — PDF mislabels lbs weights as kg, omits recency and lesson exercise names
**Repro:** Set the weight unit to `lbs`, add a passenger at 200, attach a lesson and crew recency, then generate the flight PDF.
**Expected:** Weights printed in the unit shown (or converted correctly and labeled); recency section and lesson exercise names included.
**Actual:** A 200 lbs passenger prints as `200 kg`; the crew recency section is absent; lesson exercise names are blank; assessment score 5 prints `High` while the desktop UI shows `Excellent`.
**Evidence:** `PDF-07_fail.png`, `PDF-07_weights_reference.png`, `PDF-07_page1.png`, artifact `Flight_42984_Summary_fresh.pdf`.
**Impact:** Weight & balance figures on a printed manifest carry the wrong unit label — safety relevant.

### 2. FL-12 — File download denied for the account that uploaded the file
**Repro:** Files tab → upload a file → click Download on that file.
**Expected:** File downloads.
**Actual:** Navigates to an error page: `Access Denied: You do not have permission to download flight files.` The same account can upload, preview and delete the file.
**Evidence:** `FL-12_fail.png`.

### 3. MB-02 / MB-09 / MB-10 — PDF, History and Help controls missing at narrow widths
**Repro:** Open a saved flight at 375px (also reproduced at 600, 768 and 1000px).
**Expected:** Header actions remain reachable (wrapped, collapsed into a menu, etc.).
**Actual:** The PDF, History and Help buttons are not rendered at all — those flows cannot be started on mobile. The header itself wraps without horizontal overflow.
**Evidence:** `MB-02_fail.png`, `MB-09_fail.png`, `MB-10_fail.png`.

### 4. SV-05 — Discard duplicates attached forms
**Repro:** Open a flight with 2 forms, edit a field (e.g. Route), click away/Discard changes.
**Expected:** Edits reverted; Forms badge stays `2`.
**Actual:** Edits revert and the Save button returns to neutral, but the Forms badge doubles to `4` and the form cards are duplicated. The duplicates persist until a true page reload, and a PDF generated in that state contains them.
**Evidence:** `SV-05_fail.png`.

### 5. L-13 — Engine-time picker unusable on a leg
**Repro:** Times and Weights → expand a leg → open the engine start time picker.
**Expected:** Picker is fully visible and the hour wheel is clickable.
**Actual:** The hour wheel is clipped off the left edge of the leg Times panel and the modal backdrop intercepts clicks on it; the time could not be set, so the engine-time calculation could not be verified.
**Evidence:** `L-13_fail.png`.

### 6. FL-13 — Rapid sequential file deletion throws a server error
**Repro:** Delete a file, then delete the next one ~450 ms later, before the first row disappears.
**Expected:** Each delete succeeds.
**Actual:** `Error: Document not found at /var/www/datahangar/DHLib/DHFlightdetails.pm line 3428.` — the UI reuses a stale row reference. Waiting for the row to be removed avoids it. Observed once during cleanup.
**Evidence:** `FL-13_fail.png`.

### 7. D-21 — Extra Information number field rejects decimals
**Repro:** Extra Information (Details) → enter `12.5` in the Number field → save.
**Expected:** Decimal accepted and persisted.
**Actual:** Native validation blocks it: `Please enter a valid value. The two nearest valid values are 12 and 13.` Integer `12` persists. (URL and multiline text field fixtures were not present, so those parts of D-21 are untested.)
**Evidence:** `D-21_fail.png`.

### 8. N-05 — Tab pills not used at 1000px
**Repro:** View a flight at 1000px width.
**Expected:** Pill navigation at ≥769px.
**Actual:** The mobile dropdown navigation is still used; pills appear only at larger widths (correct at 1600px).
**Evidence:** `N-05_fail.png`.

### 9. W-04 / WB-23 — Wrong "select an aircraft" notice when W&B is off
**Repro:** Select aircraft ZK-HDY (W&B disabled) and view the Weights card; also after disabling W&B on a leg (WB-23).
**Expected:** Notice explaining W&B is not configured/enabled for this aircraft.
**Actual:** Notice reads `Select an aircraft on the Details tab to enable Weight & Balance` even though an aircraft is selected.
**Evidence:** `W-04_fail.png`, `WB-23_fail.png`.

### 10. PDF-05 — PDF validation error opens behind the PDF dialog
**Repro:** Open the PDF dialog, deselect all fields, generate.
**Expected:** Readable error in front.
**Actual:** The error `Please select at least one field to include in the PDF.` renders behind the PDF modal and is neither readable nor clickable until the PDF dialog is cancelled.
**Evidence:** `PDF-05_fail.png`, `PDF-05_hidden_error.png`.

### 11. S-09 / H-02 — Unlock not labeled in History
**Repro:** Lock a flight, then unlock it, then open History.
**Expected:** A history row identifying the unlock action.
**Actual:** Unlock works and the flight becomes editable, but the newest History row carries only a timestamp and author, with no action label. Other rows (created/updated) are correct and ordered newest-first.
**Evidence:** `S-09_fail.png` / `H-02_fail.png`.

### 12. LS-06 — Inconsistent assessment label at score 5
**Repro:** Lesson tab → set an assessment slider to its maximum (5) → compare desktop, mobile and PDF.
**Expected:** One consistent label.
**Actual:** Desktop handle aligns with `Excellent`; mobile label and PDF both say `High`. Desktop shows no per-score label.
**Evidence:** `LS-06_fail.png`.

### 13. HM-03 — Help text uses obsolete tab names
**Repro:** Open the `?` Help.
**Actual:** Refers to `Custom Information`, `Passenger Manifest`, `Flight Info` instead of the current tab names, and omits the `Lesson` tab.
**Evidence:** `HM-03_fail.png`.

### 14. P-05 — Wrong popup when adding crew with nothing selected
**Repro:** Passenger List → `Add Crew Member` → click `Add to Manifest` with `Select a crew member` still chosen.
**Expected:** `Please select a crew member to add.`
**Actual:** `This crew member has no weight on file. Please enter their weight before adding.`
**Evidence:** `P-05_fail.png`.

### 15. N-08 — Back arrow shown without return context
**Repro:** Open `?action=flightdetails&flight_id=<id>` directly by URL (no `return_url`).
**Expected:** No back arrow.
**Actual:** Back arrow is displayed.
**Evidence:** `N-08_fail.png`.

---

## Not covered (needs your input)

109 IDs are Blocked/incomplete, mainly because:
- Only the `jonkeller` account was available — all permission-level cases (A / WL / WG / WO / RA / RG / RO / None) are untested.
- Several required test fixtures (named aircraft, crew and student records, low-threshold F&D rules, a location-planner booking) were not available on staging. The real aircraft are ZK-HDY / HLO / HQO / JET / NFL.
- No second desktop browser and no physical iPhone/Android device (mobile section was run with viewport emulation).
- Notification delivery (email/SMS) was deliberately not exercised.

## Test data to clean up
- Flight **42984** — left `Canceled`; two forms and test data remain (uploads deleted).
- Flight **42985** — deleted via the UI, but its direct URL still loads showing `Open`; schedule removal unverified.
- Customer **274 — BETA TEST ONLY / BETA Test20260912**, with contact **BETA Test Contact Zed**.
