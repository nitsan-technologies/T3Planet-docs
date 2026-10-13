---
title: "Recursive Mass Translate"
description: "Queue a page and all its subpages for mass translation with one action from the page tree context menu, then let the Scheduler translate them."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "Translation"
sidebarTitle: "Recursive Mass Translate"
---

Queues a page and all its subpages for [Mass Translation](/en/latest/ExtNsT3AI/Translation/MassTranslation/Index) in one action. A Scheduler task then translates them.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmraloedr0yqmqmhxmejplhxg?embed_v=2&utm_source=embed" loading="lazy" title="Recursive Mass Translate" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## Recursive Mass-Translate

1. Edit the page properties and open the **AI Assistant** tab of the parent page. Enable **Allow Mass-Translate?** and **Allow Recursive Mass-Translate?**, then save.
2. Right-click the parent page in the page tree and choose **Mass Translation > Recursively add this page to the scheduler queue**.
3. Make sure the Scheduler task **T3AF: Bulk Translate (queue)** runs. See [Scheduler & CLI](/en/latest/ExtNsT3AI/Configuration/SchedulerAndCLI/Index).

<Note>
The **Mass Translation** entry only appears in the context menu for pages with **Allow Mass-Translate?** enabled. Subpages are queued only if they have **Allow Mass-Translate?** enabled as well. To queue a page tree without setting these options, use **Add pages to queue** with **Include all subpages** in [Manage Mass Translation](/en/latest/ExtNsT3AI/Translation/MassTranslation/Index#manage-mass-translation).
</Note>

### Earlier walkthrough

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfpeyoww2l6g1d3ns8fsb5z6?embed_v=2&utm_source=embed" loading="lazy" title="Recursive Mass Translate" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

**Related:** [AI Translation card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-translation) · [Permissions](/en/latest/ExtNsT3AI/Configuration/Permissions/Index) · [Agent: queue tools](/en/latest/ExtNsT3AI/AskAiAgent/Tools/Index#mass-translation-queue) · [Scheduler & CLI](/en/latest/ExtNsT3AI/Configuration/SchedulerAndCLI/Index)
