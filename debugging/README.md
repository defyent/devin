# DataHangar debugging pack

Systematic, guide-driven bug hunt for DataHangar, based on `DataHangar_Frontend_User_Guide.md`.

## Folder structure

```
debugging/
├── README.md               ← this file: structure + workflow
├── DEBUGGING_GUIDE.md      ← rules, method, IDs, severity, evidence standards
├── STATUS.md               ← the one status document: checklist of every bug (module, status, title), then totals, progress, test data
├── bugs.json               ← master bug data (one entry per bug, incl. status); STATUS.md is built from it
├── tools/mkstatus.py       ← regenerates STATUS.md and syncs bug-file Status lines from bugs.json
├── checklists/             ← one file per module / settings page / cross-cutting area
│   ├── 00-setup-and-accounts.md      (run first)
│   ├── 01-…03-                        login, shell, common conventions
│   ├── 04-…30-                        modules (Access Manager → Maintenance)
│   ├── 31-…47-                        settings pages
│   ├── 90-…95-                        cross-cutting (permissions, popups, dates, mobile, UI/icons, perf)
│   └── 99-e2e-workflows.md            (run last)
├── external-audits/        (Forms + UI/UX audits, 17/10/2026)
├── bugs/
│   ├── BUG_TEMPLATE.md     ← copy for each bug
│   ├── BUG-<PREFIX>-<NNN>.md
│   └── screenshots/        ← BUG-<PREFIX>-<NNN>-<n>.png
└── handover/
    └── FIXIT_HANDOVER_TEMPLATE.md  ← what the bug-fixing session receives
```

## Workflow

1. **Tester session** works through `checklists/` in numeric order (00 first, 99 last), filling the `Result`, `Bug ID` and `Notes` columns.
2. Each `FAIL` → new `bugs/BUG-<PREFIX>-<NNN>.md` from the template + screenshot + entry in `bugs.json`.
3. After each checklist or retest, update `bugs.json` (status) and the bug file's Retest log, then run `python3 debugging/tools/mkstatus.py` to regenerate `STATUS.md`.
4. When a module (or a batch) is done, create `../fixit-handovers/FIXIT_HANDOVER_<module>_v<version>.md` from `handover/FIXIT_HANDOVER_TEMPLATE.md` and pass it (plus the bug files) to the **bug-fixing session** working in `defyent/code`.
5. After Jon deploys a fix: clear cache, re-run the linked checklist rows, set bug status to `Verified` or `Reopened`.

## Handing to the bug-fixing session

Give it: this `debugging/` folder, the handover file, and the user guide. It should read `DEBUGGING_GUIDE.md` §"For the bug-fixing session" first.

**Icon rule:** all modules must use icons from `/templates2/main/icons/` only. Missing icons are added to that folder. See `DEBUGGING_GUIDE.md` under "Icons".

## iPad app (DataHangar Flight)

The iPad app audit plan is in `ipad/IPAD_AUDIT_PLAN.md`. Its checklists are `checklists/60-ipad-*` to `79-ipad-*` (prefixes `IP…`). Bugs use the same workflow, with IDs `BUG-IP<area>-NNN`.
