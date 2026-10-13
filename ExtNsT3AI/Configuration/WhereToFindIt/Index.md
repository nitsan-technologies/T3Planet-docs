---
title: "Where your old settings moved"
description: "Only for upgrades: T3AI no longer has an extension configuration in Admin Tools. Where each old ns_t3ai setting is now in AI Foundation."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "Extension configuration"
  - "Upgrade"
sidebarTitle: "Where your old settings moved"
---

In older versions, T3AI was configured in **Admin Tools > Settings > Configure extensions > ns_t3ai** (tabs such as AI Engine, SEO, Page, Content, Translation, AI Image). That screen no longer lists `ns_t3ai`. This page shows where each setting is now.

<Info>
New to T3AI? You can skip this page.
</Info>

## Where is my old setting?

| Old setting | Now |
|---|---|
| API keys and models for OpenAI, Gemini, Claude, Mistral, DeepL, Google Translate, Stability AI, MidJourney | [AI Foundation > AI Providers](/en/latest/ExtNsT3AI/Configuration/AIProviders/Index) |
| Default model and AI engine | Default provider in AI Providers, or **Default AI provider** on each T3AI card |
| Feature toggles: Optimize SEO, AI page creation, TCA record fields, exception handling, System Log Solution, RTE history count | [General Settings card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#general-settings) |
| SEO feature, SERP view, content analysis type, number of results, schema, automatic SEO for new AI pages | [AI SEO card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-seo) |
| Page feature | [AI Pages card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-pages) |
| Content feature, tone, type of content | [AI Content card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-content) |
| Translation feature, Auto Page Translate, default translation model, FlexForm fields to skip, DeepL Official Glossary | [AI Translation card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-translation) |
| AI Image: number, size, style, storage folder, Stability mode and format, Unsplash, Openverse, Pixabay, and Pexels keys | [AI Media card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-media) |
| Basic Auth username and password | [Access & Notifications card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#access-and-notifications) |
| Block AI Scraping/Crawling | No setting in AI Features. The bot presets are offered in the site's Static Routes by default. See [Block AI Scraping](/en/latest/ExtNsT3AI/AISettings/Index#block-ai-scraping). |
| T3AI module > AI Logs and Statistics | [AI Usage & AI Logs](/en/latest/ExtNsT3AI/Configuration/AIUsageAndLogs/Index) |
| Backend user group custom options for T3AI | [Permissions](/en/latest/ExtNsT3AI/Configuration/Permissions/Index) |

## After an upgrade

1. Open **AI Foundation > AI Providers** and check that your providers show **Connected**.
2. Open each T3AI card in **AI Foundation > AI Features**, check the values, and click **Save Changes**.
3. Review your editor groups in **AI Foundation > AI Permissions**.
4. Check the **AI Foundation** tab of the **AI Assistant** module for open setup steps.

The full migration is described in [Reinstall After Upgrading to Extension v14.x.x](/en/latest/ExtNsT3AI/ReInstallEverything/Index).

**Related:** [Configuration](/en/latest/ExtNsT3AI/Configuration/Index) · [Update & Upgrade](/en/latest/ExtNsT3AI/UpgradeGuide/Index)
