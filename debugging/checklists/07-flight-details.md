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
| FD-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| FD-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| FD-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| FD-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| FD-001 | Read-only user (RA/RG/RO) | Yellow banner e.g. 'Read-Only Group Access…'; Save/Cancel/Delete hidden | TODO | | |
| FD-002 | Header: Back, PDF, History, Cancel, Save Changes, Delete (open only), Help | All present and working | PASS |  | Header shows Back, PDF, History, Cancel, Save Changes, Delete, Help on the open flight; individual actions tested in FD-003, FD-034, FD-037, FD-038 |
| FD-003 | PDF with unsaved changes | Asks to save first | TODO | | |
| FD-004 | Details: Aircraft dropdown | Only Active + Is Aircraft resources | TODO | | |
| FD-005 | Details: PIC / Secondary Flight Crew | Only Crew or Student role people | TODO | | |
| FD-006 | Notify toggles | Sends email/SMS on save; not stored (off on reopen) | TODO | | |
| FD-007 | Flight Category / Activity dropdowns | From Settings > Flight Types; auto-attach forms fire ('Form "X" auto-attached') | TODO | | |
| FD-008 | Start/End Time, SAR Time, SAR Watch default on | Pickers follow Time Zone setting; booking times may be exceeded by flight times (not a bug) | TODO | | |
| FD-009 | Flight Follower / Authorized By | Only Admin/Staff people | TODO | | |
| FD-010 | Notify Overdue by Text / Email | Saved | TODO | | |
| FD-011 | Extra Information (F fields) | Fields from Extra Flight Info appear and save | TODO | | |
| FD-012 | Comments | Add a Comment saves with flight | TODO | | |
| FD-013 | Customer: Existing (company first) + Contact Person suggestions | Works | TODO | | |
| FD-014 | Customer: New Customer | Creates customer record (with Customer role) | TODO | | |
| FD-015 | Passenger List: Add Crew Member | Weight from personnel record or 'No weight on file – please enter' | TODO | | |
| FD-016 | Passenger List: Add Custom Passenger | Added to manifest | TODO | | |
| FD-017 | kg/lbs toggle | Converts correctly | TODO | | |
| FD-018 | W&B toggle | Only if registration in Master W&B config; per-leg summary + graphs; newer revision prompt | TODO | | |
| FD-019 | Times and Meters | Totals with source hint; previous reading + link to previous flight | TODO | | |
| FD-020 | Cumulative meter lower than previous | 'Meter "X" value (…) is less than previous reading (…)' | TODO | | |
| FD-021 | Legs: Add Leg top/bottom; delete leg | Works; delete confirms | TODO | | |
| FD-022 | Leg waypoints unknown | Prompt to pick or add; 'Waypoint X added successfully' | TODO | | |
| FD-023 | Leg time fields | Match resource Time Inputs settings | TODO | | |
| FD-024 | Crew Recency tab | Items per crew member from direct + group template assignments | TODO | | |
| FD-025 | Lesson tab | Only when PIC/crew is Student; lessons from assigned plan; exercises, assessment sliders 0–5, debrief | TODO | | |
| FD-026 | Forms tab: Add Form | Works | TODO | | |
| FD-027 | Files tab: upload (incl. > 30 MB) | Upload works; > 30 MB rejected cleanly | TODO | | |
| FD-028 | Flight Status: Open / Complete / Canceled | Cards selectable; Reason for Cancellation when Canceled; secondary status pills | TODO | | |
| FD-029 | Complete & Locked | Only visible to WL; admins need WL explicitly | TODO | | |
| FD-030 | Locked flight | 'This flight is locked…' read-only for all; WL can unlock by changing status | TODO | | |
| FD-031 | Complete without Start/End/SAR or end < start | Required Information popup | TODO | | |
| FD-032 | W&B on, seated person weight 0 | Blocked | TODO | | |
| FD-033 | Required to Complete meter left empty | Guide: not enforced (known gap) — confirm and log | TODO | | |
| FD-034 | Save success | Returns to where you came from | TODO | | |
| FD-035 | Leave with unsaved changes | Stay on Page / Leave Page | TODO | | |
| FD-036 | Flight & Duty Limit Alert | Shown when crew exceed FRMS limits | TODO | | |
| FD-037 | History | Shows changes made in this run | TODO | | |
| FD-038 | Delete open flight | Confirmation; flight soft-deleted (D) | TODO | | |

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
| | | |
