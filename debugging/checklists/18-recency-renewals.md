# Recency and Renewals (overview page)

- **Checklist ID prefix:** `REC`
- **Guide section:** §10.3
- **Where:** Flight Safety > Recency and Renewals
- **Permission:** Recency A/RG/RO
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| REC-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Flight Safety > Recency and Renewals loads, 86 rows, no console errors |
| REC-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-REC-001 | No Help (?) button |
| REC-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | N/A |  | The page has no popups (only an error modal that never opened) |
| REC-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | N/A |  | The overview shows no dates, only days to expiry |
| REC-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | FAIL | BUG-REC-002 | At 390px the table is clipped (423px table in a 303px card); Total Items and Actions hidden |
| REC-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: 'Access Denied: You do not have permission to access Recency and Renewals' |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| REC-001 | Overview columns: Name, Status (worst), Next Expiry, Total Items, Actions | Correct | PASS |  | Columns Name, Status (worst item), Next Expiry, Total Items, Actions, grouped by group. Retest of DATA-03: still happens - Aisha Johnston 'Expired' with Next Expiry '69 days' (the column shows the next future expiry even when an item has expired) |
| REC-002 | Only active people in groups with Recency and Renewals switch | Correct | PASS |  | Only groups with the Recency switch on are listed: Pilots (83 members) and BETA TEST ONLY Group (1). Crew, Engineers and Administration have it off and don't appear. 84 people shown = 83 + 1 |
| REC-003 | Search by name | Works | PASS |  | Search 'Aisha' shows Aisha Johnston and Aisha Pearce |
| REC-004 | Click person | Opens Personnel Details > Recency tab | PASS |  | Clicking Aisha Johnston opens Personnel Details on the Recency and Renewals tab (that page throws 'getPickerMod is not defined', same file as BUG-PD-001) |
| REC-005 | Value entered on Flight Details Crew Recency | Reflected here after completion | BLOCKED |  | Needs a completed flight with a Crew Recency value for a pilot that has recency items set up (Settings > Recency and Renewals, checklist 41). Retest in 99 end-to-end |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| VIS-15 | Low | Open (external) | Recency table header styled differently - retest: header is still a grey table header unlike other modules' pill/card headers; not re-logged |
| DATA-03 | Low | Open (external) | Recency status "Expired" while Next Expiry says "74 days" - retest: still happens (Aisha Johnston Expired / 69 days, see REC-001) |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
