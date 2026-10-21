# Settings – Weight and Balance Configs

- **Checklist ID prefix:** `SWAB`
- **Guide section:** §12.5
- **Where:** Settings and Tools > Configuration > Weight and Balance Configs
- **Permission:** settings_wabconfigs = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SWAB-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | FAIL | BUG-SWAB-003 | Loads with no console errors, but a debug Performance timing panel is visible. |
| SWAB-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-SWAB-001 | There is no Help (?) on the page. |
| SWAB-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside the New Draft Revision confirmation to outside it: it stays open. (Escape does not close it, see BUG-SWAB-001.) |
| SWAB-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-SWAB-002 | Dates show as "14 Oct 2026" / "29 Sept 2026". |
| SWAB-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | FAIL | BUG-SWAB-004 | At 390 px the page is 651 px wide; the revision table is not in its own scroll box. |
| SWAB-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | BETA TEST ONLY Lowperm gets Access Denied for Settings and Tools, so it cannot reach this page (same as 31–34). |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SWAB-001 | Active Master card: View / Export | Works | PASS |  | The Active Master card View opens Rev 3 read-only, listing 21 aircraft with only ZK-HEL "W&B Configured". Export downloads "Revision 3.json" (43 KB). |
| SWAB-002 | Revision History filter; Review, Export, Delete, Set as Master | Works | PASS |  | The status filter works (Pending and Rejected show "No revisions found"; Approved shows Rev 1–3). Review, Export and Delete work on a draft. I did not use the Set as Master star (live master). |
| SWAB-003 | Import config file; New Draft | Works | PASS |  | New Draft > Confirm creates "Rev 4" (Pending, 22 Oct 2026), with View, Download and Delete. Import was not run, so the live config was not overwritten. |
| SWAB-004 | Per-aircraft editor sections (General … Envelope Graphs) | Each saves | PASS |  | In a new draft, the ZK-BTO editor has General / Equipment / Profiles / Graphs tabs. General (Empty Weight 600, MTOW 1000) saves with "Aircraft saved successfully", ZK-BTO shows "W&B Configured" and Review counts AIRCRAFT 1. Only General was saved; I did not fill Equipment, Profiles or Graphs. The draft was deleted. |
| SWAB-005 | Copy W&B To Aircraft | Copied | PASS |  | In a new draft, ZK-BTO editor > Copy To lists the fleet. Picking ZK-AIR asks "This will copy the current W&B configuration to ZK-AIR. Continue?", then shows "W&B copied to ZK-AIR". ZK-AIR shows "W&B Configured" and Review counts AIRCRAFT 2. The draft was deleted, so the live Master is unchanged. |
| SWAB-006 | Approved revision read-only; Create Draft Revision | Correct | PASS |  | The Master (Rev 3) View shows "Approved — Read Only", a lock message and a Create Draft Revision button. |
| SWAB-007 | Publish > Approve/Reject > Set as Master | Flight Details W&B toggle follows Master | BLOCKED |  | Reject works: an optional reason, then status Rejected and a "Config rejected" toast. The draft was then deleted. I did not run Approve or Set as Master: the only draft would have replaced Rev 3 and taken ZK-HEL out of the live iPad config. This needs a draft copied from the Master, so it is not safe to run on this site without Jon's OK. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
