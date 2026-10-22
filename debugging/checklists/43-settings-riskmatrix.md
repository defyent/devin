# Settings – Risk Matrix

- **Checklist ID prefix:** `SRM`
- **Guide section:** §12.13
- **Where:** Settings and Tools > Safety > Risk Matrix
- **Permission:** settings_riskmatrix = A
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SRM-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | PASS |  | Settings and Tools > Risk Matrix opens settings_riskmatrix (Standard Risk Matrix 5x5, Likelihood Levels, Consequence Levels), with no console errors. |
| SRM-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | FAIL | BUG-SRM-001 | No page Help (?), and Escape does not close Add New Matrix. |
| SRM-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | PASS |  | Drag from inside Add New Matrix to outside it: it stays open. |
| SRM-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | N/A |  | No dates or times on this page. |
| SRM-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | FAIL | BUG-SRM-002 | 390 px: page scrollWidth 419, matrix-nav 774 px, Add Level cut off. The grid scrolls inside its own box. |
| SRM-S06 | Low-permission account | Access Denied or read-only as per permission | PASS |  | betatest_low: Settings and Tools shows Access Denied (System Settings). |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| SRM-001 | Create empty / from template | Works | PASS |  | Add New Matrix asks Empty vs Default Template. The template made a full 5x5 matrix ("BETA TEST ONLY Matrix", Ok:9). Empty made one with no levels ("Add likelihood and consequence levels to create the matrix grid", Ok:10). Delete asks first and names the matrix. Small thing: after making the empty matrix, the page keeps showing the previous matrix until you click the new one. Both test matrices deleted. |
| SRM-002 | Likelihood / Consequence levels add/edit/delete/reorder | Grid updates | PASS |  | On test matrix "BETA TEST ONLY Matrix" (made from the default template, id 9): add likelihood (Ok:183) and consequence (Ok:179) levels, which add a grid column/row. Edit name and Business Impact are saved. Drag reorder saves ("Order updated successfully") and the grid columns follow. Levels belong to their own matrix: Standard Risk Matrix was not changed. Small things: the Edit Likelihood/Consequence popups label their save button "Add", and the template matrix lists consequences Catastrophic -> Insignificant, the opposite of Standard. |
| SRM-003 | Cell Risk Text + Color; reuse offered | Used on Safety Reports and Hazards | PASS |  | Clicking a cell opens Edit Risk Matrix Cell with "Previously Used Risk Text" (Extreme/High/Low/Medium; picking one fills the text box) and Previously Used Colors / Custom Color. Saved "BETA Risk" with #991b1b on the test matrix ("Matrix cell updated successfully"). Standard matrix cells were not changed. Its texts and colors are the ones shown in the Safety Report risk popup and on hazards (checked in 19/20). |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |


**Cleanup (43):** test matrices "BETA TEST ONLY Matrix" (id 9) and "BETA TEST ONLY Empty" (id 10), with their levels, deleted. Standard Risk Matrix was not changed.
