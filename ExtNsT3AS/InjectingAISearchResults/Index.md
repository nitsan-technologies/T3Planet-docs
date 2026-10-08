---
title: "Injecting AI Search result in TYPO3 Search Extensions"
description: "Show the T3AS AI overview together with ke_search, indexed_search, or Solr by setting Search Class and injecting a Fluid snippet."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "Injecting AI Search result in TYPO3 Search Extensions"
  - "ke_search"
  - "indexed_search"
  - "Solr"
sidebarTitle: "Injecting AI Search result in TYPO3 Search Extensions"
---

Already use **ke_search**, **indexed_search** or **Solr** for your website search? Then AI Search can show a short AI answer above the normal search results. Visitors get a quick answer and still see the usual result list.

You need a developer for one small change in the search template. Everything else is done in the backend.

## Prerequisites for ke_search and indexed_search

1. Your website is fully indexed by your search extension.
2. AI Search training runs regularly (the task **T3CS Training (Site N)**, see [Scheduler](/en/latest/ExtNsT3AS/Configuration/TrainingCenter/Index#scheduler)).

{/* 2. **Scheduler execution** — run the required T3AS training scheduler task to keep the data fresh. See **Scheduler** on [Configuration](/en/latest/ExtNsT3AS/Configuration/Index). */}

## Setup overview

**Part 1 – in the backend (you)**

1. Go to **AI Universe → AI Chatbot/Search → Search → Settings**.
2. In **Search Class**, enter the value for your search extension:
   - ke_search: `ke_search_sword`
   - indexed_search: `tx-indexedsearch-searchbox-sword`
   - Solr: `tx-solr-q`
3. Click **Save Configuration**.

<Note>
Enter the value without a dot in front. If your website design uses a different name for the search field, ask your developer for the right value.
</Note>

**Part 2 – in the template (your developer)**

Your developer adds one line to the search template of your search extension. See "For developers" below.

**Part 3 – test**

1. Clear all caches.
2. Search for something on your website.
3. The AI answer appears together with the normal results.

![AI overview injected below a ke_search form](../Configuration/images/extend.webp)

{/* 1. Set **Search Class** in **T3AS → Search → Settings** so T3AS can read the visitor query from the third-party search field (see [5. Search tab](/en/latest/ExtNsT3AS/Configuration/Search/Index)). */}

## For developers

<Accordion title="For developers: add the AI answer to the search template">
Add one line to your own copy (override) of the search template, where the AI answer should appear. Don't edit the files of the search extension itself.

```html
<f:cObject typoscriptObjectPath="lib.injectAiSearchResults" />
```

- **ke_search:** in `SearchForm.html`. Search Class: `ke_search_sword`.
- **indexed_search:** in `Search.fluid.html`, after the search form and before the results. Search Class: `tx-indexedsearch-searchbox-sword`.
- **Solr:** in `Results.html`, after the search form. Search Class: `tx-solr-q`.

![Fluid injectAiSearchResults snippet in indexed_search Search.fluid.html](../Configuration/images/inject-indexed-search.webp)

![Fluid injectAiSearchResults snippet in Solr Results.html](../Configuration/images/inject-solr.webp)
</Accordion>

<a id="enable-ai-search-plugin-using-typoscript"></a>

## Enable AI Search plugin using TypoScript

Developers can also show the AI Search plugin from a template, without placing it on the page.

<Accordion title="For developers: render the plugin with TypoScript">

Add this where the plugin should appear. Set `searchPid` to the ID of the page that contains the AI Search plugin (for example `4`):

```html
<f:cObject typoscriptObjectPath="lib.renderAiSearchPlugin" data="{searchPid:4}"/>
```

</Accordion>

**Related:** [Search tab](/en/latest/ExtNsT3AS/Configuration/Search/Index) · [AI Search plugin](/en/latest/ExtNsT3AS/FrontendPlugin/Index)

{/* Site-wide search defaults are in **T3AS → Search** (see [5. Search tab](/en/latest/ExtNsT3AS/Configuration/Search/Index)). For the standalone frontend plugin, see [T3AS Search Plugin](/en/latest/ExtNsT3AS/FrontendPlugin/Index). */}

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

Use this when you already run **ke_search**, **indexed_search**, or **Solr** and want the T3AS AI overview to appear together with that search UI.

When configuring T3AS with **ke_search** or **indexed_search**, make sure the following conditions are met:

Setup has two parts:

**Search Class values**

<Note>
Enter **only the class name** in **Search Class** (for example `tx-solr-q`), without a leading `.`. The value must match the CSS class on the live search input for your setup. If your theme renames the input class, use that class instead.
</Note>

## Fluid injection snippet

Add this line where the AI overview should render (usually near the search form or above the classic result list):

## ke_search

1. Set **Search Class** to `ke_search_sword`.
2. In your override of `SearchForm.html`, add the injection snippet.

*Example: AI overview rendered with the ke_search form after the Fluid snippet is in place.*

## indexed_search

1. Set **Search Class** to `tx-indexedsearch-searchbox-sword`.
2. In your override of `EXT:indexed_search/Resources/Private/Templates/Search/Search.fluid.html`, add the injection snippet (typically after the search form and before the result loop).

*indexed_search template — add `<f:cObject typoscriptObjectPath="lib.injectAiSearchResults" />` after the form render.*

## Solr

1. Set **Search Class** to `tx-solr-q`.
2. In your override of `EXT:solr/Resources/Private/Templates/Search/Results.html`, add the injection snippet (typically after the search form partial).

*Solr `Results.html` — add `<f:cObject typoscriptObjectPath="lib.injectAiSearchResults" />` after the search form.*

After saving the Search Class and template override, flush TYPO3 caches and test a search on the frontend. The AI overview should appear with the existing search results when a matching query is submitted.

To render the standalone AI Search plugin via TypoScript (not the third-party form injection above), add the following Fluid view helper where the plugin should appear. Set `searchPid` to the page ID that contains the T3AS Search plugin (for example `4`):
*/}

{/* Detailed developer notes (moved here on 2026-10-08 to keep the page short; not shown on the website):

<Accordion title="For developers: add the AI answer to the search template">

Add this line where the AI overview should appear (usually near the search form or above the result list). Use a site package override; do not edit the extension in `vendor/` or `typo3conf/ext`.

```html
<f:cObject typoscriptObjectPath="lib.injectAiSearchResults" />
```

| Search extension | Search Class (CSS class) | Template to extend |
| --- | --- | --- |
| **ke_search** | `ke_search_sword` | `EXT:ke_search/Resources/Private/Templates/SearchForm.html` |
| **indexed_search** | `tx-indexedsearch-searchbox-sword` | `EXT:indexed_search/Resources/Private/Templates/Search/Search.fluid.html` |
| **Solr** | `tx-solr-q` | `EXT:solr/Resources/Private/Templates/Search/Results.html` |

**ke_search** – add the snippet to your override of `SearchForm.html`.

**indexed_search** – add it to your override of `Search.fluid.html`, after the search form and before the result loop.

![Fluid injectAiSearchResults snippet in indexed_search Search.fluid.html](../Configuration/images/inject-indexed-search.webp)

**Solr** – add it to your override of `Results.html`, after the search form partial.

![Fluid injectAiSearchResults snippet in Solr Results.html](../Configuration/images/inject-solr.webp)

</Accordion>
*/}
