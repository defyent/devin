#!/usr/bin/env python3
"""Regenerate debugging/STATUS.md, the single audit status document.

Sources: bugs.json (bug status), bugs/BUG-*.md (retest logs), checklists/*.md (row results).
Sections between <!-- keep:NAME --> and <!-- /keep:NAME --> are hand-edited and preserved.
Also syncs the Status line of each bugs/BUG-*.md with bugs.json.
Run: python3 debugging/tools/mkstatus.py
"""
import json, os, re, glob, datetime

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
AREAS = {
 "00-setup-and-accounts": [
  "SET",
  "Session setup, accounts and baseline"
 ],
 "01-login-auth": [
  "LOG",
  "Login, 2FA, sessions, landing page"
 ],
 "02-shell-navigation": [
  "NAV",
  "Application shell, sidebar, header, mobile"
 ],
 "03-common-conventions": [
  "CON",
  "Common screen conventions (apply on every page)"
 ],
 "04-access-manager": [
  "AM",
  "Access Manager (users, roles, groups, permissions, templates)"
 ],
 "05-dashboard": [
  "DSH",
  "Dashboard"
 ],
 "06-flight-schedule": [
  "FS",
  "Flight Schedule (incl. embedded Location Planner)"
 ],
 "07-flight-details": [
  "FD",
  "Flight Details"
 ],
 "08-active-flights": [
  "AF",
  "Active Flights and Live Tracking"
 ],
 "09-daily-flight-record": [
  "DFR",
  "Daily Flight Record"
 ],
 "10-location-planner": [
  "LP",
  "Location Planner (stand-alone)"
 ],
 "11-personnel-list": [
  "PL",
  "All Personnel (Personnel List)"
 ],
 "12-personnel-details": [
  "PD",
  "Personnel Details / My Account"
 ],
 "13-roster-viewer": [
  "RV",
  "Roster Viewer"
 ],
 "14-roster-builder": [
  "RB",
  "Roster Builder"
 ],
 "15-timesheets-leave": [
  "TS",
  "Timesheets, Timesheet Details, Leave Requests"
 ],
 "16-flight-and-duty": [
  "FAD",
  "Flight and Duty"
 ],
 "17-notices": [
  "NOT",
  "Notices"
 ],
 "18-recency-renewals": [
  "REC",
  "Recency and Renewals (overview page)"
 ],
 "19-safety-reports": [
  "SMS",
  "Safety Reports (SMS)"
 ],
 "20-hazard-register": [
  "HAZ",
  "Hazard Register"
 ],
 "21-settings-hub": [
  "HUB",
  "Settings and Tools hub"
 ],
 "22-file-browser": [
  "FB",
  "File Browser"
 ],
 "23-form-builder": [
  "FBLD",
  "Form Builder"
 ],
 "24-form-browser": [
  "FBR",
  "Form Browser / Form Viewer"
 ],
 "25-task-tracker": [
  "TT",
  "Task Tracker"
 ],
 "26-reports": [
  "RPT",
  "Reports"
 ],
 "27-support": [
  "SUP",
  "Support tickets"
 ],
 "28-chat": [
  "CHAT",
  "Chat"
 ],
 "29-exams": [
  "EXM",
  "Exam Builder, Exam Editor, Exam Instances"
 ],
 "30-maintenance": [
  "MX",
  "Maintenance Portal"
 ],
 "31-settings-flightschedule": [
  "SFS",
  "Settings – Flight Schedule"
 ],
 "32-settings-dfr": [
  "SDFR",
  "Settings – Daily Flight Record"
 ],
 "33-settings-timezone": [
  "STZ",
  "Settings – Time Zone (date/time matrix)"
 ],
 "34-settings-resources": [
  "SRES",
  "Settings – Resources (Aircraft)"
 ],
 "35-settings-wab": [
  "SWAB",
  "Settings – Weight and Balance Configs"
 ],
 "36-settings-extraflightinfo": [
  "SEFI",
  "Settings – Extra Flight Info"
 ],
 "37-settings-flighttypes": [
  "SFT",
  "Settings – Flight Types"
 ],
 "38-settings-waypoints": [
  "SWP",
  "Settings – Waypoint Locations"
 ],
 "39-settings-shifttypes": [
  "SST",
  "Settings – Roster Shifts"
 ],
 "40-settings-frms": [
  "SFRMS",
  "Settings – Fatigue Risk Management"
 ],
 "41-settings-renewals": [
  "SREN",
  "Settings – Recency and Renewals"
 ],
 "42-settings-lessonplans": [
  "SLP",
  "Settings – Lesson Plans"
 ],
 "43-settings-riskmatrix": [
  "SRM",
  "Settings – Risk Matrix"
 ],
 "44-settings-smsreports": [
  "SSMS",
  "Settings – Safety Reports"
 ],
 "45-settings-inspections": [
  "SINS",
  "Settings – Inspection Notifications"
 ],
 "46-settings-integrations": [
  "SINT",
  "Settings – Google Calendar, WhatsApp"
 ],
 "47-settings-activitylog": [
  "SLOG",
  "Settings – Activity Log"
 ],
 "90-xc-permissions": [
  "PERM",
  "Cross-cutting: permission levels"
 ],
 "91-xc-popups": [
  "POP",
  "Cross-cutting: popups/modals"
 ],
 "92-xc-dates-timezones": [
  "DATE",
  "Cross-cutting: date/time formats and pickers"
 ],
 "93-xc-mobile": [
  "MOB",
  "Cross-cutting: mobile / narrow layout"
 ],
 "94-xc-ui-icons": [
  "UI",
  "Cross-cutting: UI consistency and icon inventory"
 ],
 "95-xc-performance-errors": [
  "PERF",
  "Cross-cutting: performance, console and network"
 ],
 "99-e2e-workflows": [
  "E2E",
  "End-to-end workflows"
 ]
}
SEVS = ['High', 'Medium', 'Low']


