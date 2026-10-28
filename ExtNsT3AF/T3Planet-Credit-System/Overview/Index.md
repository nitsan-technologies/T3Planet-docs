---
title: "Overview"
description: "Documentation for Overview (ExtNsT3AF)."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "ExtNsT3AF"
sidebarTitle: "Overview"
---

## Purpose

Explain what AI Credits is and when to use it.

## What it is

AI Credits is T3Planet’s managed AI access in AI Foundation (`ns_t3af`):

- You do **not** need your own OpenAI / Anthropic / similar keys for billable AI
- AI Foundation sends those calls to T3Planet
- Usage is counted in **credits**

<Tip>
**You can buy credits from the TYPO3 backend too.** Open **AI Foundation → AI Providers** and use **AI Credit Bundles**. See [Buy credits](/en/latest/ExtNsT3AF/T3Planet-Credit-System/BuyCredits/Index).
</Tip>

## Requirements

- AI Foundation (`EXT:ns_t3af`) installed and active
- Your name and email, if TYPO3 asks for them when you start the free trial (no licence key)
- A **claim code** only if you bought credits on t3planet.de or you are recovering an account. See [Use a claim code](/en/latest/ExtNsT3AF/T3Planet-Credit-System/ClaimCode/Index)

## What’s covered

When Credits is active, it can cover:

- Text completion
- Streaming
- Embeddings
- Text-to-speech (TTS)
- Image generation

## Own API Keys vs Credits

|  | Own API Keys | AI Credits |
| --- | --- | --- |
| Your API keys | Required | Not used for AI calls |
| Who runs AI | Vendor API (direct) | T3Planet |
| Providers UI | Shows provider list | Hides list; shows Credits panels |
| AI Usage id | Your provider id | `t3planet_credits` |

## Selected vs Active

- **Selected** — Credits card chosen; no access token yet. Click **Activate** (free trial) or [use a claim code](/en/latest/ExtNsT3AF/T3Planet-Credit-System/ClaimCode/Index) (credits you bought) to finish setup.
- **Active** — The site is connected to a credits account and the access token is stored. AI can run through Credits. No licence key is involved.

## Where credits come from

- Free trial credits when you click **Activate**
- Plans and top-ups bought in the backend: [Buy credits](/en/latest/ExtNsT3AF/T3Planet-Credit-System/BuyCredits/Index)
- Credits bought on [t3planet.de/ki-credits](https://t3planet.de/ki-credits) and connected with a claim code: [Use a claim code](/en/latest/ExtNsT3AF/T3Planet-Credit-System/ClaimCode/Index)

## When to use Credits

- You want AI without managing vendor keys
- You want one credit balance across all your installs

Use Own API Keys when you already manage vendor keys yourself.

## What uses credits

Credits are used when Credits is **active** and an AI Foundation AI call
completes successfully through T3Planet.

Opening modules or only switching the card does **not** use credits.

## Switch modes

**Turn on**

1. Open AI Foundation > AI Providers
2. Choose AI Credits
3. Click Activate if shown
4. Success message → page reload

**Turn off**

1. Choose Your Own API Keys
2. Confirm if asked
3. Provider list appears again

<Tip>
Switching off does not delete the stored Credits token. It only turns Credits
off.
</Tip>
