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
| FS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| FS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| FS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| FS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| FS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| FS-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FS-001 | Day / Week / Month / List views; ‹ › Today | Each renders; view and date remembered on reload | TODO | | |
| FS-002 | Past/future date banners | 'You are viewing a past/future date' with Today button | TODO | | |
| FS-003 | Group By dropdown | Only groups with Show in Dropdown; WG/RG users see only their own | TODO | | |
| FS-004 | Toggle Roster | Roster row shows only Show-on-Schedule shifts and On Roster members | TODO | | |
| FS-005 | Toggle Notes | Notes show/hide | TODO | | |
| FS-006 | Compact view (month) | Max 3 events/day with +more | TODO | | |
| FS-007 | Font size slider | Changes size; remembered? | TODO | | |
| FS-008 | Toggle Edit Mode (write users only) | Enable/Disable Live Edit; hidden for RA/RG | TODO | | |
| FS-009 | Edit mode: drag on empty slot in aircraft column | Flight Details opens pre-filled start/end/aircraft | TODO | | |
| FS-010 | Edit mode: drag in all-day area | All-day flight created | TODO | | |
| FS-011 | Add Flight button | Blank Flight Details | TODO | | |
| FS-012 | Single-click a flight | Selected; edit / note / cancelled / F&D icons shown as applicable | TODO | | |
| FS-013 | Note icon popup | PIC, crew, lesson, route, notes, aircraft inspections due | TODO | | |
| FS-014 | Move / resize open flight | Toast 'Updated flight #ID time.' | TODO | | |
| FS-015 | Move completed / cancelled flight | 'Completed flights cannot be moved.' / refused | TODO | | |
| FS-016 | Undo Last Action | Reverts last move/resize | TODO | | |
| FS-017 | Ctrl+C > click slot > Ctrl+V | Copy Flight Options (Legs, Forms + content, Files with counts); required forms locked on | TODO | | |
| FS-018 | Paste multiple copies | Each paste creates a new flight | TODO | | |
| FS-019 | Ctrl+X > Ctrl+V on open flight | Flight moved; not allowed for completed/cancelled | TODO | | |
| FS-020 | Delete key on open flight | Confirmation then deleted; refused for non-open | TODO | | |
| FS-021 | Esc during copy/cut | Cancels | TODO | | |
| FS-022 | Double booking (same aircraft or person overlapping) | Warning shown | TODO | | |
| FS-023 | F&D violation icon / popup | Flight & Duty Violations popup lists violations | TODO | | |
| FS-024 | Add Note (Start, End, Title, Details) > view/edit/delete | Works | TODO | | |
| FS-025 | Idle 20 min in edit mode | 'Edit mode has been disabled due to inactivity.' | TODO | | |
| FS-026 | Mobile width | List view; tap opens Flight Details; edit mode off; Add Flight visible | TODO | | |
| FS-027 | RG/WG user | Sees only flights on aircraft in their groups; see §14 caveat on membership read/write flag | TODO | | |
| FS-028 | View mode (if Location Planner enabled): Schedule Only / Schedule & Planner / Planner Only | Each works; Rows by Aircraft / by Location | TODO | | |
| FS-029 | Planner: Filter by Location, search, Add Location (Name, Code, Color) | Works | TODO | | |
| FS-030 | Planner: New Booking (From, To, Location, Aircraft, Notes) | Saved; appears in grid | TODO | | |
| FS-031 | Planner booking tabs: Details / Flights / Templates | Flights list correct for range; New Template requires Template Title | TODO | | |
| FS-032 | Planner template copy onto schedule | Requires edit mode; flight created | TODO | | |
| FS-033 | Undo Last Booking Change | Reverts | TODO | | |
| FS-034 | Performance on month view with 9,400+ flights | Loads; server timings < 500 ms | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| FUNC-03 | Low | Open (external) | Flight Schedule toolbar buttons disappear after toggling sticky notes |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
