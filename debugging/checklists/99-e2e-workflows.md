# End-to-end workflows

- **Checklist ID prefix:** `E2E`
- **Guide section:** §13, §6
- **Where:** Multiple modules
- **Permission:** Admin + one pilot + one student account
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| E2E-001 | 13.1 Onboard a new pilot (Access Manager > Activate > Roles > Groups > Template > Personnel > Recency > Roster publish) | Pilot can log in and sees expected modules only | PASS |  | Done in parts on BETA TEST ONLY Lowperm: activated and given a role and groups in Access Manager (04), group templates add recencies (41), Personnel details saved (12), roster publish works (14). Lowperm logs in and sees only what its permissions allow (90). |
| E2E-002 | 13.2 Schedule, fly and complete a flight (drag on schedule > Flight Details > Active Flights > Adjust SAR > complete with meters/recency/forms) | Appears in DFR, F&D, Personnel > Flights, Recency, Reports; then WL locks it | PASS |  | BETA flight #42903 (ZK-SIM, PIC Lowperm): moved and resized on the schedule (FS-014), edited in Flight Details (FD-008), OVERDUE in Active Flights (AF-004), set to Complete and gone from Active Flights (AF-011). It then shows in DFR, F&D and Personnel > Flights (checklists 09, 16, 12). With WL it locks and unlocks (PERM-005). Problems found on the way are in BUG-AF-004 and BUG-FAD-005. |
| E2E-003 | 13.3 Student training flight | Lesson tab, exercises, assessment, debrief saved; lesson progress updates | FAIL | BUG-SLP-002 | Lesson exercises are never saved (BUG-SLP-002), and there were no lesson plans on stresstest, so the lesson tab, assessment and progress could not be done end to end. |
| E2E-004 | 13.4 Safety report lifecycle | Open > Investigation > Review > Closed; action on Dashboard; hazard in register | PASS |  | Report #2060: Opened > Investigation > Review > Closed, comment and file added, action #1174 shows on the Dashboard, and Add to Hazard Register creates the hazard (checklists 19 and 20). The goal shows wrong in the register (BUG-SMS-004). |
| E2E-005 | 13.5 Roster to timesheet to approval (+ leave) | Dashboard counts update; leave updates roster | BLOCKED |  | Stresstest has no signed timesheets, claims or leave requests. Add Claim is broken (BUG-PD-016) and Request Leave can only be done by the user. Roster publish works (checklist 14). |
| E2E-006 | 13.6 Issue a notice | Badge, Dashboard, acknowledge, checklist | PASS |  | Notice #1189 created and edited, it shows on the Dashboard and in Notices, and it can be acknowledged (checklist 17). Lowperm with Notices WG sees it in its list (PERM-003). Editing resets acknowledgements (question still open). |
| E2E-007 | §6.3 Data reappears after completion | All listed places updated | PASS |  | After #42903 was completed it showed in DFR, F&D, Personnel > Flights and Reports, and left Active Flights (see E2E-002). |
| E2E-008 | Overdue alert flow (§3.5) | Banner/desktop notification to follower | BLOCKED |  | Active Flights shows OVERDUE (AF-004) and check_overdue_flights polls every ~20 s (PERF-004). A banner or desktop notification for a follower needs a second logged-in user following an open flight past its SAR time, which I could not set up. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
