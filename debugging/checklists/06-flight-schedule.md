# Flight Schedule (incl. embedded Location Planner)

- **Checklist ID prefix:** `FS`
- **Guide section:** §8.2
- **Where:** Flight Operations > Flight Schedule
- **Permission:** Flight Schedule A/RA/WG/RG
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Opened via sidebar, week view 19-25 October 2026; no console errors (iframe sandbox warning only) |
| FS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | VIS-06 | No Help (?) button on the Flight Schedule page header (only the settings page has one) - external VIS-06 |
| FS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Flight details popup: mousedown inside, release outside > stays open. Outside click closes it |
| FS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| FS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| FS-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FS-001 | Day / Week / Month / List views; ‹ › Today | Each renders; view and date remembered on reload | PASS |  | month 'October 2026', week '19 - 25 October 2026', day, list all render; < > move by view; after reload + reopen, month view and date kept |
| FS-002 | Past/future date banners | 'You are viewing a past/future date' with Today button | PASS |  | Past: 'You are viewing a past date.'; future: 'You are viewing a future date.'; today button in toolbar returns |
| FS-003 | Group By dropdown | Only groups with Show in Dropdown; WG/RG users see only their own | PASS |  | Group By lists Administration, BETA TEST ONLY Group (Show in Dropdown on), Crew, Engineers, Pilots. All 424 events/week, Pilots 191, BETA group 0. WG/RG-only part not testable (no such user) |
| FS-004 | Toggle Roster | Roster row shows only Show-on-Schedule shifts and On Roster members | PASS |  | Toggle Roster (title 'Toggle Roster') hides/shows the roster row (178 shift items in week view); flights stay |
| FS-005 | Toggle Notes | Notes show/hide | PASS |  | Toggle Notes hides/shows 'BETA TEST ONLY Note' (1 > 0 > 1) |
| FS-006 | Compact view (month) | Max 3 events/day with +more | PASS |  | Compact (title 'Compact view (show +more)') in month view: 2 items per day + '+N more' link (e.g. '+66 more'). With Roster on, the 2 slots are roster shifts so flights are only reachable via +more |
| FS-007 | Font size slider | Changes size; remembered? | PASS |  | Font button (title 'Adjust font size') opens slider 8-18; 14 -> 18 changes event text 11.9px -> 15.3px; kept after reload; restored to 14 |
| FS-008 | Toggle Edit Mode (write users only) | Enable/Disable Live Edit; hidden for RA/RG | PASS | BUG-FS-003 | 'Enable Live Edit' > 'Disable Live Edit' (active); Undo, Add Note, Add Flight buttons appear. Layout: with Live Edit on at 1568px the banner covers the 'Flight Schedule' title and the location pill is cut off (BUG-FS-003) |
| FS-009 | Edit mode: drag on empty slot in aircraft column | Flight Details opens pre-filled start/end/aircraft | PASS |  | Day view 19 Oct, drag 07:30-08:25 in empty ZK-JET column > New Flight Details opens with aircraft ZK-JET, start 19/10/2026 07:30, end 08:25 (URL starttime/endtime/resource_id=3). Not saved |
| FS-010 | Edit mode: drag in all-day area | All-day flight created | BLOCKED |  | No separate all-day flight row: in week view the top day-grid is the 'Roster' area (full of roster shifts + notes, no empty cell to drag in); day view (aircraft columns) has no all-day row and greys out Toggle Roster/Notes. Need to know where all-day flights are meant to be created |
| FS-011 | Add Flight button | Blank Flight Details | FAIL | BUG-FS-001 | Add Flight opens blank 'New Flight Details' (Open, aircraft/PIC empty, Save disabled until change). But Start defaults to 08:25 = current UTC while org local (Pacific/Auckland) is 21:25, and 'SAR TIME (LOCAL)' shows 09:25. Cancel with no changes does nothing; back arrow returns to schedule (edit mode kept) |
| FS-012 | Single-click a flight | Selected; edit / note / cancelled / F&D icons shown as applicable | PASS |  | Click selects the flight (blue outline, fc-event-selected); small edit + note icons appear on its top edge. Edit mode shows 'Live Edit Mode - Changes are live for everyone.' banner |
| FS-013 | Note icon popup | PIC, crew, lesson, route, notes, aircraft inspections due | PASS |  | View Details icon (aria 'View Details') opens '#8656 ZK-SIM' popup: PIC, Crew, Route NZWN-NZNS, Notes, OK. Lesson/inspections empty for this flight so not shown. Esc does not close it (BUG-POP-004) |
| FS-014 | Move / resize open flight | Toast 'Updated flight #ID time.' | PASS |  | Move #42903 down 1h: 08:30-09:30 > 09:30-10:30, toast 'Updated flight #42903 time.'. Resize end handle +30 min: 09:30-11:00, toast 'Updated flight #42903 duration.' |
| FS-015 | Move completed / cancelled flight | 'Completed flights cannot be moved.' / refused | PASS |  | Completed #8795 (status C, editable false, week 12-18 Oct): drag does nothing, time stays 06:00-07:00. No 'Completed flights cannot be moved.' message, it just does not move. Delete key: Error modal 'Completed flights cannot be deleted.' |
| FS-016 | Undo Last Action | Reverts last move/resize | PASS |  | Undo twice: 'Undo successful.' each time, 09:30-11:00 > 09:30-10:30 > 08:30-09:30; Undo button then disabled |
| FS-017 | Ctrl+C > click slot > Ctrl+V | Copy Flight Options (Legs, Forms + content, Files with counts); required forms locked on | PASS |  | Ctrl+C on #42903 > toast 'Flight ... copied. Click on the schedule to place it, then press Ctrl+V'. Click empty slot > 'Press Ctrl+V to paste the flight here' > Copy Flight Options: Legs 0, Forms 0 + Include form content, Files 0, all ticked. Required-form lock not testable (no forms on flight). Ctrl+V before choosing a slot gives an Error modal 'Click on the schedule to choose where to paste the flight.' |
| FS-018 | Paste multiple copies | Each paste creates a new flight | PASS |  | Paste > 'Flight pasted successfully. Click another spot and press Ctrl+V to paste again, or press Escape to finish.' Two pastes created #42904 (Mon 19 07:25) and #42905 (16:05); 2nd paste reused the chosen options without reopening the modal |
| FS-019 | Ctrl+X > Ctrl+V on open flight | Flight moved; not allowed for completed/cancelled | PASS |  | Ctrl+X on #42905 > toast 'Flight ... cut. Click on the schedule to place it, then press Ctrl+V to move.' > click slot > 'Press Ctrl+V to move the flight here' > Ctrl+V moved #42905 16:05 > 09:05 (no copy left behind). Completed/cancelled not tested yet (no such BETA flight) |
| FS-020 | Delete key on open flight | Confirmation then deleted; refused for non-open | PASS |  | Delete key on selected open flight > app modal 'Delete Flight - Are you sure you want to delete this flight? #42906 ... This action cannot be undone.' Cancel/Delete > 'Flight deleted successfully.' Deleted #42904-#42906. Non-open refusal: see FS-015 |
| FS-021 | Esc during copy/cut | Cancels | FAIL | BUG-FS-002 | After pasting, toast says 'press Escape to finish'. Pressed Esc (no toast), clicked another slot > 'Press Ctrl+V to paste the flight here' > Ctrl+V created another copy #42906. Esc did not end paste mode |
| FS-022 | Double booking (same aircraft or person overlapping) | Warning shown | PASS |  | Overlapping #42905/#42906 (same ZK-SIM + PIC, Tue 20 Oct) both get a 'Flight Alert' icon; it opens 'Double Booking Detected': Aircraft Double Booked (#42905, #8847), Personnel Double Booked (PIC on #42905), advice line, OK. No warning at paste time, only the icon afterwards |
| FS-023 | F&D violation icon / popup | Flight & Duty Violations popup lists violations | IN PROGRESS |  | Same alert popup (#fad-modal) works for double bookings; no flight with an F&D violation found yet to test the violations list |
| FS-024 | Add Note (Start, End, Title, Details) > view/edit/delete | Works | PASS |  | Add Note: Start/End Date, Title, Details > 'Note added successfully'. Click note > Edit Note modal > Update > 'Note updated successfully'. Delete Note > app confirm 'Are you sure you want to delete this note?' > 'Note deleted successfully', gone from schedule. Esc on note modals does nothing (see BUG-POP-004) |
| FS-025 | Idle 20 min in edit mode | 'Edit mode has been disabled due to inactivity.' | TODO | | |
| FS-026 | Mobile width | List view; tap opens Flight Details; edit mode off; Add Flight visible | PASS |  | 390 px: list view (listMonth 'October 2026'), no horizontal scroll, Live Edit button + banner hidden, Add Flight visible. Tap #8688 opens Flight Details. Note: list starts at 1 Oct (not today) and each day lists ~20 Roster rows before the flights, so flights are hard to find |
| FS-027 | RG/WG user | Sees only flights on aircraft in their groups; see §14 caveat on membership read/write flag | TODO | | |
| FS-028 | View mode (if Location Planner enabled): Schedule Only / Schedule & Planner / Planner Only | Each works; Rows by Aircraft / by Location | PASS |  | Schedule Only / Schedule & Planner (planner left + schedule right; schedule half switches to list view from 1 Oct) / Planner Only all work. Rows by Aircraft lists aircraft + type (ZK-AIR C172-02 ...); Rows by Location lists AKL Auckland Base. Planner range 19/10-15/11 (4 Weeks), Day/Week/Month + 4/8/12 Weeks |
| FS-029 | Planner: Filter by Location, search, Add Location (Name, Code, Color) | Works | FAIL | BUG-FS-004 | Filter by Location: search 'zzz' > 'No locations found', 'auck' > AKL; picking it filters + shows pill. Add Location (Name, Code, Color #3b82f6): empty Save > Error 'Name and Code are required.'; saved 'BETA TEST ONLY Loc' / BTO > toast 'Location created'. But opening Add Location closes the New Booking popup (typed notes lost) and OK on the error closes everything (BUG-FS-004) |
| FS-030 | Planner: New Booking (From, To, Location, Aircraft, Notes) | Saved; appears in grid | PASS |  | New Booking ZK-SIM @ AKL 31/10-02/11/2026 + notes > Save Booking > toast 'Booking created'; bar 'ZK-SIM C182-02' appears in AKL row, header '1 aircraft in this period', planner Undo button appears. Needs Live Edit ON (drag silently ignored otherwise) |
| FS-031 | Planner booking tabs: Details / Flights / Templates | Flights list correct for range; New Template requires Template Title | PASS |  | Booking detail modal: Details (Aircraft, Location, From/To, Duration 3 days, Notes), Flights tab lists '#8963 NZWN-NZNS 02/11/2026 13:58 - Clayton Wheeler - ZK-SIM', Templates tab + New Template > Flight Template page. Empty title > app modal 'Template Title is required.' Saved 'BETA TEST ONLY Template' > returns to schedule (no success toast) and the template is listed with Edit / Copy / Delete Template |
| FS-032 | Planner template copy onto schedule | Requires edit mode; flight created | PASS |  | Copy Template with Live Edit off > app modal 'Edit Mode Required' (Cancel / Enable Edit Mode). Enable Edit Mode > toast 'Template ... copied. Click on the schedule to place it, then press Ctrl+V'. Click 22/10 15:00 + Ctrl+V > Copy Flight Options > Paste > flight #42908 15:10-16:10 ZK-SIM, PIC BETA TEST ONLY Lowperm created. Note: returning from the template page resets the schedule to Live Edit off and the 28 Sep week |
| FS-033 | Undo Last Booking Change | Reverts | PASS |  | Live Edit on, drag booking bar 2 days right > toast 'Booking updated', planner Undo ('Undo Last Booking Change') enabled > click > toast 'Undo successful', bar back on 31/10-02/11, button disabled again |
| FS-034 | Performance on month view with 9,400+ flights | Loads; server timings < 500 ms | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| FUNC-03 | Low | Open (external) | Flight Schedule toolbar buttons disappear after toggling sticky notes |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Note 'BETA TEST ONLY Note' (21/10/2026) | Flight Schedule | Yes (deleted in FS-024) |
| Flight #42903 ZK-SIM, PIC BETA TEST ONLY Lowperm, route NZWN-NZWN, notes 'BETA TEST ONLY flight', 21/10/2026 08:30 | Flight Schedule / Flight Details | No |
| Flights #42904, #42905, #42906 (pasted copies of #42903, week 19-25 Oct 2026; #42906 from BUG-FS-002) | Flight Schedule | Yes (deleted in FS-020) |
| Planner booking ZK-SIM @ AKL Auckland Base 31/10-02/11/2026, notes 'BETA TEST ONLY booking' | Flight Schedule > Planner | No |
| Flight template 'BETA TEST ONLY Template' (ZK-SIM, PIC BETA TEST ONLY Lowperm) on the AKL booking | Flight Schedule > Planner > Templates | No |
| Flight #42908 ZK-SIM, PIC BETA TEST ONLY Lowperm, 22/10/2026 15:10-16:10 (pasted from the template) | Flight Schedule | No |
| Location 'BETA TEST ONLY Loc' (code BTO) | Flight Schedule > Planner > Add Location | No |
