---
title: "Known Problems"
description: "Known problems with T3AI (EXT:ns_t3ai) and how to solve them, for example new default prompts that are missing after an update."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "Known Problems"
sidebarTitle: "Known Problems"
---

## New default prompts are missing after an update

The default prompts (type **System** in [AI Prompts](/en/latest/ExtNsT3AI/Prompts/Index)) are delivered with T3AI and AI Foundation, so an update brings new default prompts automatically. If a T3AI window or the AI Prompts list still shows the old set:

1. Check that AI Foundation (`EXT:ns_t3af`) was updated together with T3AI.
2. Go to **Admin Tools > Maintenance** and click **Flush TYPO3 and PHP Cache**.
3. Reload the backend.

Your custom prompts are kept.

## Report problems

For other issues, open a ticket at [t3planet.de/support](https://t3planet.de/support) with your TYPO3, PHP, and T3AI versions and the exact error text.

**Related:** [FAQ](/en/latest/ExtNsT3AI/FAQ/Index) · [Prompts](/en/latest/ExtNsT3AI/Prompts/Index)
