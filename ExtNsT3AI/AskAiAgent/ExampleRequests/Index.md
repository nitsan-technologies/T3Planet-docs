---
title: "Example requests"
description: "Friendly, everyday AI agent requests you can copy: create pages and blog posts, write Google and social media texts, translate pages and news, keep brand names in translations, find images, and handle many pages at once, plus a quick reference of T3AI tools."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "AI agent"
  - "Prompts"
sidebarTitle: "Example requests"
---

Talk to the AI agent the way you would ask a colleague. Copy an example below, change the names, and send it.

- Select the page first. *This page* means the page shown in the agent's context line.
- For every change, you get a preview first. Nothing is saved until you click **Apply**.

## Try these first

Three safe requests to get to know the agent:

```text
What is in the Mass Translation queue?
```

```text
Can you suggest a better meta description for this page?
```

```text
Show me the German glossary terms.
```

The first and the last only read. The second shows a suggestion, and nothing is saved unless you click **Apply selected**.

## Pages and blog posts

**"I need a new page."**

```text
Can you create a page "Web Hosting" under this page? Add a short intro and three benefits.
```

**"Please write a blog post for us."**

```text
Write a blog post about 5 easy tips to make a website faster.
```

**"We are starting a new website and need the menu structure."**

```text
Create these pages under this page: About us, Services, Prices, Blog, Contact.
```

**"We have news to share."**

```text
Create a news article: we are at the TYPO3 Conference on 14 October, booth B12.
```

You always see the pages and texts in a preview. Click **Apply** to create them, or **Cancel** and say what to change.

## Google and social media

**"This page needs better texts for Google."**

```text
Please write a new SEO title and meta description for this page.
```

**"The meta description must mention our free delivery."**

```text
Write a meta description for this page that mentions free delivery. Keep it short.
```

**"The page looks bad when shared on LinkedIn."**

```text
Write the Open Graph title and description for this page.
```

**"Google should know this page is about our company."**

```text
Add Organization schema to this page.
```

The preview shows the current text next to the AI suggestion. Keep the suggestion or type your own, then click **Apply selected**.

## Translation

**"This page should also be in German."**

```text
Translate this page into German.
```

**"We need it in German and French."**

```text
Translate this page into German and French.
```

**"Only one text block needs a translation."**

```text
Translate only the first text element on this page into French.
```

**"Our news article should also be in German."**

```text
Translate this news article into German.
```

**"Our product name must never be translated."**

```text
Add a German glossary term: CloudSync stays CloudSync.
```

New translations then keep the name. Pages that are already translated keep the old text until you re-translate them.

## Images

**"I need a picture for this blog post."**

```text
Generate an image of a bright modern office and save it in fileadmin.
```

**"A real photo would be better than an AI image."**

```text
Find a free stock photo from Unsplash of a team meeting.
```

The image is saved in the fileadmin. Add it to your content element as usual.

## Many pages at once

For more than a few pages, put them in a queue. The Scheduler then does the work in the background.

**"All our product pages need SEO texts."**

```text
Queue the Products page and its subpages for Mass SEO.
```

**"The whole Services section should be in French."**

```text
Queue the Services page and its subpages for Mass Translation into French.
```

**"Did anything go wrong over the weekend?"**

```text
Show the Mass Translation queue. Did any translations fail?
```

**"Please try the failed ones again."**

```text
Retry the failed translations.
```

Pages are only queued when Mass SEO or Mass Translation is allowed in the **AI Assistant** tab of their page properties. See [Mass SEO](/en/latest/ExtNsT3AI/MassSEO/Index) and [Mass Translation](/en/latest/ExtNsT3AI/Translation/MassTranslation/Index).

## Tips for better results

- **Say what matters to you.** *Write a meta description that mentions free delivery* works better than *Do SEO*.
- **Name the page or language** when it is not the selected page, for example *Translate the Contact page into German*.
- **Not happy with the preview?** Click **Cancel** and say what to change, for example *Make it shorter* or *Use a more formal tone*.
- **Ask in any language.** The agent understands German, English, and other languages.

## Quick reference

### SEO

| Request | T3AI tool |
|---|---|
| *Generate SEO for this page* | `t3ai_generate_all_seo` |
| *Generate meta description and Open Graph title for this page* | `t3ai_generate_meta_description`, `t3ai_generate_og_title` |
| *Suggest five SEO keywords for this page* | `t3ai_generate_keywords` |
| *Write SEO meta descriptions for all subpages of Products* | `t3ai_generate_seo_batch` |
| *Add Article schema markup to this page* | `t3ai_apply_schema_markup` |
| *Analyze the content of this page and improve the weak paragraphs* | `t3ai_apply_content_analysis` |

### Translation

| Request | T3AI tool |
|---|---|
| *Translate this page into German* | `t3ai_translate_page` (after the core tool that lists site languages) |
| *Translate only the second text element on this page into French* | `t3ai_translate_content` |
| *Translate news record 12 into German* | `t3ai_translate_news` |
| *Translate the category record 4 into all site languages* | `t3ai_record_translate` |

### Pages, news, and blogs

| Request | T3AI tool |
|---|---|
| *Create a page "Services" under this page with an intro and three feature sections* | `t3ai_create_page_simple` |
| *Create a detailed landing page about TYPO3 hosting with FAQ and call to action* | `t3ai_create_page_advanced` |
| *Create a page tree for a dental clinic: About, Treatments with three subpages, Contact* | `t3ai_create_page_structure` |
| *Add a text element with a short company introduction to this page* | `t3ai_create_content_element` |
| *Use T3AI to create a simple news record about our TYPO3 v14 upgrade* | `t3ai_create_news_simple` |
| *Use T3AI to create an advanced blog post about accessibility basics* | `t3ai_create_blog_advanced` |

### Glossary

| Request | T3AI tool |
|---|---|
| *List the translation glossary terms* | `t3ai_glossary_list` |
| *Add a glossary term for German: T3Planet should stay T3Planet* | `t3ai_glossary_save` |
| *Delete the German glossary term "Layout"* | `t3ai_glossary_delete` |

### Mass SEO and Mass Translation queues

| Request | T3AI tool |
|---|---|
| *Show the pages in the Mass SEO queue and the Mass Translation queue* | `t3ai_mass_seo_queue_list`, `t3ai_mass_translation_queue_list` |
| *Queue this page for Mass SEO* | `t3ai_mass_seo_queue_add` |
| *Queue all subpages of Products for Mass SEO* | `t3ai_mass_seo_queue_add` |
| *Queue this page and its subpages for Mass Translation into French* | `t3ai_mass_translation_queue_add` |
| *Retry the failed entries in the Mass Translation queue* | `t3ai_mass_translation_queue_requeue` |
| *Clear completed entries from the Mass Translation queue* | `t3ai_mass_translation_queue_clear_completed` |

### Media

| Request | T3AI tool |
|---|---|
| *Generate a hero image of a modern office with plants and save it in fileadmin* | `t3ai_generate_image` |
| *Find three free stock photos from Pexels of a team meeting* | `t3ai_generate_image` |

## Troubleshooting requests

- Start queue requests with *Queue …* rather than *Add … to the queue*. Some models read the word after *Add* as a page title and ask which page you mean.
- If the AI agent uses a generic record tool instead of T3AI (for example, *Change a record* fails with a JSON error), repeat the request with *Use T3AI to …*.
- Several related actions can go in one request, for example *Translate this page into German and queue it for Mass SEO*. Each change still needs its own **Apply**.
