---
title: "Update & Upgrade"
description: "Update T3AI (EXT:ns_t3ai) within v14, find the right path for an upgrade from v13 or earlier, and upgrade very old T3AI versions."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "Update"
  - "Upgrade"
sidebarTitle: "Update & Upgrade"
---

Use this page for every T3AI version change. For a fresh installation, follow [Installation](/en/latest/ExtNsT3AI/Installation/Index) instead.

## Which steps do I need?

| Your situation | Follow |
|---|---|
| Already on T3AI 14.x, new 14.x release available | [Update within v14](#update-within-v14) |
| On T3AI 13.7.0 or earlier, moving to 14.x | [Reinstall After Upgrading to v14](/en/latest/ExtNsT3AI/ReInstallEverything/Index) |
| On T3AI v1, v2, or v3 | [Older versions](#older-versions) first, then [Reinstall After Upgrading to v14](/en/latest/ExtNsT3AI/ReInstallEverything/Index) |

<Warning>
Back up the database, `fileadmin`, and the project files before every update, and test the update on a staging system first.
</Warning>

## Update within v14

1. Update T3AI with the T3Planet Shop or Composer, as described in [Update Version](/en/latest/License/UpdateVersion/Index).
2. Update AI Foundation (`EXT:ns_t3af`) to the latest compatible version.
3. Go to **Admin Tools > Maintenance > Analyze Database Structure** and apply all changes.
4. Flush all TYPO3 caches. New default prompts are then available in **AI Foundation > AI Prompts**; your custom prompts are kept.

To find out whether a new version is available, see [How to know the latest version](/en/latest/License/UpdateVersion/CheckNewVersion/Index).

## Older versions

### T3AI v3 to v4

T3AI v4 is a complete redevelopment:

1. Deactivate the license key in the T3Planet Shop module.
2. Uninstall and delete the extension.
3. Install T3AI again as described in [License Activation](/en/latest/License/LicenseActivation/Index).

Then continue with [Reinstall After Upgrading to v14](/en/latest/ExtNsT3AI/ReInstallEverything/Index).

### T3AI v1 to v3

Follow the standard [Update Version](/en/latest/License/UpdateVersion/Index) guide.

**Related:** [Installation](/en/latest/ExtNsT3AI/Installation/Index) · [Configuration](/en/latest/ExtNsT3AI/Configuration/Index) · [Releases](/en/latest/ExtNsT3AI/Releases/Index)
