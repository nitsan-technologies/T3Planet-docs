---
title: "Reinstall After Upgrading to Extension v14.x.x"
description: "The steps below are required only when upgrading to Extension v14.x.x from an earlier version."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "Reinstall After Upgrading to Extension v14.x.x"
sidebarTitle: "Reinstall After Upgrading to Extension v14.x.x"
---

<Info>
This page is **only** for upgrading from an old version (before v14) to version 14. For a new installation, use [Installation](/en/latest/ExtNsT3AS/Installation/Index).
</Info>

## Overview

Since version 14, AI Search works together with **AI Foundation** (`ns_t3af`). AI Foundation now holds the connection to your AI service (API keys, models and prompts). AI Search still does the search, the training and the statistics.

Do the steps below in the given order. Skipping a step can cause missing settings or errors.

## Before Updating

- Test the upgrade on a copy of your website (staging) first.
- Check that your server meets the requirements: TYPO3 v12, v13 or v14 and PHP 8.2 – 8.5 (see [TYPO3 v12, v13 and v14](/en/latest/ExtNsT3AS/Introduction/Index#typo3-versions)).
- Have the API keys of your AI service ready. You will enter them again in AI Foundation.

## Migration Steps

### Backup Project

1. Make a full backup of your website files and database.
2. Write down your AI API keys.

<Tip>
With a backup of the trained data you don't need to train your content again. Ask your developer to back up the tables listed under "For developers" below.
</Tip>

### Upgrade

1. Install or update **AI Foundation** (`ns_t3af`).
2. In AI Foundation, add your AI provider and API key (see [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)).
3. Test the provider connection.
4. Install or update AI Search.
5. Go to **Admin Tools → Maintenance** (on TYPO3 v14: **System → Maintenance**) and run **Analyze Database Structure**. Apply all changes.
6. Go to **Admin Tools → Upgrade → Upgrade Wizard** (on TYPO3 v14: **System → Upgrade**) and run all wizards for AI Search and AI Chatbot/Search.
7. Clear all caches.
8. Check the settings that moved out of the site configuration. 1. Go to **AI Universe → AI Chatbot/Search → Search**.
2. Your old values are already filled in. Check them.
3. Click **Save Configuration**. Only then are they saved.
9. Sync your data sources again if needed, and run the training.
10. Search for something on your website and check the answer.

<Note>
On TYPO3 13.4 and v14 this list includes **EXT:ns_t3as: Migrate T3AS Search plugin to content type**. It converts your existing AI Search plugins to the new content element type.
</Note>

See [Upgrading? Where your old settings moved](/en/latest/ExtNsT3AS/Configuration/WhereToFindIt/Index)

{/* - complete the **Backup Project** steps below (trained `t3cs_` data and AI API keys) */}

{/* - Already trained database content (all database tables prefixed with `t3cs_`). This allows you to retain your trained data and avoids the need to re-train your content after the upgrade. */}

{/* 7. Run the TYPO3 Upgrade Wizard after updating to TYPO3 v14 so existing plugins are migrated from `list_type` to `CType`. This should be done after the extension update and database changes. The expected result is that legacy plugin registrations are converted to the TYPO3 v14-compatible format. Clear TYPO3 caches afterwards if needed. */}

{/* 7. Open **Admin Tools → Upgrade → Upgrade Wizard** and run all wizards for AI Search and AI Chatbot/Search. On TYPO3 v14 this includes **EXT:ns_t3as: Migrate T3AS Search plugin to content type**, which moves the plugin from `list_type` to `CType` (the new content element format). Run the wizards after the extension update and the database changes. The Database Analyzer also adds a new full-text index (`content_ft`) to the AI data table `tx_nst3cs_domain_model_datasource_embedd`; apply it so search stays fast. */}

{/* 9. Re-check T3AS search settings, prompts, and provider access. */}

## After the update, check

- The **Dashboard** shows the right AI provider and model.
- One data source can be synced, and training runs without errors.
- Search for something on your website and check the answer.
- The Scheduler task for training still runs.
- **AI Logs** show no errors (see [AI Usage & Logs](/en/latest/ExtNsT3AF/Configuration/AIUsageAndLogs/Index)).

## Common Migration Issues

- **AI Foundation is not installed** – AI Search needs it. Install AI Foundation.
- **AI provider not connected** – add a provider in AI Foundation, set it as default, save and test the connection.
- **Answers are empty or weak** – check the prompts, data sources and the Training Center.
- **Training does not run** – check that the Scheduler task exists and that your server runs the Scheduler.

<Accordion title="For developers: tables to back up">
Back up the database tables of the extension before you reinstall. They hold the trained data.

- Back up all tables that start with `tx_nst3cs_` and `tx_nst3as_`.
- After the reinstall, open the **Database Analyzer** (**Admin Tools → Maintenance → Analyze Database Structure**) and apply the changes. It adds an index that keeps the search fast.
</Accordion>

## Related Documentation

- [Installation](/en/latest/ExtNsT3AS/Installation/Index)
- [Update Guide](/en/latest/ExtNsT3AS/UpdateGuide/Index)
- [Configuration](/en/latest/ExtNsT3AS/Configuration/Index)
- [AI Foundation installation](/en/latest/ExtNsT3AF/Installation/Index)

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

<Info>
This upgrade introduces major breaking changes.

The steps below are required **only when upgrading to Extension v14.x.x** from an earlier version.

Before starting the reinstallation process, ensure that you review and complete every step in the order provided.

Skipping or changing the sequence of these steps may result in configuration issues, missing functionality, or data inconsistencies.

If you are performing a fresh installation or upgrade extension, please follow the instructions in the [Installation](/en/latest/ExtNsT3AS/Installation/Index) section.
</Info>

T3AS now works as a child extension of T3AF (`ns_t3af`).
If you used T3AS with the previous standalone setup, this guide shows how to move your AI search project to the new parent-extension architecture.

## Previous Version

Earlier T3AS projects usually followed this pattern:

1. Install T3AS directly
2. Configure the search-related AI setup inside the child extension
3. Start indexing, training, and answering search requests

## New Architecture

T3AS still provides the search, training, analytics, and frontend answer workflows.
T3AF now provides the shared provider setup, prompts, AI features, and core services used by those workflows.

Before you update, make sure you:

Helpful references:

- [T3AF Installation](/en/latest/ExtNsT3AF/Installation/Index)
- [T3AF Configuration](/en/latest/ExtNsT3AF/Configuration/Index)
- [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)

Before upgrading, make sure to back up the following:

Also create a complete backup of your TYPO3 files and full database before you continue.

## What users should do after updating

After the update, confirm that:

- data sources still sync correctly
- training can run without errors
- search answers still return relevant content
- source links, feedback, or chatbot mode still work if enabled
- usage logs and statistics still show activity

## Recommended Post-Update Checks

- Open the Dashboard and confirm the expected provider and model are shown
- Test one sync from a real data source
- Run one training cycle
- Perform a frontend search and review the answer quality
- Confirm the Scheduler task still runs as expected
- Review AI logs for failed training or answer requests

- **T3AF is not installed**: T3AS now depends on `ns_t3af`.
- **Provider setup is incomplete**: training or answer generation may fail until the shared provider setup is finished.
- **AI Provider Not Connected**: AI features require a successfully connected AI provider. Common causes include a provider that is not connected, no default provider selected, failed authentication, or a model that is not configured. Open T3AF, configure the provider, select a default provider, save the configuration, and verify the connection before testing AI features again.
- **Answers are empty or weak**: re-check prompts, data sources, and training status.
- **Training does not run**: verify the Scheduler task and pending queue items.

- [Installation](/en/latest/ExtNsT3AS/Installation/Index)
- [Update Guide](/en/latest/ExtNsT3AS/UpdateGuide/Index)
- [Configuration](/en/latest/ExtNsT3AS/Configuration/Index)
- [T3AF Installation](/en/latest/ExtNsT3AF/Installation/Index)
- [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)
*/}

{/* Detailed developer notes (moved here on 2026-10-08 to keep the page short; not shown on the website):

<Accordion title="For developers: tables to back up">

Back up all database tables that start with `tx_nst3cs_` and `tx_nst3as_`. They contain the trained data. The Database Analyzer also adds a full-text index (`content_ft`) to `tx_nst3cs_domain_model_datasource_embedd`; apply it so search stays fast.

</Accordion>
*/}
