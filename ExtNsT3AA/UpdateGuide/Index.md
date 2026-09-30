---
title: "Update Guide"
description: "Update T3AA Premium (EXT:ns_t3aa) safely: remove the old version, update EXT:ns_license, re-activate the license, then run the Database Analyzer and check AI Foundation."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AA"
sidebarTitle: "Update Guide"
---

To update the **T3AA Premium** extension, follow the general
[update documentation](/en/latest/License/UpdateVersion/Index) before you
upgrade your installation.

<Warning>
**Migration Steps**

**Step 1 — Remove the current extension**

Uninstall `EXT:ns_t3aa` from your TYPO3 installation before proceeding with the update.

**Step 2 — Update EXT:ns_license**

Make sure the latest version of the T3Planet Shop extension is installed. Update `EXT:ns_license` first before downloading the new T3AA version.

**Step 3 — Re-activate your license**

**Without Composer**

Go to **Admin Tools** → **T3Planet Shop**, remove the existing license key, enter the license key again, and activate it. The new extension version will be downloaded automatically.

**With Composer**

Completely remove T3AA from your project first. Then, in your `composer.json` file, update the `only` parameter in the Composer `repositories` configuration:

```json
"only": [
  "nitsan/ns-t3aa"
]
```

Install the latest T3AA package and update dependencies. Confirm that AI Foundation (`EXT:ns_t3af`) is installed — either with Composer or from the TYPO3 Extension Repository (TER) via **Admin Tools** → **Extensions** → **Get Extensions**.

Download / TER page: [extensions.typo3.org/extension/ns_t3af](https://extensions.typo3.org/extension/ns_t3af)

Full details: [License Activation](/en/latest/License/LicenseActivation/Index)

**Step 4 — Run the Database Analyzer**

Go to **Admin Tools** → **Maintenance** → **Database Analyzer** and apply all pending database changes.

**Step 5 — Configure AI Foundation**

Install and configure `EXT:ns_t3af` first. Then configure the AI Provider from AI Foundation before using T3AA.

**Step 6 — Complete T3AA setup**

Follow the [T3AA documentation](/en/latest/ExtNsT3AA/Index) for the full setup.
</Warning>

<Note>
Always create a complete backup of your database, uploaded files, and project before performing an update. This helps prevent data loss and allows you to restore the previous version if any compatibility issues occur during the upgrade.
</Note>
