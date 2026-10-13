---
title: "Mass Translation"
description: "Translate many TYPO3 pages at once: queue pages in Manage Mass Translation or from the page tree, then let the Scheduler or CLI process the queue."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "Translation"
sidebarTitle: "Mass Translation"
---

Mass Translation translates many pages in the background. You put pages in a **queue**, and a Scheduler task translates them one batch at a time. This avoids long waits in the browser and works for whole sites.

## Mass Translation

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfpei6sj2kta1d3n7mns6mnh?embed_v=2&utm_source=embed" loading="lazy" title="Mass Translation" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

There are two ways to fill the queue:

- **Manage Mass Translation** module: pick pages and languages in one place. No page settings needed.
- **Page tree context menu**: queue single pages or page trees. The pages need **Allow Mass-Translate?** enabled.

## Manage Mass Translation

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmttyv0zu149lqmgz7dxycp3b?embed_v=2&utm_source=embed" loading="lazy" title="Manage Mass Translation Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

The **Manage Mass Translation** module lets you queue, configure, and monitor translation tasks for multiple pages from one place.

Open it from **AI Assistant → Translation → Manage Mass Translation**.

**Key Features:**

- Select pages and add them to the translation queue.
- Configure target languages for mass translation and save the language mapping.
- Remove pages from the queue when they are no longer needed.
- Re-queue failed translation jobs so they can run again.
- Filter the queue by status: **Pending**, **Completed**, **Failed**, or **All**.
- Filter by site root or view pages across all sites.
- Add pages to the queue by page ID and choose the target language.
- Run the related Scheduler task to process queued translations.

### Add pages to the queue

1. Click **Add pages to queue**.
2. Choose the **Site root** and click **Continue**. The page tree of that site loads.
3. Tick the pages under **Select pages**, or use **Select all**. For a single page, tick **Include all subpages** to add the whole branch.
4. Optionally tick **Re-translate mode (re-translate queue)** to replace existing translations instead of creating new ones.
5. Select the target languages, or **Select all languages**.
6. Click **Add to queue**.

### Work with the queue

![Manage Mass Translation with the status summary, status tabs, and queue actions](../images/t3ai-mass-translation-queue.webp)

- The summary bar counts **Pending**, **Processing**, **Completed**, and **Failed** entries. Filter with the tabs **All**, **Pending**, **Completed**, and **Failed**, and by **Site root**.
- The table shows the page, site, language, **Status**, **Mode** (Translate or Re-translate), **Allowed Languages**, and **Last processed**.
- **Re-queue failed** sends all failed pages back to Pending. **Re-queue Selected (n)** does this for the ticked pages.
- **Clear completed** removes finished entries. **Delete selected (n)** removes the ticked entries.

## Mass Pages Translation

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmralcltn0ycwqmhx52pq7pre?embed_v=2&utm_source=embed" loading="lazy" title="Mass Translate Pages" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Queue pages directly from the page tree.

1. Edit the page properties, open the **AI Assistant** tab, enable **Allow Mass-Translate?**, and save.
2. Right-click the page in the page tree and choose **Mass Translation > Add this page to the scheduler queue**.

![The AI Assistant tab in the page properties](../images/t3ai-page-ai-assistant-tab.webp)

Other entries in the same submenu:

- **Recursively add this page to the scheduler queue**: the page and its subpages. See [Recursive Mass Translate](/en/latest/ExtNsT3AI/Translation/RecursiveMassTranslate/Index).
- **Add this page to the auto-renew translation queue in the scheduler**: re-translate the page in the next run.

## Process the queue

On TYPO3 v14, create these Scheduler tasks:

- **T3AF: Bulk Translate (queue)** for new translations
- **T3AF: Bulk Re-translate (queue)** for entries in Re-translate mode

Both have **Batch size** (pages per batch, default 10) and **Pages per run** (0 = whole queue).

On TYPO3 v13, create an **Execute console commands** task with `t3af:bulk:translate` (or `t3af:bulk:retranslate`) and set the options `batch-size` and `limit`:

![Scheduler options batch-size and limit on TYPO3 v13](../images/mass_translation_scheduler_limit.webp)

Example: **batch-size** `10` and **limit** `10` processes up to 10 pending pages per run. The rest stay in the queue for the next run.

<Note>
The Scheduler only runs when a cron job on the server triggers it. Without cron, run the task manually in the **Scheduler** module or use the CLI below.
</Note>

## Run Mass Translation: From TYPO3-CLI

Composer:

```bash
vendor/bin/typo3 t3af:bulk:translate --batch-size=10 --limit=10
vendor/bin/typo3 t3af:bulk:retranslate --batch-size=10 --limit=10
vendor/bin/typo3 scheduler:run --task=<taskUid> -f
```

Non-Composer:

```bash
php typo3/sysext/core/bin/typo3 t3af:bulk:translate --batch-size=10 --limit=10
php typo3/sysext/core/bin/typo3 t3af:bulk:retranslate --batch-size=10 --limit=10
php typo3/sysext/core/bin/typo3 scheduler:run --task=<taskUid> -f
```

Replace `<taskUid>` with the task UID from the Scheduler module. All options: [Scheduler & CLI](/en/latest/ExtNsT3AI/Configuration/SchedulerAndCLI/Index).

**Related:** [AI Translation card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-translation) · [Permissions](/en/latest/ExtNsT3AI/Configuration/Permissions/Index) · [Agent: queue tools](/en/latest/ExtNsT3AI/AskAiAgent/Tools/Index#mass-translation-queue) · [Scheduler & CLI](/en/latest/ExtNsT3AI/Configuration/SchedulerAndCLI/Index) · [AI Usage & AI Logs](/en/latest/ExtNsT3AI/Configuration/AIUsageAndLogs/Index)
