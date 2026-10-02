---
title: "Update Guide"
description: "Update T3AI Premium: remove the current version, update EXT:ns_license, re-activate the license, run the Database Analyzer, and configure AI Foundation."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "Update Guide"
sidebarTitle: "Update Guide"
---

To update the **T3AI Premium** extension, please follow the official update documentation before upgrading your installation:
[https://docs.t3planet.de/en/latest/License/UpdateVersion/Index.html](/en/latest/License/UpdateVersion/Index)

<Note>
To change the existing provider, navigate to **Provider**, select the existing **OpenAI** provider, and click **Edit**. Change the provider to **Mistral**, save the updated configuration, and then use **Test Connection** to verify the connection. After the test is completed, manually check and confirm that the **Mistral** provider is connected successfully and working as expected.
</Note>

<Note>
Before using T3AI, make sure the **News** extension is up to date and running the latest version.
</Note>

<Info>
**Migration Steps**

**Step 1 — Remove the current extension**

Uninstall `EXT:ns_t3ai` from your TYPO3 installation before proceeding with the update.

**Step 2 — Update EXT:ns_license**

Make sure the latest version of the T3Planet Shop extension is installed. Update `EXT:ns_license` first before downloading the new T3AI version.

**Step 3 — Re-activate your license**

**Without Composer**

Go to **Admin Tools** → **T3Planet Shop**, remove the existing license key, enter the license key again, and activate it. The new extension version will be downloaded automatically.

**With Composer**

Completely remove T3AI from your project first. Then, in your `composer.json` file, update the `only` parameter in the Composer `repositories` configuration:

```json
"only": [
  "nitsan/ns-t3ai"
]
```

Install the latest T3AI package and update dependencies. Confirm that AI Foundation (`EXT:ns_t3af`) is installed — either with Composer or from the TYPO3 Extension Repository (TER) via **Admin Tools** → **Extensions** → **Get Extensions**.

Download / TER page: [https://extensions.typo3.org/extension/ns_t3af](https://extensions.typo3.org/extension/ns_t3af)

Full details:
[https://docs.t3planet.de/en/latest/License/LicenseActivation/Index.html](/en/latest/License/LicenseActivation/Index)

**Step 4 — Run the Database Analyzer**

Go to **Admin Tools** → **Maintenance** → **Database Analyzer** and apply all pending database changes.

**Step 5 — Configure AI Foundation**

Install and configure `EXT:ns_t3af` first. Then configure the AI Provider from AI Foundation before using T3AI.

**Step 6 — Complete T3AI setup**

Follow the T3AI documentation for the full setup:
[https://docs.t3planet.de/en/latest/ExtNsT3AI/Index.html](/en/latest/ExtNsT3AI/Index)
</Info>

<Note>
Always create a complete backup of your database, uploaded files, and project before performing an update. This helps prevent data loss and allows you to restore the previous version if any compatibility issues occur during the upgrade.
</Note>
