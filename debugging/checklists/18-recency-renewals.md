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
| REC-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| REC-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| REC-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| REC-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| REC-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| REC-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| REC-001 | Overview columns: Name, Status (worst), Next Expiry, Total Items, Actions | Correct | TODO | | |
| REC-002 | Only active people in groups with Recency and Renewals switch | Correct | TODO | | |
| REC-003 | Search by name | Works | TODO | | |
| REC-004 | Click person | Opens Personnel Details > Recency tab | TODO | | |
| REC-005 | Value entered on Flight Details Crew Recency | Reflected here after completion | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| VIS-15 | Low | Open (external) | Recency table header styled differently |
| DATA-03 | Low | Open (external) | Recency status "Expired" while Next Expiry says "74 days" |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
