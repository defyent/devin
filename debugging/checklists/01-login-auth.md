# Login, 2FA, sessions, landing page

- **Checklist ID prefix:** `LOG`
- **Guide section:** §2
- **Where:** Site root / Logout
- **Permission:** none (public) / Personnel Details for Security tab
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `../DEBUGGING_GUIDE.md` under "Icons".

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| LOG-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | N/A |  | The login page is the site start page, there is no menu before login. |
| LOG-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | N/A |  | The login page has no Help (?). It only has Username, Password, Forgot Password? and Log In. |
| LOG-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | N/A |  | No popups on the login or Forgot Password pages. |
| LOG-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | N/A |  | No dates or times on the login pages. |
| LOG-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | PASS |  | At 390 px the login page fits with no sideways scroll (scrollWidth 390, shot login_mobile). |
| LOG-S06 | Low-permission account | Access Denied or read-only as per permission | N/A |  | Logged-out page, so permissions do not apply. |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| LOG-001 | Log out, load site root | Login card: 'Welcome back! Please login to your account.' | PASS |  | Text matches |
| LOG-002 | Wrong password for a valid username | 'Invalid Username or Password' (no hint which field was wrong) | PASS |  | 'Invalid Username or Password' |
| LOG-003 | Unknown username | Same generic message | PASS |  | Same generic message |
| LOG-004 | Log in as an Inactive user (create one in Access Manager) | Same generic message; no login | PASS |  | Inactive betatest_low: 'Invalid Username or Password', no 2FA prompt, no login |
| LOG-005 | Forgot Password? > enter any username > Send Reset Link | Always: 'If that username exists, a reset email has been sent.' | PASS |  | 'If that username exists, a reset email has been sent.' |
| LOG-006 | Reset Password page: mismatched passwords, < 8 chars | Validation messages; Back to Login works | BLOCKED |  | Forgot Password? asks for a username and sends a reset link by email. The Reset Password page needs that link, and stresstest has no test mailbox. |
| LOG-007 | Enable 2FA on a test account (My Account > Security), log out and in | 2FA page appears: 'Enter the 6-digit code from your authenticator app' | PASS |  | betatest_low with 2FA: page 'Enter the 6-digit code from your authenticator app', backup-code hint, Trust this device checkbox |
| LOG-008 | 2FA wrong code | 'Invalid verification code. Please try again.' | PASS |  | 'Invalid verification code. Please try again.' |
| LOG-009 | 2FA backup code XXXX-XXXX | Accepted once; cannot be reused | PASS |  | Backup code accepted once; reuse gives 'Invalid verification code. Please try again.' |
| LOG-010 | 2FA 'Trust this device for 30 days' | Next login on same browser skips 2FA | PASS | BUG-LOG-003 | Retest 22/10/2026: fixed. Logout keeps dhkey_trusted_betatest_low (30 days); next login skips 2FA |
| LOG-011 | 2FA > 10 wrong attempts within 15 min | 'Too many failed attempts. Please try again later.' | PASS |  | After ~10 wrong codes in 15 min: 'Too many failed attempts. Please try again later.'; a valid code is also refused while locked. Lock cleared about 19 min after it started |
| LOG-012 | 2FA '← Back to login' | Returns to login page | PASS |  | '← Back to login' returns to login card |
| LOG-013 | Login message popup after login | Login Message popup; closes with OK and with Esc | PASS | BUG-LOG-001 | Retest 22/10/2026: fixed. Shown once after login, not after reloads; OK closes it |
| LOG-014 | Reload browser while on a non-default page | Same page reopens | PASS |  | DFR reopened after reload |
| LOG-015 | Set Login Landing Page (My Account > Customize), log out and in | Lands on the chosen page; test every option (Dashboard, Active Flights, Flight Schedule, DFR, Roster Viewer, W&B Config, My Personnel Details, Support) | PASS |  | Done in PD-028: Lowperm landing page set to Flight Schedule opened Flight Schedule on the next login. It was set back to Dashboard afterwards. |
| LOG-016 | Logout confirmation | 'Are you sure you want to log out?' Cancel keeps you in; Log Out logs out and clears remembered page | PASS | BUG-LOG-002 | Retest 22/10/2026: fixed. Esc closes the confirm; Cancel stays; Log Out logs out with no console errors |
| LOG-017 | Deactivate a logged-in test user from another browser/session | That user's session ends immediately; module shows Session Expired card with Login button | PASS |  | Deactivated from Service Account while betatest_low was logged in: next navigation shows 'Session Expired - Your session has expired. Please click the button below to login again.' Open page is not cleared until the user clicks something |
| LOG-018 | Session Expired card Login button | Reloads whole page to login | PASS |  | Card 'Login' link reloads the whole page (single frame) to the login card |
| LOG-019 | Disable 2FA and regenerate backup codes (password required) | Works; codes downloadable | PASS |  | Regenerate: password required (wrong pw gives vague 'Failed to regenerate backup codes'); 10 new codes, all different; Download gives datahangar-new-backup-codes.txt. Disable 2FA: password prompt > '2FA disabled successfully' |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
