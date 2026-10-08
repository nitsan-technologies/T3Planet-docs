---
title: "Upgrading? Where your old settings moved"
description: "Only for upgrades: the old T3AS tab in the site configuration is gone. Here is where each of those settings is now."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "Site configuration"
  - "Upgrade"
sidebarTitle: "Moved settings (upgrade)"
---

<a id="site-module-settings"></a>

In older versions, you set up AI Search in **Sites → Edit site**, on a tab called **T3AS**. That tab is gone. This page shows where each of those settings is now.

<Info>
New to AI Search? You can skip this page.
</Info>

## Where is my old setting?

- **Want to switch AI Search on, or change the answer style?** Go to **AI Universe → AI Chatbot/Search → Search → Settings**.
- **Want to change the look of the search box or button?** Go to **Search → Widget**.
- **Want to show example questions?** Go to **Search → Questions**.
- **Want to set CSS classes for the search button or field?** Use the [AI Search plugin](/en/latest/ExtNsT3AS/FrontendPlugin/Index).
- **Want to connect Solr?** Go to **AI Universe → AI Foundation → AI Features → Solr configurations**.
- **Looking for "Search Engine"?** It no longer exists. Just add the content you want as a [data source](/en/latest/ExtNsT3AS/Configuration/DataSource/Index).

## After an upgrade

1. Go to **AI Universe → AI Chatbot/Search → Search**.
2. Your old values are already filled in. Check them.
3. Click **Save Configuration**. Only then are they saved.
4. If you use Solr, enter your Solr settings again in **AI Features → Solr configurations**.

<Note>
In the site configuration you still choose the **site set** (a package of settings you switch on for your website) on TYPO3 v13 and v14, and the optional **Plugin PID** under **Edit site settings**. See [Installation, Step 5](/en/latest/ExtNsT3AS/Installation/Index#load-typoscript).
</Note>

{/* SUPADEMO NEEDED: Where the old T3AS site settings are now (Search tab, Edit site settings) */}
