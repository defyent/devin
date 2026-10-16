# Fix-it Handover: Location Planner (embedded + stand-alone), DataHangar v2.0.108

- **Site tested:** https://stresstest.datahangar.net (Service Account; `locationplanner_json` reports `permission: A`)
- **Date:** 2026-10-16 (UTC 06:39–06:50)
- **Reference:** DataHangar_Frontend_User_Guide.md §8.2 (embedded planner), §8.6 (stand-alone), permissions table
- **Companion:** `FIXIT_HANDOVER_flightschedule3_v2.0.108.md`

## Summary

| ID | Severity | Title |
|---|---|---|
| LP-01 | High | Stand-alone planner `?action=locationplanner` returns "Invalid Action: locationplanner" |
| LP-02 | Medium | "Undo Last Booking Change" does not cover booking create or delete |
| LP-03 | Low | New Booking From/To date inputs truncate the year ("19/10/202") |
| LP-04 | Low | Delete-booking confirmation shows ISO dates (2026-10-19 to 2026-10-21) |
| LP-05 | Low (doc/UX) | No "New Booking" button; bookings can only be created by dragging in Live Edit |
| LP-06 | Low | Planner Day/Week/Month toggle: "Day" is active while a 4-week range shows; Month click had no visible effect |

---

### LP-01: Stand-alone Location Planner is unreachable (High)
**Steps:** Logged in as admin → open `https://stresstest.datahangar.net/index.pl?action=locationplanner` (also tried `/?action=locationplanner` and `action=location_planner`).
**Expected (guide §8.6 and the permissions table, which lists `locationplanner`):** The stand-alone planner with rows by groups, people or aircraft.
**Actual:** HTTP 200 with the body `Invalid Action: locationplanner`. The JSON endpoints work (`action=locationplanner_json`, `_flights`, `_templates`, `_create_booking`, `_update_booking`, `_delete_booking`).
**Fix hint:** The page action is not registered in the `index.pl` dispatcher, or the module's page handler is missing from this build. Check the action map and the module install.

### LP-02: Undo only covers move/resize (Medium)
**Steps:** Live Edit on → drag on the AKL row 19–21 Oct → pick ZK-AIR → Save Booking (`locationplanner_create_booking` → `Ok:7`) → check `#planner-undo-btn`.
**Actual:** Undo stays **disabled** after create, and after delete. After a drag-move (19–21 → 21–23, `locationplanner_update_booking`) it is enabled, and undo correctly restored 19–21.
**Expected:** "Undo Last Booking Change" should undo the last change, including create (delete the new booking). Otherwise the guide should say "move/resize only". The delete confirmation already says "This action cannot be undone", which is consistent for delete.

### LP-03: Date inputs truncated in the New Booking modal (Low)
The From/To fields show `19/10/202`, with the last digit clipped. Widen the input or reduce padding.
**Evidence:** `screenshots/LP_new_booking_date_truncated.png`

### LP-04: ISO dates in the delete confirmation (Low)
"Are you sure you want to delete this booking? C172-02 — Auckland Base (2026-10-19 to 2026-10-21)". The rest of the planner uses DD/MM/YYYY. Format the dates with the site `date_format`.
**Evidence:** `screenshots/LP_delete_confirm_iso_dates.png`

### LP-05: How to create a booking is undiscoverable (Low, doc/UX)
The guide says "New Booking asks for From, To, Location, Aircraft…". There is no New Booking button. The modal only opens by dragging across a planner row, and only in Live Edit (Undo Last Booking Change also appears only in Live Edit). Add a button, or document the drag and the edit-mode requirement. In rows-by-location the Location field is hidden (preset from the row); that works.

### LP-06: Granularity toggle unclear (Low, needs confirmation)
The header shows "Day" selected with the range 12/10/2026 – 08/11/2026 (4 Weeks). A scripted click on "Month" did not visibly change the grid. Please confirm what Day/Week/Month should do next to 4/8/12 Weeks.

---

## Verified working
Schedule & Planner and Planner Only layouts; rows by aircraft and by location; Filter by Location modal (search, counts, Add Location form present); New Booking validation ("Please select an aircraft."); create booking; booking details (Details, **Flights** tab correctly listed #8849 20/10 for ZK-AIR, **Templates** tab "No templates for this location" with New Template); drag-move booking with Undo; delete booking with confirmation.

## Test data left behind
None. Test bookings **#6** and **#7** (ZK-AIR @ AKL, notes "DEVIN TEST - safe to delete") were created and then **deleted**. Only pre-existing booking #5 (ZK-AIR, 15–20 Jul 2026) remains.
