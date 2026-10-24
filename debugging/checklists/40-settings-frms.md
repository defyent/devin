# Settings – Fatigue Risk Management

- **Checklist ID prefix:** `SFRMS`
- **Guide section:** §12.10
- **Where:** Settings and Tools > Safety > Fatigue Risk Management Settings
- **Permission:** settings_frms = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SFRMS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Fatigue Risk Management Settings opens settings_frms, with no console errors. |
| SFRMS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-SFRMS-001 | No page Help (?), and Escape does not close Add Flight Time Limit Rule. |
| SFRMS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside Add Flight Time Limit Rule to outside it: it stays open. |
| SFRMS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | N/A |  | No dates or times on this page, only hours and day counts. |
| SFRMS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | FAIL | BUG-SFRMS-002 | At 390 px the section pills become a dropdown (good), but the page is 506 px wide: it scrolls sideways, Add Rule is off-screen and rule text is clipped. |
| SFRMS-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Administration > Settings and Tools shows Access Denied (System Settings), same as 31-33, so FRMS can't be reached. |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SFRMS-001 | Flight/Duty Time limit rules CRUD with all fields | Saved; validation of Warning/Caution vs Max | PASS |  | Flight and Duty Time Limit rules: add/edit/delete work on a BETA TEST ONLY Group rule (delete asks first and names the rule). Validation: required fields (native), "Warning threshold (12h) must be lower than the Caution threshold (11h)", "Caution threshold (11h) must not exceed Max Hours (10h)". Edit Max 10 -> 11 saved and showed. Test rules deleted. |
| SFRMS-002 | Rest & Recovery types | Saved | PASS |  | Rest & Recovery: "Require minimum rest period" with Fixed duration (10 h) shows "Recovery Rule: Fixed 10 hours", and Equal to time worked shows "Recovery Rule: Equal to time worked". |
| SFRMS-003 | Roster rules: Max Consecutive / Max in Period / Shift Sequence | Saved; Roster Builder violations | PASS |  | Rule types Max Consecutive / Max in Period / Shift Sequence (If shift is X, it can ONLY be followed by ...) are all there. A BETA Max Consecutive rule (2) saved as "No more than 2 'Any' shifts in a row BETA TEST ONLY Group" and was deleted (confirm names the rule). Roster Builder violations from FRMS rules were checked in 14 (RB). Minor: "In Period (Days)" is shown for Max Consecutive too, where it does not apply. |
| SFRMS-004 | AC119-2 wizard Next/Back through all 5 steps (add vs replace) | Rules imported | PASS |  | AC119-2 wizard: 5 steps (Existing Rules keep/wipe, Operation Type, Rules toggle, User Groups, Rostered Shift Rules), and Back works. Each step checks its input: "Please select at least one operation type", "...user group", "...duty shift type or uncheck the roster rule". Imported with "Keep existing rules" + General Restrictions + BETA TEST ONLY Group + Day Shift: 2 duty rules (Max 200/30 days, Max 14/1 day) and roster rule "No more than 6 'Day Shift' shifts in a row" were added next to the existing rules, which were all kept. "Wipe all" was not run (it would remove the live rules). The imported BETA rules were then deleted. |
| SFRMS-005 | Results appear in Schedule, Flight Details, F&D page, Roster Builder, Timesheets | Consistent | PASS | sfrms005_sched | Added BETA FRMS rule "Max 0.5 flight time hours in any 1 days" for BETA TEST ONLY Group, then flew Grpuser 0.8h on #42909. Schedule: #42909 shows the F&D alarm icon, and it opens "Flight & Duty Limit Exceeded ... 0.80 hours in last 1 days (max 0.50)". Flight Details: "F&D Exceeded" badge with the same text. F&D page: Grpuser shows "0.8h Over Limit (0.5h)" under BETA TEST ONLY Group. Roster Builder (RB-011) and Timesheets F&D Analysis (TS-007) already showed FRMS results earlier. All the same. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |

**Test data (40):** all BETA TEST ONLY Group rules (flight, duty, roster and the 3 imported AC119-2 rules) were deleted. No existing rules were changed.
