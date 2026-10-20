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
