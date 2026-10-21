# Flight Details

- **Checklist ID prefix:** `FD`
- **Guide section:** §8.3, §6.1, §6.2
- **Where:** From Schedule / Active Flights / DFR / Dashboard / Personnel > Flights
- **Permission:** Flight Details A/RA/WG/RG/WO/RO/WL
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FD-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Flight Schedule (menu) > Schedule Only > week > double-click flight #42903 > Flight Details 'Flight #42903 ZK-SIM Open 21/10/2026 08:30' loads, no console errors. Single click only selects the flight |
| FD-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS |  | Help opens 'Flight Details Help'; Got it!, x, Esc and a click on the backdrop each close it, no console errors (one removeChild error seen once in an earlier attempt, not reproducible) (shot fd_help) |
| FD-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Mouse down inside Help and inside Add Form Template, release outside: both popups stay open; Escape closes them |
| FD-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | PASS |  | Dates/times on Flight Details use DD/MM/YYYY and 24 h local time, matching the header Local clock (Pacific/Auckland) and the schedule |
| FD-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | 390 px: no horizontal scroll (375 <= 390), tabs become a dropdown, header buttons wrap, fields stack (shot fd_mobile). Minor: status badge shows only a tick icon (no 'Complete' text); tab dropdown lists 'Lesson' which the desktop tab bar hides for this non-student PIC |
| FD-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FD-001 | Read-only user (RA/RG/RO) | Yellow banner e.g. 'Read-Only Group Access…'; Save/Cancel/Delete hidden | TODO | | |
| FD-002 | Header: Back, PDF, History, Cancel, Save Changes, Delete (open only), Help | All present and working | PASS |  | Header shows Back, PDF, History, Cancel, Save Changes, Delete, Help on the open flight; individual actions tested in FD-003, FD-034, FD-037, FD-038 |
| FD-003 | PDF with unsaved changes | Asks to save first | PASS |  | With unsaved passenger change, PDF > Required Information 'You have unsaved changes. Please save or cancel your changes before printing.' (shot fd_pdf_unsaved) |
| FD-004 | Details: Aircraft dropdown | Only Active + Is Aircraft resources | TODO | | |
| FD-005 | Details: PIC / Secondary Flight Crew | Only Crew or Student role people | FAIL | BUG-FD-004 | Main PIC / Secondary Flight Crew lists 84 people incl. BETA TEST ONLY Lowperm (Crew); not every name role-checked. Leg PIC / Secondary Flight Crew dropdowns however list the custom passenger 'BETA TEST ONLY Pax' (shot fd_leg) |
| FD-006 | Notify toggles | Sends email/SMS on save; not stored (off on reopen) | PASS |  | Notify (PIC) toggled on > Save > after reload the toggle is off again (not stored). Email/SMS delivery not checked (PIC is betatest.low@example.com) |
| FD-007 | Flight Category / Activity dropdowns | From Settings > Flight Types; auto-attach forms fire ('Form "X" auto-attached') | BLOCKED |  | Category list: Dual / PIC / PICUS / Solo; Activity list: Charter, Check Ride, Commercial Operation, Cross Country, Ferry Flight, Maintenance Test, Night Flight, Private, Scenic Flight, Training... Picking Charter, Training, Dual attached no form and showed no 'auto-attached' message (Forms count stayed 1). Need to confirm in checklist 37 whether any auto-attach rule exists; Discard restored the values |
| FD-008 | Start/End Time, SAR Time, SAR Watch default on | Pickers follow Time Zone setting; booking times may be exceeded by flight times (not a bug) | PASS |  | Flight #42903: Start 21/10/2026 08:30, End 21/10/2026 09:30, SAR Time 21/10/2026 09:30 (= end), SAR Watch toggle on by default; DD/MM/YYYY + 24 h like the Local clock |
| FD-009 | Flight Follower / Authorized By | Only Admin/Staff people | TODO | | |
| FD-010 | Notify Overdue by Text / Email | Saved | PASS |  | Notify Overdue by Text and by Email switched on > Save > after reload both still on |
| FD-011 | Extra Information (F fields) | Fields from Extra Flight Info appear and save | BLOCKED |  | No Extra Information section on Flight Details - no extra fields configured on stresstest. Retest after checklist 36 (Settings: Extra Flight Info) adds a field |
| FD-012 | Comments | Add a Comment saves with flight | PASS |  | Typed 'BETA TEST ONLY comment' in Add a Comment (no separate add button) > Save Changes > comment listed 'Service Account, Oct 21, 2026, 10:17 PM' |
| FD-013 | Customer: Existing (company first) + Contact Person suggestions | Works | PASS |  | Customer tab: Existing Customer / New Customer cards; Customer list has 'DEVIN TEST Customer Ltd' (only customer on stresstest) + Contact Person field. Suggestions not checked further (single customer) |
| FD-014 | Customer: New Customer | Creates customer record (with Customer role) | TODO |  | New Customer shows First/Last/Company Name, Email, Address, City, Country, Mobile, Phone. Not saved yet |
| FD-015 | Passenger List: Add Crew Member | Weight from personnel record or 'No weight on file – please enter' | PASS |  | Passenger List > Add Crew Member 'Aaron Foster' (no weight on file) > Required Information popup 'This crew member has no weight on file. Please enter their weight before adding.' with OK. PIC BETA TEST ONLY Lowperm listed in Crew with 0 kg |
| FD-016 | Passenger List: Add Custom Passenger | Added to manifest | PASS |  | Add Custom Passenger 'BETA TEST ONLY Pax', 80 kg, NOK 'BETA TEST ONLY NOK 000' > listed under Passengers (type Passenger) with delete action |
| FD-017 | kg/lbs toggle | Converts correctly | PASS |  | kg > lbs: table headers and the Weight input label switch to LBS, 80 kg shows 176 lbs; back to kg shows 80 again |
| FD-018 | W&B toggle | Only if registration in Master W&B config; per-leg summary + graphs; newer revision prompt | TODO |  | ZK-SIM: Weights shows 'Weight & Balance is not configured for this aircraft.' (correct for an unregistered aircraft). Configured-aircraft case still to test |
| FD-019 | Times and Meters | Totals with source hint; previous reading + link to previous flight | FAIL | BUG-FD-003 | Times: Total Engine Time 'Calculated from engine start/stop times', Total Flight Time 'Calculated from takeoff/landing times' (source hints OK). Meters Cycles / Engine Hours / Flight Hours show 'Previous: 2450.3 (+0.0)' but there is no link to the previous flight |
| FD-020 | Cumulative meter lower than previous | 'Meter "X" value (…) is less than previous reading (…)' | PASS |  | Times and Weights > Engine Hours odometer: thousands digit down (2450.3 > 1450.3) > inline 'Value (1450.3) is less than previous reading (2450.3)', 'Previous: 2450.3 (-1000.0)' (shot fd_meter_low). Message does not name the meter but sits under it |
| FD-021 | Legs: Add Leg top/bottom; delete leg | Works; delete confirms | PASS |  | Add Leg buttons at the top and bottom of Legs; new leg 1 with Departure/Destination, PIC, Secondary crew, Leg Category, engine/flight times, crew and passengers on board, notes. Delete (bin) > 'Delete Leg - Are you sure you want to delete this leg? This action cannot be undone.' Cancel / Delete; Delete removes it (shot fd_leg_delete) |
| FD-022 | Leg waypoints unknown | Prompt to pick or add; 'Waypoint X added successfully' | FAIL | BUG-FD-005 | Leg ZZZQ > NZWN (both not in the waypoint list) > Save > prompt 'Add New Waypoint - "ZZZQ" is not in the waypoint list...' (Stay on Page / Add Waypoint) > Add Waypoint > toast 'Waypoint "ZZZQ" added successfully' and flight saved, but no prompt for NZWN and the leg Destination was saved empty. Saving NZWN again then prompts for it. Prompt only on save, cancel is labelled 'Stay on Page' |
| FD-023 | Leg time fields | Match resource Time Inputs settings | TODO | | |
| FD-024 | Crew Recency tab | Items per crew member from direct + group template assignments | PASS |  | Crew Recency tab: 'BETA TEST ONLY Lowperm (BETA TEST ONLY Group, Crew) / PIC - No currencies assigned to this crew member.' (no direct/group templates assigned). Populated case to retest with a crew member who has currencies |
| FD-025 | Lesson tab | Only when PIC/crew is Student; lessons from assigned plan; exercises, assessment sliders 0–5, debrief | TODO |  | PIC is Crew, not Student: no Lesson tab shown (correct). Student case still to test |
| FD-026 | Forms tab: Add Form | Works | PASS |  | Forms > Add Form > 'Add Form Template' picker with search, grouped QA Flight / Personnel / Safety Forms, Cancel and x; picking 'QA Post-Flight Report' attaches it (11 fields, required Flight Date / Flight Purpose, delete) (shot fd_form_added) |
| FD-027 | Files tab: upload (incl. > 30 MB) | Upload works; > 30 MB rejected cleanly | PASS |  | Files: 31.5 MB file > Upload > 'Error: File size exceeds the maximum limit of 30MB.' (popup titled 'Required Information'), nothing attached; 32 B 'BETA_TEST_ONLY_small.txt' uploads and is listed (21/10/2026, Service Account, 32 B, download/delete) (shots fd_upload_big, fd_upload_small) |
| FD-028 | Flight Status: Open / Complete / Canceled | Cards selectable; Reason for Cancellation when Canceled; secondary status pills | PASS |  | Flight Status cards Open / Complete / Canceled selectable; Canceled shows 'Reason for Cancellation' (Aircraft Maintenance, Airspace Closure, Crew Unavailable, Customer Request, Fuel Shortage, Medical, Other, Weather). Secondary Status shows no pills (none configured?) (shot fd_status_cancel). Cancel button > 'Discard Changes' popup with Stay on Page / Discard Changes |
| FD-029 | Complete & Locked | Only visible to WL; admins need WL explicitly | PASS |  | Service Account (no WL right granted explicitly): Flight Status shows only Open / Complete / Canceled, no 'Complete & Locked' card. WL user not available to check the positive case |
| FD-030 | Locked flight | 'This flight is locked…' read-only for all; WL can unlock by changing status | PASS |  | With an explicit WL row, flight #42903 set to Complete & Locked shows "This flight is locked..." and every field is read-only. Choosing Complete and Save unlocks it (checklist 90 PERM-005). |
| FD-031 | Complete without Start/End/SAR or end < start | Required Information popup | TODO |  | Not yet tested with missing times. Note: #42903 could be set to Complete and saved with no prompt although leg 1 has no destination/times and the attached QA Post-Flight Report has empty required fields (Flight Date, Flight Purpose); header badge then 'Complete', Delete button hidden (shot fd_complete) |
| FD-032 | W&B on, seated person weight 0 | Blocked | TODO | | |
| FD-033 | Required to Complete meter left empty | Guide: not enforced (known gap) — confirm and log | TODO | | |
| FD-034 | Save success | Returns to where you came from | FAIL | BUG-FD-001 | Opened from Flight Schedule (week view), Save Changes > stays on Flight Details (page reloads with return_url=flightschedule, Save Changes greyed out), no success message; not returned to the schedule (shot fd_after_save) |
| FD-035 | Leave with unsaved changes | Stay on Page / Leave Page | PASS |  | With unsaved changes, Back > app popup 'Unsaved Changes - You have unsaved changes. Are you sure you want to leave without saving?' with Stay on Page / Leave Page; Stay keeps the page and the changes (shot fd_leave_prompt) |
| FD-036 | Flight & Duty Limit Alert | Shown when crew exceed FRMS limits | TODO | | |
| FD-037 | History | Shows changes made in this run | FAIL | BUG-FD-002 | History lists 5 entries (Created 09:29 pm + 4 schedule moves/resizes) but not the 10:17 pm Flight Details save (passenger + comment). Every schedule move also logs 'Aircraft: ZK-SIM > Unassigned' and 'Source: (blank) > Flight Schedule' although the aircraft did not change (shot fd_history) |
| FD-038 | Delete open flight | Confirmation; flight soft-deleted (D) | PASS |  | Open flight #42908 > delete > 'Delete Flight - Are you sure you want to delete this flight? This will mark it as deleted and return you to the flight schedule.' (Stay on Page / Delete Flight) > Delete Flight > back on Flight Schedule, #42908 gone from 19-25 Oct. No toast. Soft-delete (D) not visible from UI. Delete button hidden on the Complete flight #42903 (shots fd_delete_confirm, fd_deleted) |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| FORM-01 | High | Open (external) | Flight Details saves a form with 9 empty required fields, no warning |
| FORM-10 | Medium | Open (external) | Field count differs: Viewer 8/11 vs Flight Details 11/11; defaults count as filled |
| FORM-11 | Medium | Open (external) | "Updated" time doesn't change after a later save of a flight form |
| FORM-22 | Low | Open (external) | Flight Delete Form confirm uses "Stay on Page" instead of "Cancel" |
| FUNC-02 | Medium | Open (external) | PDF Summary "Generate PDF" gives no visible result or feedback |
| VIS-26 | Low | Open (external) | Flight Details card heading and checkbox sizes vary |
| VIS-27 | Low | Open (external) | Weight unit wording "KG/Lbs" vs "kg/lbs" |
| UX-09 | Low | Open (external) | Flight Details: two Add Leg buttons, empty "Secondary Status" label, no units on Crew Recency inputs |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Custom passenger 'BETA TEST ONLY Pax' (80 kg, NOK 'BETA TEST ONLY NOK 000') | Flight #42903 > Passenger List | No |
| Comment 'BETA TEST ONLY comment' | Flight #42903 > Comments | No |
| Leg 1 (Departure ZZZQ) | Flight #42903 > Times and Weights | No |
| Waypoint 'ZZZQ' (added from the leg prompt) | Settings > Waypoints | No |
| Notify Overdue by Text / Email switched on; status set to Complete | Flight #42903 > Details / Flight Status | No (deleted with the flight) |
| Pre-existing, not created in this run: customer 'DEVIN TEST Customer Ltd' | Customers | No (check with Jon) |
