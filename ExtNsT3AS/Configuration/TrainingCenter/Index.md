---
title: "Training Center & Scheduler"
description: "See what AI Search has learned, re-queue failed items, and how the Scheduler trains your content in the background."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "Training Center"
  - "Scheduler"
sidebarTitle: "Training Center & Scheduler"
---

The Training Center shows every piece of content waiting to be learned, being learned, or already learned.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrajhhoo0t19qmhxcu9sljuu?utm_source=link" loading="lazy" title="T3AS Training Center Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

1. Go to **AI Universe → AI Chatbot/Search → Training Center**.
2. At the top you see the numbers: **Total**, **Pending**, **Processing**, **Completed**, **Failed** and **Tokens** (how much AI was used).
3. Below is the list of items. Use the filters to show only one source or one status.

![Training Center with counts, data sources and the training queue](../images/training-center.webp)

**What the status means**

- **Pending** – waiting to be learned.
- **Processing** – being learned right now.
- **Completed** – learned. AI Search can use it.
- **Failed** – something went wrong.

**Train an item again**

1. Select the item (for example a **Failed** one).
2. Click **Re-queue**. The item goes back to **Pending**.
3. Click **Run Task Now** to start training.

**Delete an item**

1. Select the item.
2. Click **Delete**. AI Search will no longer use this content.

<Warning>
Deleted items only come back if you sync the data source again.
</Warning>

{/* SUPADEMO NEEDED: Training Center: re-queue and run */}

