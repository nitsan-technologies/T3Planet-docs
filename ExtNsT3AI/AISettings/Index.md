---
title: "More T3AI tools"
description: "Extra T3AI tools: AI solutions for TYPO3 system log errors, the RTE Co-Pilot preset, AI scraping protection in robots.txt, issue reports, and feature requests."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "System Log Solution"
  - "Co-Pilot"
  - "Block AI Scraping"
sidebarTitle: "More T3AI tools"
---

Settings, logs, and permissions moved to [Configuration](/en/latest/ExtNsT3AI/Configuration/Index): [AI Features cards](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index), [AI Usage & AI Logs](/en/latest/ExtNsT3AI/Configuration/AIUsageAndLogs/Index), and [Permissions](/en/latest/ExtNsT3AI/Configuration/Permissions/Index).

<a id="feature-settings"></a>
<a id="ai-logs"></a>
<a id="statistics"></a>
<a id="user-permissions"></a>
<a id="restrict-prompts"></a>

## System Log Solution

Get AI suggestions for errors in the TYPO3 system log.

1. In the [General Settings card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#general-settings), enable **Enable System Log Solution** and click **Save Changes**.
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

The AI bot rules are enabled by default and have no setting in the AI Features cards.

1. Open the **Sites** module, edit your site configuration, and go to **Static Routes**.

![Static routes in the site configuration](images/Scrappng.webp)

2. Add a static route of type **Static Text** for `robots.txt`.
3. Pick the bots to block from the value picker: GPTBot, Claude-Web, anthropic-ai, CCBot, FacebookBot, Google-Extended, PiplBot, or all of them.

![Select the AI bots to block](./images/Scrapping.webp)

4. Save the site configuration.

## Report an Issue

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfpg5l59022j130uk8ek60xr?embed_v=2&utm_source=embed" loading="lazy" title="Report an Issue" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## Suggest Features

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfpgljut032r130uobcgvex7?embed_v=2&utm_source=embed" loading="lazy" title="Suggest Features" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

If you find any issues or want to add any custom feature contact us at [Contact](https://t3planet.de/contact)

## TYPO3 AI Chatbot

Are you seeking help with TYPO3 code as a developer or integrator? Try the custom TYPO3 AI Chatbot: [T3AI - TYPO3 AI Chatbot](https://chatgpt.com/g/g-MDKrvyZk5-t3ai)

**Related:** [Configuration](/en/latest/ExtNsT3AI/Configuration/Index) · [Scheduler & CLI](/en/latest/ExtNsT3AI/Configuration/SchedulerAndCLI/Index) (`t3af:exception:solve`) · [Content](/en/latest/ExtNsT3AI/Content/Index)
