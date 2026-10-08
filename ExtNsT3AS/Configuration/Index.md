---
title: "Configuration"
description: "Set up AI Search step by step: AI Features, Dashboard, Data Source, Training Center, Search settings, External Embed, analytics, permissions and more."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "Configuration"
  - "Data Source"
  - "Training Center"
sidebarTitle: "Configuration"
---

Set up AI Search step by step: add your content, let the AI learn it, and choose how the search box looks on your website.

All AI Search settings are in the TYPO3 backend under **AI Universe → AI Chatbot/Search**. Before you start, connect an AI provider in AI Foundation (see [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)).

**The basic idea in 4 steps**

1. **Add content** – tell AI Search which pages, PDFs or texts it may use ([Data Source](/en/latest/ExtNsT3AS/Configuration/DataSource/Index)).
2. **Train** – AI Search reads the content and prepares it for searching ([Training Center](/en/latest/ExtNsT3AS/Configuration/TrainingCenter/Index)).
3. **Switch on the search** – turn on AI Search and style the search box ([Search tab](/en/latest/ExtNsT3AS/Configuration/Search/Index)).
4. **Check the results** – see what visitors searched ([Usage Analytics](/en/latest/ExtNsT3AS/Configuration/UsageAnalytics/Index)).

<Note>
AI Search and AI Chatbot share the same backend module. Content you add and train once is used by both.
</Note>

**Follow the pages in this order.** Pages 1–5 are the basic setup. The others are optional or for later.

<CardGroup cols={2}>
  <Card title="1. AI Features & Prompts" icon="sparkles" href="/en/latest/ExtNsT3AS/Configuration/AIFeatures/Index">
    Shared settings in AI Foundation and the tone of the answers.
  </Card>
  <Card title="2. Dashboard" icon="layout-dashboard" href="/en/latest/ExtNsT3AS/Configuration/Dashboard/Index">
    Check at a glance if everything is set up and working.
  </Card>
  <Card title="3. Data Source" icon="database" href="/en/latest/ExtNsT3AS/Configuration/DataSource/Index">
    Add pages, PDFs, Q&A and text. Use source groups per page.
  </Card>
  <Card title="4. Training Center & Scheduler" icon="graduation-cap" href="/en/latest/ExtNsT3AS/Configuration/TrainingCenter/Index">
    Watch the training and let the Scheduler run it automatically.
  </Card>
  <Card title="5. Search, Widget & Questions" icon="search" href="/en/latest/ExtNsT3AS/Configuration/Search/Index">
    Switch AI Search on, style the search box and choose the button position.
  </Card>
  <Card title="6. External Embed" icon="code" href="/en/latest/ExtNsT3AS/Configuration/ExternalEmbed/Index">
    Show AI Search on another website (+ .htaccess / CORS).
  </Card>
  <Card title="7. Solr & other search extensions" icon="server" href="/en/latest/ExtNsT3AS/Configuration/SearchExtensions/Index">
    Only if you use Solr, ke_search or indexed_search.
  </Card>
  <Card title="8. Usage Analytics" icon="chart-column" href="/en/latest/ExtNsT3AS/Configuration/UsageAnalytics/Index">
    What visitors searched and how they rated the answers.
  </Card>
  <Card title="9. AI Usage & AI Logs" icon="scroll-text" href="/en/latest/ExtNsT3AS/Configuration/AIUsageAndLogs/Index">
    How much AI was used, and error messages.
  </Card>
  <Card title="10. Permissions" icon="shield" href="/en/latest/ExtNsT3AS/Configuration/Permissions/Index">
    Who may see or change AI Search.
  </Card>
  <Card title="11. Providers & MCP Tools" icon="plug" href="/en/latest/ExtNsT3AS/Configuration/MCPTools/Index">
    The AI provider, and MCP for AI assistants.
  </Card>
  <Card title="12. Upgrading? Where your old settings moved" icon="map" href="/en/latest/ExtNsT3AS/Configuration/WhereToFindIt/Index">
    Only if you upgrade from an older version: where the old site settings are now.
  </Card>
  <Card title="13. For developers" icon="terminal" href="/en/latest/ExtNsT3AS/Configuration/ForDevelopers/Index">
    Command line, TypoScript, MCP tools and more.
  </Card>
