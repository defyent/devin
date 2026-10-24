# BUG-IPSEC-001: iPad app: DataHangar password stored in plain text in localStorage

| Field | Value |
|---|---|
| Checklist row | `IPSEC-001` in `checklists/75-ipad-security.md` |
| Module | iPad: Security |
| Severity | High |
| DataHangar version | iPad web build /ipad/ (index.js 1,583,035 bytes, 24/10/2026) |
| Account / permission level | Service Account (datahangar), admin |
| Browser / width | Chrome 137, iPad emulation 820 x 1180 |
| Status | New |
| Found / session | 24/10/2026 / https://app.devin.ai/sessions/839d58b7e5cc4031982ca8bb491e8b6f |

## Steps to reproduce
1. Open https://stresstest.datahangar.net/ipad/ > Configuration > Datahangar
2. Enter URL, username and password > Test Authentication
3. In DevTools > Application > Local Storage, look at `datahangarPassword` and `datahangarPassword_backup`

## Expected
The password is not kept in web storage. The app keeps only the session cookie, or a token held in the iOS Keychain through the native bridge, and asks for the password again when the session expires.

## Actual
Both keys hold the password as a plain JSON string. The /ipad/ build is served from the same origin as the DataHangar frontend, so any script on stresstest.datahangar.net can read it. That includes an uploaded .html file opened inline (BUG-ATT-001). In the native wrapper the origin is different, but the password is still kept unencrypted in WKWebView storage.

## Evidence
- Screenshot: `screenshots/BUG-IPSEC-001-1.png` (Configuration > Datahangar)
- localStorage keys checked over CDP. Only the value lengths and types were read; the value was not logged.
- Console / network errors: none

## Suspected cause (optional)
Configuration saves `datahangarUsername`/`datahangarPassword` with `localStorage.setItem` and mirrors every key to `*_backup`.

## Test data involved
none

## Related
BUG-ATT-001

## Retest log
| Date | Version | Result | Notes |
|---|---|---|---|
