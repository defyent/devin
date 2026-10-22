# BUG-AM-002: Last Activity hover date ignores Settings > Time Zone format

| Field | Value |
|---|---|
| Checklist row | `AM-007` in `checklists/04-access-manager.md` |
| Module | Access Manager |
| Severity | Low |
| DataHangar version | v2.0.111 |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137 desktop, 1600 px |
| Status | New |
| Found / session | 21/10/2026 / https://app.devin.ai/sessions/15f654c4481f4789abb726226cefac9c |

## Steps to reproduce
1. Settings > Time Zone is DD/MM/YYYY, 24-hour
2. Access Manager: hover the Last Activity value of Service Account ('4 mins ago')

## Expected
Exact date in org format, e.g. 21/10/2026 20:45 (local).

## Actual
Tooltip '21 Oct 2026, 07:45 am': hard-coded format, 12-hour, and shows the UTC time (07:45) rather than local (20:45). Retest 22/10/2026 (v2.0.113, accessmanager/index.js?v=2.0.113): fixed. The Last Activity hover title is now in local time and org format, e.g. '22/10/2026 15:01' for '1h 17m ago' at local 16:19.

## Evidence
- Screenshot: `screenshots/BUG-AM-002-1.png`, `screenshots/BUG-AM-002-2.png`
- Console / network errors: none

## Suspected cause (optional)
Tooltip built with toLocaleString / fixed format instead of formatDateWithConfig; timestamp not converted to org time zone.

## Test data involved
none

## Related
DATE-01

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
