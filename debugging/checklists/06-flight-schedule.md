# Flight Schedule (incl. embedded Location Planner)

- **Checklist ID prefix:** `FS`
- **Guide section:** §8.2
- **Where:** Flight Operations > Flight Schedule
- **Permission:** Flight Schedule A/RA/WG/RG
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Opened via sidebar, week view 19-25 October 2026; no console errors (iframe sandbox warning only) |
| FS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS | VIS-06 | Retest 22/10/2026 (v2.0.114): Help (?) button now in the page header; opens the Help popup, which closes with Esc and with an outside click |
| FS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Flight details popup: mousedown inside, release outside > stays open. Outside click closes it |
| FS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-FS-001 | Header shows UTC + Local (Pacific/Auckland); schedule/planner dates dd/mm/yyyy and event times local. Retest 22/10/2026: Add Flight still defaults Start/End/SAR to the UTC time (BUG-FS-001) |
| FS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | See FS-026: 390 px switches to list view, no horizontal scroll, tap opens Flight Details |
| FS-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low (Crew, 1 permission, no Flight Schedule permission): menu still lists Flight Schedule; opening it shows 'Access Denied: You do not have permission to access the flight schedule', no Live Edit / Add Flight. See checklist 90 for menu visibility |

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
| FS-008 | Toggle Edit Mode (write users only) | Enable/Disable Live Edit; hidden for RA/RG | PASS | BUG-FS-003, BUG-FS-005 | Retest 22/10/2026 (v2.0.114): toggling logs no script errors (BUG-FS-005 fixed); with a location picked, a past week and Live Edit on, the banners sit on their own row with no overlap and Show All works (BUG-FS-003 fixed) |
| FS-009 | Edit mode: drag on empty slot in aircraft column | Flight Details opens pre-filled start/end/aircraft | PASS |  | Day view 19 Oct, drag 07:30-08:25 in empty ZK-JET column > New Flight Details opens with aircraft ZK-JET, start 19/10/2026 07:30, end 08:25 (URL starttime/endtime/resource_id=3). Not saved |
| FS-010 | Edit mode: drag in all-day area | All-day flight created | BLOCKED |  | No separate all-day flight row: in week view the top day-grid is the 'Roster' area (full of roster shifts + notes, no empty cell to drag in); day view (aircraft columns) has no all-day row and greys out Toggle Roster/Notes. Need to know where all-day flights are meant to be created |
| FS-011 | Add Flight button | Blank Flight Details | FAIL | BUG-FS-001 | Retest 22/10/2026 (v2.0.114): Add Flight opens blank New Flight Details, but at local 18:09 Start is 22/10/2026 05:10, End 06:10, SAR TIME (LOCAL) 06:10 = UTC. Cancel with no changes still does nothing. Second retest (v2.0.114): at local 20:43 Start 07:45 / End 08:45 (UTC); Cancel still stays. Third retest (v2.0.115): still UTC (local 20:49 -> 07:50); Cancel still stays |
| FS-012 | Single-click a flight | Selected; edit / note / cancelled / F&D icons shown as applicable | PASS |  | Click selects the flight (blue outline, fc-event-selected); small edit + note icons appear on its top edge. Edit mode shows 'Live Edit Mode - Changes are live for everyone.' banner |
| FS-013 | Note icon popup | PIC, crew, lesson, route, notes, aircraft inspections due | PASS | BUG-POP-004 | Retest 22/10/2026: View Details on #8834 shows PIC, Crew, Route, Notes; Esc now closes it (BUG-POP-004 fixed) |
| FS-014 | Move / resize open flight | Toast 'Updated flight #ID time.' | PASS |  | Move #42903 down 1h: 08:30-09:30 > 09:30-10:30, toast 'Updated flight #42903 time.'. Resize end handle +30 min: 09:30-11:00, toast 'Updated flight #42903 duration.' |
| FS-015 | Move completed / cancelled flight | 'Completed flights cannot be moved.' / refused | PASS |  | Completed #8795 (status C, editable false, week 12-18 Oct): drag does nothing, time stays 06:00-07:00. No 'Completed flights cannot be moved.' message, it just does not move. Delete key: Error modal 'Completed flights cannot be deleted.' |
| FS-016 | Undo Last Action | Reverts last move/resize | PASS |  | Undo twice: 'Undo successful.' each time, 09:30-11:00 > 09:30-10:30 > 08:30-09:30; Undo button then disabled |
| FS-017 | Ctrl+C > click slot > Ctrl+V | Copy Flight Options (Legs, Forms + content, Files with counts); required forms locked on | PASS |  | Ctrl+C on #42903 > toast 'Flight ... copied. Click on the schedule to place it, then press Ctrl+V'. Click empty slot > 'Press Ctrl+V to paste the flight here' > Copy Flight Options: Legs 0, Forms 0 + Include form content, Files 0, all ticked. Required-form lock not testable (no forms on flight). Ctrl+V before choosing a slot gives an Error modal 'Click on the schedule to choose where to paste the flight.' |
| FS-018 | Paste multiple copies | Each paste creates a new flight | PASS |  | Paste > 'Flight pasted successfully. Click another spot and press Ctrl+V to paste again, or press Escape to finish.' Two pastes created #42904 (Mon 19 07:25) and #42905 (16:05); 2nd paste reused the chosen options without reopening the modal |
| FS-019 | Ctrl+X > Ctrl+V on open flight | Flight moved; not allowed for completed/cancelled | PASS |  | Ctrl+X on #42905 > toast 'Flight ... cut. Click on the schedule to place it, then press Ctrl+V to move.' > click slot > 'Press Ctrl+V to move the flight here' > Ctrl+V moved #42905 16:05 > 09:05 (no copy left behind). Completed/cancelled not tested yet (no such BETA flight) |
| FS-020 | Delete key on open flight | Confirmation then deleted; refused for non-open | PASS |  | Delete key on selected open flight > app modal 'Delete Flight - Are you sure you want to delete this flight? #42906 ... This action cannot be undone.' Cancel/Delete > 'Flight deleted successfully.' Deleted #42904-#42906. Non-open refusal: see FS-015 |
| FS-021 | Esc during copy/cut | Cancels | PASS | BUG-FS-002 | Retest 22/10/2026: after pasting #42912, Esc shows 'Copy/paste finished. Ctrl+V will no longer paste.' and a later click + Ctrl+V creates nothing. #42912 deleted. Second retest: copy #42909, Esc, click a slot, Ctrl+V: no popup and no new flight (Ctrl+V is now a no-op) |
| FS-022 | Double booking (same aircraft or person overlapping) | Warning shown | PASS |  | Overlapping #42905/#42906 (same ZK-SIM + PIC, Tue 20 Oct) both get a 'Flight Alert' icon; it opens 'Double Booking Detected': Aircraft Double Booked (#42905, #8847), Personnel Double Booked (PIC on #42905), advice line, OK. No warning at paste time, only the icon afterwards |
| FS-023 | F&D violation icon / popup | Flight & Duty Violations popup lists violations | IN PROGRESS |  | Alert popup (#fad-modal) verified via Double Booking. No flight with a real Flight & Duty violation found yet; retest with FD-036 and checklist 40 (FRMS limits) |
| FS-024 | Add Note (Start, End, Title, Details) > view/edit/delete | Works | PASS |  | Add Note: Start/End Date, Title, Details > 'Note added successfully'. Click note > Edit Note modal > Update > 'Note updated successfully'. Delete Note > app confirm 'Are you sure you want to delete this note?' > 'Note deleted successfully', gone from schedule. Esc on note modals does nothing (see BUG-POP-004) |
| FS-025 | Idle 20 min in edit mode | 'Edit mode has been disabled due to inactivity.' | PASS | BUG-FS-007 | Retest 22/10/2026 (betatest_grp): at 20.0 min Live Edit turned off with 'Edit mode has been disabled due to inactivity.', no errors, schedule still shows flights |
| FS-026 | Mobile width | List view; tap opens Flight Details; edit mode off; Add Flight visible | PASS |  | 390 px: list view (listMonth 'October 2026'), no horizontal scroll, Live Edit button + banner hidden, Add Flight visible. Tap #8688 opens Flight Details. Note: list starts at 1 Oct (not today) and each day lists ~20 Roster rows before the flights, so flights are hard to find |
| FS-027 | RG/WG user | Sees only flights on aircraft in their groups; see §14 caveat on membership read/write flag | PASS | re_fs008_week | Retest 22/10/2026: betatest_grp (#209=WG, member of BETA TEST ONLY Group) sees ZK-BTO with #42909 and #42910 in week, list and Group By views (BUG-FS-008 fixed) |
| FS-028 | View mode (if Location Planner enabled): Schedule Only / Schedule & Planner / Planner Only | Each works; Rows by Aircraft / by Location | PASS |  | Schedule Only / Schedule & Planner (planner left + schedule right; schedule half switches to list view from 1 Oct) / Planner Only all work. Rows by Aircraft lists aircraft + type (ZK-AIR C172-02 ...); Rows by Location lists AKL Auckland Base. Planner range 19/10-15/11 (4 Weeks), Day/Week/Month + 4/8/12 Weeks |
| FS-029 | Planner: Filter by Location, search, Add Location (Name, Code, Color) | Works | PASS | BUG-FS-004 | Retest 22/10/2026: Add Location opens on top of New Booking; error OK returns to Add Location; Save returns to New Booking with the note kept and 'BETA TEST ONLY Loc2' listed (BUG-FS-004 fixed). Minor: Locations filter popup stays open after picking a location. Second retest: picking Auckland Base applies the filter but the Locations popup still stays open until Esc. Third retest (v2.0.115): the Locations popup still stays open after picking |
| FS-030 | Planner: New Booking (From, To, Location, Aircraft, Notes) | Saved; appears in grid | PASS |  | New Booking ZK-SIM @ AKL 31/10-02/11/2026 + notes > Save Booking > toast 'Booking created'; bar 'ZK-SIM C182-02' appears in AKL row, header '1 aircraft in this period', planner Undo button appears. Needs Live Edit ON (drag silently ignored otherwise) |
| FS-031 | Planner booking tabs: Details / Flights / Templates | Flights list correct for range; New Template requires Template Title | PASS |  | Booking detail modal: Details (Aircraft, Location, From/To, Duration 3 days, Notes), Flights tab lists '#8963 NZWN-NZNS 02/11/2026 13:58 - Clayton Wheeler - ZK-SIM', Templates tab + New Template > Flight Template page. Empty title > app modal 'Template Title is required.' Saved 'BETA TEST ONLY Template' > returns to schedule (no success toast) and the template is listed with Edit / Copy / Delete Template |
| FS-032 | Planner template copy onto schedule | Requires edit mode; flight created | PASS |  | Copy Template with Live Edit off > app modal 'Edit Mode Required' (Cancel / Enable Edit Mode). Enable Edit Mode > toast 'Template ... copied. Click on the schedule to place it, then press Ctrl+V'. Click 22/10 15:00 + Ctrl+V > Copy Flight Options > Paste > flight #42908 15:10-16:10 ZK-SIM, PIC BETA TEST ONLY Lowperm created. Note: returning from the template page resets the schedule to Live Edit off and the 28 Sep week |
| FS-033 | Undo Last Booking Change | Reverts | PASS |  | Live Edit on, drag booking bar 2 days right > toast 'Booking updated', planner Undo ('Undo Last Booking Change') enabled > click > toast 'Undo successful', bar back on 31/10-02/11, button disabled again |
| FS-034 | Performance on month view with 9,400+ flights | Loads; server timings < 500 ms | FAIL | BUG-FS-006 | Retest 22/10/2026: month JSON 1,072-1,369 ms (first byte 365-384 ms), 2,497 events, no errors. Better than 1,590 ms but still over 500 ms. Second retest: 1,286-1,344 ms, first byte 576-633 ms, not gzipped. Third retest (v2.0.115): now gzipped, 465 KB; warm requests 364-373 ms, but the first request takes 835 ms and in the browser the first byte arrives at 635 ms |

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
| Flight #42908 ZK-SIM, PIC BETA TEST ONLY Lowperm, 22/10/2026 15:10-16:10 (pasted from the template) | Flight Schedule | Yes - deleted in FD-038 |
| Location 'BETA TEST ONLY Loc' (code BTO) | Flight Schedule > Planner > Add Location | No |
