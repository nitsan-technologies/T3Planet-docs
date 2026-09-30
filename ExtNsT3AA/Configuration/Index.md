---
title: "Configuration"
description: "T3AA uses AI Foundation for shared provider setup, model selection, prompts, and core AI services. Complete the parent setup first, then review the T3AA-specific options below."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AA"
sidebarTitle: "Configuration"
---

T3AA uses AI Foundation for shared provider setup, model selection, prompts, and core AI services.
Complete the parent setup first, then review the T3AA-specific options below.

Helpful AI Foundation references:

- [AI Foundation Configuration](/en/latest/ExtNsT3AF/Configuration/Index)
- [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)
- [AI Features](/en/latest/ExtNsT3AF/Configuration/AIFeatures/Index)
- [AI Prompts](/en/latest/ExtNsT3AF/AIPrompts/Index)
- [AI Usage and Logs](/en/latest/ExtNsT3AF/AIUsageAndLogs/Index)

## Step 1: Open AI Features in AI Foundation

All T3AA feature settings are managed in AI Foundation — not under **Admin Tools > Settings > Configure Extensions**.

Open **AI Foundation** → **AI Features**. The T3AA settings are split over
three cards with the tag **AI Accessibility**:

| Card | Subtitle | What it controls |
| --- | --- | --- |
| **General Settings** | PageSpeed, editor | Google PageSpeed API key, licensed audit screenshots, frontend widget, simplify prompt, Live Audit for CKEditor |
| **AI Audio** | Voiceover & storage | Audio and voiceover features, storage folder |
| **AI File Meta** | Image metadata & alt text | AI alt text and image metadata |

Use the extension filter or the search field to show only the AI Accessibility
cards. Click **Configure** on a card to open its settings.

For the shared module overview, see [AI Foundation AI Features](/en/latest/ExtNsT3AF/Configuration/AIFeatures/Index).

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmral44e20xqkqmhxbcch9g65?utm_source=link" loading="lazy" title="AI FileMeta Overview Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## Step 2: Review Shared Provider Setup

Provider credentials and shared model setup belong to AI Foundation, not to T3AA.
Before testing T3AA, confirm that the required provider is already configured in the parent extension.
This includes ElevenLabs: add it as a provider (adapter type **ElevenLabs**)
with your own ElevenLabs API key. ElevenLabs is not available in T3Planet
Credits mode.

Common provider-related references:

- [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)
- [AI Foundation Configuration](/en/latest/ExtNsT3AF/Configuration/Index)

## Step 3: Feature-Specific Configuration Options

### General Settings

| Option | What it does |
| --- | --- |
| **Google Page Speed API** | Your Google PageSpeed Insights API key. Required for [Lighthouse](/en/latest/ExtNsT3AA/FeatureGuide/Scans/Lighthouse/Index). Without a key, Lighthouse scans cannot run. The page URL is sent to Google, so Google must be able to reach it. |
| **Include screenshots in licensed accessibility audits** | When enabled, licensed [Scanner](/en/latest/ExtNsT3AA/FeatureGuide/Scans/Scanner/Index) audits include screenshots of the findings. When disabled (default), audits run without screenshots. |
| **Enable Assistant Widget** | Shows the frontend accessibility widget on the website. The value is saved per site (in the site configuration of the site you work on). Configure the widget itself in [Accessibility Widgets](/en/latest/ExtNsT3AA/FeatureGuide/AccessibilityWidgets/Index). |
| **Default Content Prompts** → **Default AI Prompt for Content Simplify** | Prompt used by [Simplified Text](/en/latest/ExtNsT3AA/FeatureGuide/SimplifiedText/Index). Keep **Default (built-in)** or choose a prompt from [AI Prompts](/en/latest/ExtNsT3AF/AIPrompts/Index). |
| **Live Audit for CKEditor** | Runs accessibility checks inside the CKEditor (RTE) while editors write. Flush the TYPO3 caches after enabling or disabling it. |

### AI Audio

| Option | What it does |
| --- | --- |
| **Enable/Disable AI Audio features** | Turns the audio features on or off one by one: **AI Audio** (audio from a script), **Elevenlab AI Voiceover** and **Open AI Voiceover** (page voiceovers). All three are enabled by default. |
| **Storage** (**Voiceover audio storage folder**) | Folder in the File List where generated audio and voiceover files are saved. |

See [AI Audio](/en/latest/ExtNsT3AA/FeatureGuide/AIAudio/Index) and
[AI Voiceover](/en/latest/ExtNsT3AA/FeatureGuide/AIVoiceover/Index).

### AI File Meta

| Option | What it does |
| --- | --- |
| **Activate Feature Ai-Metadata for Images** | Turns on AI file metadata for images, including the **Generate file meta with T3AA** button in the file metadata form. |
| **Only alternative text generation** | Generates alternative text only. Title and description are not generated. |
| **Default Ai-Filemeta generate Model** | Default generator for file metadata with your own API keys: `vision-ai` (Vision via your AI provider) or `altText-ai` (AltText.ai). In AI Credits mode this setting is ignored: T3AA always uses Vision through T3Planet Credits. |
| **Enable AI file metadata generation when uploading files with TYPO3 Core.** | Generates metadata automatically when a new file is added through TYPO3 Core (for example an upload in the File List). It uses the **Default Ai-Filemeta generate Model**. |
| **Alternative Text Length** | **short** (default) for brief alt text, **long** for detailed alt text. |
| **Select Default File Metadata Feature** | Prompts used for file metadata: **Default AI Prompt for File Alt Text Short**, **Default AI Prompt for File Alt Text Long** and **Default AI Prompt for File Meta Title Description**. Keep **Default (built-in)** or choose a prompt from [AI Prompts](/en/latest/ExtNsT3AF/AIPrompts/Index). |

