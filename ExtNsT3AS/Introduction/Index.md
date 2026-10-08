---
title: "T3AS - TYPO3 AI Search Extension"
description: "**T3AS (TYPO3 AI Search)** adds AI-powered search to your TYPO3 website. It works with your existing search setup — site content, Solr, ke_search, or indexed_search — and returns direct answers based on your trained data."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "T3AS - TYPO3 AI Search Extension"
sidebarTitle: "T3AS - TYPO3 AI Search Extension"
---

## EXT:ns_t3as

![Extension Banner](images/T3AS.webp)

**AI Search** gives your website a search box that answers questions. Visitors type a question in their own words and get a short, clear answer from your own website content, with links to the pages it comes from.

Use it when visitors struggle to find information with a normal search, for example on large websites, help pages or product catalogues.

### Key Features

- **Ask in normal words** – visitors type a question, not just keywords.
- **Answers from your content** – the AI only uses the pages, PDFs and texts you choose.
- **Follow-up questions** – visitors can keep asking, like in a chat (**Chatbot Mode**).
- **Feedback** – visitors rate answers with thumbs up or down.
- **Listen to answers** – answers can be read aloud (**Voiceover**).
- **Example questions** – clickable questions in the search box.
- **Works with your current search** – can also show AI answers in ke_search, indexed_search or Solr.

### Feature overview

Everything AI Search can do, and where to read more. In the TYPO3 backend you find AI Search under **AI Universe → AI Chatbot/Search**.

**Add and train your content**

