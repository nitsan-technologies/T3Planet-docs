---
title: "AI Features"
description: "AI Features for EXT:ns_t3af (T3AF)."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AF"
  - "ns_t3af"
sidebarTitle: "AI Features"
---

## Purpose

**AI Features** has a settings card for each installed AI extension. Here you can, for example, use a cheap and fast AI model for routine SEO work and a better model for important pages.

**Path:** **AI Universe → AI Foundation → AI Features**

![AI Features cards for extension-level AI settings](./images/ai-features.webp)

<Note>
The cards only appear when an AI extension is installed, for example:

- [AI Assistant](https://t3planet.de/t3ai-typo3-erweiterung)
- [AI Chatbot](https://t3planet.de/t3ac-typo3-erweiterung)
- [AI Search](https://t3planet.de/t3as-typo3-erweiterung)
- [AI Accessibility](https://t3planet.de/t3aa-typo3-erweiterung)

Set a default provider in [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index) first. Then change it for single features here.
</Note>

## How to configure

1. Go to **AI Universe → AI Foundation → AI Features**.
2. Click **Configure** on a card.
3. Choose a provider for a feature, or leave it empty to use the default provider.
4. Click **Save**.
5. Test one request in the AI extension.
6. Check the costs in [AI Usage & Logs](/en/latest/ExtNsT3AF/Configuration/AIUsageAndLogs/Index).

## Feature types

- **SEO** — Meta data, keywords, schema-related tasks
- **Pages** — Page creation and structure
- **Content** — Text generation and rewriting
- **Translation** — Language conversion

## Resolution order

Which AI service is used? AI Foundation checks in this order:

1. The provider the editor picked in the AI window (if any).
2. The provider set for this feature on **AI Features**.
3. The default provider from [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index).

## When to use per-feature providers

- **Small team** – leave the features empty and use the default only.
- **Large team** – a cheap model for routine tasks, a premium model for important pages.
- **Multilingual website** – a model that is strong in German for **Translation**, a fast model for SEO.

## Example setup

- **SEO** — Fast, cost-effective model (for example Gemini Flash or GPT-4o-mini)
- **Pages** — Premium model (for example Claude Sonnet or GPT-4o)
- **Content** — Balanced model for everyday editing
- **Translation** — Model strong in German and English

## Why this matters for cost

Without these settings, every task uses the default model – often the most expensive one. Using a smaller model for SEO texts can cut monthly costs a lot.

## Scenario: agency with dev and live keys

Use global default for staging. On production, set SEO to a fast model and Pages to premium. Dev team keeps separate provider rows in [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index) with dev API keys.

## Related

- [AI Search: AI Features cards](/en/latest/ExtNsT3AS/Configuration/AIFeatures/Index) and [AI Chatbot: AI Features cards](/en/latest/ExtNsT3AC/Configuration/AIFeatures/Index) – the four **AI Chatbot/Search** cards
- [AI Permissions](/en/latest/ExtNsT3AF/Configuration/AIPermissions/Index) – who may change these settings

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

Assign **different AI providers** per task type. Use a fast cheap model for bulk SEO work and a premium model for important pages.

**Path:** T3AF > AI Features

AI Features — extension cards for per-feature settings and provider overrides.

<Note>
Use **AI Features** only when at least one child extension is installed. This module displays the per-feature settings that child extensions register. Examples:

If no child extension is connected, the feature list stays empty or incomplete. Set a global default provider in [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index) first, then override providers for individual features on this page.
</Note>

When an AI request runs, T3AF picks the provider in this order:

1. Provider chosen in the UI modal (if the editor selected one)
2. **Feature default** from this page
3. **Global default** provider from [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)

**Small team** — Leave feature defaults empty. Use the global default only.

**Large team** — Cheap model for bulk tasks; premium model for key landing pages.

**Multilingual site** — Strong German model for Translation; fast model for SEO meta fields.

Without per-feature settings, every task uses the most expensive default. Routing SEO meta generation to a smaller model can cut monthly spend significantly while keeping premium quality where it counts.

1. Open T3AF > AI Features
2. For each feature row, select a provider (or leave empty for global default)
3. Save
4. Test one request per feature type from a connected extension
5. Review token usage in [AI Usage & Logs](/en/latest/ExtNsT3AF/Configuration/AIUsageAndLogs/Index)
*/}
