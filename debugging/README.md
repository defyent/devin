# DataHangar debugging pack

Systematic, guide-driven bug hunt for DataHangar, based on `DataHangar_Frontend_User_Guide.md`.

## Folder structure

```
debugging/
├── README.md               ← this file: structure + workflow
├── DEBUGGING_GUIDE.md      ← rules, method, IDs, severity, evidence standards
├── TRACKER.md              ← one row per checklist: progress + bug counts (update as you go)
├── checklists/             ← one file per module / settings page / cross-cutting area
│   ├── 00-setup-and-accounts.md      (run first)
│   ├── 01-…03-                        login, shell, common conventions
│   ├── 04-…30-                        modules (Access Manager → Maintenance)
│   ├── 31-…47-                        settings pages
│   ├── 90-…95-                        cross-cutting (permissions, popups, dates, mobile, UI/icons, perf)
│   └── 99-e2e-workflows.md            (run last)
├── bugs/
│   ├── BUG_TEMPLATE.md     ← copy for each bug
│   ├── BUGS_INDEX.md       ← list of all bugs (ID, module, severity, status)
│   ├── BUG-<PREFIX>-<NNN>.md
│   └── screenshots/        ← BUG-<PREFIX>-<NNN>-<n>.png
└── handover/
    └── FIXIT_HANDOVER_TEMPLATE.md  ← what the bug-fixing session receives
```

## Workflow

1. **Tester session** works through `checklists/` in numeric order (00 first, 99 last), filling the `Result`, `Bug ID` and `Notes` columns.
2. Each `FAIL` → new `bugs/BUG-<PREFIX>-<NNN>.md` from the template + screenshot + row in `bugs/BUGS_INDEX.md`.
3. After each checklist, update its row in `TRACKER.md`.
4. When a module (or a batch) is done, create `../fixit-handovers/FIXIT_HANDOVER_<module>_v<version>.md` from `handover/FIXIT_HANDOVER_TEMPLATE.md` and pass it (plus the bug files) to the **bug-fixing session** working in `defyent/code`.
5. After Jon deploys a fix: clear cache, re-run the linked checklist rows, set bug status to `Verified` or `Reopened`.

## Handing to the bug-fixing session

Give it: this `debugging/` folder, the handover file, and the user guide. It should read `DEBUGGING_GUIDE.md` §"For the bug-fixing session" first.
