---
title: "Update Guide"
description: "To update the **T3AS Premium** extension, please follow the official update documentation before upgrading your installation: https://docs.t3planet.de/en/latest/License/UpdateVersion/Index.html"
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "Update Guide"
sidebarTitle: "Update Guide"
---

This page shows you how to update AI Search to a new version. For general information about updates, see [Update a T3Planet extension](/en/latest/License/UpdateVersion/Index).

<Warning>
Make a full backup of your database and files before you update. Then you can go back if something goes wrong.
</Warning>

<Note>
AI Search works with **TYPO3 v12, v13 and v14**. On TYPO3 v14, **Admin Tools** is called **System**. See [TYPO3 v12, v13 and v14](/en/latest/ExtNsT3AS/Introduction/Index#typo3-versions).
</Note>

## Update step by step

1. **Remove the old version.** Uninstall AI Search (`ns_t3as`) in the Extension Manager.
2. **Update the License Manager.** Install the newest version of the License Manager (`ns_license`).
3. **Activate the license again.**
   1. Go to **Admin Tools → T3Planet Shop** (on TYPO3 v14: **System → T3Planet Shop**).
   2. Remove your license key.
   3. Enter the license key again.
   4. Activate it. The new version is downloaded automatically.
4. **Check AI Foundation.** Make sure AI Foundation (`ns_t3af`) is installed and has a working AI provider (see [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)).
5. **Update the database.**
   1. Go to **Admin Tools → Maintenance** (on TYPO3 v14: **System → Maintenance**).
   2. Click **Analyze Database Structure**.
   3. Apply all changes.
6. **Clear all caches.**
7. **Check your settings.** Older versions had a **T3AS** tab in the site configuration. It is gone. See [Upgrading? Where your old settings moved](/en/latest/ExtNsT3AS/Configuration/WhereToFindIt/Index)
8. **Test.** Search for something on your website and check the answer.

{/* Go to **Admin Tools** → **License Manager**, remove the existing license key, enter the license key again, and activate it. The new extension version will be downloaded automatically. */}

<Accordion title="Update with Composer (for developers)">

1. Remove the package from the project first.
2. In `composer.json`, make sure the T3Planet repository allows the packages:

```json
"only": [
  "nitsan/ns-t3as",
  "nitsan/ns-t3cs"
]
```

3. Require the newest version and update dependencies.
4. Make sure `nitsan/ns-t3af` is installed, or install AI Foundation from [extensions.typo3.org](https://extensions.typo3.org/extension/ns_t3af).

Full details: [License activation](/en/latest/License/LicenseActivation/Index)

</Accordion>

More help: [AI Search documentation](/en/latest/ExtNsT3AS/Index) · [AI Foundation installation](/en/latest/ExtNsT3AF/Installation/Index)

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

To update the **T3AS Premium** extension, please follow the official update documentation before upgrading your installation:
[https://docs.t3planet.de/en/latest/License/UpdateVersion/Index.html](/en/latest/License/UpdateVersion/Index)

<Info>
**Migration Steps**

**Step 1 — Remove the current extension**

Uninstall `EXT:ns_t3as` from your TYPO3 installation before proceeding with the update.

**Step 2 — Update EXT:ns_license**

Make sure the latest version of the License Manager extension is installed. Update `EXT:ns_license` first before downloading the new T3AS version.

**Step 3 — Re-activate your license**

**Without Composer**

**With Composer**

Completely remove T3AS from your project first. Then, in your `composer.json` file, update the `only` parameter in the Composer `repositories` configuration:

Download / TER page: [https://extensions.typo3.org/extension/ns_t3af](https://extensions.typo3.org/extension/ns_t3af)

Full details:
[https://docs.t3planet.de/en/latest/License/LicenseActivation/Index.html](/en/latest/License/LicenseActivation/Index)

**Step 4 — Run the Database Analyzer**

**Step 5 — Configure T3AF**

Install and configure `EXT:ns_t3af` first. Then configure the AI Provider from T3AF before using T3AS.

Review these pages if needed:

- [T3AF Installation](/en/latest/ExtNsT3AF/Installation/Index)
- [T3AF Configuration](/en/latest/ExtNsT3AF/Configuration/Index)
- [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)

**Step 6 — Complete T3AS setup**

<Note>
Always create a complete backup of your database, uploaded files, and project before performing an update. This helps prevent data loss and allows you to restore the previous version if any compatibility issues occur during the upgrade.
</Note>
*/}
