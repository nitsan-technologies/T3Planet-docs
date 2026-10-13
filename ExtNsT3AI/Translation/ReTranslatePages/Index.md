---
title: "Re-Translate Pages"
description: "Replace the existing translations of a TYPO3 page with a fresh AI translation using the Re-Translate button in the Languages view of the Page module."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "Translation"
sidebarTitle: "Re-Translate Pages"
---

Replaces the existing translation of a page with a fresh AI translation. Use it after larger changes in the default language.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmfpiu19404xj130u5ah2ekrs?embed_v=2&utm_source=embed" loading="lazy" title="Re-Translate Pages" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

### Earlier walkthrough

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cm1iyxwth37itououeb054igl?embed_v=2&utm_source=embed" loading="lazy" title="Re-Translate Pages" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

## Re-translate a page

1. Open the **Page** module, select the page, and set the display mode to **Languages** (TYPO3 v14: **Language Comparison**).
2. In the column of the language, click **Re-Translate**. The button appears when all elements of the page are translated.
3. Confirm **Re-translate all elements on this page? Existing translations will be replaced.**

**Result:** T3AI translates all elements of the page again and reloads the view.

<Warning>
Manual changes in the existing translation are overwritten.
</Warning>

## Re-translate one record

To re-translate only one translated page or content element, edit the translated record and choose a provider in the **Translate with T3AI** dropdown in the form header.

To re-translate many pages, add them to [Manage Mass Translation](/en/latest/ExtNsT3AI/Translation/MassTranslation/Index#manage-mass-translation) with **Re-translate mode**.

**Related:** [AI Translation card](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#ai-translation) · [Permissions](/en/latest/ExtNsT3AI/Configuration/Permissions/Index) · [AI Usage & AI Logs](/en/latest/ExtNsT3AI/Configuration/AIUsageAndLogs/Index)
