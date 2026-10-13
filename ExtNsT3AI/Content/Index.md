---
title: "Content"
description: "Write, rewrite, and translate TYPO3 content with T3AI: AI tools in the rich text editor, the Content Rewriter for pages, news, and blogs, and AI buttons in the content element form."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "Content"
sidebarTitle: "Content"
---

The **Content** tab of the AI Assistant module groups the T3AI tools for writing text. Some tools open a window from the tab. Others live where you edit content: in the rich text editor (RTE) and in the content element form.

Settings, permissions, AI agent tools, and logs for this feature are listed in [Settings, access and logs](#settings-access-and-logs).

| Tool | Where you use it |
|---|---|
| [RTE AI Copilot](#rte-ai-copilot) | Toolbar of the rich text editor |
| [Content Rewriter](#content-rewriter), [News](#news-content-rewriter), [Blog](#blog-content-rewriter) | **AI Assistant > Content**, button **Build AI Rewriter** |
| [Content Elements (Create)](#content-elements-create) and [(Edit)](#content-elements-edit) | Header of the content element form |
| [Content Translate](#content-translate) | Header of the content element form |
| [Content Fields](#content-fields) | **T3AI** button next to the fields of a content element |

<Note>
For the tools that live in the editor or the content element form, the card button in the Content tab opens a short demo, not the tool itself.
</Note>

## RTE AI Copilot

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfparfqb2e1z1d3nuc7u27hg?embed_v=2&utm_source=embed" loading="lazy" title="RTE AI Copilot" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

T3AI adds three buttons to the CKEditor toolbar: **T3AI Prompts**, **T3AI Translator**, and the AI Assistant Copilot.

### Enable the T3AI RTE preset

1. Edit the root page properties and open the **Resources** tab.
2. Under **Include static Page TSconfig**, add **Ns T3Ai :: Config RTE Preset (ns_t3ai)** and save.

![Include the T3AI RTE preset in the page properties](./images/new_rte.webp)

The preset sets `RTE.default.preset = nst3ai`. If you use your own RTE preset, copy the T3AI `importModules` and the toolbar items `t3aicommands`, `t3aitranslator`, and `t3aiassistance` from `EXT:ns_t3ai/Configuration/RTE/Plugin.yaml` into it.

### T3AI Prompts

Select text in the editor, click **T3AI Prompts**, and choose an action:

- **Optimize Content**: Improve Content, Shorten Content, Expand Content, Simplify Language, Spelling & Grammar
- **Adjust Content**: Summarize, Rewrite, Bulletize
- **Tone of Content**: Business, Legal, Journal, Friendly, Poetic

Use **Search T3AI Prompts** to find an action quickly.

![T3AI Prompts in the RTE toolbar](./images/Co_Prompts.webp)

### T3AI Translator

Select text, click **T3AI Translator**, and choose the target language. The list shows default and custom languages.

![T3AI Translator in the RTE toolbar](./images/co_Translate.webp)

### AI Assistant Copilot

Click the sparkle icon to open the **AI Assistant Copilot**. Describe what you need, set **Writing Style**, **Writing Tone**, **Temperature** (higher is more creative), and **Number of results**, then insert the text you like.

## Content Rewriter

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfo05vp51bih1d3nx2mm01pa?step=1" loading="lazy" title="Content Rewriter" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Rewrites existing content in a new style. Card **Content Rewriter**, button **Build AI Rewriter**.

1. Select the page or storage folder in the page tree and click **Build AI Rewriter**.
2. Select the **AI Provider**.
3. Under **Rewriter AI**, choose the source:
   - **Internal**: a TYPO3 record. Choose the **Selected Page** with **Navigate to a Page**, or a **News Record**.
   - **External**: one or more web addresses under **URLS**. T3AI fetches the content from there.
   - **Text**: paste the text.
4. Choose the **Record Type** (Pages, News, Blog) and enter the **Topic**.
5. Choose the **Writing Style**: Casual, Approachable, Easy Readability, or **Others** for your own style.
6. Set the **Word Count**. Optionally add an **Additional Instruction**, **Background Context**, and **Autolink** with **Autolink Text** to link a phrase.
7. Click **Generate AI**, then choose the outline and the element types and edit the texts.
8. Click **Save**.

**Result:** The rewritten content as content elements of the selected page, or as a news or blog record in the storage folder.

<Tip>
External sources work with providers that can fetch web pages. If T3AI shows "content cannot be fetched from external URLs", paste the text with **Text** instead.
</Tip>

## News Content Rewriter

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfqja3b60yda130uutqwjfwr?embed_v=2&utm_source=embed" loading="lazy" title="News Content Rewriter" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Same window as Content Rewriter, opened from the **News Content Rewriter** card. Select the news storage folder first. With **Internal**, choose the **News Record** to rewrite.

**Result:** A news record in the storage folder. Edit it in the **List** module or **News Administration**.

## Blog Content Rewriter

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfqj657f0y6c130ud3zh0goi?embed_v=2&utm_source=embed" loading="lazy" title="Blog Content Rewriter" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Same window as Content Rewriter, opened from the **Blog Content Rewriter** card, with **Blog** as record type. Select the blog page or folder first.

**Result:** A blog post with the rewritten content elements.

## Content Elements (Create)

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfqip70w0xi6130um9g1ndwf?embed_v=2&utm_source=embed" loading="lazy" title="Content Elements (Create)" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Fills a new content element with AI text and images. Works for TYPO3 core elements and custom elements.

1. In the **Page** module, create a content element and choose its type.
2. In the form header, click **Generate Content with T3AI**.
3. Enter what the element should say and choose which text fields to fill.
4. Optionally add an AI image: enter the **Prompt for Image Generation**, choose **Style** and **Size**, and click **Generate Images**.
5. Check the **Element Content**, then click **Save**.

## Content Elements (Edit)

### Guidance

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfqju3jw0yyq130uvav5h5r1" loading="lazy" title="Content Elements (Edit)" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Regenerates an existing content element.

1. Edit the content element.
2. In the form header, click **Re-Generate Content with T3AI**.
3. Change the prompt or click **Re-generate**, review the text, and click **Save**.

## Content Translate

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfpdagob2ias1d3n5w7nptm0?embed_v=2&utm_source=embed" loading="lazy" title="Content Translate" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Translates one content element.

1. Edit the content element in the default language.
2. In the form header, click **Translate with T3AI**.
3. Select the **AI Provider** and the target language, then click **Translate Record**.

**Result:** A translated copy of the element in the target language. To translate whole pages, see [Translation](/en/latest/ExtNsT3AI/Translation/Index).

## Content Fields

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfqju3jw0yyq130uvav5h5r1" loading="lazy" title="Content Fields" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Fills single fields with AI. Text fields such as header and subheader have a **T3AI** button next to them.

1. Click **T3AI** next to the field.
2. Enter a prompt describing the content.
3. Choose one of the suggestions and click **Save**.

Which fields get the **T3AI** button is set under TCA record fields in the [General Settings card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#general-settings).

## Settings, access and logs

| Topic | Where |
|---|---|
| Opens in | **AI Assistant > Content**: RTE AI Copilot, Content Rewriter, News Content Rewriter, Blog Content Rewriter, Content Elements (Create), Content Elements (Edit), Content Translate, Content Fields |
| Settings | [AI Content card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-content); TCA record fields and RTE history in the [General Settings card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#general-settings) |
| Permissions | **Content Generation**, **Page Content Elements**, **RTE AI Commands**. See [Permissions](/en/latest/ExtNsT3AI/Configuration/Permissions/Index) |
| Ask AI agent | Creates or updates header and text content elements on request. See [T3AI tools](/en/latest/ExtNsT3AI/AskAiAgent/Tools/Index#pages-news-and-blogs) |
| Logs | AI Logs channel **AI Assistant Content**. See [AI Usage & AI Logs](/en/latest/ExtNsT3AI/Configuration/AIUsageAndLogs/Index) |

**Related:** [Prompts](/en/latest/ExtNsT3AI/Prompts/Index) · [SEO](/en/latest/ExtNsT3AI/SEO/Index) · [Configuration](/en/latest/ExtNsT3AI/Configuration/Index)