def keep(old, name, default):
    m = re.search(r'<!-- keep:%s -->\n(.*?)<!-- /keep:%s -->' % (name, name), old, re.S)
    body = m.group(1) if m else default.rstrip('\n') + '\n'
    return '<!-- keep:%s -->\n%s<!-- /keep:%s -->' % (name, body, name)


def kind(st):
    if not st:
        return 'Open'
    s = st.lower()
    if s.startswith('fixed'):
        return 'Fixed'
    if s.startswith('closed'):
        return 'Closed'
    return 'Open'


def last_retest(bid):
    p = D + 'bugs/%s.md' % bid
    if not os.path.exists(p):
        return ''
    s = open(p).read()
    if '## Retest log' not in s:
        return ''
    rows = [l for l in s.split('## Retest log', 1)[1].splitlines()
            if l.startswith('|') and not l.startswith('| Date') and not l.startswith('|---')]
    if not rows:
        return ''
    c = [x.strip() for x in rows[-1].strip('|').split('|')]
    return '%s %s: %s' % (c[0], c[1], c[2]) if len(c) >= 3 else ''


def sync_bug_files(bugs):
    n = 0
    for b in bugs:
        p = D + 'bugs/%s.md' % b['id']
        if not os.path.exists(p):
            continue
        s = open(p).read()
        t = re.sub(r'(\| Status \| )[^|\n]*( \|)', lambda m: m.group(1) + (b.get('status') or 'New') + m.group(2), s, count=1)
        if t != s:
            open(p, 'w').write(t)
            n += 1
    return n


def checklist_counts():
    out = []
    for p in sorted(glob.glob(D + 'checklists/*.md')):
        name = os.path.basename(p)[:-3]
        s = open(p).read()
        res = [r.split('|')[4].strip() for r in s.split('\n')
               if re.match(r'\| [A-Z][A-Z0-9]*-S?\d{2,3} \|', r) and len(r.split('|')) > 6]
        pre, area = AREAS.get(name, ['', name])
        todo = res.count('TODO')
        state = 'TODO' if res and todo == len(res) else ('DONE' if todo == 0 else 'IN PROGRESS')
        out.append(dict(name=name, pre=pre, area=area, n=len(res), p=res.count('PASS'), f=res.count('FAIL'),
                        b=res.count('BLOCKED'), na=res.count('N/A'), state=state))
    return out


def test_data_rows():
    rows = []
    for p in sorted(glob.glob(D + 'checklists/*.md')):
        s = open(p).read()
        if '## Test data created' not in s:
            continue
        for l in s.split('## Test data created', 1)[1].splitlines():
            if l.startswith('## '):
                break
            if l.startswith('|') and not l.startswith('| Record') and not l.startswith('|---'):
                c = [t.strip() for t in l.strip().strip('|').split('|')]
                if len(c) >= 3 and c[0]:
                    rows.append('| %s | %s | %s | %s |' % (os.path.basename(p)[:-3], c[0], c[1], c[2]))
    return rows


