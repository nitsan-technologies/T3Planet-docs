---
title: "T3AC - TYPO3 AI Chatbot Extension"
description: "T3AC adds an AI-powered chatbot to TYPO3 so teams can answer user questions with trained project data. It supports chatbot configuration, training, data sources, usage tracking, and embedded chatbot delivery for supported websites."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AC"
  - "T3AC - TYPO3 AI Chatbot Extension"
sidebarTitle: "T3AC - TYPO3 AI Chatbot Extension"
---

## EXT:ns_t3ac

![Extension Banner](./images/AC.webp)

**AI Chatbot** adds a chat window to your website. Visitors ask questions in their own words and get answers from your own website content, any time of day.

Use it to answer common visitor questions automatically, for example about products, opening hours, services or support topics.

### Key Features

- **Answers from your content** – the chatbot only uses the pages, PDFs and texts you choose.
- **Your look** – your logo, colours, welcome text and position on the screen.
- **Quick replies** – up to 5 buttons with prepared answers under the welcome message (no AI needed).
- **Source links** – links to the pages an answer came from.
- **Many languages** – chatbot texts for each website language.
- **Feedback and statistics** – see what visitors asked and how they rated the answers.

### Feature overview

Everything AI Chatbot can do, and where to read more. In the TYPO3 backend you find AI Chatbot under **AI Universe → AI Chatbot/Search**.

**Add and train your content**

