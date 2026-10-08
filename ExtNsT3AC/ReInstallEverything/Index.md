---
title: "Reinstall After Upgrading to Extension v14.x.x"
description: "The steps below are required only when upgrading to Extension v14.x.x from an earlier version."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AC"
  - "Reinstall After Upgrading to Extension v14.x.x"
sidebarTitle: "Reinstall After Upgrading to Extension v14.x.x"
---

<Info>
This page is **only** for upgrading from an old version (before v14) to version 14. For a new installation, use [Installation](/en/latest/ExtNsT3AC/Installation/Index).
</Info>

## Overview

Since version 14, AI Chatbot works together with **AI Foundation** (`ns_t3af`). AI Foundation now holds the connection to your AI service (API keys, models and prompts). AI Chatbot still does the chatbot, the training and the statistics.

Do the steps below in the given order. Skipping a step can cause missing settings or errors.

## Before Updating

- Test the upgrade on a copy of your website (staging) first.
- Check that your server meets the requirements: TYPO3 v12, v13 or v14 and PHP 8.2 – 8.5 (see [TYPO3 v12, v13 and v14](/en/latest/ExtNsT3AC/Introduction/Index#typo3-versions)).
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
4. Install or update AI Chatbot.
5. Go to **Admin Tools → Maintenance** (on TYPO3 v14: **System → Maintenance**) and run **Analyze Database Structure**. Apply all changes.
6. Go to **Admin Tools → Upgrade → Upgrade Wizard** (on TYPO3 v14: **System → Upgrade**) and run all wizards for AI Chatbot and AI Chatbot/Search.
7. Clear all caches.
8. Check the settings that moved out of the site configuration. The old values are **not** copied. Enter them again:

1. Go to **AI Universe → AI Chatbot/Search → Chatbot**.
2. On **Configuration**, turn on **Enable AI Chatbot**.
3. On **General**, enter the pages and your CSS.
4. On **External Embed**, enter the allowed websites.
5. Click **Save Configuration**.
9. Sync your data sources again if needed, and run the training.
10. Open your website and ask the chatbot a question.


See [Upgrading? Where your old settings moved](/en/latest/ExtNsT3AC/Configuration/WhereToFindIt/Index)

{/* - complete the **Backup Project** steps below (trained `t3cs_` data and AI API keys) */}

{/* - Already trained database content (all database tables prefixed with `t3cs_`). This allows you to retain your trained data and avoids the need to re-train your content after the upgrade. */}

{/* 8. Re-check chatbot configuration, prompts, and provider access. */}

## After the update, check

- The **Dashboard** shows the right AI provider and model.
- One data source can be synced, and training runs without errors.
- Open your website and ask the chatbot a question.
- The Scheduler task for training still runs.
- **AI Logs** show no errors (see [AI Usage & Logs](/en/latest/ExtNsT3AF/Configuration/AIUsageAndLogs/Index)).

## Common Migration Issues

- **AI Foundation is not installed** – AI Chatbot needs it. Install AI Foundation.
- **AI provider not connected** – add a provider in AI Foundation, set it as default, save and test the connection.
- **Answers are empty or weak** – check the prompts, data sources and the Training Center.
- **Training does not run** – check that the Scheduler task exists and that your server runs the Scheduler.

<Accordion title="For developers: tables to back up">
Back up the database tables of the extension before you reinstall. They hold the trained data and the chat history.

- Back up all tables that start with `tx_nst3cs_` and `tx_nst3ac_`.
- After the reinstall, open the **Database Analyzer** (**Admin Tools → Maintenance → Analyze Database Structure**) and apply the changes. It adds an index that keeps the search fast.
</Accordion>

## Related Documentation

- [Installation](/en/latest/ExtNsT3AC/Installation/Index)
- [Update Guide](/en/latest/ExtNsT3AC/UpdateGuide/Index)
- [Configuration](/en/latest/ExtNsT3AC/Configuration/Index)
- [AI Foundation installation](/en/latest/ExtNsT3AF/Installation/Index)

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

<Info>
This upgrade introduces major breaking changes.

The steps below are required **only when upgrading to Extension v14.x.x** from an earlier version.

Before starting the reinstallation process, ensure that you review and complete every step in the order provided.

Skipping or changing the sequence of these steps may result in configuration issues, missing functionality, or data inconsistencies.

If you are performing a fresh installation or upgrade extension, please follow the instructions in the [Installation](/en/latest/ExtNsT3AC/Installation/Index) section.
</Info>

T3AC now works as a child extension of T3AF (`ns_t3af`).
If you used T3AC with the previous standalone setup, this guide explains how to move your chatbot project to the new parent-extension architecture.

## Previous Version

Earlier T3AC projects usually followed this pattern:

1. Install T3AC directly
2. Configure chatbot-related AI settings inside the child extension
3. Start training content and serving chatbot answers

## New Architecture

T3AC still provides the chatbot, training, and embed workflows, but T3AF now handles the shared provider setup, prompts, AI features, and common AI services used by those workflows.

Before you update, make sure you:

Helpful references:

- [T3AF Installation](/en/latest/ExtNsT3AF/Installation/Index)
- [T3AF Configuration](/en/latest/ExtNsT3AF/Configuration/Index)
- [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)

Before upgrading, make sure to back up the following:

Also create a complete backup of your TYPO3 files and full database before you continue.

## What users should do after updating

After the update, confirm that:

- the chatbot opens correctly
- training still completes without errors
- answers still use the expected data and tone
- source links or embed behavior still work where enabled
- logs and usage tracking still show activity

## Recommended Post-Update Checks

- Test one chatbot question with a real project query
- Review greeting, welcome text, and prompt behavior
- Verify the training pipeline and data source sync
- Check one external embed if your project uses it
- Review AI logs for failed requests or training issues

- **T3AF is not installed**: T3AC now depends on `ns_t3af`.
- **Provider setup is incomplete**: chatbot requests may fail until the shared provider setup is finished.
- **Answers changed after the update**: review chatbot prompts and training data.
- **Chatbot opens but has weak results**: re-check training, source data, and prompt instructions.

- [Installation](/en/latest/ExtNsT3AC/Installation/Index)
- [Configuration](/en/latest/ExtNsT3AC/Configuration/Index)
- [T3AF Installation](/en/latest/ExtNsT3AF/Installation/Index)
- [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)
*/}

{/* Detailed developer notes (moved here on 2026-10-08 to keep the page short; not shown on the website):

<Accordion title="For developers: tables to back up">

Back up all database tables that start with `tx_nst3cs_` and `tx_nst3ac_`. They contain the trained data and chat history. The Database Analyzer also adds a full-text index (`content_ft`) to `tx_nst3cs_domain_model_datasource_embedd`; apply it so search stays fast.

</Accordion>
*/}
