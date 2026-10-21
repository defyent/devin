# Settings – Safety Reports

- **Checklist ID prefix:** `SSMS`
- **Guide section:** §12.14
- **Where:** Settings and Tools > Safety > Safety Reports
- **Permission:** settings_smsreports = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SSMS-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Safety Reports opens settings_smsreports (tabs: Report Types, Extra Info Fields, Investigators & Reviewers), with no console errors. |
| SSMS-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-SSMS-001 | No page Help (?), and Escape does not close Add Report Type. |
| SSMS-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside Add Report Type to outside it: it stays open. |
| SSMS-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | N/A |  | No dates or times on this settings page. |
| SSMS-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | 390 px: tabs become a dropdown, scrollWidth 390 on all three tabs (nothing goes off the right edge), and the tables are readable. |
| SSMS-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Settings and Tools shows Access Denied (System Settings), the same as checked in 31-43. |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SSMS-001 | Report Types Name/Status, reorder | New Report type search follows | PASS |  | Add Report Type (Name required, Status Active/Inactive) saved as "BETA TEST ONLY Type" (Ok:6), and it shows straight away in the New Report Report Type dropdown and its "Search types..." box. Renamed and set Inactive ("Report type updated successfully"): it is then left out of New Report. There is no reorder control. The dropdown lists types A-Z. |
| SSMS-002 | Extra Info Fields (types) | Shown under Extra Safety Report Info | PASS |  | Add Extra Info Field (types Text/Number/Yes/No/URL/Date, Active/Inactive, drag reorder handle) saved "BETA TEST ONLY EIF" (Text). It is not on the New Report form. It shows on the report page under "Extra Safety Report Info" (report #2060). The value "BETA eif value" saved ("Extra info saved successfully!") and was still there after a reload. Small thing: the label has for="extra-field-8" but the input has no id, so clicking the label does not focus the box. Deleting a field that has data is refused ("Cannot delete this field because it has data in 1 SMS report(s). Please set it to Inactive instead"). Deleting an unused report type works, and asks first naming the type. |
| SSMS-003 | Permanent Investigators & Reviewers | Auto-assigned to new reports | PASS |  | Add Personnel (Person + Investigator/Reviewer) added Zoe Mason as a permanent Investigator (Ok:64). New report #2061 "BETA TEST ONLY report 2" then had Zoe Mason under Investigators on its Final Report tab with nothing else done. Note: the Person list (110 people) leaves out the BETA TEST ONLY Lowperm user, and the list is filtered on the server (allPeople). Also, the new report again took the UTC Event Date/Time (21/10 14:42 posted, while History shows 22/10/2026 03:43 local), the same as BUG-SMS-002. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |


**Cleanup (44):** report type "BETA TEST ONLY Type2" deleted. Permanent investigator Zoe Mason removed, and taken off report #2061. Extra Info Field "BETA TEST ONLY EIF" (id 8) can't be deleted because report #2060 has a value in it, so it is set to Inactive. New test report #2061 "BETA TEST ONLY report 2 (permanent investigator)" stays, because the app can't delete safety reports.
