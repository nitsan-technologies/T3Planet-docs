---
title: "For developers"
description: "For developers: training on the command line, AI answers in other search extensions, MCP tools, page types and upgrade wizards."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "Developers"
  - "CLI"
  - "TypoScript"
sidebarTitle: "For developers"
---

Developers can run the training on the command line, show AI answers in other search extensions and connect AI tools. Most websites don't need anything on this page.

- **Start the training on the command line:** `nst3af:training <rootPageId>`. Add `--dry-run` to test or `--force` to train everything again. See all options with `typo3 nst3af:training --help`.
- **Delete old usage history:** `t3af:history:cleanup [days]` (default 90 days).
- **Show AI answers in ke_search, indexed_search or Solr:** add `lib.injectAiSearchResults` to the search template. See [AI answers in other search extensions](/en/latest/ExtNsT3AS/InjectingAISearchResults/Index).
- **Set the Plugin PID** (the page with the AI Search content element): on TYPO3 v13/v14 in **Edit site settings → Ns AI Search → Settings → Plugin PID**, on TYPO3 v12 in the TypoScript constant `plugin.tx_nst3as_aisearch.settings.pluginPid`.
- **Use MCP tools** to read or change the search settings, data sources and training queue from an AI assistant. See [Providers & MCP Tools](/en/latest/ExtNsT3AS/Configuration/MCPTools/Index).
- **Don't reuse these page types** for your own pages: `1597569645`, `1597569646`, `1597569647`, `1753285380`, `1753195737`, `1762515317`.
- **Run the upgrade wizards after an update** (**Admin Tools → Upgrade → Upgrade Wizard**, TYPO3 v14: **System → Upgrade**). Run **Migrate T3AS Search plugin to content type** before you move to TYPO3 v14.

```bash
ddev typo3 nst3af:training <rootPageId> --detailed
```

{/* ============= */}

{/* `--retention-days=N`
   Delete or archive queue rows older than *N* days (default: extension **Retention days** or 30). **Set on the scheduler task** from extension settings. */}

{/* `--no-archive`
   Delete old queue rows without writing a CSV archive first. */}

{/* ### Extension settings used by training (AI Foundation → AI Features)

These **T3CS / AI Chatbot & Search** settings are applied when the scheduler task is configured:

* **Batch size** → `--batch-size` on the task
* **Retention days** → `--retention-days` on the task
* **Chunk size**, **Max link crawl**, rate limits — affect sync and embedding behavior during the run
* **Log archive path** (optional) — where cleanup CSV archives are stored */}

{/* **Site setting / constant**

- `plugin.tx_nst3as_aisearch.settings.pluginPid` – the ID of the page that holds the AI Search content element. */}

{/* - EXT:ns_t3as: Migrate T3AS Search plugin to content type (needed for TYPO3 v14) */}