</CardGroup>

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

T3AS uses AI Foundation for shared provider setup, model selection, prompts, and core AI services.
Complete the parent setup first, then review the T3AS-specific search and training settings below.

Helpful AI Foundation references:

For the shared module overview, see [AI Foundation AI Features ](/en/latest/ExtNsT3AF/Configuration/AIFeatures/Index).

## AI Search Features

T3AS focuses on AI search, training, and answer delivery on top of the shared AI Foundation setup.
Use these features when you want to connect project content to AI search, control answer behavior, and monitor how search performs after rollout.

Key T3AS capabilities include:

- Search and answer generation based on trained project content
- Data source syncing and training queue management
- Scheduler-based background processing
- Usage analytics, logs, and request statistics
- Prompt-controlled search answers and instructions

For shared model routing and central AI behavior, see [AI Foundation AI Features ](/en/latest/ExtNsT3AF/Configuration/AIFeatures/Index).

The Dashboard gives an overview of your AI training pipeline for the current site.

Add and manage the sources of content that will be used for AI search, such as website pages, PDFs, and Q&A records.

**Editing or deleting a source**

Use the actions next to each data source to **edit** (type, URLs, interval, usage) or **delete** it.

### Source Groups | Page-Level Source Configuration

Source Groups allow administrators and editors to organize data sources and control which content is available to AI Search and the AI Chatbot on a page-by-page basis.
This gives you precise control over retrieval because only the selected Source Groups are considered for that page.

Source Groups are used only during content retrieval.
They do **not** affect AI training, vector indexing, Scheduler execution, embedding generation, or data synchronization.
The filtering is applied by the **VectorService** during retrieval.

#### Backend Configuration

#### Manage Source Groups

Go to **Data Sources -> Source Groups** to manage Source Groups.
Administrators can:

- create Source Groups
- edit Source Groups
- delete Source Groups

*Create, edit, or delete Source Groups. The **Global** group is a system default and cannot be changed.*

<Note>
The **Global** Source Group is a system group and cannot be edited or deleted.
</Note>

#### Assign Source Groups to Data Sources

When creating or editing a data source, users can:

- select one or more Source Groups
- rely on the **Global** Source Group, which is assigned automatically
- configure the **Used by** field (formerly **Type**) to control where the source is available

Available **Used by** options:

This setting controls where the data source can be used after retrieval starts.

#### Page-Level Configuration (T3AS / T3AC)

Only data sources assigned to the selected Source Groups are used on that page and their child/recursive pages.
This filtering applies to both **AI Search** and **AI Chatbot**, and different pages can use different Source Groups.

#### Practical Example

A company has separate documentation for **Products**, **HR**, and **Internal Policies**.

Three Source Groups are created:

- **Products**
- **HR**
- **Internal**

On product pages, only the **Products** Source Group is selected, so AI Search and AI Chatbot return product-related information.
On HR pages, only the **HR** Source Group is selected, so HR content is used while product information is excluded.

<Note>
Source Groups only affect content retrieval. Existing training data, embeddings, vector indexing, and scheduled synchronization continue to operate normally.
</Note>

<Note>
If no custom Source Groups are selected, the **Global** Source Group remains available according to the configured behavior.
</Note>

#### Header / Footer for Sitemap and Web-Page Source Types

These options help you keep repeated layout content out of the main page body while still making shared site information available to AI retrieval.

*Enable **Index site header** and **Index site footer** when adding or editing a Sitemap XML or Web Pages data source.*

Use **Index Site Header** when the site header contains useful shared information that should be indexed only once.

Purpose:

- extract the website `<header>` content one time for each unique header
- store that content as a separate training item
- remove the same header content from the page body before indexing

Benefits:

- reduces duplicate information across many pages
- keeps repeated navigation or shared header text from being indexed over and over
- preserves useful shared site information for retrieval

When to enable:

