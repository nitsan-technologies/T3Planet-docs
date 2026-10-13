---
title: "T3AI Media"
description: "Create AI images with OpenAI, MidJourney, and Stability AI, or find free stock images on Unsplash, Openverse, Pixabay, and Pexels, and save them to a fileadmin folder with T3AI Media."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "T3AI Media"
  - "AI Credits"
sidebarTitle: "T3AI Media"
---

The **Media** tab of the AI Assistant module gets images into your fileadmin. You either **generate** a new image from a text prompt (OpenAI, MidJourney, Stability AI) or **search** free stock libraries (Unsplash, Openverse, Pixabay, Pexels). The image you pick is saved to a folder you choose.

Settings, permissions, AI agent tools, and logs for this feature are listed in [Settings, access and logs](#settings-access-and-logs).

## Requirements

Media API keys are added in two different places in AI Foundation:

| Image source | Where to add the API key |
|---|---|
| OpenAI Image | **AI Foundation > AI Providers**: OpenAI provider with the `image_generation` capability |
| MidJourney | **AI Foundation > AI Providers**: MidJourney provider |
| Stability AI | **AI Foundation > AI Providers**: Stability AI provider |
| Unsplash | **AI Foundation > AI Features > AI Media**, tab **Unsplash**: Unsplash Access Key |
| Openverse | **AI Foundation > AI Features > AI Media**, tab **Openverse**: Openverse Client ID and Client Secret |
| Pixabay | **AI Foundation > AI Features > AI Media**, tab **Pixabay**: Pixabay Access Key |
| Pexels | **AI Foundation > AI Features > AI Media**, tab **Pexels**: Pexels Access Key |

- **AI image sources** (OpenAI, MidJourney, Stability AI) use a connected provider or active [T3Planet Credits](/en/latest/ExtNsT3AF/T3Planet-Credit-System/Index). With credits, no provider API key is needed. See [AI provider & API keys](/en/latest/ExtNsT3AI/Configuration/AIProviders/Index).
- **Stock libraries** (Unsplash, Openverse, Pixabay, Pexels) are not providers. Their keys are entered only in the [AI Media card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-media).
- You need write access to the target fileadmin folder.

If no source is set up, the window shows "No image source is configured" with a pointer to AI Foundation > Providers.

## Available features

| Card | Button | What it does |
| --- | --- | --- |
| OpenAI Image | **Create AI Image** | Generates an image with OpenAI (DALL·E) |
| MidJourney | **Build AI Image** | Generates an image with MidJourney |
| Stability | **Craft AI Image** | Generates an image with Stability AI |
| Unsplash | **Get AI Image** | Searches Unsplash photos |
| Openverse | **Access Image** | Searches openly licensed images on Openverse |
| Pixabay | **Collect Image** | Searches Pixabay images |
| Pexels | **Get Image** | Searches Pexels photos |

All windows work the same way:

1. Go to **AI Universe > AI Assistant > Media** and click the card button.
2. In the folder tree of the window, select the folder where the image should be saved.
3. Enter a prompt (for AI sources) or search words (for stock libraries).
4. Set the options and click **Explore Images**.
5. Pick an image and click **Save**. Close the window with **Cancel**.

<a id="dall-e-ai-images"></a>

## OpenAI Image

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmraqpvtz1crwqmhxktl7vjx2?embed_v=2&utm_source=embed" loading="lazy" title="DALL-E AI Image" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Card **OpenAI Image**, button **Create AI Image**. Options:

- **Style**: None, Realistic, Painting, Sketch, Abstract, Photorealistic
- **Size**: 1024x1024, 1024x1792, 1792x1024
- **Number of Images**: 1, 3, or 5

## MidJourney AI Images

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmue6na4g09juqm4th7mc8v04?embed_v=2&utm_source=embed" loading="lazy" title="T3AI - Midjourney" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Card **MidJourney**, button **Build AI Image**. Describe the image in **Type your prompt here** and click **Explore Images**.

## Stability AI Images

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmraqyvk01egeqmhxy26psv3d?embed_v=2&utm_source=embed" loading="lazy" title="Stability AI" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Card **Stability**, button **Craft AI Image**. Enter the image prompt, click **Explore Images**, and save the result.

## Unsplash AI

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrar00ng1el4qmhxadb8be0z?embed_v=2&utm_source=embed" loading="lazy" title="Unsplash" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Card **Unsplash**, button **Get AI Image**. Enter search words and click **Explore Images** to browse matching Unsplash photos.

## Openverse AI

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmuf5hlb30mdaqmg17z3ayqg3?embed_v=2&utm_source=embed" loading="lazy" title="T3AI - Openverse" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Card **Openverse**, button **Access Image**. Searches free, openly licensed images.

- The lightbulb icon refines your search text with AI.
- **Size** filters by image size, for example **Small**.
- The second dropdown (**Use Default**) sets the number of results.

Check the license of the image before you use it.

## Pixabay

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmuf66m0s0n2yqmg1lhmk9e3s?embed_v=2&utm_source=embed" loading="lazy" title="T3AI - Pixabay" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Card **Pixabay**, button **Collect Image**. Enter search words, set the number of results in the **Use Default** dropdown, and click **Explore Images**.

## Pexels

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmuf687a00n8hqmg1ac4afhqa?embed_v=2&utm_source=embed" loading="lazy" title="T3AI - Pexels" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Card **Pexels**, button **Get Image**. Enter search words, choose the **Size** and the number of results, and click **Explore Images**.

## AI images in the Filelist and in records

In the **Filelist** module, the **AI Assistant** button in the module header lists the same image sources. The image is saved to the folder you have open.

Image fields in the TYPO3 backend, for example **Media** in the page properties or **Images** in a content element, have a **Generate AI Image with T3AI** button. It opens the same image window and adds the saved image to the field.

## Settings, access and logs

| Topic | Where |
|---|---|
| Opens in | **AI Assistant > Media**: OpenAI Image, MidJourney, Stability, Unsplash, Openverse, Pixabay, Pexels |
| Settings | [AI Media card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-media): toggles, storage folder, per-source settings, stock library keys. Image providers: [AI provider & API keys](/en/latest/ExtNsT3AI/Configuration/AIProviders/Index) |
| Permissions | **Media & Alt Texts**. See [Permissions](/en/latest/ExtNsT3AI/Configuration/Permissions/Index) |
| Ask AI agent | Generate an image. See [T3AI tools](/en/latest/ExtNsT3AI/AskAiAgent/Tools/Index#media) |
| Logs | AI Logs channel **AI Assistant Media**; AI Usage scope `image_generate`. See [AI Usage & AI Logs](/en/latest/ExtNsT3AI/Configuration/AIUsageAndLogs/Index) |

**Related:** [Content](/en/latest/ExtNsT3AI/Content/Index) · [Configuration](/en/latest/ExtNsT3AI/Configuration/Index)
