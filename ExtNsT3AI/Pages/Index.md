---
title: "Pages"
description: "Create TYPO3 pages, page trees, blog posts, and news articles with AI from the Pages tab of the AI Assistant module: keyword, title, outline, and content elements in one wizard."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "Pages"
  - "AI page generator"
sidebarTitle: "Pages"
---

The **Pages** tab of the AI Assistant module creates new content for you: a page with content elements, a whole page tree, a blog post, or a news article. You give a keyword or a short description, choose from the AI's suggestions, and T3AI creates the TYPO3 records.

Settings, permissions, AI agent tools, and logs for this feature are listed in [Settings, access and logs](#settings-access-and-logs).

## Before you start

- An AI provider is connected. See [AI provider & API keys](/en/latest/ExtNsT3AI/Configuration/AIProviders/Index).
- The generators you need are enabled in the [AI Pages card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-pages).
- For news: EXT:news is installed and you have a news storage folder.

## How the generators work

All page, blog, and news generators follow the same flow.

<Steps>
  <Step title="Select the target page">
    In the page tree, click the page where the new content should go. The wizard shows it at the top right as **Path**.
  </Step>
  <Step title="Open the generator">
    Go to **AI Universe > AI Assistant > Pages** and click the button on the card, for example **Launch AI Page**.
  </Step>
  <Step title="Describe what you need">
    Select the **AI Provider**, keep **Use Default** as prompt or pick another one (the pencil icon edits it), enter a keyword, and click **Generate AI**.
  </Step>
  <Step title="Choose from the suggestions">
    Select one of the suggested titles, then tick the outline items you want. Each ticked item becomes one content element.
  </Step>
  <Step title="Create the content">
    Click **Create elements on an existing page.** to add the elements to the selected page, or **Create a new sub-page with elements.** to create a new page below it. Confirm the dialog.
  </Step>
</Steps>

<Note>
Generated content elements are placed in the main column (`colPos` 0). Review them in the **Page** module before you publish.
</Note>

Every T3AI window has four icons in the footer: **Report an Issue**, **Suggest Feature**, **Documentation** (opens this page), and **Demo Guide** (opens the interactive demo).

## Page (Simple)

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfpb58t72efv1d3n9wg7p1vc?embed_v=2&utm_source=embed" loading="lazy" title="Page (Simple)" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Use it to fill one page quickly from a keyword.

1. Select the target page in the page tree.
2. In **AI Assistant > Pages**, click **Launch AI Page** on the **Page (Simple)** card.
3. Under **Choose Category**, select **Default**, **Product**, or **Service**.
4. Select the **AI Provider** and the **Prompt**.
5. Enter a keyword:
   - **Default**: also set **Topic Number Of Results** (how many titles the AI suggests).
   - **Product** and **Service**: also enter **Brief Information** and set **Number Of Words** (100 to 1200).
6. Click **Generate AI** and select a suggested page title.
7. In the outline, tick **Create Element** for each item you want and check the **Element Title**.
8. Click **Create elements on an existing page.** or **Create a new sub-page with elements.**

**Result:** One content element per ticked outline item, on the selected page or on a new subpage.

## Page (Advanced)

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfpbi59j2ewq1d3n4y86429w?embed_v=2&utm_source=embed" loading="lazy" title="Page (Advanced)" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Use it when you want to decide what each content element looks like.

1. Select the target page and click **Launch AI Page** on the **Page (Advanced)** card.
2. Fill in the form as in Page (Simple) and click **Generate AI**.
3. Select a page title.
4. For every outline item, choose the **Element Type** (for example Text & Image, Header, Text Element, Text & Media) and the fields the text goes into.
5. Optionally generate an AI image for an element: enter the **Prompt for Image Generation**, choose the style and size, and click **Generate Images**.
6. Click **Create elements on an existing page.** or **Create a new sub-page with elements.**

**Result:** Content elements of the types you chose, with optional AI images, on the selected page or on a new subpage.

## Page Tree

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfpc1dkp2fs31d3nswhel36q?embed_v=2&utm_source=embed" loading="lazy" title="Page Tree" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Use it to plan a whole section or site structure.

1. Click **Build AI Page Tree** on the **Page Tree** card.
2. Keep **Page** under **Choose Category** and select the **AI Provider**.
3. Describe the structure in **Prompt**, for example "Website for a dental practice with services, team, and contact".
4. Under **Insert the new structure below this page:**, pick the parent page with **Navigate to a Page**. Without a parent, T3AI asks whether to create the tree at root level.
5. Click **Generate Page Tree** and wait for the proposal.
6. Rename, add, remove, or move pages in the proposal.
7. Click **Create Page Tree**. T3AI confirms with **Page Tree Successfully Created**.

**Result:** The page hierarchy below the chosen parent page. Fill the new pages with Page (Simple) or Page (Advanced).

## Blog Tree

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmr94376n1yy8qm3akt7qcya0?utm_source=link" loading="lazy" title="Blog Tree" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>
<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfqhfk6p0vmi130uwfz3julq?embed_v=2&utm_source=embed" loading="lazy" title="Blog Tree" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Use it to create the structure of a blog, for example categories and first posts.

1. Click **Build AI Blog Tree** on the **Blog Tree** card. The same wizard as Page Tree opens with **Blog** selected under **Choose Category**.
2. Select the **AI Provider**, describe the blog in **Prompt**, and choose the parent page.
3. Click **Generate Blog Tree**, adjust the proposal, and click **Create Blog Tree**.

**Result:** A blog page hierarchy below the chosen page. T3AI confirms with **Blog Tree Successfully Created**.

## News (Simple)

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfpco2552gvu1d3nh0mom5lq?embed_v=2&utm_source=embed" loading="lazy" title="News (Simple)" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Use it to write a news article from a topic.

1. Select your news storage folder in the page tree.
2. Click **Publish AI News** on the **News (Simple)** card. A new news record opens.
3. Enter the **Topic** and **Keywords**, and choose a **Style** (Formal, Informal, Concise, Creative).
4. Generate the article and select one of the suggested titles.
5. Check the headline, teaser, text, and meta fields, then click **Save News Records**.

**Result:** An EXT:news record in the storage folder. Open it in the **List** module or **News Administration**.

## News (Advanced)

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfpcrrvz2h4l1d3nagqpnejh?embed_v=2&utm_source=embed" loading="lazy" title="News (Advanced)" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Use it for longer articles built from an outline.

1. Select your news storage folder and click **Publish AI News** on the **News (Advanced)** card.
2. Enter the **Topic** and **Keywords** and choose the **Style**.
3. Under **Create outline with**, choose **RTE** (the article goes into the news text) or **Content Elements** (one content element per outline section).
4. Generate the outline, select the sections you want, and generate the content.
5. Optionally add an AI image in **Available Image Fields**.
6. Click **Save News Records**.

**Result:** An EXT:news record with the generated sections, as text or as related content elements.

## Blog (Simple)

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfpc5nm82g181d3n6o8ik3p9?embed_v=2&utm_source=embed" loading="lazy" title="Blog (Simple)" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Use it to write a short blog post.

1. Select the blog page or the blog folder in the page tree.
2. Click **Generate AI Blog** on the **Blog (Simple)** card.
3. Select the **AI Provider** and the **Prompt**, enter a keyword, and click **Generate AI**.
4. Select a title and tick the outline items you want.
5. On a blog post page (page type 137), click **Create elements on an existing page.** or **Create a new sub-page with elements.** On any other page, T3AI creates a new subpage.

**Result:** A blog post with one content element per ticked outline item.

## Blog (Advanced)

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfo11pg21cum1d3ne0q1fnfp?embed_v=2&utm_source=embed" loading="lazy" title="Blog (Advanced)" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Use it for longer blog posts with your own element types and images.

1. Click **Generate AI Blog** on the **Blog (Advanced)** card.
2. Fill in the form, click **Generate AI**, and select a title.
3. Set the **Element Type** and fields for each outline item, and optionally generate AI images.
4. Create the elements on the current blog page or on a new subpage.

**Result:** A multi-section blog post.

## Interactive demos

Each demo below walks through one generator from start to finish in the current backend. Use the table to pick the right one, then follow the matching steps above.

| You want to | Use | Result |
|---|---|---|
| Fill one page quickly from a few keywords | Page (Simple) | Content elements on the current page, or new subpages |
| Control the page type, template, and length of the page | Page (Advanced) | Structured content elements on the current page, or new subpages |
| Plan a whole section or site structure | Page Tree | A page hierarchy below the selected page |
| Publish a news article from a topic | News (Simple) | One EXT:news record in the storage folder |
| Write a longer news article from an outline | News (Advanced) | An EXT:news record with generated sections |
| Write a short blog post | Blog (Simple) | Content on the blog page |
| Write a multi-section blog post | Blog (Advanced) | A blog page with multiple sections |

<Tip>
Simple generators ask for a keyword and create the content from the outline you tick. Advanced generators let you set the **Element Type** and the fields of every outline item and generate an AI image per element.
</Tip>

### Demo: Page (Simple)

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmr93kk611xl1qm3aruhhood7?utm_source=link" loading="lazy" title="T3AI - Page Simple" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Select the AI provider, enter keywords, pick a title, generate the outline, and create the elements on the page. The demo ends with activating the created elements. Steps: [Page (Simple)](#page-simple).

### Demo: Page (Advanced)

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmr93vofp1yezqm3a9tewxyn3?utm_source=link" loading="lazy" title="T3AI - Page Advanced" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Choose the page type and template, select the provider, and generate content from an outline. Use it for product, service, or blog-style pages where the structure matters. Steps: [Page (Advanced)](#page-advanced).

### Demo: Page Tree

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmr93ztmb1ynjqm3awsok5811?utm_source=link" loading="lazy" title="T3AI - Page Tree" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Describe the site or section in the prompt, review the proposed hierarchy, and create it. The demo then opens the new pages in the page tree. Steps: [Page Tree](#page-tree).

### Demo: News (Simple)

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrajvz700ukzqmhxqr0lmo42?utm_source=link" loading="lazy" title="T3AI News Simple" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Select the provider, enter the topic, and generate the article with a headline you can edit before saving. Requires EXT:news; the record is saved in the news storage folder. Steps: [News (Simple)](#news-simple).

### Demo: News (Advanced)

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrajyl2e0uswqmhxdgb2jlzl?utm_source=link" loading="lazy" title="T3AI News- Advanced" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Select the language model, define the topic, generate the outline and the content, and save the complete news record. Steps: [News (Advanced)](#news-advanced).

### Demo: Blog (Simple)

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrajl4zr0tngqmhxpncd89qr?utm_source=link" loading="lazy" title="T3AI Blog Simple" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Set up the blog template, configure the AI settings, and generate keyword-driven content for the blog post. Steps: [Blog (Simple)](#blog-simple).

### Demo: Blog (Advanced)

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrajo09x0tz1qmhxe0qsssrm?utm_source=link" loading="lazy" title="T3AI Blog - Advanced" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Generate blog topics, build a detailed outline, and create a multi-section post with structured content. Steps: [Blog (Advanced)](#blog-advanced).

### After generating

- Check the created pages and elements in the **Page** module before publishing. Generated content elements are placed in column 0 (`colPos` 0).
- Generate the SEO fields with [SEO](/en/latest/ExtNsT3AI/SEO/Index), or turn on automatic SEO for new AI pages in the [AI SEO card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-seo).
- Translate the new pages with [One-Click Page Translations](/en/latest/ExtNsT3AI/Translation/OneClickPageTranslations/Index).
- To change the default prompts, element type, or number of results, use the [AI Pages card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-pages).

## Settings, access and logs

| Topic | Where |
|---|---|
| Opens in | **AI Assistant > Pages**: Page (Simple), Page (Advanced), Page Tree, Blog Tree, News (Simple), News (Advanced), Blog (Simple), Blog (Advanced) |
| Settings | [AI Pages card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-pages): feature toggles, default prompts, element type, number of results. Automatic SEO for new AI pages: [AI SEO card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-seo) |
| Permissions | **AI Assistant** module access. See [Permissions](/en/latest/ExtNsT3AI/Configuration/Permissions/Index) |
| Ask AI agent | Create a page, Create a page (detailed), Create a page structure, Write a blog post, news tools. See [T3AI tools](/en/latest/ExtNsT3AI/AskAiAgent/Tools/Index#pages-news-and-blogs) |
| Logs | **AI Usage** filtered by module `ns_t3ai`. See [AI Usage & AI Logs](/en/latest/ExtNsT3AI/Configuration/AIUsageAndLogs/Index) |

**Related:** [Configuration](/en/latest/ExtNsT3AI/Configuration/Index) · [SEO](/en/latest/ExtNsT3AI/SEO/Index) · [Content](/en/latest/ExtNsT3AI/Content/Index)
