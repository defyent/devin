# Fix-it Handover: Flight Schedule (`flightschedule3`), DataHangar v2.0.108

- **Site tested:** https://stresstest.datahangar.net (as Service Account, Flight Schedule permission A)
- **Date:** 2026-10-16 (UTC 06:30–06:50)
- **Reference:** DataHangar_Frontend_User_Guide.md §8.2, §12.1, §14
- **Method:** Manual browser testing with console/network capture (Chrome DevTools Protocol). No source code changes.
- **Companion:** `FIXIT_HANDOVER_locationplanner_v2.0.108.md` (embedded and stand-alone planner)

## Summary

| ID | Severity | Title |
|---|---|---|
| FS-01 | Medium | **Confirmed by Jon.** A single click on an empty week slot with Live Edit OFF opens "New Flight Details" |
| FS-02 | Medium | Cancel on a new (unsaved) Flight Details does nothing |
| FS-03 | Medium | Flights missing category/type render without #ID / crew / type; short flights are hairline bars |
| FS-04 | Medium | Same person allowed as PIC and Crew on one flight (#42894), plus overlapping aircraft double-bookings |
| FS-05 | Medium | "Day" button from a week that contains today jumps to Monday instead of today |
| FS-06 | Low | US-style dates in list view and month "+more" popover (site is DD/MM/YYYY) |
| FS-07 | Low | New flight created from a slot spans 5 min although `slot_duration` = 00:30:00 |
| FS-08 | Low | `flightschedule_json` is requested 4× per load; one response reports `date_format: YYYY-MM-DD` |
| FS-09 | Low | Compact month view shows 2 events + "+N more" (guide says 3) |
| FS-10 | Low | Roster toggled off still leaves an empty "Roster" label row in week view |
| FS-11 | Low | Month/list views are blank for ~3 s while loading, with no spinner |
| SH-01 | Medium | (Shell) Chat badge / new-message polling returns an HTML error page, so console errors every poll |
| SH-02 | Low | (Shell) Iconify sidebar icon requests 404 in the browser console |
| SH-03 | Low | (Flight Details) Console warnings: "Could not find hidden input for DateTimePicker" |

SH-xx items were seen while testing the schedule but belong to the shell or Flight Details. Route them to those owners.

---

### FS-01: A single click on an empty slot opens New Flight Details while Live Edit is OFF (Medium)
**Status:** Confirmed bug (Jon, 2026-10-16). Required behaviour: clicks and drags on empty schedule space must not create or open a new flight unless Live Edit is enabled.
**Steps:** Flight Schedule → week view → Live Edit **disabled** → single-click an empty slot (Fri 16 Oct, ~07:15).
**Expected (guide §8.2):** Flights are created by **click-dragging empty space while Live Edit is on**. With Live Edit off, a click should do nothing or show a hint.
**Actual:** Navigates to `index.pl?action=flightdetails&starttime=2026-10-16+07:15:00&endtime=2026-10-16+07:20:00` ("New Flight Details", no aircraft).
**Fix hint:** Gate the `select`/`dateClick` handler on edit mode; ignore clicks that are not drags.
**Evidence:** `screenshots/B_click_empty_slot_opens_new_flight_no_edit_mode.png`

### FS-02: Cancel on a new Flight Details does nothing (Medium)
**Steps:** Open a new flight as in FS-01 → click **Cancel** (header).
**Expected:** Return to the schedule (or discard the form).
**Actual:** Nothing happens and the page stays. The Back (←) arrow does return to the schedule.
**Evidence:** `screenshots/B_new_flight_cancel_does_nothing.png`

### FS-03: Incomplete flights render without identifying text (Medium)
**Seen (week 12–18 Oct):**
- `ZK-JET · Nathan Bradley` Fri 11:36–12:21, no `#ID`, Crew or Type lines
- `ZK-SIM · John Clarke` Sun 17:08–17:53
- `· Aaron Fisher` Fri, **no aircraft**
- `ZK-HEL ·` Wed, **no PIC**
- `ZK-HEL · Aaron Higgins` (#42897, 10:40–10:45): a 5-min flight drawn as a hairline bar with no time or ID
**Expected:** Every event shows `#ID · Rego · PIC` in the same format. Very short events get a minimum height or a tooltip.
**Fix hint:** The title template seems to drop the `#ID` line when category/type is null. Build the label from `id` independently of type, and set a minimum event height.

### FS-04: PIC = Crew and aircraft double-bookings accepted (Medium, confirm intended)
- #42894 ZK-HEL 14/10 00:05: **PIC Aaron Foster, Crew Aaron Foster**
- #42894 / #42893, both ZK-HEL at 14/10 00:05 (overlapping)
- #42899 / #8795, both ZK-RVN at 16/10 06:00–07:00
**Expected:** Block, or at least warn, when PIC == Crew. Flag overlapping flights on the same aircraft.
**Note:** The overlaps may be deliberate stress data. PIC==Crew looks like a missing validation in Flight Details save.

### FS-05: "Day" from week view goes to Monday, not today (Medium)
**Steps:** Week view (12–18 Oct, today = Fri 16) → click **day**.
**Expected:** Today (Fri 16 Oct), or the day the user was looking at.
**Actual:** Mon 12 Oct, with the "past date" banner.

### FS-06: Inconsistent date formats (Low)
List view header shows "October 1, 2026". The month "+more" popover shows "Monday, September 28". The site setting is `DD/MM/YYYY` (from `get_date_time_formats`).
**Evidence:** `screenshots/B_list_view_us_date_roster_flood.png`, `screenshots/B_month_popover_us_date.png`

### FS-07: Slot-created flight is 5 min (Low)
`slot_duration` is `00:30:00` but the slot click produced 07:15–07:20. A slot click or drag should default to at least one slot.

### FS-08: Duplicate data requests and conflicting date_format (Low)
One week-view load fires `?action=flightschedule_json` 4 times (two without `start`/`end`). One response contains `"date_format":"YYYY-MM-DD"` while `get_date_time_formats` returns `DD/MM/YYYY`. This may be related to FS-06.

### FS-09: Compact month view limit (Low)
Compact mode shows 2 events per day then "+N more". Guide §8.2 says 3. Align the code or the doc.
**Evidence:** `screenshots/B_compact_month_doublebookings.png`

### FS-10: Empty Roster row when roster is off (Low)
With the roster toggled off in week view, the "Roster" label row is still drawn, empty.

### FS-11: No loading indicator (Low)
Switching to month or list leaves the grid blank for about 3 s with no spinner.

### SH-01: Chat polling endpoints return HTML (Medium, shell)
`GET index.pl?action=get_chat_badge_count` and `GET index.pl?action=get_chat_new_messages` return **HTTP 200 with an HTML "Error" page**. The console logs every poll:
`Error updating chat badge: SyntaxError: Unexpected token '<', "<!DOCTYPE "... is not valid JSON` (and the same for new messages).
**Fix hint:** These actions are probably not registered, or not permitted for this user. Return JSON (`{"count":0}`) or a 403 with JSON, and have the client check `content-type`.

### SH-02: Iconify icon 404s (Low, shell)
The browser logs many `404 https://api.iconify.design/material-symbols/<name>.svg` for sidebar icons. The same URLs return 200 with curl from the VM, so this may depend on the environment or browser. Consider self-hosting the icon set.

### SH-03: DateTimePicker warnings (Low, Flight Details)
Opening Flight Details logs `Could not find hidden input for DateTimePicker with container ID: start_time / end_time / sar_time`.

---

## Verified working
Month, week, day and list views; prev/next/today; Group By; roster, notes, compact and font-size toggles; Schedule Only / Schedule & Planner / Planner Only; Live Edit enable/disable with the banner; **drag-move a flight (#8833 +30 min) and Undo Last Action restored it exactly**; opening an existing Flight Details.

## Test data left behind
None. #8833 was moved and then restored with Undo (08:46–10:29). No flights were saved.