- [Data sources](/en/latest/ExtNsT3AS/Configuration/DataSource/Index) – choose the content the AI may use (pages, sitemap, PDFs, questions and answers, text).
- [Source groups](/en/latest/ExtNsT3AS/Configuration/DataSource/Index#source-groups) – choose which content is used on which page.
- [Training and Scheduler](/en/latest/ExtNsT3AS/Configuration/TrainingCenter/Index#scheduler) – the AI learns your content automatically in the background.
- [Training Center](/en/latest/ExtNsT3AS/Configuration/TrainingCenter/Index) – see what was learned and fix failed items.
- [Dashboard](/en/latest/ExtNsT3AS/Configuration/Dashboard/Index) – everything at a glance.

**Set up the search**

- [Search settings](/en/latest/ExtNsT3AS/Configuration/Search/Index) – switch AI Search on and choose the answer style.
- [Search widget](/en/latest/ExtNsT3AS/Configuration/Search/Index#search-widget) – the look of the search box and button.
- [Change the widget position](/en/latest/ExtNsT3AS/Configuration/Search/Index#search-widget-position) – move the search button to another corner or side, for desktop and mobile (**Search → Widget**).
- [Example questions](/en/latest/ExtNsT3AS/Configuration/Search/Index#search-questions) – clickable questions for visitors.
- [External Embed](/en/latest/ExtNsT3AS/Configuration/ExternalEmbed/Index) – show AI Search on another website.
- [AI Search plugin](/en/latest/ExtNsT3AS/FrontendPlugin/Index) – a search box on one page, with its own settings.
- [AI answers in other search extensions](/en/latest/ExtNsT3AS/InjectingAISearchResults/Index) – an AI answer above ke_search, indexed_search or Solr results.

**Measure and control**

- [Usage Analytics](/en/latest/ExtNsT3AS/Configuration/UsageAnalytics/Index) – what visitors searched and how they rated the answers.
- [AI Usage and AI Logs](/en/latest/ExtNsT3AS/Configuration/AIUsageAndLogs/Index) – how much AI was used, and error messages.
- [AI Prompts](/en/latest/ExtNsT3AS/Configuration/AIFeatures/Index#ai-prompts) – the tone and style of the answers.
- [MCP tools](/en/latest/ExtNsT3AS/Configuration/MCPTools/Index) – for teams that work with AI assistants.
- [Permissions](/en/latest/ExtNsT3AS/Configuration/Permissions/Index) – who may change AI Search.
- [Privacy (DPA & GDPR)](/en/latest/ExtNsT3AS/DPAandGDPR/Index) – what is stored and how to turn it off.

<Note>
AI Search and [AI Chatbot](/en/latest/ExtNsT3AC/Introduction/Index) share the same backend module. Content you train once is used by both. The connection to your AI provider is set up in [AI Foundation](/en/latest/ExtNsT3AF/Introduction/Index).
</Note>

**Coming from an older version?** Some settings have moved. See [Upgrading? Where your old settings moved](/en/latest/ExtNsT3AS/Configuration/WhereToFindIt/Index)

{/* ### System Requirements

- TYPO3 v12 – v13
- PHP v8.2 – v8.4

**Required extensions:**

- EXT:backend
- EXT:filelist
- EXT:ns_t3af
- EXT:ns_t3cs
- EXT:fluid
- EXT:scheduler
- EXT:ns_license

See also:

- [T3AF System Requirements](/en/latest/ExtNsT3AF/Installation/Index#ns-t3af-system-requirements)
- [T3AF Installation](/en/latest/ExtNsT3AF/Installation/Index) */}

### System Requirements

- TYPO3 v12, v13 or v14
- PHP 8.2 – 8.5

**What else you need**

These are installed for you with Composer. Without Composer, install them from the T3Planet Shop or the Extension Manager.

- **AI Foundation** (`ns_t3af`) – connects TYPO3 to your AI provider.
- **AI Chatbot/Search base** (`ns_t3cs`) – the shared backend module.
- **License Manager** (`ns_license`) – activates your license.
- **Scheduler** – TYPO3's tool for background tasks; it runs the training.

See also: [AI Foundation installation](/en/latest/ExtNsT3AF/Installation/Index).

<a id="typo3-versions"></a>

{/* - TYPO3 v12.4 – v14
- PHP 8.2 – 8.5 */}

### TYPO3 v12, v13 and v14

<Note>
AI Search works the same on **TYPO3 v12, v13 and v14** (12.4 LTS, 13.4 LTS, 14.3 or newer). Only some menu names differ: on TYPO3 v14, **Admin Tools** is called **System**, the site configuration is under **Sites → Setup**, and the page module is **Content → Layout**. On TYPO3 v12 you load the settings with static templates; on v13 and v14 you can use a site set. See [Installation, Step 5](/en/latest/ExtNsT3AS/Installation/Index#load-typoscript).
</Note>

<Accordion title="All menu names per TYPO3 version">

| What | TYPO3 v12 | TYPO3 v13 | TYPO3 v14 |
|---|---|---|---|
| AI Search backend module | **AI Universe → AI Chatbot/Search** | **AI Universe → AI Chatbot/Search** | **AI Universe → AI Chatbot/Search** |
| T3Planet Shop, Extensions, Maintenance, Upgrade | **Admin Tools** | **Admin Tools** | **System** |
| Site configuration | **Site Management → Sites** | **Site Management → Sites** | **Sites → Setup** |
| TypoScript module | **Site Management → TypoScript** | **Site Management → TypoScript** | **Sites → TypoScript** |
| Load the TypoScript | Static templates | Site set (recommended) or static templates | Site set (recommended) or static templates |
| Page module | **Web → Page** | **Web → Page** | **Content → Layout** |
| Scheduler | **System → Scheduler** | **System → Scheduler** | **Administration → Scheduler** |
| Plugin page ID (**Plugin PID**) | TypoScript constant | **Edit site settings → Ns AI Search** (with the site set) or TypoScript constant | Same as v13 |
| AI Search plugin | Plugin content element | Own content type (TYPO3 13.4) | Own content type |

</Accordion>

## Helpful Links

<Note>
- Product Page: [https://t3planet.de/t3as-typo3-erweiterung](https://t3planet.de/t3as-typo3-erweiterung)
- Support Portal: [https://t3planet.de/support](https://t3planet.de/support)
</Note>

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

**T3AS (TYPO3 AI Search)** adds AI-powered search to your TYPO3 website. It works with your existing search setup — site content, Solr, ke_search, or indexed_search — and returns direct answers based on your trained data.

T3AS now works as a child extension of T3AF (`ns_t3af`), which provides the shared AI providers, authentication, common configuration, and core AI services used by the extension.

Instead of only showing a list of links, visitors get a clear answer with optional source references.

- **Natural language search** — Visitors can ask questions in everyday language
- **Answers from your content** — AI uses your trained pages, PDFs, and other sources
- **Easy setup** — Install, add data sources, train, and place the search plugin on a page
- **Chatbot mode** — Follow-up questions after the first answer
- **Search feedback** — Thumbs up/down ratings, visible in **Usage Analytics**
- **Voiceover** — Listen to answers read aloud
- **Result styles** — Short summaries or longer detailed answers
- **Predefined questions** — Clickable suggestions in the search box
*/}
