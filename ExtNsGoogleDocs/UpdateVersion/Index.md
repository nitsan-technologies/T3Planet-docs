---
title: "Update Version"
description: "Update Google Docs (EXT:ns_googledocs) to version 14, including the upgrade from marker-based versions 2.x."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "ns_GoogleDocs"
  - "Update Version"
  - "UpdateVersion"
  - "Upgrade"
sidebarTitle: "Update Version"
---

For general update steps of T3Planet premium extensions, see the [License Update Version guide](/License/UpdateVersion/Index).

## Updating to version 14 from 2.x (marker-based versions)

Version 2.x was a free extension that used markers such as `###TEXT###`. Version 14 is premium, needs EXT:ns_license and reads **Heading 1** / **Heading 2** instead of markers. Your Google credentials (Client ID, Client Secret, Refresh Token) are kept.

1. **Check TYPO3 and PHP.** Version 14 needs TYPO3 12.4, 13.4 or 14 and PHP 8.1 or newer. On TYPO3 11 or older, upgrade TYPO3 first.
2. **Take a full backup** of the database and files.
3. **Install EXT:ns_license 14.5.x** (14.5.0 up to 14.9.x; Composer `nitsan/ns-license:^14.5`) and activate your license in the **T3Planet Shop** module. The license key must match the current domain, or imports are blocked. See [License Activation](/License/LicenseActivation/Index).
4. **Update the extension.**
   - Composer: add the T3Planet Composer repository as shown in [Installation](/ExtNsGoogleDocs/Installation/Index#step-2-install-extns_googledocs), then run:

     ```bash
     composer require nitsan/ns-license:^14.5 nitsan/ns-googledocs --with-all-dependencies
     ```

   - Non-Composer: remove the old 2.x version, then download version 14 through the **T3Planet Shop** module and activate it.
5. **Update the database.** Open **Analyze Database Structure** and apply all changes. This adds the new record and image settings.
   - TYPO3 14: **System › Maintenance**
   - TYPO3 12 and 13: **Admin Tools › Maintenance**
6. **Include the TypoScript** if it is not included yet: site set **EXT:GoogleDocs :: Basic Setup** (`nitsan/ns-googledocs`) or static template **Google Docs**. Without it, the classes and colours of imported content are removed. See [Installation, Step 4](/ExtNsGoogleDocs/Installation/Index#step-4-include-the-typoscript).
7. **Flush all caches.**
8. **Review Global Settings** and set **Publish Status**, **Image Alignment**, **Enlarge on Click** and **Number of Column**. See [Global Settings](/ExtNsGoogleDocs/NSGoogleDocsModule/Index#global-settings).
9. **Update your Google Docs.** Remove the `###TEXT###`, `###TEXTIMAGETOP###`, `###TEXTIMAGELEFT###`, `###TEXTIMAGERIGHT###`, `###TEXTIMAGEBOTTOM###` and `###IMAGES###` markers and use **Heading 1** / **Heading 2** instead. You now choose the element type per section in the import dialog. See [How to prepare Google Docs with headers?](/ExtNsGoogleDocs/PrepareGoogleDocWithMarkers/Index) and [Reformation](/ExtNsGoogleDocs/Reformation/Index).
10. **Test one import** into a test page before you import into live pages.