**Related:** [Data Source](/en/latest/ExtNsT3AS/Configuration/DataSource/Index) · [Scheduler](#scheduler) · [Dashboard](/en/latest/ExtNsT3AS/Configuration/Dashboard/Index)

{/* - **Summary counts**: Total items, Pending, Embedding (processing), Completed, Failed, and Tokens used. */}

{/* **Delete**

Removes selected queue items. */}

{/* **Run training**

Use the link to the **Scheduler** module and run the **T3AF Training** task for this site.

When the task runs, it:

- Processes all **Pending** queue items (generates embeddings).
- Runs cleanup of old completed/failed items according to the retention setting. */}

## Scheduler

Training runs in the background with the TYPO3 **Scheduler** (the TYPO3 tool that runs tasks automatically at set times).

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrakildl0wh8qmhx97rf9642?utm_source=link" loading="lazy" title="Scheduler Feature Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

- Each website has one task called **T3CS Training (Site N)**. N is the page ID of your website's start page.
- AI Search creates this task for you when you save your first data source.
- To start training right away, click **Run All** on the Dashboard or **Run Task Now** in the Training Center.

When the task runs, it:

1. Reads the sources again that you marked with **Sync**.
2. Trains all new content (status **Pending**).
3. Deletes old **Failed** items after the number of days in **Retention Days**. Trained content is kept.

<Note>
**Sync** only marks content to be read again. The AI learns it when the training task runs.
</Note>

<Warning>
The Scheduler only runs if your server starts it regularly (a "cron job"). Ask your administrator or hosting provider if training never runs.
</Warning>

{/* SUPADEMO NEEDED: Scheduler task T3CS Training (Site N) */}

<a id="t3as-history-cleanup"></a>

**Delete old visitor history automatically**

You can delete old search history (what visitors searched) after a number of days.

1. Go to the **Scheduler** module.
2. Create a new task and choose **Execute console commands**.
3. Choose `t3af:history:cleanup`.
4. Enter the number of **days** to keep (default: 90).
5. Set how often it runs on the **Timing** tab.
6. Save.

![Scheduler task t3af:history:cleanup with days argument set to 3](../images/t3af-history-cleanup.webp)

**Related:** [Data Source](/en/latest/ExtNsT3AS/Configuration/DataSource/Index) · [Scheduler & CLI in AI Foundation](/en/latest/ExtNsT3AF/Configuration/Index#scheduler-and-cli)

{/* **T3AF Training** is the shared console command `nst3af:training` (AI Foundation / T3CS). It powers automatic indexing for **AI Search (T3AS)**.

When you create a data source, T3AS will automatically create the **T3AF Training** Scheduler task for this site (if it does not exist yet) and **run it at the frequency you set** (e.g. Hourly, Daily, Weekly). You do not need to create the scheduler task manually—it is created when the source is saved and will execute according to the chosen sync interval.

From the Dashboard you can open the TYPO3 Scheduler and locate the automatic training task (typically named **T3AF Training** for this site). Use **Run All** or **Run Task Now** to process the training queue immediately. */}

{/* When the scheduler runs this task for a site, it:

1. **Syncs** enabled data sources for that site (crawl or refresh content into the **training queue**).
2. **Trains** pending queue items (chunks content and **generates embeddings** via your configured AI provider or T3Planet Credits).
3. **Cleans up** old completed/failed queue rows according to the retention setting (optional archive to CSV).

<Note>
**Sync** in the Data Sources UI only marks content for refresh. It does **not** call the AI or create embeddings by itself. Embeddings are created when **T3AF Training** runs (scheduler, CLI, or **Training Center** actions that trigger the same pipeline).
</Note> */}

## Training settings

How content is split, embedded and cached is set on the shared **Training** card (**AI Universe → AI Foundation → AI Features → Training**, badge **AI Chatbot/Search**). The card is shared: the same values apply to AI Chatbot and AI Search. Most websites can keep the defaults. Click **Configure** on the card to open the settings drawer, change a value and click **Save**.

![AI Foundation, AI Features: Training drawer with chunk size, batch size, retention, embedding cache, repeated blocks, query analysis time limit and AI Search result list](../images/training-settings-drawer.webp)

The same settings are also described for [AI Chatbot](/en/latest/ExtNsT3AC/FeatureGuide/TrainingCenter/Index#training-settings).

### Training options explained {#retrieval-options}

**Chunk Size** – default: `1000`

How many records are read from the database at a time while the content is prepared for training. When to change: lower it if the training stops because the server runs out of memory; raise it on strong servers to train large sites faster.

**Batch Size** – default: `100`

How many items are sent to the AI provider in one request when the embeddings are created. Also used by the `--batch-size` option of the training command. When to change: lower it if your AI provider reports rate limits or time-outs; raise it to train faster when your provider allows larger requests.

**Retention Days** – default: `30`

After how many days old **Failed** queue items are archived (CSV in `var/log/t3cs`) or deleted by the cleanup step. Completed (trained) items are always kept. When to change: raise it if you want to look into failed items for longer; lower it to keep the queue table small.

**Embedding cache lifetime (seconds)** – default: `2592000` (30 days)

How long the embeddings of visitor questions in search and chat are cached. A question that was asked before is answered without a new embedding call, which is faster and saves AI credits. When to change: lower it if you often switch the embedding provider or model; shorter values mean more AI calls.

**Repeated blocks** – default: `0.5` (allowed `0.2`–`0.9`)

Removes text that repeats on many pages, such as promo banners, "shop the video" boxes, call-to-action boxes or legal notes. Such a block is kept once instead of on every page, so it does not push real content out of answers. A block counts as repeated when it appears on more than this share of the pages – across the whole site or within one URL folder (for example all `/products/` pages). Empty or invalid values use `0.5`.

- Lower (for example `0.3`) – removes more repeated text.
- Higher (for example `0.7`) – keeps content that is shared on purpose, for example the same product card in several collections.

When to change: lower it if answers keep quoting banners; raise it if shared content is missing in answers. It applies at the next sync, so run **Sync** and the training afterwards.

**Query analysis time limit** – default: `4` seconds

Follow-up questions (for example "and how much is it?") are turned into a standalone search query with a short AI call. This setting is how long that call may take. If it takes longer, the question is searched as typed, so a slow AI service cannot block the answer. `0` uses the time limit of the AI provider. When to change: raise it if your AI provider is often slow and follow-up answers miss; lower it if answers must start faster.

**AI Search (result list)** – default: on

AI Search shows a numbered result list – one entry per page, with highlighted snippets – before the AI summary. The summary refers to these entries. Switch it off to show only the AI summary. It does not affect the chatbot.

<Accordion title="All training settings and their defaults">

| Setting | Default | What it does |
|---|---|---|
| Chunk Size | 1000 | How many records are read from the database at a time. Lower it if your server runs out of memory. |
| Batch Size | 100 | How many items are sent to the AI provider in one go. |
| Retention Days | 30 | After how many days old **Failed** queue items are archived or deleted. Completed (trained) items are kept. |
| Embedding cache lifetime | 2592000 | How long (in seconds) search and chat questions are cached. 2592000 = 30 days. |
| Repeated blocks | 0.5 | A block (banner, shared box) that appears on more than this share of a site's pages or of one URL folder is removed from the pages and kept once (0.2–0.9). Applies at the next sync. |
| Query analysis time limit | 4 | Seconds (0 = provider default). If the AI call for a follow-up question takes longer, the question is searched as typed. |
| AI Search (result list) | on | AI Search shows a numbered result list (one entry per page, with highlighted snippets) before the AI summary. |
| Maximum Requests per Minute | 10 | **Rate Limiting** card. How many search or chat requests one visitor may send per minute. |
| Suspicious Pattern Threshold | 3 | **Rate Limiting** card. How many suspicious requests are allowed before a visitor is blocked. |
| Cache Lifetime (seconds) | 60 | **Rate Limiting** card. How long the rate limit counter is kept. |
| Maximum Links to Crawl | 30 | **Rate Limiting** card. How many links are read per sitemap or web page source in one run. |

</Accordion>

### Command line {#command-line}

The same commands are described for [AI Chatbot](/en/latest/ExtNsT3AC/FeatureGuide/TrainingCenter/Index#command-line).

<Accordion title="For developers: run training on the command line">
You can start the training yourself on the command line instead of waiting for the Scheduler, for example to test it or to train everything again. The commands come from the shared AI Chatbot/Search core and work the same for AI Chatbot and AI Search.

Run them with `vendor/bin/typo3` (Composer), `php typo3/sysext/core/bin/typo3` (non-Composer) or `ddev typo3` (DDEV).

**Training – `nst3af:training [rootPageId]`**

Syncs the data sources of a site, trains all **Pending** items (creates the embeddings) and cleans up old **Failed** items. `rootPageId` is the ID of the site root page. The aliases `t3cs:training` and `aiuniverse:training` run the same command.

| Option | What it does |
|---|---|
| `--source=ID` | Only process the data source with this ID. |
| `--detailed` | Show each page URL or file while it is processed. |
| `--dry-run` | Show what would happen; no AI calls, no database changes. |
| `--limit=N` | Process at most N items per data source (default: all). |
| `--batch-size=N` | Items sent to the AI provider in one go (default: **Batch Size** setting or 100). |
| `--queue-failed` | Put **Failed** items back to **Pending** before training. |
| `-f`, `--force` | Train everything again (Completed, Failed and Processing items go back to Pending). |
| `--skip-cleanup` | Train without the cleanup step. |
| `--cleanup-only` | Only run the cleanup, no training. |
| `--retention-days=N` | Archive/delete **Failed** items older than N days (default: **Retention Days** setting or 30). Completed items are kept. |
| `--no-archive` | Delete old items without writing a CSV archive first. |
| `--optimize-db` | Run `OPTIMIZE TABLE` after the cleanup. |

```bash
# Composer
vendor/bin/typo3 nst3af:training 1 --detailed
# Non-Composer
php typo3/sysext/core/bin/typo3 nst3af:training 1 --detailed
# DDEV: test first, then train only data source 5 again
ddev typo3 nst3af:training 1 --dry-run
ddev typo3 nst3af:training 1 --source=5 --force
```

**Run the Scheduler task – `scheduler:run --task=<taskUid> -f`**

Runs the site's **T3CS Training (Site N)** task directly, with the options saved on the task. The task UID is shown in the Scheduler module.

```bash
vendor/bin/typo3 scheduler:run --task=12 -f
```

**Compound words – `t3cs:keyword:compounds`**

Adds the parts of compound words (for example "Sonnen" and "schutz" from "Sonnenschutz") to the keyword index of already trained content, so the keyword search also finds the single words. No AI calls, no new embeddings. Run it after a training on sites with compound words, for example German.

| Option | What it does |
|---|---|
| `-s`, `--site=ID` | Only this site root page (default: every site with indexed content). |
| `--dry-run` | Count and show examples, write nothing. |
| `--show=N` | Number of examples to print (default 10). |

```bash
vendor/bin/typo3 t3cs:keyword:compounds --site=1 --dry-run
vendor/bin/typo3 t3cs:keyword:compounds --site=1
```

See all options with `vendor/bin/typo3 nst3af:training --help`.
</Accordion>

<Accordion title="For developers: run history cleanup on the command line">
`t3af:history:cleanup [days]` deletes AI Search and AI Chatbot usage history (visitor searches, conversations) and request traces older than `days` (default 90). It is separate from the training cleanup. The alias `t3cs:history:cleanup` runs the same command. You can also add it as a Scheduler task (**Execute console commands**).

```bash
vendor/bin/typo3 t3af:history:cleanup
ddev typo3 t3af:history:cleanup 90
```
</Accordion>


