---
title: "SEO"
description: "Generate and improve SEO metadata, social previews, schema, and slugs with T3AI, including Mass SEO for many pages at once."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "SEO"
sidebarTitle: "SEO"
---

## T3AI SEO

T3AI SEO helps editors generate and improve metadata, social previews, schema, and search-facing text directly from TYPO3 content.
Use AI Foundation for shared provider and model setup, then use the SEO tools below for page-level SEO work.

See also:

- [AI Foundation Configuration](/en/latest/ExtNsT3AF/Configuration/Index)
- [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)

Open the **T3AI** module, select a page in the page tree, and go to the **SEO** tab. Generated data is saved to the page properties when you click **Save & Close**. Defaults such as the SERP snippet view and the number of suggestions per field are set in [T3AI Features](/en/latest/ExtNsT3AI/AISettings/Index#feature-settings).

## Mass SEO

Mass SEO helps you fill in SEO data for many TYPO3 pages at the same time.
The AI reads your page content and suggests meta titles, descriptions, keywords, and Open Graph text.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmranl2rf12m9qmhxqwmx41z4?utm_source=link" loading="lazy" title="T3AI Mass SEO Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

### Before you start

- T3AI must be installed and active.
- Shared provider and model setup must already be configured in AI Foundation.
- Pages should contain real content so the AI has something useful to analyze.

### How it works

1. Add pages to the queue or open a single page in Mass Optimize SEO.
2. Run the task manually or with the TYPO3 Scheduler.
3. Review the generated SEO suggestions.
4. Save the data to the page.

### Scheduler

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmq7sizd80nqcqml6hobhev7r?utm_source=embed" loading="lazy" title="T3AI Mass SEO Scheduler Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Create a Scheduler task with the command `nst3ai:bulk:seo-optimize` when you want queued SEO work to run automatically.
Use task options such as SEO fields, limits, dry-run mode, and provider/model overrides when needed.

### Page wise Mass SEO

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrc2khs118r3qmo5stu972a6?utm_source=link" loading="lazy" title="T3AI Page Wise Mass SEO Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Use page-wise Mass SEO when you want to enable or optimize one page at a time.

### Recursive Mass SEO

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrc2s2uw19cnqmo5qdlz7g7h?utm_source=link" loading="lazy" title="T3AI Recursive Mass SEO Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Use recursive Mass SEO when you want to add a parent page and all of its child pages to the queue.

## Language-wise SEO Optimization

T3AI can generate and optimize SEO metadata in multiple languages.
Use this when you want localized SEO output for translated content.

## One-Click SEO Optimization

Generate multiple SEO fields at once for a selected page: meta title, description, keywords, and Open Graph title, description, and image.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmr94eqvt1zdaqm3a1p8ofvxi?utm_source=link" loading="lazy" title="One-Click AI SEO" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## New SEO

Create new SEO metadata for a page when nothing useful exists yet. Add keywords and a topic, choose the number of results, then select the meta title, description, keywords, and Open Graph data you want to keep.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmr95394o20qzqm3ab4lc8iau?utm_source=link" loading="lazy" title="Create AI SEO" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## Optimized Meta

Generate or improve metadata by analyzing the current page content.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrbsktxn0l6fqmo5uizi0x3x?utm_source=link" loading="lazy" title="Optimize Meta" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## Social Meta

Use Social Meta when you want better Open Graph titles, descriptions, and image-related preview content.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmranwwej12ywqmhxd1dkm9mm?utm_source=link" loading="lazy" title="Social Media Meta" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## SERP Snippet

Preview and refine how your page may look in search results.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrbngb3z0camqmo5q29vt80k?utm_source=link" loading="lazy" title="SERP Snippet" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## Content Analysis

Analyze content quality and receive AI-based SEO suggestions for the current page.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmr958hz620v5qm3acmu4m2c4?utm_source=link" loading="lazy" title="Content Analysis" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## SEO Page Score

Check the SEO score for a page and review improvement opportunities.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmr95o3j821g3qm3amu8k68ox?utm_source=link" loading="lazy" title="SEO Page Score" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## Schema Markup

T3AI can generate and edit structured data for pages, blog records, and news records.
Use this when you want search engines to understand the content type more clearly.

### AI Schema for Page

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmr95u4pt21q0qm3agmdu390p?utm_source=link" loading="lazy" title="AI Schema" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

### AI Schema for Blog

Use the same schema workflow for blog records when you want blog-specific structured data. Select **Blog** as the record type.

### AI Schema for News

Use the same schema workflow for news records after confirming the required news detail-page setting is available.

<Note>
Enter the page ID that holds the news detail plugin in **Schema news detail id** in the SEO group of the [T3AI feature card](/en/latest/ExtNsT3AI/AISettings/Index#feature-settings). Then select **News** as the record type and choose the news record.
</Note>

### Edit Generated Schema

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmpkvewkb2mhxqms9l3b4ikuh?embed_v=2&utm_source=embed" loading="lazy" title="Edit Generated Schema" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## T3AI Slug

Generate SEO-friendly slugs for pages, blog entries, and news records.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfqip70w0xi6130um9g1ndwf?embed_v=2&utm_source=embed" loading="lazy" title="AI Slug" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>
