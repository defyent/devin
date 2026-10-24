# BUG-IPSMS-001 — Safety Report form attached in iPad app is silently lost on push

- **Severity:** High (data loss, false success)
- **Area:** iPad app — Safety Reports > Forms (checklist 74)
- **App:** DataHangar Flight 1.0.13 (46), iOS 26.5 Simulator · **Website:** stresstest v2.0.123
- **Found:** 2026-10-24 · https://app.devin.ai/sessions/8b79cff4b7ea4af2989164dd937fd4e4

## Steps
1. In the app open Safety Report #2064 (BETA TEST ONLY iPad SMS report) > Forms > Attach Form > QA Hazard Observation.
2. Fill Risk Level=Medium, Location, Description, Hazard Category=Maintenance, Reported to Supervisor=on; Save (shows 5/8 fields, "#2064 needs push").
3. Tap Push > confirm.

## Expected
Form instance is created on the server with the entered values and appears in the website Forms tab and stays in the app.

## Actual
- App shows "Report Synced — Successfully pushed to DataHangar Report #2064."
- Website #2064 Forms tab: "No forms have been attached."
- App Forms tab after the post-push refresh: "No forms attached" (local `attachedForms` = []). The user's entered form data is gone on both sides.

## Root cause (code)
- `SMSReportSyncService.addForm` (`smsreportdetails_addform`) has no callers anywhere in the project.
- `SMSReportUploadService` step 9 calls `saveForms`, which sends `instance_id = form.localId` for forms without a server instance; the server does not create an instance from it.
- The call is `try? await smsSync.saveForms(...)` — any error is swallowed and the push still reports success; step 11 then refreshes from server and overwrites the local form list.

## Evidence
- screenshots/IPSMS-013_app_attach_form_list.png, screenshots/IPSMS-013_app_form_blank.png, screenshots/IPSMS-013_app_form_saved_local.png
- screenshots/IPSMS-013_app_form_push_ok_but_empty.png, screenshots/IPSMS-013_web_no_forms.png

## Suggested fix
For forms with `instanceId == nil`, call `addForm` first and store the returned instance id before `saveForms`; stop using `try?` for forms/status (surface errors and keep local data/needsPush on failure).
