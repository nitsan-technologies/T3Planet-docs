---
title: "Troubleshooting"
description: "Messages you may see in Google Docs (EXT:ns_googledocs) and what to do about them."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "ns_GoogleDocs"
  - "Troubleshooting"
  - "Google Docs error"
sidebarTitle: "Troubleshooting"
---

Find the message you see in the backend, then follow the steps in the right column.

| Message | What to do |
| --- | --- |
| Google account is not connected. Configure it in Global Settings. | Enter your Client ID, Client Secret and Refresh Token in [Global Settings](/ExtNsGoogleDocs/NSGoogleDocsModule/Index#global-settings) |
| No Docs are listed / the list shows an error | Check the refresh token (it must start with `1//`), check that the Google Drive API is enabled, and generate a new refresh token if your consent screen is in Testing mode (tokens expire after 7 days) |
| Your connected Google account does not have permission to read this document. | Share the Doc with the connected Google account |
| The Google Doc content could not be loaded. | The Doc is empty, or the connected account has no read access |
| The Google Doc has no importable text or images after processing. | Add content to the Doc, or tick at least one section |
| The selected content column does not allow "…" elements. | Choose another column or another element type |
| The selected page does not exist or you do not have access to it. | Check the page and your backend page permissions |
| Folder import requires EXT:news to be installed and activated. | Install and activate EXT:news, then update the database |
| Valid license required / license is missing, expired or invalid | Activate a valid license in the **T3Planet Shop** module. See [License Manager](/License/LicenseManager/Index) |
| The current domain is not registered for this Google Docs license. | Register the domain in the **T3Planet Shop** module. See [Register and manage domains](/License/RegisterAndManageDomains/Index), or contact support for staging/development domains |
| The NS License extension (EXT:ns_license) must be installed and activated | Install and activate EXT:ns_license 14.5.x (14.5.0 up to 14.9.x; Composer `nitsan/ns-license:^14.5`) |
| Imported classes or text colours are missing on the frontend | Same fix: include the site set or static template, so the RTE parser keeps the imported classes and styles |
| Image alignment or columns have no visible effect on the frontend | The values are saved on the element; check your theme's CSS for Fluid Styled Content image positions |

Your problem is not listed? Contact [Help & Support](/ExtNsGoogleDocs/Support).
