# BUG-IPSMS-004 — Safety Report push says 'Successfully pushed' even if saving forms, deleting files or changing status fails

- **Severity:** Medium
- **Area:** iPad app — Safety Reports > Push (SMSReportUploadService)
- **Found:** 2026-10-24, iPad Pro 13-inch (M5) Simulator, iOS 26.5, DataHangar Flight 1.0.13 (46), stresstest v2.0.123

## Steps
1. Source review of SMSReportUploadService.swift push path (about lines 156-178).
2. To reproduce live: push a report whose status change or form save the server rejects (for example a user without investigator access on that report).

## Expected
Push reports which part failed and keeps that change pending for retry.

## Actual
deleteDocument (file deletions), saveForms (form save/removal) and changeStatus are all called with `try?`, so server errors are discarded and the app still shows 'Successfully pushed to DataHangar Report #N'. The 'Step 11: Refresh from server' comment has no call behind it. This is part of why BUG-IPSMS-001 (forms lost) shows a success message. Found in source; the happy path works (file delete IPFILE-006, form removal IPFORM-006, status change IPPERM-080) - a live server-side failure was not reproduced.

## Cause
SMSReportUploadService.swift: `try? await smsSync.deleteDocument`, `try? await smsSync.saveForms`, `try? await smsSync.changeStatus`.

## Evidence
- Source review / audit log only (see checklist row).
