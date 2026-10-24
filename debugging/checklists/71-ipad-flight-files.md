# iPad flight files

- **Checklist ID prefix:** `IPFILE`
- **Guide section:** `debugging/IPAD_SWIFT_AUDIT_PLAN.md` §3
- **Where:** iPad app — Flight/Safety Report file upload, delete, pull and website parity
- **Permission:** Admin / Service Account unless a different permission level is identified in the row notes
- **Tester:** Devin
- **Date / DataHangar version:** 24/10/2026 / iPad DataHangar Flight 1.0.13 (46) on iOS 26.5 Simulator; stresstest v2.0.123
- **Account / level used:** Service Account unless a different account is identified in the row notes

Result values: `TODO` · `PASS` · `FAIL` · `BLOCKED` · `N/A`. A `FAIL` must have a Bug ID (see `../DEBUGGING_GUIDE.md`).

## Module checks

| ID | Check | Expected | Result | Bug ID | Notes |
|---|---|---|---|---|---|
| IPFILE-001 | Push auto-uploads flight PDF: website #42914 Files: 'flight_ZK_HEL___BETA_TEST_ONLY_NZAA_NZCH...' 23/10/2026, Service Account, 87 KB. Discarded accidental W&B toggle via Cancel -> 'Discar… | TBD (not recorded) | PASS |  | L74: Push auto-uploads flight PDF: website #42914 Files: 'flight_ZK_HEL___BETA_TEST_ONLY_NZAA_NZCH...' 23/10/2026, Service Account, 87 KB. Discarded accidental W&B toggle via Cancel -> 'Discard Changes' confirm (works). PASS |
| IPFILE-002 | App Files tab shows 'flight_ZK_HEL___BETA_TEST_ONLY_NZAA_NZCH_20261023.pdf' 89 KB (89158 B, decimal KB) vs website 87 KB (binary KiB) - same file, docId 587, synced. Minor unit inconsiste… | TBD (not recorded) | PASS |  | L75: App Files tab shows 'flight_ZK_HEL___BETA_TEST_ONLY_NZAA_NZCH_20261023.pdf' 89 KB (89158 B, decimal KB) vs website 87 KB (binary KiB) - same file, docId 587, synced. Minor unit inconsistency (cosmetic). PASS |
| IPFILE-003 | App (service account, iPad Pro) #2064 Files (2): photo.jpg (app upload), BETA_TEST_ONLY_web_upload.txt (website upload). Deleting the website-uploaded file in the app, then Push, then che… | TBD (not recorded) | TODO |  | L437: App (service account, iPad Pro) #2064 Files (2): photo.jpg (app upload), BETA_TEST_ONLY_web_upload.txt (website upload). Deleting the website-uploaded file in the app, then Push, then check website. Evidence [IPFILE-003_app_2064_files_before_delete.png](../bugs/screenshots/IPFILE-003_app_2064_files_before_delete.png) |
| IPFILE-004 | App: file delete confirm dialog clear; after Delete, Files (1), report '#2064 needs push', toast. Pushing. Evidence IPFILE-004_app_2064_file_deleted_local.png | TBD (not recorded) | TODO |  | L438: App: file delete confirm dialog clear; after Delete, Files (1), report '#2064 needs push', toast. Pushing. Evidence [IPFILE-004_app_2064_file_deleted_local.png](../bugs/screenshots/IPFILE-004_app_2064_file_deleted_local.png) |
| IPFILE-005 | App Push after file delete: 'Report Synced — Successfully pushed', #2064 synced, Files (1). Verifying website. | TBD (not recorded) | TODO |  | L439: App Push after file delete: 'Report Synced — Successfully pushed', #2064 synced, Files (1). Verifying website. |
| IPFILE-006 | App->web file delete: website #2064 Files now only photo.jpg; BETA_TEST_ONLY_web_upload.txt gone. Evidence IPFILE-006_web_2064_file_deleted_from_app.png. Next: delete photo.jpg on website… | TBD (not recorded) | PASS |  | L440: PASS App->web file delete: website #2064 Files now only photo.jpg; BETA_TEST_ONLY_web_upload.txt gone. Evidence [IPFILE-006_web_2064_file_deleted_from_app.png](../bugs/screenshots/IPFILE-006_web_2064_file_deleted_from_app.png). Next: delete photo.jpg on website, Pull in app. |
| IPFILE-007 | Website: deleting photo.jpg (app-uploaded) on #2064 via Files tab trash -> 'Delete File' confirm. | TBD (not recorded) | TODO |  | L441: Website: deleting photo.jpg (app-uploaded) on #2064 via Files tab trash -> 'Delete File' confirm.<br>L442: Website: photo.jpg deleted, 'No files have been attached'. Evidence [IPFILE-007_web_2064_no_files.png](../bugs/screenshots/IPFILE-007_web_2064_no_files.png). Next: app Pull. |
| IPFILE-008 | Web->app file delete: after Pull, app #2064 Files 'No files attached', synced. File deletion works both ways. Evidence IPFILE-008_app_2064_no_files_after_pull.png. Next: form removal. | TBD (not recorded) | PASS |  | L443: PASS Web->app file delete: after Pull, app #2064 Files 'No files attached', synced. File deletion works both ways. Evidence [IPFILE-008_app_2064_no_files_after_pull.png](../bugs/screenshots/IPFILE-008_app_2064_no_files_after_pull.png). Next: form removal. |

## Test data created

| Record | Where | Cleanup done? |
|---|---|---|
| Safety Report #2064 | BETA test report used for file upload/delete checks | No |
