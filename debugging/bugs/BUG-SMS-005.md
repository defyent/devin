# BUG-SMS-005: Safety Reports: group-level (WG) and own-level (WO) users see no reports at all, not even ones they submitted

| Field | Value |
|---|---|
| Checklist row | `SMS-015` in `checklists/19-safety-reports.md` |
| Module | Safety Reports |
| Severity | High |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. BETA TEST ONLY Grpuser has Safety Reports = WG. BETA TEST ONLY Second has Safety Reports = WO.
2. As Grpuser: Safety Reports > New Report > 'BETA TEST ONLY confidential' (Near Miss, Confidential Yes) > Create Report. It opens report #2062.
3. Go back to the Safety Reports list as Grpuser.
4. Open Safety Reports as Second.

## Expected
Grpuser sees #2062 (their own) and the group's reports. Second sees their own reports. A confidential report from someone else stays hidden.

## Actual
Grpuser's list says '0 Total Reports, No reports found' right after creating #2062. Second also sees 0. The Service Account sees #2062 (Opened, submitter Grpuser). So non-admin reporters can't find or follow up on their own reports.

## Evidence
- Screenshot: `screenshots/BUG-SMS-005-1.png`, `screenshots/BUG-SMS-005-2.png`, `screenshots/BUG-SMS-005-3.png`
- Console / network errors: none

## Suspected cause (optional)


## Test data involved
none

## Related


## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