- [Data sources](/en/latest/ExtNsT3AC/FeatureGuide/DataSource/Index#adding-a-data-source) – choose the content the chatbot learns from (Sitemap XML, PDF Documents, TYPO3 Pages, Web Pages, Q&A Pairs, Text and, if installed, Indexed Search, ke_search or Solr).
- [Source groups](/en/latest/ExtNsT3AC/FeatureGuide/DataSource/Index#source-groups) – choose which content is used on which page.
- [Training and Scheduler](/en/latest/ExtNsT3AC/FeatureGuide/DataSource/Index#scheduler) – the chatbot learns your content automatically in the background.
- [Training Center](/en/latest/ExtNsT3AC/FeatureGuide/TrainingCenter/Index) – see what was learned and fix failed items.
- [Dashboard](/en/latest/ExtNsT3AC/FeatureGuide/Dashboard/Index) – everything at a glance. **Run All** starts the training.

**Set up the chatbot**

- [Chatbot settings](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#configuration) – switch the chatbot on, set the title, welcome messages and instructions.
- [Email transcript](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#email-transcript) – visitors can email themselves a copy of the chat.
- [Logo, avatar and colours](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#customization) – change how the chatbot looks.
- [Page visibility](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#page-visibility) – show or hide the chatbot on chosen pages.
- [Hide the chatbot on a page](/en/latest/ExtNsT3AC/Configuration/DisableChatbotOnPage/Index) – a switch in the page properties.
- [Source links](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#sources-links) – links to the pages an answer came from.
- [Quick replies](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#quick-replies) – up to 5 buttons under the welcome message with prepared answers (no AI needed). Set them on **Chatbot → General**.
- [Change the widget position](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#widget-position) – move the chat button to another corner or side, for desktop and mobile (**Chatbot → General → Chatbot Position**).
- [Custom CSS](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#custom-styling) – your own design for the chatbot.
- [External Embed](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#external-embed) – show the chatbot on another website (your developer needs to allow it, see [Step 4](/en/latest/ExtNsT3AC/Configuration/ExternalEmbed/Index)).
- [Multilanguage](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#multilanguage) – chatbot texts for each website language.

**Measure and control**

- [Usage Analytics](/en/latest/ExtNsT3AC/FeatureGuide/UsageAnalytics/Index) – visitor conversations and their feedback.
- [AI Usage and AI Logs](/en/latest/ExtNsT3AF/Configuration/AIUsageAndLogs/Index) – how much AI was used, and error messages (in AI Foundation).
- [AI Prompts](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#ai-prompts) – the tone and style of the answers.
- [MCP tools](/en/latest/ExtNsT3AC/Configuration/MCPTools/Index) – for teams that work with AI assistants.
- [Permissions](/en/latest/ExtNsT3AC/Configuration/Permissions/Index) – who may change AI Chatbot.
- [Privacy (DPA & GDPR)](/en/latest/ExtNsT3AC/DPAandGDPR/Index) – what is stored and how to turn it off.

<Note>
AI Chatbot and [AI Search](/en/latest/ExtNsT3AS/Introduction/Index) share the same backend module. **Dashboard**, **Data Source**, **Training Center** and **Usage Analytics** are shared, so content you train once is used by both. The connection to your AI provider is set up in [AI Foundation](/en/latest/ExtNsT3AF/Introduction/Index).
</Note>

**Coming from an older version?** Some settings have moved. See [Upgrading? Where your old settings moved](/en/latest/ExtNsT3AC/Configuration/WhereToFindIt/Index)

{/* ### System Requirements

- TYPO3 v11 - v13
- PHP v8.2 - v8.4

**Required TYPO3 Extensions:**

- EXT:backend
- EXT:filelist
- EXT:dashboard
- EXT:ns_t3af
- EXT:ns_t3cs
- EXT:fluid
- EXT:seo
- EXT:ns_license
- EXT:sitemap_locator (This extension is only required when using T3AC version 1.4.0 or earlier for sitemap crawling. It is not required in the latest versions of the extension.) */}

### System Requirements

- TYPO3 v12, v13 or v14
- PHP 8.2 – 8.5

**What else you need**

These are installed for you with Composer. Without Composer, install them from the T3Planet Shop or the Extension Manager.

- **AI Foundation** (`ns_t3af`) – connects TYPO3 to your AI provider.
- **AI Chatbot/Search base** (`ns_t3cs`, version 14.2.4 or newer) – the shared backend module.
- **License Manager** (`ns_license`) – activates your license.
- **Scheduler** – TYPO3's tool for background tasks; it runs the training.

See also: [AI Foundation installation](/en/latest/ExtNsT3AF/Installation/Index) · [AI Foundation requirements](/en/latest/ExtNsT3AF/Installation/Index#requirements)

<a id="typo3-versions"></a>

{/* - TYPO3 v12.4 – v14
- PHP 8.2 – 8.5 */}

### TYPO3 v12, v13 and v14

<Note>
AI Chatbot works the same on **TYPO3 v12, v13 and v14** (12.4 LTS, 13.4 LTS, 14.3 or newer). Only some menu names differ: on TYPO3 v14, **Admin Tools** is called **System**, the site configuration is under **Sites → Setup**, and the page module is **Content → Layout**. On TYPO3 v12 you load the settings with static templates; on v13 and v14 you can use a site set. See [Installation, Step 5](/en/latest/ExtNsT3AC/Installation/Index#load-typoscript).
</Note>

<Accordion title="All menu names per TYPO3 version">

| What | TYPO3 v12 | TYPO3 v13 | TYPO3 v14 |
|---|---|---|---|
| AI Chatbot backend module | **AI Universe → AI Chatbot/Search** | **AI Universe → AI Chatbot/Search** | **AI Universe → AI Chatbot/Search** |
| T3Planet Shop, Extensions, Maintenance, Upgrade | **Admin Tools** | **Admin Tools** | **System** |
| Site configuration | **Site Management → Sites** | **Site Management → Sites** | **Sites → Setup** |
| TypoScript module | **Site Management → TypoScript** | **Site Management → TypoScript** | **Sites → TypoScript** |
| Load the TypoScript | Static templates | Site set (recommended) or static templates | Site set (recommended) or static templates |
| Page module | **Web → Page** | **Web → Page** | **Content → Layout** |
| Scheduler | **System → Scheduler** | **System → Scheduler** | **Administration → Scheduler** |

</Accordion>

{/* - [T3AF System Requirements](/en/latest/ExtNsT3AF/Installation/Index#ns-t3af-system-requirements) */}

## Helpful Links

<Note>
- Product Page: [https://t3planet.de/t3ac-typo3-erweiterung](https://t3planet.de/t3ac-typo3-erweiterung)
- Support Portal: [https://t3planet.de/support](https://t3planet.de/support)
</Note>

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

T3AC adds an AI-powered chatbot to TYPO3 so teams can answer user questions with trained project data.
It supports chatbot configuration, training, data sources, usage tracking, and embedded chatbot delivery for supported websites.

T3AC now works as a child extension of T3AF (`ns_t3af`), which provides the shared AI providers, authentication, common configuration, and core AI services used by the extension.

For the shared setup, see:
*/}
