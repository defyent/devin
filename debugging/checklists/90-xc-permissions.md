# Cross-cutting: permission levels

- **Checklist ID prefix:** `PERM`
- **Guide section:** §1.4, §5.4, §14, §15.1
- **Where:** All modules
- **Permission:** Needs one account per level
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| PERM-001 | For each permission type in §15.1, with a level-A account | Full access | PASS |  | The Service Account is an admin with 0 permission rows and gets full access: every module and settings page in checklists 04 to 47 opened with all write controls. No separate level-A test user exists. |
| PERM-002 | Same with RA | View all, no write controls | PASS |  | Lowperm given Flight Schedule (permission type id 2) = RA: the schedule shows every flight (413 events), with no Live Edit or Add Flight. Selecting a flight still shows the edit pencil, which opens Flight Details with "Access Denied" (no Flight Details permission). That is the shown-but-denied pattern from BUG-PERM-001. |
| PERM-003 | Same with WG / RG | Only group-shared items; write only for WG | PASS |  | Flight Schedule (id 2) = G: Lowperm sees 0 flights (its groups have no aircraft) and no Live Edit or Add Flight. Notices (id 219) = WG: Lowperm sees 28 notices against 30 for the Service Account, and New Notice is shown (shot perm_wo_notices). I did not create a notice, because notices cannot be deleted. |
| PERM-004 | Same with WO / RO | Only own items | PASS |  | Personnel Details = WO: Lowperm opens and edits its own My Account (checklist 12), and All Personnel is Access Denied. Notices first card (id 11) = WO gives Access Denied, because the page checks the other Notices card (BUG-AM-005). |
| PERM-005 | Flight Details WL (admin with explicit WL) | Can lock/unlock | PASS |  | Gave the Service Account an explicit Flight Details (id 214) = WL row. "Complete & Locked" then shows on the Flight Status tab (it was missing before, FD-029). Locking flight #42903 shows "This flight is locked. Select a different status..." with all 21 inputs disabled (shot perm_wl_locked). Choosing Complete and Save unlocks it. The flight is back to Complete and the WL row was removed afterwards. |
| PERM-006 | Admin with an explicit lower row | Explicit level wins (deliberate) | PASS |  | Gave the Service Account (admin, 0 rows) an explicit Notices (id 219) = RA row: Notices then shows no New Notice button and no edit/delete actions (shot perm_ra_notices_sa). The explicit lower level wins, as the guide says it should. The row was removed afterwards. |
| PERM-007 | No permission row | 'Access Denied' — never a blank page or JS error | PASS |  | 0-permission user: all 17 visible menu items show an Access Denied card, no blank page / JS error. But sidebar still lists them (BUG-PERM-001; confirmed 22/10/2026 that they should be hidden) |
| PERM-008 | Inactive user with permissions | No access at all | PASS |  | Inactive user with 1 permission: login refused with generic message; live session ends on next request |
| PERM-009 | Server-side enforcement: hidden button but action attempted (e.g. Delete key, drag) as read-only | Server rejects with Access Denied popup | PASS |  | As Lowperm (Flight Schedule = G, no write), sent the update request the schedule uses for a drag (flight #42903, same times and aircraft, so nothing would change). The server answered "Access Denied: You do not have permission to update flights". A delete request answered "Access Denied: You do not have permission to delete flights". Flight Details by its own link also gives Access Denied (PERM-002). |
| PERM-010 | Group membership read/write flag caveat (§14) | Check whether Access Manager-saved memberships give WG schedule write | PASS | re_fs008_week | Retest 22/10/2026: with only the 'On Roster' membership and Flight Schedule WG, betatest_grp now sees ZK-BTO flights and can turn on Live Edit (BUG-FS-008 fixed). No flight was edited as Grpuser |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
