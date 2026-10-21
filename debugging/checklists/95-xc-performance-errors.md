# Cross-cutting: performance, console and network

- **Checklist ID prefix:** `PERF`
- **Guide section:** Login message
- **Where:** Every page
- **Permission:** n/a
- **Tester:**  
- **Date / DataHangar version:**  
- **Account / level used:**  

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| PERF-001 | Performance panel timings | Server < 500 ms (orange values flagged) | TODO | | |
| PERF-002 | Console | No JS errors / uncaught promise rejections | TODO | | |
| PERF-003 | Network | No 4xx/5xx; no duplicate repeated calls | TODO | | |
| PERF-004 | Badge polling (60 s / chat 20 s) | No runaway requests | TODO | | |

## Known issues from external audits

From [`external-audits/`](../external-audits/) (see [`BUGS_INDEX.md`](../bugs/BUGS_INDEX.md)). Retest each one while working this checklist and note the result.

| Ext ID | Severity | Status | Issue |
|---|---|---|---|
| INFO-01 | Info | Info | Version tag (?v=) missing on about half the modules (see section 5). Seen in the POP-01 retest: without ?v= the browser kept serving old JS, so the drag-out fixes only appeared after clearing the cache. Users may not get fixes until their cache expires |
| INFO-02 | Info | Info | Performance popup shows on 9 modules and covers content (see section 6) |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| | | |
