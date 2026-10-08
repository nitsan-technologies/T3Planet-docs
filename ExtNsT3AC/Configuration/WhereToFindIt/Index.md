---
title: "Upgrading? Where your old settings moved"
description: "Only for upgrades: the old T3AC tab in the site configuration is gone. Here is where each of those settings is now."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AC"
  - "Site configuration"
  - "Upgrade"
sidebarTitle: "Moved settings (upgrade)"
---

<a id="site-module-settings"></a>

In older versions, you set up the chatbot in **Sites → Edit site**, on a tab called **T3AC**. That tab is gone. This page shows where each of those settings is now.

<Info>
New to AI Chatbot? You can skip this page.
</Info>

## Where is my old setting?

Everything is now in **AI Universe → AI Chatbot/Search → Chatbot**.

- **Where do I turn the chatbot on?** → **Configuration** → **Enable AI Chatbot**. See [Settings](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#t3ac-save-chatbot-history).
- **Where do I choose the pages?** (was **Show Chatbot on Specific Pages** / **Hide Chatbot on Specific Pages**) → **General**. See [Page Visibility](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#page-visibility).
- **Where is my own CSS?** (was **Custom Internal CSS**) → **General** → **Custom Internal CSS**. See [Custom Styling](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#custom-styling).
- **Where are the allowed websites?** (was **Allow Any Domain**, **Allowed Domains for Chatbot Embedding**, **Custom CSS**) → **External Embed** → **External Embedding Settings**: **Allow Any Domain**, **Allowed Domains**, **External CSS Path**. See [External Embed](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#external-embed).

## What is still in the site configuration?

- **Sets for this Site** (TYPO3 v13 and v14): add **AI Chatbot - TYPO3 Extension**. See [Installation, Step 5](/en/latest/ExtNsT3AC/Installation/Index#load-typoscript).
- The **Languages** of your website. The chatbot **Language** list only shows these languages. See [Multilanguage](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#multilanguage).

<Warning>
After an upgrade, the old values are **not** copied. Enter them again on the **Chatbot** tab (**Configuration**, **General**, **External Embed**) and click **Save Configuration**.
</Warning>

{/* SUPADEMO NEEDED: Where the old T3AC site settings are now (Chatbot tab) */}
