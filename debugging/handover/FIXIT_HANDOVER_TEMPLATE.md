# FIXIT HANDOVER — <module> — DataHangar v<version>

Save as `fixit-handovers/FIXIT_HANDOVER_<module>_v<version>.md` (repo root), screenshots in `fixit-handovers/screenshots/`.

## Context
- Site tested: https://stresstest.datahangar.net
- Code repo: `defyent/code` (module folder `<module>/`, Perl in `<module>/perl/`, shell/popups in `main/index.js`)
- Checklist(s): `debugging/checklists/<file>.md`
- Accounts/levels used:

## Bugs to fix (priority order)

| Bug ID | Severity | Title | Bug file | Suspected file(s) |
|---|---|---|---|---|
| | | | `debugging/bugs/BUG-….md` | |

## Acceptance for each fix
- The checklist row(s) linked to the bug pass on staging after deploy + cache clear.
- No regression in the module's Standard checks (`<PREFIX>-S01..S06`).
- Static assets get a `?v=` bump so browsers don't serve stale JS.

## Out of scope / not bugs
- (e.g. flight time beyond booking times is allowed)

## Test data left for cleanup
| Record | Where |
|---|---|

> **Icon rule (all modules, from 22/10/2026):** every icon must be a self-hosted SVG from `/templates2/main/icons/`. Don't use Material Icons or Material Symbols (Google Fonts), api.iconify.design, or any other external icon source. If an icon you need isn't in that folder, add the SVG to `/templates2/main/icons/` (same naming: `<name>-outline-rounded.svg` or `<name>-rounded.svg`) and use it from there. Any icon that doesn't come from this folder is a UI FAIL under ICON-01. The full list is in `debugging/DEBUGGING_GUIDE.md` under "Icons".
