# BUG-IPFORM-003 — Form Date/Time widgets ignore website values and show (and can save) the current date/time

- **Severity:** High (silent data corruption of form answers)
- **Area:** iPad app — Forms engine (Safety Report forms and Flight forms), checklist 70/74
- **App:** DataHangar Flight 1.0.13 (46), iOS 26.5 Simulator · **Website:** stresstest v2.0.123
- **Found:** 2026-10-24 · https://app.devin.ai/sessions/8b79cff4b7ea4af2989164dd937fd4e4

## Steps
1. Website: Safety Report #2064 > Forms > Add Form > QA Hazard Observation; Observed Time 01:25, fill others, Save Changes.
2. App: open #2064, Pull, Forms > QA Hazard Observation.
3. Close, wait one minute, reopen.

## Expected
Observed Time shows 01:25 (the saved value).

## Actual
Shows 01:26, then 01:27 after reopening — always the current time. Local stored value is still `"2026-10-24 01:25:00"`. Observed Date shows today (coincidentally correct here; a value from any other day would display as today).

## Root cause
`Views/Forms/FormWidgetViews.swift`: `FormDateField` parses `yyyy-MM-dd`, `FormTimeField` uses `TimeUtils.dateFromHHMM` (`HH:mm`). The website stores date and time widgets as `yyyy-MM-dd HH:mm:ss`. Both getters fall back to `Date()` on parse failure, so the picker shows now; any edit/Save writes the wrong value back.

## Evidence
screenshots/IPSMS-014_web_form_saved.png, screenshots/IPSMS-014_app_form_values.png, screenshots/IPSMS-014_app_form_time_now.png

## Suggested fix
Accept the server format (and `HH:mm:ss`) when parsing; never substitute `Date()` for an unparseable non-empty value; write back in the server's format.
