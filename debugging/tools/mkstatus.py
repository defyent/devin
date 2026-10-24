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
 "96-xc-attachments": [
  "ATT",
  "Cross-cutting: attachments and file types"
 ],
 "99-e2e-workflows": [
  "E2E",
  "End-to-end workflows"
 ],
 "60-ipad-setup": [
  "IPSET",
  "iPad: Setup and baseline"
 ],
 "61-ipad-configuration": [
  "IPCFG",
  "iPad: Configuration: General Info"
 ],
 "62-ipad-aircraft-wab": [
  "IPAC",
  "iPad: Configuration: Aircraft and W&B"
 ],
 "63-ipad-personnel-waypoints": [
  "IPPER",
  "iPad: Configuration: Personnel and Waypoints"
 ],
 "64-ipad-datahangar-sync": [
  "IPSYN",
  "iPad: DataHangar connection and Sync All Data"
 ],
 "65-ipad-flights-list": [
  "IPFL",
  "iPad: Flights list and Download"
 ],
 "66-ipad-flight-legs": [
  "IPLEG",
  "iPad: Flight: legs, times, meters, fuel"
 ],
 "67-ipad-flight-crew-wab": [
  "IPWB",
  "iPad: Flight: crew, passengers and W&B"
 ],
 "68-ipad-flight-forms-files": [
  "IPFF",
  "iPad: Flight: forms and files"
 ],
 "69-ipad-push-pull-conflicts": [
  "IPPP",
  "iPad: Push, pull and conflicts"
 ],
 "70-ipad-safety-reports": [
  "IPSMS",
  "iPad: Safety reports"
 ],
 "71-ipad-calculator": [
  "IPCAL",
  "iPad: Calculator"
 ],
 "72-ipad-comms": [
  "IPCOM",
  "iPad: Comms (chat)"
 ],
 "73-ipad-live-tracking-native": [
  "IPLT",
  "iPad: Live tracking and native bridge"
 ],
 "74-ipad-offline-lifecycle": [
  "IPOFF",
  "iPad: Offline, persistence and lifecycle"
 ],
 "75-ipad-security": [
  "IPSEC",
  "iPad: Security and data handling"
 ],
 "76-ipad-ux-layout": [
  "IPUX",
  "iPad: UX/UI: layout and orientation"
 ],
 "77-ipad-ux-consistency": [
  "IPUXC",
  "iPad: UX/UI: touch, visual, wording, accessibility"
 ],
 "79-ipad-e2e": [
  "IPE2E",
  "iPad: End-to-end field day"
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


def plain_status(st):
    if not st:
        return 'Open, not retested'
    d = re.search(r'\d\d/\d\d/\d{4}', st)
    v = re.search(r'v\d+\.\d+\.\d+', st)
    when = ', '.join(x.group(0) for x in (d, v) if x)
    s = st.lower()
    if s.startswith('fixed'):
        return 'Fixed' + (' (%s)' % when if when else '')
    if s.startswith('closed'):
        return 'Closed, by design' + (' (%s)' % d.group(0) if d else '')
    if 'part fixed' in s:
        return 'Open, part fixed' + (' (%s)' % when if when else '')
    return 'Open, still failing' + (' (%s)' % when if when else '')


def short_title(b, limit=100):
    if b.get('short'):
        return b['short']
    t = b['title'].strip()
    mod = re.sub(r'\s*\(.*?\)', '', b.get('module', '')).strip()
    names = {mod, mod.replace('Settings: ', ''), mod.replace('Settings: ', '') + ' Settings'}
    head, sep, rest = t.partition(': ')
    if sep and head in names and len(rest) > 15:
        t = rest[0].upper() + rest[1:]
    if len(t) > limit:
        t = t[:limit].rsplit(' ', 1)[0].rstrip(',;:(-') + '…'
    return t.replace('|', '/')


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

    L = ['# DataHangar bug status', '',
         'Every bug found in the DataHangar beta audit, and where it stands. Ticked = fixed or closed. '
         'Click a bug ID for the full write-up (steps, expected vs actual, cause, fix, screenshots, retest history).', '',
         '**%d bugs: %d open, %d fixed, %d closed.** Last updated %s.'
         % (len(bugs), sum(cnt['Open'].values()), sum(cnt['Fixed'].values()), sum(cnt['Closed'].values()), today), '',
         '## Bug checklist', '']
    order = list(AREAS)
    groups = {}
    for b in bugs:
        groups.setdefault(b.get('cl') or '~', []).append(b)
    krank = {'Open': 0, 'Fixed': 1, 'Closed': 2}
    for cl in sorted(groups, key=lambda c: order.index(c) if c in order else 999):
        bb = sorted(groups[cl], key=lambda b: (krank[b['_k']], sevrank.get(b['sev'], 9), b['id']))
        k = lambda x: sum(1 for b in bb if b['_k'] == x)
        parts = ['%d open' % k('Open')] + (['%d fixed' % k('Fixed')] if k('Fixed') else []) + (['%d closed' % k('Closed')] if k('Closed') else [])
        L += ['### %s (%s)' % (AREAS.get(cl, ['', 'Other'])[1], ', '.join(parts)), '']
        for b in bb:
            L.append('- [%s] %s · **%s** · %s · %s' % (' ' if b['_k'] == 'Open' else 'x', link(b), plain_status(b.get('status')), b['sev'], short_title(b)))
        L.append('')

    L += ['## Summary', '',
          '| Bugs | High | Medium | Low | Total |', '|---|---|---|---|---|']
    for k, lab in [('Open', 'Open'), ('Fixed', 'Fixed (verified by retest)'), ('Closed', 'Closed (by design)')]:
        L.append('| %s | %s | %s | %s | **%d** |' % (lab, *[cnt[k][s] for s in SEVS], sum(cnt[k].values())))
    L.append('| **All** | %s | %s | %s | **%d** |' % (*[sum(cnt[k][s] for k in cnt) for s in SEVS], len(bugs)))
    L += ['', '- %d of the %d open bugs have never been retested since they were found, so some may already be fixed.'
          % (len(never), sum(cnt['Open'].values())),
          '- Checklists: %d of %d done. %d checks: %d pass, %d fail, %d blocked, %d N/A.'
          % (done, len(cls), T['n'], T['p'], T['f'], T['b'], T['na']),
          '- Issues from the two earlier external audits are listed separately under "External audit issues".', '']

    L += ['## Decisions needed and not yet tested', '',
          keep(old, 'todo', open('/home/ubuntu/dh/todo_section.md').read() if not old else ''), '']

    L += ['## Open High bugs', '', '| Bug | Module | Title | Status | Last retest |', '|---|---|---|---|---|']
    for b in bugs:
        if b['_k'] == 'Open' and b['sev'] == 'High':
            L.append('| %s | %s | %s | %s | %s |' % (link(b), b['module'], b['title'], plain_status(b.get('status')), b['_last'] or '-'))
    L.append('')

    L += ['## Progress by checklist', '',
          '| Checklist | Prefix | Area | Checks | Pass | Fail | Blocked | N/A | Bugs | Fixed | Closed | Open | State |',
          '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for c in cls:
        bb = [b for b in bugs if b.get('cl') == c['name']]
        k = lambda x: sum(1 for b in bb if b['_k'] == x)
        L.append('| [%s](checklists/%s.md) | `%s` | %s | %d | %d | %d | %d | %d | %d | %d | %d | %d | %s |'
                 % (c['name'], c['name'], c['pre'], c['area'], c['n'], c['p'], c['f'], c['b'], c['na'],
                    len(bb), k('Fixed'), k('Closed'), k('Open'), c['state']))
    L.append('')

    L += ['## Bug details', '',
          'Full title, checklist row and latest retest for every bug, open first. The bug files have the complete write-up.', '',
          '| Bug | Severity | Checklist row | Module | Title | Status | Last retest |', '|---|---|---|---|---|---|---|']
    for b in sorted(bugs, key=lambda b: (krank[b['_k']], sevrank.get(b['sev'], 9), order.index(b['cl']) if b.get('cl') in order else 999, b['id'])):
        L.append('| %s | %s | `%s` | %s | %s | %s | %s |' % (link(b), b['sev'], b['row'], b['module'], b['title'].replace('|', '/'),
                                                         b.get('status') or 'Open (not retested)', b['_last'] or '-'))
    L.append('')

    L += ['## Test data left on stresstest', '', '### From the checklist runs', '',
          '| Checklist | Record | Where | Cleanup done? |', '|---|---|---|---|'] + test_data_rows()
    L += ['', '### From retests', '', keep(old, 'testdata', open('/home/ubuntu/dh/testdata_section.md').read() if not old else ''), '']

    L += ['## External audit issues', '', keep(old, 'external', open('/home/ubuntu/dh/ext_section.md').read() if not old else ''), '']
    L += ['## Background notes', '', keep(old, 'background', open('/home/ubuntu/dh/bg_section.md').read() if not old else ''), '']
    open(D + 'STATUS.md', 'w').write('\n'.join(L) + '\n')
    print('STATUS.md: %d bugs, %d checklists, %d bug files status-synced' % (len(bugs), len(cls), synced))


if __name__ == '__main__':
    main()
