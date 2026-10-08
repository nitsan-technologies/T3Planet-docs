---
title: "T3Planet Credits"
description: "T3Planet Credits — managed AI access for AI Foundation without storing your own vendor API keys."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "ExtNsT3AF"
  - "Credits"
  - "BYOK"
sidebarTitle: "T3Planet Credits"
---

**T3Planet Credits** lets you use AI without your own account at OpenAI, Anthropic or another AI service. You buy credits from T3Planet, and T3Planet runs the AI requests for you. You don't need to manage any API keys.

**Path:** **AI Universe → AI Foundation → AI Providers**

<Note>
On **AI Providers** you choose between **Your Own API Keys** (the default) and **T3Planet Credits**.
</Note>

![AI Foundation Dashboard in T3Planet Credits mode with balance, credit burn, and spend by extension](images/t3planet-credits-dashboard.webp)

*Dashboard — **T3Planet Credits** mode with remaining balance, credit burn over time, and spend by extension.*

## Where to configure it

1. Go to **AI Universe → AI Foundation → AI Providers**.
2. Choose **T3Planet Credits**.
3. Click **Activate** if it is shown.

Until you do this, **Your Own API Keys** stays the default. Full steps: [Configuration](/en/latest/ExtNsT3AF/T3Planet-Credit-System/Configuration/Index).

## What it is

- An optional add-on for AI Foundation. It pays for AI use only.
- You get **50 credits** once when you sign up.
- One shared credit balance for this TYPO3 installation.
- You see the balance on the **Dashboard** and in the Credits panel on **AI Providers**.
- Credits are only used when an AI request runs through T3Planet.
- Each request is listed in **AI Usage** (provider `t3planet_credits`).

## What it is not

- Not the default setup mode
- Not required when you use your own API keys
- Not a license for AI Foundation

## BYOK vs T3Planet Credits

- **Your Own API Keys** (BYOK, "bring your own key" – the default) – your server sends requests directly to the AI service you set up.
- **T3Planet Credits** (optional) – T3Planet sends your requests to AI services for you. Credits pay for the use.

Your own providers stay saved while Credits is on. They come back when you switch back to **Your Own API Keys**.

## Licensing and billing

- AI Foundation is 100% OSS (GPL-2.0-or-later)
- Activate the OSS license key via **T3Planet Shop** > **AI Universe** > **AI Foundation** > **Start**
- T3Planet Credits covers AI usage only
- Credits never replace the OSS license key
- Plan credits never roll over

## What's covered

When Credits is active:

- Text completion
- Streaming
- Embeddings
- Text-to-speech (TTS)
- Image generation

## When to use it

- **Credits** – editors need AI quickly, without setting up API keys.
- **Your Own API Keys** – you already have accounts and keys with AI services.

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

**T3Planet Credits** is T3Planet’s managed AI access for AI Foundation. Use it when you want AI features **without storing or managing your own vendor API keys**.

When Credits is active, billable AI requests go to T3Planet. T3Planet runs the AI work and reduces your credit balance. In **AI Usage**, those requests are stored with provider id `t3planet_credits`.

**Path:** **AI Foundation > AI Providers**

<Note>
On **AI Providers** choose **Your Own API Keys** or **T3Planet Credits**.
</Note>

- Optional add-on for AI Foundation
- Pays for AI usage only
- Does not replace the OSS license key
- Credits are used only when billable AI requests run through T3Planet
- You'll receive 50 credits once upon signup
- One shared credit balance for this installation
- Balance on the Dashboard and AI Providers Credits panel
- Usage history in **AI Usage** (provider `t3planet_credits`)

**BYOK / Your Own API Keys (default)** — Your TYPO3 server sends prompts directly to the provider you configure.

**T3Planet Credits (optional)** — T3Planet routes your content to third-party model providers on your behalf. Credits pay for usage only.

When Credits is active, billable AI requests go to T3Planet and reduce your credit balance. Saved BYOK providers stay in the database and return when you switch back to **Your Own API Keys**.

1. Open **AI Foundation > AI Providers**.
2. Choose **T3Planet Credits**.
3. Complete **Activate** if shown.

Default stays **Own API Keys** until you select Credits and finish activation.

Use Credits when editors need AI quickly without key setup.

Use Own API Keys when you already manage vendor accounts and keys yourself.
*/}
