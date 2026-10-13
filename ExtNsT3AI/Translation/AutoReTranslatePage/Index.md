---
title: "Auto Re-Translate Page"
description: "Let T3AI translate new content automatically and re-translate changed content when editors save in the default language, enabled per page."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "Translation"
sidebarTitle: "Auto Re-Translate Page"
---

Keeps translations up to date while editors work in the default language. You enable it per page.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmramdz3d0zs0qmhxu84rlt2k?embed_v=2&utm_source=embed" loading="lazy" title="Auto Translate Page" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmral78wn0xzlqmhxtogkt0yt?embed_v=2&utm_source=embed" loading="lazy" title="Auto Re-Translate Page" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## Enable automatic translation

1. Edit the page properties and open the **AI Assistant** tab.
2. Enable one or both options and save:
   - **Allow Auto-Translate?**: new records in the default language are translated into all other languages when you save.
   - **Allow Re-Translation?**: when you change content in the default language, T3AI updates the translations.

**Result:** From now on, saving content in the default language of this page triggers the translation. The provider used is set in the [AI Translation card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-translation).

<Note>
Automatic translation runs on every save and uses AI credits or provider tokens each time. Enable it on pages that change often and need fast translations.
</Note>

### Earlier walkthrough

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfpfnj6801l3130u1i9exdl7?embed_v=2&utm_source=embed" loading="lazy" title="Auto Re-Translate Page" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

**Related:** [AI Translation card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-translation) (Auto Page Translate, default model) · [Permissions](/en/latest/ExtNsT3AI/Configuration/Permissions/Index)
