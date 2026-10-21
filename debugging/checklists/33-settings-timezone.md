# Settings – Time Zone (date/time matrix)

- **Checklist ID prefix:** `STZ`
- **Guide section:** §12.3
- **Where:** Settings and Tools > Configuration > Time Zone
- **Permission:** settings_timezone = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| STZ-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Configuration > Time Zone loads with no console errors. |
| STZ-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-STZ-002 | There is no Help (?) on the page. |
| STZ-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside the Save confirmation popup to outside it: the popup stays open. The dropdown lists close normally. |
| STZ-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | FAIL | BUG-STZ-001 | Example preview shows 21/10/2026 13:16 (UTC) when local Pacific/Auckland time is 22/10/2026 02:16. |
| STZ-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | At 390px there is no sideways scroll, and the dropdowns and Save Changes are usable. |
| STZ-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Settings and Tools shows "Access Denied: You do not have permission to access the System Settings feature", so Time Zone cannot be reached. |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| STZ-001 | Searchable timezone | Search works; clocks update | PASS |  | The time zone list has 598 zones and a search box; typing "Honolulu" leaves only Pacific/Honolulu. Clocks not checked, because I did not save a different zone. |
| STZ-002 | Cycle all 10 date formats | Example preview correct; then spot-check every module's dates (see 42-dates-timezones) | FAIL | BUG-STZ-003 | 6 of the 10 date formats can be picked, 4 are greyed out. The preview shows 10/21/2026 for YYYY-MM-DD and DD.MM.YYYY. |
| STZ-003 | Cycle all 5 time formats | Preview + header clocks | FAIL | BUG-STZ-003 | Only 2 of the 5 time formats can be picked; the 3 12-hour ones are greyed out. The preview does not show the chosen format. Once saved, HH:mm:ss shows in the header clocks and in Daily Flight Record. |
| STZ-004 | Cycle picker types: Scroll Wheel / Type-In / Native | Every date field across modules uses selected type | PASS |  | Saved Scroll Wheel: the Flight Schedule settings start time and the Daily Flight Record date filters became wheel pickers. Saved Native: they became native inputs. Type-In: type-in boxes. Put back to Type-In. |
| STZ-005 | Restore original settings | Back to baseline recorded in SET | PASS |  | Put back to the SET-005 baseline: Pacific/Auckland, DD/MM/YYYY, 24-hour HH:mm, Type-In Fields. Checked after a reload. |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| DATE-12 | Low | Open (external) | Time Zone settings: greyed-out formats with no explanation |
| DATE-13 | Low | Open (external) | Time Zone save: banner and toast both show; page reload required |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
