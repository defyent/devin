# BUG-IPREF-001 — Sync All reports 'Flight Custom Fields: 0' although a custom field is synced and used

- **Severity:** Low
- **Area:** iPad app — Configuration > DataHangar > Sync All (Flight Custom Fields)
- **Found:** 2026-10-24, iPad Pro 13-inch (M5) Simulator, iOS 26.5, DataHangar Flight 1.0.13 (46), stresstest v2.0.123

## Steps
1. Website: Settings > Extra Flight Info has the field 'BETA TEST ONLY EFI'.
2. iPad app: Configuration > DataHangar > Sync All Data and read the results summary.
3. Open flight #42914 > Details tab.

## Expected
The Sync All summary shows 1 Flight Custom Field.

## Actual
The summary says 'Flight Custom Fields: 0', yet the field is stored locally (extraFlightInfoFields), shown on the flight Details tab, and its value 'BETA TEST ONLY EFI audit value' pushed to the website correctly. Only the count is wrong/misleading.

## Cause
Not traced in source (summary count vs stored data).

## Evidence
- Source review / audit log only (see checklist row).
