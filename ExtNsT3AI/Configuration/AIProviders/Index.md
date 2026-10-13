---
title: "AI provider & API keys"
description: "Choose the AI Provider Mode, add the AI providers T3AI uses for text, translation, and images, and set the default provider in AI Foundation."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "AI Providers"
  - "API keys"
sidebarTitle: "AI provider & API keys"
---

T3AI has no API key fields of its own. All T3AI features use the providers in **AI Universe > AI Foundation > AI Providers**.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrbo0w7i0d96qmo57ifnabvz?utm_source=link" loading="lazy" title="T3AF Providers Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## Step 1: Choose the provider mode

**AI Provider Mode** applies to all T3AI features:

- **Your Own API Keys**: T3AI uses the providers you add with your own API keys. Keys are encrypted at rest.
- **T3Planet Credits**: T3AI uses T3Planet's hosted AI infrastructure with prepaid credits, so you need no API keys. See [T3Planet Credits](/en/latest/ExtNsT3AF/T3Planet-Credit-System/Index).

## Step 2: Add your providers

1. Click **New Provider**.
2. Enter an identifier and a display name, then select the **Adapter type**.
3. Enter the **API key** and the chat or completion model.
4. Select the capabilities the provider may use, for example `image_generation` for AI images.
5. Click **Save Provider** and check that the **Connection** column shows **Connected**.

Add one provider for each T3AI feature group you use:

| T3AI feature | Adapter types |
|---|---|
| Pages, Content, SEO, AI agent, LLM-based translation | OpenAI, Anthropic, Gemini, Mistral, Azure OpenAI, OpenRouter, Ollama, Meta, Hugging-face, Open-responses, Custom / Other |
| Translation with a dedicated engine | DeepL Translate, Google Translate |
| AI images | OpenAI (with the `image_generation` capability), Stability AI, MidJourney |

<Note>
Stock image libraries (Unsplash, Openverse, Pixabay, Pexels) are not providers. Their keys are entered in the [AI Media card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-media).
</Note>

## Step 3: Set the default provider

Enable **Set as Default Provider** on the provider that T3AI should use when a feature has no provider of its own. Each T3AI card in AI Features can override it with its own **Default AI provider**.

Fields, capabilities, testing, and import are described in [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index).

## Where to get API keys

- [OpenAI](https://platform.openai.com/api-keys)
- [Anthropic (Claude)](https://console.anthropic.com/)
- [Google Gemini](https://aistudio.google.com/apikey)
- [Mistral](https://console.mistral.ai/)
- [Azure OpenAI](https://portal.azure.com/)
- [DeepL](https://support.deepl.com/hc/en-us/articles/360020695820-API-Key-for-DeepL-s-API)
- [Google Translate](https://cloud.google.com/docs/authentication/api-keys)
- [Stability AI](https://platform.stability.ai/account/keys)
- [MidJourney](https://docs.midjourney.com/)
- Stock images: [Unsplash](https://unsplash.com/developers), [Openverse](https://api.openverse.org/v1/), [Pixabay](https://pixabay.com/api/docs/), [Pexels](https://www.pexels.com/api/)

**Related:** [AI Features cards](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index) · [AI Usage & AI Logs](/en/latest/ExtNsT3AI/Configuration/AIUsageAndLogs/Index) · [AI Providers in AI Foundation](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)
