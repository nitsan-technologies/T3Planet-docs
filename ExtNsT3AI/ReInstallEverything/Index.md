---
title: "Reinstall After Upgrading to Extension v14.x.x"
description: "Required only when upgrading T3AI to v14.x.x from v13.7.0 or earlier: remove the old version, install T3AI 14 with AI Foundation, update the database, set up AI Foundation, and check the result."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "Reinstall After Upgrading to Extension v14.x.x"
sidebarTitle: "Reinstall After Upgrading to Extension v14.x.x"
---

<Info>
These steps are required **only when upgrading to T3AI v14.x.x** from v13.7.0 or earlier. For a fresh installation, follow [Installation](/en/latest/ExtNsT3AI/Installation/Index). For updates within v14, see [Update & Upgrade](/en/latest/ExtNsT3AI/UpgradeGuide/Index).
</Info>

<Warning>
Back up the database, `fileadmin`, and the project files first, and test the upgrade on a staging system.
</Warning>

T3AI 14 is a breaking release. T3AI now runs as a child extension of **AI Foundation** (`EXT:ns_t3af`). Providers, API keys, feature settings, prompts, permissions, and logs moved from T3AI to AI Foundation. T3AI keeps the editor tools.

Do the steps in this order. Skipping or reordering them can leave missing settings or broken modules.

## Before you start

- Check that your TYPO3 and PHP versions are supported: [System Requirements](/en/latest/ExtNsT3AI/SystemRequirements/Index).
- Have the API keys of your AI providers ready. You enter them again in AI Foundation.
- If you use T3AI with `EXT:news`, update `EXT:news` to the latest version as well.

## Step 1: Remove the current T3AI

Uninstall `EXT:ns_t3ai`. With Composer, remove the package from the project.

## Step 2: Update the T3Planet Shop

Install the latest version of `EXT:ns_license` before you download the new T3AI version.

## Step 3: Install T3AI 14 and AI Foundation

**Non-Composer**

1. Open **Admin Tools > T3Planet Shop** (TYPO3 v14: **System > T3Planet Shop**).
2. Remove the existing T3AI license key, enter it again, and activate it. The new version is downloaded.
3. If AI Foundation is not installed yet, install `ns_t3af` from **Admin Tools > Extensions > Get Extensions** ([TER page](https://extensions.typo3.org/extension/ns_t3af)).

**Composer**

1. In the T3Planet repository entry of your `composer.json`, make sure the `only` parameter contains T3AI:

```json
"only": [
  "nitsan/ns-t3ai"
]
```

2. Install T3AI and AI Foundation:

```bash
composer require nitsan/ns-t3ai nitsan/ns-t3af
```

Details: [License Activation](/en/latest/License/LicenseActivation/Index).

## Step 4: Update the database

Go to **Admin Tools > Maintenance > Analyze Database Structure**, apply all changes, and flush all caches.

## Step 5: Set up AI Foundation

1. Add your providers in **AI Foundation > AI Providers** and check that they show **Connected**. See [AI provider & API keys](/en/latest/ExtNsT3AI/Configuration/AIProviders/Index).
2. Open each T3AI card in **AI Foundation > AI Features**, check the values, and click **Save Changes**. Where each old setting is now: [Where your old settings moved](/en/latest/ExtNsT3AI/Configuration/WhereToFindIt/Index).
3. Review your editor groups in **AI Foundation > AI Permissions**, and check that the access set in older versions is still correct. See [Permissions](/en/latest/ExtNsT3AI/Configuration/Permissions/Index).
4. Check your prompts in **AI Foundation > AI Prompts**. The default prompts are delivered with the extensions; see [Prompts](/en/latest/ExtNsT3AI/Prompts/Index).

## Step 6: Check the result

- The **AI Foundation** tab of the **AI Assistant** module shows no open setup steps.
- One test per area you use works, for example page generation, SEO, translation, or media.
- [AI Usage & AI Logs](/en/latest/ExtNsT3AI/Configuration/AIUsageAndLogs/Index) show no provider or request errors.
- Results still match your writing style. If not, review the [Prompts](/en/latest/ExtNsT3AI/Prompts/Index).

## Common problems after the upgrade

| Problem | Solution |
|---|---|
| T3AI modules are missing | Install AI Foundation, then apply the database changes and flush caches. |
| No provider is available | Add a provider in AI Foundation > AI Providers. |
| Modules open but requests fail | Check the provider credentials and the **Connection** column, then flush caches. |
| Results look different | Check the T3AI cards in AI Features and your custom prompts. |

**Related:** [Where your old settings moved](/en/latest/ExtNsT3AI/Configuration/WhereToFindIt/Index) · [Installation](/en/latest/ExtNsT3AI/Installation/Index) · [Update & Upgrade](/en/latest/ExtNsT3AI/UpgradeGuide/Index)