{/* Detailed developer notes (moved here on 2026-10-08 to keep the page short; not shown on the website):

<Accordion title="For developers: training command, settings, TypoScript and more">

**Training command**

The Scheduler task runs the command `nst3af:training`. You can run it yourself from the project root. Replace `<rootPageId>` with the site root page ID and `<taskUid>` with the task UID from the Scheduler module.

| Option | What it does |
|---|---|
| `rootPageId` | Site root page ID (needed for direct CLI runs) |
| `--source=ID` | Only one data source |
| `--detailed` | Verbose output (on by default in the Scheduler task) |
| `--dry-run` | Preview only, no API calls, no database changes |
| `--limit=N` | At most N queue items per data source |
| `--batch-size=N` | Embedding batch size (default: **Batch Size** setting or 100) |
| `--skip-cleanup` | Skip the cleanup after training |
| `--cleanup-only` | Only clean up |
| `--retention-days=N` | Delete or archive **Failed** rows older than N days (default: **Retention Days** or 30). Completed rows are kept. |
| `--no-archive` | Delete old Failed rows without a CSV archive |
| `--optimize-db` | Run `OPTIMIZE TABLE` after cleanup |
| `--queue-failed` | Put **Failed** items back to **Pending** first |
| `--force` / `-f` | Re-train everything. Does not set the sync flag; use **Sync** for that. |

The automatic Scheduler task only uses `rootPageId`, `--batch-size`, `--retention-days` and `--detailed`. The **Custom cron expression** sync interval accepts your own cron schedule, for example `0 0 * * 0`.

```bash
ddev typo3 scheduler:run --task=<taskUid> -f
ddev typo3 nst3af:training <rootPageId> --detailed
ddev typo3 nst3af:training <rootPageId> --dry-run
ddev typo3 nst3af:training <rootPageId> --source=5 --limit=20
ddev typo3 nst3af:training <rootPageId> --cleanup-only
```

Non-Composer installs may need `scheduler:execute` instead of `scheduler:run` ([TYPO3 Scheduler CLI](https://docs.typo3.org/c/typo3/cms-scheduler/13.4/en-us/Administration/ConsoleTools/Running.html)).

![Example command-line output for TYPO3 scheduler task run](../images/CLI01.webp)

![Example command-line output showing queue processing and training completion](../images/CLI02.webp)

**History cleanup command**

`t3af:history:cleanup [days]` deletes AI Search and Chatbot usage history older than `days` (default 90). It is separate from the training cleanup.

```bash
ddev typo3 t3af:history:cleanup
ddev typo3 t3af:history:cleanup 90
```

**Training settings** (AI Foundation → AI Features, cards **Training** and **Rate Limiting**)

| Setting | Default | What it does |
|---|---|---|
| Chunk Size | 1000 | How many records are read from the database at a time. Lower it if your server runs out of memory. |
| Batch Size | 100 | How many items are sent to the AI provider in one go. |
| Retention Days | 30 | After how many days old **Failed** queue items are archived or deleted. Completed (trained) items are kept. |
| Retrieval confidence threshold | 0.62 | How well the best match must fit (0.40–0.90) before the AI answers with your content. Higher = stricter. |
| Embedding cache lifetime | 2592000 | How long (in seconds) search and chat questions are cached. 2592000 = 30 days. |
| Retrieval shortlist size | 300 | How many likely matches are first picked by keyword search and then compared with the AI data. |
| Retrieval vector scan cap | 2000 | The maximum number of stored items compared when the keyword shortlist finds nothing useful. |
| Minimum shortlist top score | 0.55 | If the best shortlist match scores below this (0.40–0.90), a wider search runs (up to the scan cap). |
| Maximum Requests per Minute | 10 | How many search or chat requests one visitor may send per minute. |
| Suspicious Pattern Threshold | 3 | How many suspicious requests are allowed before a visitor is blocked. |
| Cache Lifetime (seconds) | 60 | How long the rate limit counter is kept. |
| Maximum Links to Crawl | 30 | How many links are read per sitemap or web page source in one run. |

The cleanup archive folder is `var/log/t3cs` (no backend field). Old Index mode **Legacy (database columns only)** reads only the page records; **Frontend** is recommended on TYPO3 13.4 and newer.

**MCP tools**

| Tool | What it does |
|---|---|
| `t3as_search_settings` | Read or change the Search settings of a site |
| `t3as_list_predefined_questions` | List the predefined questions |
| `t3cs_list_datasources` | List the data sources |
| `t3cs_save_datasource` | Create or change a data source |
| `t3cs_sync_datasource` | Mark a data source for sync |
| `t3cs_list_queue_items` | List items in the training queue |
| `t3cs_reset_failed_queue_item` | Put a failed queue item back to Pending |
| `t3cs_training_summary` | Show training queue counts |
| `t3cs_usage_analytics_summary` | Show usage analytics numbers |

**TypoScript objects**

- `lib.injectAiSearchResults` – adds the AI answer to ke_search, indexed_search or Solr result pages.
- `lib.renderAiSearchPlugin` – renders the first AI Search content element found on the search page.

**Plugin PID**

`plugin.tx_nst3as_aisearch.settings.pluginPid` – page ID of the AI Search content element. TYPO3 v13/v14 with the site set: **Edit site settings → Ns AI Search → Settings → Plugin PID**. TYPO3 v12 or static templates: TypoScript constant (**Plugin PID** in the Constant Editor).

**Page types used by AI Search**

`1597569645`, `1597569646`, `1597569647`, `1753285380`, `1753195737`, `1762515317` – do not use them for your own page types.

**Upgrade wizards** (**Admin Tools → Upgrade → Upgrade Wizard**, on TYPO3 v14 **System → Upgrade**)

- EXT:ns_t3as: Add enable voiceover setting
- EXT:ns_t3as: Add external embed settings
- EXT:ns_t3as: Add search history response time column
- EXT:ns_t3as: Add search history session fields for chatbot-mode grouping
- EXT:ns_t3as: Migrate T3AS Search plugin to content type (shown on TYPO3 13.4 and v14; run it before you move to TYPO3 v14)

**Frontend middlewares**

`AiSearchChatRateLimiterMiddleware`, `AISearchRenderMiddleware`, `SearchIframeMiddleware`, `SearchEmbedCorsMiddleware`

</Accordion>
*/}
