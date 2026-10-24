# BUG-IPSMS-003 — Safety Report action 'Assign To' picker shows a blank person row

- **Severity:** Low
- **Area:** iPad app — Safety Reports > Actions > New Action
- **Found:** 2026-10-24, iPad Pro 13-inch (M5) Simulator, iOS 26.5, DataHangar Flight 1.0.13 (46), stresstest v2.0.123

## Steps
1. Safety Reports > report #2064 > Actions > + New Action.
2. Open the Assign To picker.

## Expected
Only named people are listed; records with no name are hidden or labelled.

## Actual
A blank row appears under 'Unassigned' (report options people[0] = id 274 with an empty name). The same nameless person also appears in the website's personnel pickers, so the record itself is probably a server data-quality issue; the app should still filter or label it.

## Cause
The picker lists every person from the report options without filtering empty names.

## Evidence
- `screenshots/IPSMS-007_app_action_assignee_picker.png`
