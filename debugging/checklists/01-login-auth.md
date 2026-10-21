# Login, 2FA, sessions, landing page

- **Checklist ID prefix:** `LOG`
- **Guide section:** §2
- **Where:** Site root / Logout
- **Permission:** none (public) / Personnel Details for Security tab
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Standard checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| LOG-S01 | Open the module by clicking through the menu (never ?action= URLs) | Page loads, no console errors | TODO | | |
| LOG-S02 | Help (?) opens and closes (Got it / × / outside / Esc) | Works | TODO | | |
| LOG-S03 | Every popup on this page: drag-out test (mousedown inside, release outside) | Popup stays open | TODO | | |
| LOG-S04 | Dates/times on this page follow Settings > Time Zone | Correct format | TODO | | |
| LOG-S05 | Narrow (< 768 px) layout | Usable; cards/dropdown pills | TODO | | |
| LOG-S06 | Low-permission account | Access Denied or read-only as per permission | TODO | | |

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| LOG-001 | Log out, load site root | Login card: 'Welcome back! Please login to your account.' | PASS |  | Text matches |
| LOG-002 | Wrong password for a valid username | 'Invalid Username or Password' (no hint which field was wrong) | PASS |  | 'Invalid Username or Password' |
| LOG-003 | Unknown username | Same generic message | PASS |  | Same generic message |
| LOG-004 | Log in as an Inactive user (create one in Access Manager) | Same generic message; no login | TODO | | |
| LOG-005 | Forgot Password? > enter any username > Send Reset Link | Always: 'If that username exists, a reset email has been sent.' | PASS |  | 'If that username exists, a reset email has been sent.' |
| LOG-006 | Reset Password page: mismatched passwords, < 8 chars | Validation messages; Back to Login works | TODO | | |
| LOG-007 | Enable 2FA on a test account (My Account > Security), log out and in | 2FA page appears: 'Enter the 6-digit code from your authenticator app' | PASS |  | betatest_low with 2FA: page 'Enter the 6-digit code from your authenticator app', backup-code hint, Trust this device checkbox |
| LOG-008 | 2FA wrong code | 'Invalid verification code. Please try again.' | PASS |  | 'Invalid verification code. Please try again.' |
| LOG-009 | 2FA backup code XXXX-XXXX | Accepted once; cannot be reused | PASS |  | Backup code accepted once; reuse gives 'Invalid verification code. Please try again.' |
| LOG-010 | 2FA 'Trust this device for 30 days' | Next login on same browser skips 2FA | FAIL | BUG-LOG-003 | Trusted cookie dhkey_trusted_betatest_low (29 days) is set, but Logout deletes every cookie including it; next login asks for 2FA again |
| LOG-011 | 2FA > 10 wrong attempts within 15 min | 'Too many failed attempts. Please try again later.' | TODO | | |
| LOG-012 | 2FA '← Back to login' | Returns to login page | PASS |  | '← Back to login' returns to login card |
| LOG-013 | Login message popup after login | Login Message popup; closes with OK and with Esc | FAIL | BUG-LOG-001 | OK and Esc close it, but it also reappears on every browser reload, not just after login |
| LOG-014 | Reload browser while on a non-default page | Same page reopens | PASS |  | DFR reopened after reload |
| LOG-015 | Set Login Landing Page (My Account > Customize), log out and in | Lands on the chosen page; test every option (Dashboard, Active Flights, Flight Schedule, DFR, Roster Viewer, W&B Config, My Personnel Details, Support) | TODO | | |
| LOG-016 | Logout confirmation | 'Are you sure you want to log out?' Cancel keeps you in; Log Out logs out and clears remembered page | FAIL | BUG-LOG-002 | Cancel/Log Out work and remembered page cleared, but Esc doesn't close the confirm (POP-02) and logout throws a JS error |
| LOG-017 | Deactivate a logged-in test user from another browser/session | That user's session ends immediately; module shows Session Expired card with Login button | TODO | | |
| LOG-018 | Session Expired card Login button | Reloads whole page to login | TODO | | |
| LOG-019 | Disable 2FA and regenerate backup codes (password required) | Works; codes downloadable | TODO | | |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