- when the header contains meaningful text that supports AI answers
- when many pages share the same header content

Recommended use cases:

- websites with shared product navigation or service overviews in the header
- websites where the header contains reusable company or category information

Use **Index Site Footer** when the site footer contains shared information that should be indexed only once.

Purpose:

- extract the website `<footer>` content one time for each unique footer
- store that content as a separate training item
- exclude that footer content from the page body during indexing

Benefits:

- prevents duplicate footer text from being trained again on every page
- keeps the main page content cleaner for retrieval
- preserves useful global site information such as company details or support links

When to enable:

- when the footer contains helpful shared text for search or chatbot answers
- when the same footer appears on many pages

Recommended use cases:

- websites with shared contact details, policy references, or company summaries in the footer
- large sites where repeated footer content would otherwise be indexed many times

<Note>
Enable **Index Site Header** and/or **Index Site Footer** in the data source form when creating or editing a **Sitemap XML** or **Web Pages** source.
</Note>

<Warning>
Deleting a data source also removes its training queue and embedded data for that source.
</Warning>

### Command `nst3af:training` — all options

You can run the same command manually from the project root (for example with DDEV). Replace `<rootPageId>` with your site root page ID and `<taskUid>` with the numeric UID from the Scheduler module (do **not** assume a fixed ID such as `9`).

**Argument**

`rootPageId` (optional when using `scheduler:run --task=`)
   Site root page ID. Required for direct CLI runs unless the scheduler passes it via the task.

**Options**

`--source=ID`
   Process only one data source (must belong to the site).

`--detailed`
   Verbose output (each URL, PDF, and similar). **Enabled by default** on the automatic scheduler task. It will show the detailed progress in the CLI command.

`--dry-run`
   Preview only — no API calls and no database updates.

`--limit=N`
   Process at most *N* queue items per data source.

`--batch-size=N`
   Embedding batch size (default: extension **Batch size** or 100). **Set on the scheduler task** from extension settings when the task is created or updated.

`--skip-cleanup`
   Skip the post-training cleanup phase.

`--cleanup-only`
   Run cleanup only (no sync, no embedding).

`--optimize-db`
   Run `OPTIMIZE TABLE` after cleanup.

`--queue-failed`
   Move **Failed** queue items back to **Pending** before processing.

`--force` / `-f`
   Re-train all: set all queue items (completed/failed/processing) back to **Pending** and process.

   It does **not** automatically set `sync_requested`. Sync still requires the **Sync** action from the DataSource tab.

**What the automatic scheduler task uses**

Only `rootPageId`, `--batch-size`, `--retention-days`, and `--detailed`. All other options are for **manual CLI** or custom scheduler tasks you create yourself.

**Example commands**

Composer / TYPO3 v13+ (typical):

