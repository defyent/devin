# Hazard Register

- **Checklist ID prefix:** `HAZ`
- **Guide section:** §10.5
- **Where:** Flight Safety > Hazard Register
- **Permission:** Hazard Register A/RG
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| HAZ-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Flight Safety > Hazard Register loads (2 hazards). One 'removeChild' page error appeared once during the first run and did not come back on later loads |
| HAZ-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | PASS |  | Help opens; closes with Got it, x, a click outside and Esc |
| HAZ-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag-out keeps Help open |
| HAZ-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | PASS |  | List and details show DD/MM/YYYY HH:MM (08/01/2026 11:10, 22/10/2026 00:38). DATE-09 ('8 Jan 2026') no longer seen |
| HAZ-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | At 390px the list shows as cards (Type, Date/Time, Goal, Risk); document width 390px |
| HAZ-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low still sees the menu link; opening it shows 'Access Denied: You do not have permission to access Hazard Register' |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| HAZ-001 | List columns ID, Type, Subject, Date/Time, Goal, Risk; search | Works | PASS |  | Columns ID, Type, Subject, Date/Time, Goal, Risk; search 'Bird' leaves #176 only, clear brings back both |
| HAZ-002 | Create New Hazard entry | Also creates underlying safety report | FAIL | BUG-HAZ-003 | No Create button on Hazard Register; entries can only be added from a Safety Report's Final Report tab (#2060 added that way) |
| HAZ-003 | Details tabs: Hazard Details, Original SMS Report, Risk Assessment | Correct data | FAIL | BUG-HAZ-001, BUG-HAZ-002 | Hazard Details, Original SMS Report and Risk Assessment tabs open with the right report data, but Hazard Type always shows '--' and the saved Final Risk shows '--' |
| HAZ-004 | Edit hazard fields (Type, Goal, Controls, Review Date, Responsible) | Saved | PASS | BUG-HAZ-001 | Hazard Details is read-only; fields are edited on the Safety Report's Final Report tab. Changing Goal to Eliminate and Controls there shows up in Hazard Register. Type still shows '--'. Review Date was saved as 21/10/2026 (the UTC date) even though I left it blank |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| DATE-09 | Low | Open (external) | Hazard Register date has no leading zero ("8 Jan 2026") |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Hazard entry for safety report #2060 'BETA TEST ONLY hazard' (goal Eliminate, controls edited, responsible Aisha Pearce) | Flight Safety > Hazard Register (edited via Safety Reports > #2060 > Final Report) | No - goes with report #2060 |
