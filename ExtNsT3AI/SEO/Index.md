---
title: "SEO"
description: "Generate meta titles, descriptions, keywords, Open Graph data, schema markup, and slugs with T3AI, for one page or many pages at once with Mass Optimize SEO."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "SEO"
sidebarTitle: "SEO"
---

The **SEO** tab of the AI Assistant module writes and checks the search-facing data of your pages: meta title, meta description, keywords, Open Graph (social media) texts, structured data (schema), and slugs. T3AI reads the page content, suggests texts, and you choose what to save.

Settings, permissions, AI agent tools, and logs for this feature are listed in [Settings, access and logs](#settings-access-and-logs).

## T3AI SEO

### Before you start

- An AI provider is connected. See [AI provider & API keys](/en/latest/ExtNsT3AI/Configuration/AIProviders/Index).
- The SEO tools you need are enabled in the [AI SEO card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-seo). There you also set the number of suggestions per field and the default SERP view.
- The page has real content. The AI bases its suggestions on it.

### Which tool do I need?

| You want to | Use |
|---|---|
| Fill all SEO fields of one page at once | [Optimize SEO](#one-click-seo-optimization) |
| Write SEO data from a keyword and topic | [New SEO](#new-seo) |
| Improve only meta title, description, and keywords | [Optimize Meta](#optimized-meta) |
| Improve only the social media preview | [Social Meta](#social-meta) |
| See how the page looks in Google | [SERP Snippet](#serp-snippet) |
| Get feedback on the text quality | [Content Analysis](#content-analysis) |
| Get an SEO score with recommendations | [SEO Page Score](#seo-page-score) |
| Add structured data | [Schema Markup](#schema-markup) |
| Optimize many pages | [Mass SEO](/en/latest/ExtNsT3AI/MassSEO/Index) |

### How the SEO windows work

1. Select the page in the page tree. The window shows it at the top as **Path**.
2. Go to **AI Universe > AI Assistant > SEO** and click the button on the card. The same tools are in the **T3AI** button of the page properties form and in the page tree context menu.
3. Select the **AI Provider** and click **Generate AI**.
4. For each field, pick one of the suggestions or edit the text. The pencil icon next to a field opens its prompt (**Edit Meta Title Prompt**, **Edit Meta Description Prompt**, and so on).
5. Click **Save** to keep the window open, or **Save & Close**. The texts are written to the page properties (tabs **SEO** and **Social Media**).

## Mass SEO

Optimize meta titles, descriptions, keywords, and Open Graph texts for many pages at once with **AI Assistant > SEO > Mass Optimize SEO**. You run the pages right away or add them to a queue that the Scheduler processes. Pages can also be queued from the page tree context menu, one by one or recursively.

The full guide is on [Mass SEO](/en/latest/ExtNsT3AI/MassSEO/Index): Mass Optimize SEO, the queue, the Scheduler, page-wise and recursive Mass SEO, and language-wise optimization.

## Language-wise SEO Optimization

T3AI writes SEO texts for translated pages too:

- In **Mass Optimize SEO**, use the **Language** filter to list and optimize the pages of one language. See [Mass SEO](/en/latest/ExtNsT3AI/MassSEO/Index#language-wise-seo-optimization).
- **SERP Snippet** previews the page in the language selected in the module.

## One-Click SEO Optimization

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmr94eqvt1zdaqm3a1p8ofvxi?utm_source=link" loading="lazy" title="One-Click AI SEO" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Card **Optimize SEO**, button **One-Click AI SEO**. Fills meta title, description, keywords, and Open Graph title and description in one window.

1. Select the page and click **One-Click AI SEO**.
2. Select the **AI Provider**. Set **Topic Number Of Results** to choose how many suggestions you get per field.
3. Tick **With Page Content?** to let the AI read the page content.
4. Click **Generate AI** and choose a suggestion in the tabs **Metadata**, **Keywords**, and **Social Media**.
5. Check the **SERP Snippet** and **OpenGraph Cards** previews, then click **Save & Close**.

## New SEO

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmr95394o20qzqm3ab4lc8iau?utm_source=link" loading="lazy" title="Create AI SEO" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Card **New SEO**, button **Create AI SEO**. Use it when the page has little or no content yet.

1. Select the page and click **Create AI SEO**.
2. Enter a **Keyword** and a **Topic**, and choose the number of results.
3. Click **Generate AI**.
4. Choose the meta title, meta description, keywords, and Open Graph texts you want to keep, then click **Save & Close**.

## Optimized Meta

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrbsktxn0l6fqmo5uizi0x3x?utm_source=link" loading="lazy" title="Optimize Meta" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Card **Optimize Meta**, button **Optimize AI SEO**. Same window as Optimize SEO, limited to **Meta Title**, **Meta Description**, and **Meta Keywords**.

## Social Meta

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmranwwej12ywqmhxd1dkm9mm?utm_source=link" loading="lazy" title="Social Media Meta" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Card **Social Meta**, button **Write AI OG**. Same window as Optimize SEO, limited to **Open Graph Title** and **Open Graph Description**. The **OpenGraph Cards** preview shows how the page looks when it is shared.

## SERP Snippet

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrbngb3z0camqmo5q29vt80k?utm_source=link" loading="lazy" title="SERP Snippet" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Card **SERP Snippet**, button **Preview AI SERP**. Shows the page as a Google result, with **Desktop** and **Mobile** views. Use it to check title and description length before you save.

## Content Analysis

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmr958hz620v5qm3acmu4m2c4?utm_source=link" loading="lazy" title="Content Analysis" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Card **Content Analysis**, button **Analyze AI Content**. The AI reviews text quality and headings and suggests improvements.

1. Select the **AI Provider**.
2. Under **Content Type**, choose **Current Page** to analyze the page, or **Manual** to paste a text into **Content**.
3. Click **Content Analysis** and read the suggestions.

## SEO Page Score

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmr95o3j821g3qm3amu8k68ox?utm_source=link" loading="lazy" title="SEO Page Score" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Card **SEO Page Score**, button **View AI SEO**. Checks the frontend URL of the page (**Current Page Url**) with the AI and returns a score with recommendations.

## Schema Markup

Card **Schema Markup**, button **Generate AI Schema**. Creates structured data (JSON-LD) that helps search engines understand the content type.

### AI Schema for Page

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmr95u4pt21q0qm3agmdu390p?utm_source=link" loading="lazy" title="AI Schema" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

1. Click **Generate AI Schema** and check **Selected Page** (use **Navigate to a Page** to change it).
2. Under **Record Type**, keep **Pages**.
3. Choose the **Schema Type**: Organization, Person, Local Business, Product & Offer, Breadcrumbs, Article, News Article, Event, or Recipe.
4. Click **Generate AI**, check the result under **Schema (please verify before save your schema)**, and click **Save**.

<Note>
If the window shows "Please enable schema from settings for frontend rendering!", turn on **Enable Schema** in the [AI SEO card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-seo). Without it, the schema is saved but not output in the frontend.
</Note>

### AI Schema for Blog

Follow the same steps and select **Blog** as **Record Type**.

### AI Schema for News

Select **News** as **Record Type**, then choose the **News Record**.

<Note>
Enter the page ID that holds the news detail plugin in **Schema news detail id** in the [AI SEO card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-seo). T3AI needs it to build the news URL.
</Note>

### Edit Generated Schema

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmpkvewkb2mhxqms9l3b4ikuh?embed_v=2&utm_source=embed" loading="lazy" title="Edit Generated Schema" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

After saving, the schema of a page is stored in the page properties, tab **AI Assistant**, field **Editable AI Schema (JSON-LD)**. Edit the JSON there, or run **Generate AI Schema** again to replace it.

## T3AI Slug

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfqip70w0xi6130um9g1ndwf?embed_v=2&utm_source=embed" loading="lazy" title="AI Slug" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Every URL segment (slug) field in the TYPO3 backend, for example in the page properties or a news record, has a T3AI button. Click it, select the **AI Provider**, and choose one of the suggested SEO-friendly slugs.

## Settings, access and logs

| Topic | Where |
|---|---|
| Opens in | **AI Assistant > SEO**: Mass Optimize SEO, Optimize SEO, New SEO, Optimize Meta, Social Meta, SERP Snippet, Content Analysis, SEO Page Score, Schema Markup |
| Settings | [AI SEO card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-seo) |
| Permissions | **SEO Tools**, **Schema Markup Records**; for Mass SEO also **Bulk Operations** and **Bulk SEO Jobs**. See [Permissions](/en/latest/ExtNsT3AI/Configuration/Permissions/Index) |
| Ask AI agent | Write all SEO texts, Write SEO texts for several pages, Add structured data, SEO queue tools. See [T3AI tools](/en/latest/ExtNsT3AI/AskAiAgent/Tools/Index#seo) |
| Scheduler & CLI | **T3AF: Mass SEO Optimization (queue)**, `t3af:bulk:seo-optimize`. See [Scheduler & CLI](/en/latest/ExtNsT3AI/Configuration/SchedulerAndCLI/Index) |
| Logs | AI Logs channel **AI Assistant SEO**; AI Usage scopes `seo.*`. See [AI Usage & AI Logs](/en/latest/ExtNsT3AI/Configuration/AIUsageAndLogs/Index) |

**Related:** [Mass SEO](/en/latest/ExtNsT3AI/MassSEO/Index) · [Content](/en/latest/ExtNsT3AI/Content/Index) · [Configuration](/en/latest/ExtNsT3AI/Configuration/Index)