See [AI Alt Text](/en/latest/ExtNsT3AA/FeatureGuide/AIAltText/Index).

## Step 4: Save the Configuration

Click **Save** in each card after you change its options.

<Note>
If a T3AA feature does not run, first check the shared provider setup in **AI Foundation > AI Providers** before changing feature settings.
</Note>

## Using T3AA with AI Credits

T3AA works with both provider modes in **AI Foundation → AI Providers**:

- **AI Credits** — no API keys needed. T3AA sends its AI requests to T3Planet, and each request reduces your credit balance. In T3AA dialogs, **Select AI Provider** shows only **T3Planet Credits**.
- **Your Own API Keys** — T3AA uses the providers you add in AI Foundation. Your AI vendor bills you directly.

See [AI Credits](/ExtNsT3AF/T3Planet-Credit-System/Index).

### Scan page quota and AI credits

These are two separate limits:

| | Scan page quota | AI credits |
| --- | --- | --- |
| Comes from | Your T3AA license | Your AI Credits balance in AI Foundation |
| Used by | Scanner and Bulk Scans. Each scanned page counts as one page. | T3AA AI features, only in **AI Credits** mode |
| Shown in | T3AA Dashboard, Scanner and Bulk Scans (**Pages scanned**, **Pages remaining**, **Page limit**) | AI Foundation Dashboard and AI Providers (balance), AI Usage (each request) |

Scans never use AI credits, and AI features never reduce the scan page quota.

### What uses AI credits

In **AI Credits** mode:

| T3AA action | Uses AI credits | AI requests |
| --- | --- | --- |
| Image metadata ([AI Alt Text](/ExtNsT3AA/FeatureGuide/AIAltText/Index), **Generate file meta with T3AA**, **Mass AI Filemeta**, generation on upload) | Yes | One for the alternative text and one for title and description. With **Only alternative text generation**: one. |
| [Simplified Text](/ExtNsT3AA/FeatureGuide/SimplifiedText/Index) | Yes | One per simplification |
| [Fix Hub](/ExtNsT3AA/FeatureGuide/FixHub/Index) **AI Solution** | Yes | One per solution |
| [AI Voiceover](/ExtNsT3AA/FeatureGuide/AIVoiceover/Index) and [AI Audio](/ExtNsT3AA/FeatureGuide/AIAudio/Index) | Yes | One per generated audio file (always OpenAI) |
| Scanner and Bulk Scans | No | Uses the scan page quota |
| Lighthouse | No | Uses your Google PageSpeed API key |
| Accessibility Widgets, Live Audit for CKEditor | No | — |

ElevenLabs is not available in AI Credits mode. It needs your own ElevenLabs API key.

### Credit cost

T3AA actions have no fixed credit price. Each request is metered: the cost depends on how much text or image data the AI model processes. For example, simplifying a long text costs more than a short one. T3Planet sets the rates. The **AI Credits** panel in **AI Foundation → AI Providers** shows the minimum charge per request.

To see what an action really costs:

- **AI Foundation → AI Usage** lists each request with its **Credits** value (provider `t3planet_credits`).
- The **AI Foundation Dashboard** shows credit burn over time and spend by extension.

Run an action on one record first and check AI Usage before you start bulk jobs.

## AI Features

T3AA focuses on accessibility and content-support workflows that build on the shared AI Foundation setup.
Use these features when you want to improve metadata, accessibility support, and editor assistance without repeating the same manual tasks.

Key T3AA capabilities include:

- AI file metadata and alt-text generation
- AI audio generation and voiceover support
- Simplified text for easier reading
- CKEditor accessibility checks while editing
- Performance and accessibility-related support features

For shared model behavior and feature routing, see [AI Foundation AI Features](/en/latest/ExtNsT3AF/Configuration/AIFeatures/Index).

## AI Prompts

T3AA can use shared AI prompts from AI Foundation to keep metadata, audio, accessibility, and page suggestions consistent across your TYPO3 project.
Customize prompts when you want stricter writing rules, clearer accessibility wording, or reusable instructions for repeated editor tasks.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrborirv0dr9qmo5w1fothof?utm_source=link" loading="lazy" title="T3AA AI Prompts Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Best practices:

- Keep prompts short and task-specific.
- Test prompt changes with one real record before wider use.
- Review [AI Foundation AI Prompts](/en/latest/ExtNsT3AF/AIPrompts/Index) when you want shared prompt control across multiple AI Foundation extensions.

## AI Usage

Use AI Usage to review token and request activity generated by T3AA features.
This helps teams understand how often metadata, audio, and accessibility-related AI actions are being used.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrascwby1i72qmhxfeue5to5?utm_source=link" loading="lazy" title="T3AA AI Usage Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## AI Logs

Use AI Logs to inspect individual T3AA requests when you need to debug output, check failures, or review what happened during metadata and audio generation.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrase4m61ib5qmhxmxn7g5j8?utm_source=link" loading="lazy" title="T3AA AI Logs Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## Providers & MCP Tools

T3AA depends on the shared provider and MCP setup from AI Foundation.
Use this area to confirm the correct AI provider is available and to review any MCP tools that support connected automation workflows.

See also:

- [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index)
- [MCP Server](/en/latest/ExtNsT3AF/MCPServer/Index)
- [MCP Tools](/en/latest/ExtNsT3AF/MCPTools/Index)

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmral5ln50xu7qmhx0cqoj5mu?utm_source=link" loading="lazy" title="T3AA Providers and MCP Tools Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>
