# BUG-IPSMS-002: Final Report tab shows stale values after Pull (overwrite risk)

- Severity: Medium
- Area: iPad app > Safety Reports > Final Report
- Build: DataHangar Flight 1.0.13 (46), iPad Pro 13" Simulator iOS 26.5; site stresstest v2.0.123
- Status: Open

## Steps
1. Report #2064 open in the app on the Final tab (summary "BETA TEST ONLY final summary from iPad").
2. On the website, change the Final Report summary to "...edited on website" and Save.
3. In the app, Pull while staying on the Final tab.

## Expected
Final tab shows the website summary.

## Actual
The local model gets the new value (SQLite closedDescription = "edited on website"), but the text box still shows the old "from iPad" text until you switch tabs and come back. Editing the stale box autosaves the old text over the website value.

## Cause
`SafetyFinalReportSection.loadState()` runs on `.onAppear` and is guarded by `isLoaded`, so later report changes from Pull never reach the `@State` fields (closedDescription, final likelihood/consequence, hazard fields).

## Suggested fix
Reload state on `.onChange(of: report.lastSyncedAt)` (or report identity/version) when nothing has been edited locally.

## Evidence
evidence/IPSMS-016_app_final_pulled.png, screenshots/IPSMS-016_web_final_after_reload.png, screenshots/IPSMS-016_app_final_after_tabswitch.png