def main():
    bugs = json.load(open(D + 'bugs.json'))
    synced = sync_bug_files(bugs)
    old = open(D + 'STATUS.md').read() if os.path.exists(D + 'STATUS.md') else ''
    for b in bugs:
        b['_k'] = kind(b.get('status'))
        b['_last'] = last_retest(b['id'])
    cnt = {k: {s: 0 for s in SEVS} for k in ['Fixed', 'Closed', 'Open']}
    for b in bugs:
        cnt[b['_k']][b['sev']] = cnt[b['_k']].get(b['sev'], 0) + 1
    never = [b for b in bugs if not b.get('status')]
    cls = checklist_counts()
    T = {k: sum(c[k] for c in cls) for k in ['n', 'p', 'f', 'b', 'na']}
    done = sum(1 for c in cls if c['state'] == 'DONE')
    today = datetime.date.today().strftime('%d/%m/%Y')
    link = lambda b: '[%s](bugs/%s.md)' % (b['id'], b['id'])
    sevrank = {s: i for i, s in enumerate(SEVS)}

    L = ['# DataHangar audit: current status', '',
         'This is the only audit status document. It replaces REPORT.md, TRACKER.md, BUGS_BY_MODULE.md, '
         'ACCESSMANAGER_BUGS.md, BLOCKED_RETEST_CLEANUP.md and bugs/BUGS_INDEX.md.', '',
         '- **Last regenerated:** %s' % today,
         '- **Site:** https://stresstest.datahangar.net (demo data). Org settings: Pacific/Auckland, DD/MM/YYYY, 24-hour HH:mm, Type-In Fields.',
         '- **Test accounts:** Service Account (admin); betatest_low (BETA TEST ONLY Lowperm, own level); '
         'betatest_grp (BETA TEST ONLY Grpuser, group level); betatest_two (BETA TEST ONLY Second, own level + some admin).',
         '- **Source data:** `bugs.json` (status of every bug), `bugs/BUG-<ID>.md` (full details and retest log), '
         '`checklists/` (result of every check). Regenerate this file with `python3 debugging/tools/mkstatus.py` '
         'after changing any of them; edit the hand-written sections directly.', '',
         '## 1. Summary', '',
         '| Bugs | High | Medium | Low | Total |', '|---|---|---|---|---|']
    for k, lab in [('Open', 'Open'), ('Fixed', 'Fixed (verified by retest)'), ('Closed', 'Closed (by design)')]:
        L.append('| %s | %s | %s | %s | **%d** |' % (lab, *[cnt[k][s] for s in SEVS], sum(cnt[k].values())))
    L.append('| **All** | %s | %s | %s | **%d** |' % (*[sum(cnt[k][s] for k in cnt) for s in SEVS], len(bugs)))
    L += ['', '- %d of the %d open bugs have never been retested since they were found, so some may already be fixed.'
          % (len(never), sum(cnt['Open'].values())),
          '- Checklists: %d of %d done. %d checks: %d pass, %d fail, %d blocked, %d N/A.'
          % (done, len(cls), T['n'], T['p'], T['f'], T['b'], T['na']),
          '- External audit issues are tracked separately in section 7.', '']

    L += ['## 2. Decisions needed and not yet tested', '',
          keep(old, 'todo', open('/home/ubuntu/dh/todo_section.md').read() if not old else ''), '']

    L += ['## 3. Open High bugs', '', '| Bug | Checklist row | Module | Title | Status | Last retest |', '|---|---|---|---|---|---|']
    for b in bugs:
        if b['_k'] == 'Open' and b['sev'] == 'High':
            L.append('| %s | `%s` | %s | %s | %s | %s |' % (link(b), b['row'], b['module'], b['title'], b.get('status') or 'Open (not retested)', b['_last'] or '-'))
    L.append('')

    L += ['## 4. Progress by checklist', '',
          '| Checklist | Prefix | Area | Checks | Pass | Fail | Blocked | N/A | Bugs | Fixed | Closed | Open | State |',
          '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for c in cls:
        bb = [b for b in bugs if b.get('cl') == c['name']]
        k = lambda x: sum(1 for b in bb if b['_k'] == x)
        L.append('| [%s](checklists/%s.md) | `%s` | %s | %d | %d | %d | %d | %d | %d | %d | %d | %d | %s |'
                 % (c['name'], c['name'], c['pre'], c['area'], c['n'], c['p'], c['f'], c['b'], c['na'],
                    len(bb), k('Fixed'), k('Closed'), k('Open'), c['state']))
    other = [b for b in bugs if b.get('cl') not in {c['name'] for c in cls}]
    if other:
        L.append('| (no checklist) | | | | | | | | %d | | | | |' % len(other))
    L.append('')

    L += ['## 5. All bugs', '',
          'Open bugs first (High to Low), then fixed, then closed. Full steps, expected/actual, cause, fix and screenshots are in each bug file.', '']
    for k, title in [('Open', '### Open'), ('Fixed', '### Fixed'), ('Closed', '### Closed')]:
        sel = sorted([b for b in bugs if b['_k'] == k], key=lambda b: (sevrank.get(b['sev'], 9), b.get('cl') or '', b['id']))
        L += [title + ' (%d)' % len(sel), '', '| Bug | Severity | Checklist row | Module | Title | Status | Last retest |', '|---|---|---|---|---|---|---|']
        for b in sel:
            L.append('| %s | %s | `%s` | %s | %s | %s | %s |' % (link(b), b['sev'], b['row'], b['module'], b['title'].replace('|', '/'),
                                                             b.get('status') or 'Open (not retested)', b['_last'] or '-'))
        L.append('')

    L += ['## 6. Test data left on stresstest', '', '### From the checklist runs', '',
          '| Checklist | Record | Where | Cleanup done? |', '|---|---|---|---|'] + test_data_rows()
    L += ['', '### From retests', '', keep(old, 'testdata', open('/home/ubuntu/dh/testdata_section.md').read() if not old else ''), '']

    L += ['## 7. External audit issues', '', keep(old, 'external', open('/home/ubuntu/dh/ext_section.md').read() if not old else ''), '']
    L += ['## 8. Background notes', '', keep(old, 'background', open('/home/ubuntu/dh/bg_section.md').read() if not old else ''), '']
    open(D + 'STATUS.md', 'w').write('\n'.join(L) + '\n')
    print('STATUS.md: %d bugs, %d checklists, %d bug files status-synced' % (len(bugs), len(cls), synced))


if __name__ == '__main__':
    main()
