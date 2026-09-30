---
title: "FAQ"
description: "Frequently asked questions about T3AI (EXT:ns_t3ai) for TYPO3."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "FAQ"
sidebarTitle: "FAQ"
---

Short answers to common questions about the AI Assistant (T3AI). For licenses, trials, staging, Composer and support, see the [general FAQ](/en/latest/FAQ/Index).

## Product and setup

### Is T3AI available as a free TYPO3 extension?

No. T3AI is a premium extension with no free version, and it is not distributed through the TYPO3 Extension Repository (TER). Test it with the 30-day free trial, then buy a license for your production domain.

### What does T3AI need to run?

AI Foundation (`EXT:ns_t3af`, free), the T3Planet Shop module (`EXT:ns_license`) with an active T3AI license, and an AI provider configured in AI Foundation. Full list: [System Requirements](/en/latest/ExtNsT3AI/SystemRequirements/Index).

### Which TYPO3 and PHP versions are supported?

TYPO3 12.4 LTS, 13.4 LTS and 14.x with PHP 8.2 or higher, the same range as AI Foundation.

## Translation

### Can T3AI translate my pages and content?

Yes. T3AI translates a page in one click, translates many pages at once (also recursively), and translates news and other records. A language glossary keeps your terms consistent. See [Translation](/en/latest/ExtNsT3AI/Translation/Index).

### Should I use T3AI or T3AL to translate my website?

T3AI. It translates your pages and content. AI Localization (T3AL) only translates the label files (XLIFF) of TYPO3 extensions, which is a developer task.

## Providers and data

### Which AI model does T3AI use, and where does the data go?

The provider you set up in AI Foundation. With your own API keys (the default), requests go from your server to that provider, with no T3Planet server in between. With the optional [AI Credits](/en/latest/ExtNsT3AF/T3Planet-Credit-System/Index), requests are routed through T3Planet to the AI providers. Details: [DPA & GDPR](/en/latest/ExtNsT3AI/DPAandGDPR/Index).

## Troubleshooting

### New prompts from an update do not show up

Synchronize the AI prompts after the update. Back up your database first: the sync overwrites custom prompts, so note them down and add them again afterwards. Steps: [Known Problems](/en/latest/ExtNsT3AI/KnownProblems/Index).

### Something else is not working

Open a ticket at [t3planet.de/support](https://t3planet.de/support) with your TYPO3, PHP and T3AI versions and the exact error text.

Product page: [t3planet.de/en/t3ai-typo3-extension](https://t3planet.de/en/t3ai-typo3-extension)