Legacy non-Composer installs may use `scheduler:execute` instead of `scheduler:run`; see the [TYPO3 Scheduler CLI documentation](https://docs.typo3.org/c/typo3/cms-scheduler/13.4/en-us/Administration/ConsoleTools/Running.html).

*Example of scheduler task output in the terminal.*

*Example showing queue processing and training completion summary.*

### Command `t3af:history:cleanup` — history log cleanup

**T3AF History Cleanup** is the shared console command `t3af:history:cleanup` (AI Foundation / T3CS). It deletes **AI Search** and **Chatbot** usage history older than the retention period.

This is separate from training-queue cleanup (`--retention-days` on `nst3af:training`). Use it to keep **Usage Analytics** history within a privacy or storage limit.

1. Create a new task and select **Execute console commands**.
2. Choose `t3af:history:cleanup`.
3. Set the **days** argument and the frequency on the **Timing** tab.
4. Save the task.

**Argument**

`days`
   Retention in days before deletion. Edit this argument on the scheduler task. Default is `90` when omitted.

**Example commands**

Composer / TYPO3 v13+ (typical):

```bash
ddev typo3 t3af:history:cleanup
ddev typo3 t3af:history:cleanup 3
ddev typo3 t3af:history:cleanup 90
```

The first command uses the default of **90** days. Setting `days` to `3` deletes usage history older than 3 days (CLI: `t3af:history:cleanup 3`).

*Configure **days** on the `t3af:history:cleanup` scheduler task. Default retention is 90 days when the argument is omitted.*

More options for other AI Foundation scheduler commands (MCP cleanup, and so on) are listed under **AI Foundation → Scheduler & CLI** in the TYPO3 backend.

View the training queue (items collected from all data sources) and control training and cleanup.

Queue item statuses:

- **Pending** – Waiting to be processed.
- **Processing / Embedding** – Currently being sent to the embeddings service.
- **Completed** – Successfully trained.
- **Failed** – Error during training.

**Actions**

Refreshes content from the data source into the queue (same as in the **Data Source** tab).

**Reset (Re-queue)**

Puts a **failed** or **completed** item back to **Pending** so it will be processed again on the next training run.

<Warning>
Deleted items will not be trained again unless they are added again by a new sync.
</Warning>

**Training behaviour (simple terms)**

- Only items in status **Pending** are processed when training runs.
- **Processing** means: the text is sent to the configured embeddings service, and the result is stored for search usage.
- After success, the item is marked **Completed**; on error, **Failed**.
- How often training runs depends on the Sync interval of your data sources and on the Scheduler actually being triggered (e.g. via cron).

## 5. Search tab
The **Search** tab controls AI search for the whole site. Here you turn search on, set how answers look, enable **Save search history**, style the widget, and manage suggested questions. Settings on a single page plugin can override these defaults.

Turn AI search on and control answer behaviour.

Set up clickable question suggestions in the search box.

The **Usage Analytics** tab records visitor search activity. You can see what was searched, what answer was given, feedback ratings, and reference links used.

Each row in the log list shows:

- **Search term** — What the visitor typed
- **AI answer** — Short summary of the result
- **Module** — e.g. **Search**
- **Feedback** — Thumbs up or down (when **Search Feedback** is enabled)
- **Reference links** — Number of source links shown
- **Page, language, time** — Where and when the search happened

**Open a log entry**

Click a row to see the full detail:

- **Negative feedback** and any visitor comment
- **Search badge** — Click to filter logs by that search term
- **Reference sources** — Pages or files used to build the answer
- **All messages** — Full chat history (when **Chatbot Mode** is on)
- **Delete This Log** — Remove a single entry

**Filter and export**

- **Search queries or responses** — Find text in the logs
- **All Modules** — Filter by module (e.g. Search only)
- **All Languages** — Filter by language
- **Export** — Download log data as a file

<Note>
Enable **Save search history** in **Search → Settings** so visitor queries and answers appear in this log.
Enable **Search Feedback** in **Search → Settings** or in the plugin **Search Results** tab to collect thumbs up/down ratings.
To delete old usage history automatically, use the `t3af:history:cleanup` scheduler task (see **Scheduler** on this page). Default retention is **90** days.
</Note>

Use AI Prompts to control how T3AS writes answers, summaries, and search-related responses.
This is useful when you want search output to follow a consistent tone, answer style, or instruction set across the whole site.

Best practices:

T3AS uses AI Foundation for shared provider setup and MCP-based integrations.
Review this area when you need to confirm that the correct provider, model, and MCP capabilities are available for search and training workflows.

See also:

When configuring T3AS with **ke_search** or **indexed_search**, ensure the website is fully indexed and the training scheduler has run. Full steps: [Injecting AI Search result in TYPO3 Search Extensions](/en/latest/ExtNsT3AS/InjectingAISearchResults/Index).

Show the T3AS AI overview together with **ke_search**, **indexed_search**, or **Solr** by setting **Search Class** and adding a Fluid injection snippet.

Full guide: [Injecting AI Search result in TYPO3 Search Extensions](/en/latest/ExtNsT3AS/InjectingAISearchResults/Index).

To render the standalone AI Search plugin via TypoScript, see [Enable AI Search plugin using TypoScript](/en/latest/ExtNsT3AS/InjectingAISearchResults/Index#enable-ai-search-plugin-using-typoscript).
*/}
