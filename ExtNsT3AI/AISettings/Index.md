---
title: "T3AI Features"
description: "Review and configure T3AI feature groups in AI Foundation, monitor AI Logs, and set up Co-Pilot, AI scraping protection, and editor permissions."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "AI Settings"
  - "T3AI Features"
  - "AI Logs"
sidebarTitle: "T3AI Features"
---

T3AI Features help administrators review which AI-powered capabilities are active and how they are configured for page, content, SEO, translation, media, and assistant workflows.
Use this section after installation, after an update, or before enabling new editor workflows.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrabnhz30bh0qmhx012m66o5?utm_source=link" loading="lazy" title="T3AI Features" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## Overview

Use this area to confirm which T3AI features are available in your project and whether the shared AI Foundation setup is ready.
For provider selection, model setup, and shared AI rules, also review [AI Foundation Configuration](/en/latest/ExtNsT3AF/Configuration/Index), [AI Foundation Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index), and [AI Foundation AI Features](/en/latest/ExtNsT3AF/Configuration/AIFeatures/Index).

## Key capabilities

- Review enabled T3AI feature groups
- Confirm the project is connected to the right provider and model setup
- Check whether editors can use the expected modules before rollout

## Basic workflow

T3AI feature settings are managed in AI Foundation — not under **Admin Tools > Settings > Configure Extensions**.

1. Go to the **TYPO3 backend**.
2. Open **AI Foundation** → **AI Features**.
3. Open the **T3AI** (`ns_t3ai`) feature card.
4. Review the available feature settings and defaults.
5. Confirm the required feature options are enabled.
6. Click **Save**, then test the related T3AI modules.

For the shared module overview, see [AI Foundation AI Features](/en/latest/ExtNsT3AF/Configuration/AIFeatures/Index).

## Feature settings

The T3AI feature card groups its settings as follows.

| Group | What you configure |
|---|---|
| Feature toggles | Enable or disable the SEO, Page, Content, Translation, and Media feature groups, plus AI Sidebar, AI-SEO optimization, AI page creation, TCA record field generation, System Log Solution, and the maximum RTE history count |
| SEO | Default provider and SEO feature, default SERP snippet view (Desktop or Mobile), content type for content analysis, number of suggestions per field (topic, page title, description, keywords, OG title, OG description), schema and the news detail page ID used for news schema, automatic SEO metadata for new AI pages |
| Page | Default provider and Pages feature |
| Content | Default provider and Content feature, tone, and type of content |
| Translation | Default provider and Translation feature, Auto Page Translate, default model for auto-translate, re-translate, and mass translation, and the DeepL official glossary |
| Media | Number of images, image size and style, default storage folder, items per page for stock libraries, Stability AI generate mode and format, and access keys for Unsplash, Openverse, Pixabay, and Pexels |

<Note>
API keys for AI providers — including OpenAI, Gemini, Claude, DeepL, MidJourney, and Stability AI — are configured once in [AI Foundation → AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index), not in T3AI.
</Note>

## AI Logs

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrbpsdl20frlqmo521y5if8m?utm_source=link" loading="lazy" title="T3AI AI Logs Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

AI Logs help you monitor requests made by T3AI modules.
Use this section to review successful and failed AI requests, identify which module initiated a request, and troubleshoot issues during development, testing, or production use.

To review AI Logs:

1. Open the **T3AI** module in the TYPO3 backend.
2. Select **AI Logs**.
3. Use the available filters, such as **AI Provider**, **Model**, or **Module**, to narrow down the results.
4. Review individual log entries to inspect request details, responses, and possible errors.
5. Reset the filters at any time to display the complete log history.

## Statistics

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfnzchrg19yk1d3nfyx5nru0?embed_v=2&utm_source=embed" loading="lazy" title="T3AI Statistics" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Access all your AI model analytics in one place with predefined AI model statistics.

## System Log Solution

Get AI suggestions for errors in the TYPO3 system log.

1. In the T3AI feature card, enable **Enable System Log Solution** and save.
2. Open the **System** module and go to **Log**.

![System log](./images/Log_2.webp)

3. Open a log entry and click **AI suggestion**.

![AI suggestion in the system log](./images/Log_3.webp)

4. Click the button to have the AI suggest solutions for the system log error.

![AI solution for a system log error](./images/Log_4.webp)

## T3AI Co-Pilot

The **T3AI Co-Pilot** is your easy-to-use AI assistant in TYPO3. It helps you write, improve, translate, and optimize content quickly - all directly in the backend with just a few clicks.

**Step 1:** Click on Edit Page property

**Step 2:** Go to tab **“Resources”**

**Step 3:** Include **NS t3ai :: Config RTE Preset (ns_t3ai)** in **Include static Page TSconfig (from extensions)** and Save this.

![Co-Pilot configurations](./images/Co-pilot_image.webp)

![RTE Co-Pilot](./images/t3ai-co-pilot.webp)

## Block AI Scraping

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfph5l5q03ea130uj100dsfm?embed_v=2&utm_source=embed" loading="lazy" title="Block AI Scraping" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Protect your website’s content from AI crawlers with ready-made `robots.txt` rules.

1. Enable **Block AI Scraping/Crawling** in the T3AI settings.
2. Open the **Sites** module, edit your site configuration, and go to **Static Routes**.

![Static routes in the site configuration](images/Scrappng.webp)

3. Add a static route of type **Static Text** for `robots.txt`.
4. Pick the bots to block from the value picker: GPTBot, Claude-Web, anthropic-ai, CCBot, FacebookBot, Google-Extended, PiplBot, or all of them.

![Select the AI bots to block](./images/Scrapping.webp)

5. Save the site configuration.

## User Permissions

You can grant editors or users access to specific features of T3AI using the custom permission settings. For AI Foundation module access and per-group credit limits, see [AI Permissions](/en/latest/ExtNsT3AF/Configuration/AIPermissions/Index).

![Backend user groups](./images/per1.webp)

- **Step 1:** Navigate to the Backend Users module in the TYPO3 backend.
- **Step 2:** Select the Backend User Group.
- **Step 3:** Edit the user group.

![Edit backend user group](./images/per2.webp)

- **Step 4:** Go to tab **Access Rights**.

You can enable or restrict access to specific modules for editor users.

To grant more granular control, you can also allow specific features within a particular module for editor users.

![Module access for T3AI](./images/per3.webp)

![Feature access for T3AI](./images/per4.webp)

## Restrict Prompts

To prevent editors from adding, editing, or deleting prompts (SEO prompts, Page prompts, and so on), exclude prompt management when you configure the editor users or user groups.

With integrator-level access, manage prompts as described in [Prompts](/en/latest/ExtNsT3AI/Prompts/Index).

## Report an Issue

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfpg5l59022j130uk8ek60xr?embed_v=2&utm_source=embed" loading="lazy" title="Report an Issue" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## Suggest Features

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfpgljut032r130uobcgvex7?embed_v=2&utm_source=embed" loading="lazy" title="Suggest Features" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

If you find any issues or want to add any custom feature contact us at [Contact](https://t3planet.de/contact)

## TYPO3 AI Chatbot

Are you seeking help with TYPO3 code as a developer or integrator? Try the custom TYPO3 AI Chatbot: [T3AI - TYPO3 AI Chatbot](https://chatgpt.com/g/g-MDKrvyZk5-t3ai)
