# BUG-TS-008: Approving a leave request doesn't change the rostered shifts, and rejecting with no reason gives no message

| Field | Value |
|---|---|
| Checklist row | `TS-008` in `checklists/15-timesheets-leave.md` |
| Module | Timesheets / Leave Requests |
| Severity | Medium |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Roster Builder (Live): give BETA TEST ONLY Second a Day Shift (DS) on 26 and 27 Nov 2026.
2. As BETA TEST ONLY Second: My Account > Timesheets > Request Leave > Annual Leave 26/11/2026 to 27/11/2026 > Submit.
3. As admin: Settings and Tools > Timesheets > Leave Requests > Pending Queue > Approve that request > Approve.
4. Open Roster Builder Nov 2026 and check Second's 26 and 27 Nov.
5. Also: on another pending request, click Reject with Your Comments left empty.

## Expected
The approve message says the roster shifts were updated, and 26 and 27 Nov change from DS to Annual Leave. Rejecting with no reason tells you a reason is required.

## Actual
The request shows Approved, but no roster-updated message appeared, and Roster Builder still shows DS on 26 and 27 Nov. Second's timesheet shows DS plus 'Annual Leave — Approved' on both days, so the person is rostered to work while on leave. With an empty reason, Reject does nothing and shows no message (the field placeholder says it's required for rejections).

## Evidence
- Screenshot: `screenshots/BUG-TS-008-1.png`, `screenshots/BUG-TS-008-2.png`, `screenshots/BUG-TS-008-3.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
