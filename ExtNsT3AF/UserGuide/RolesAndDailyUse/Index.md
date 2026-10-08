---
title: "Roles and Daily Use"
description: "Roles and Daily Use for EXT:ns_t3af (T3AF)."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AF"
  - "ns_t3af"
sidebarTitle: "Roles and Daily Use"
---

What administrators, editors and managers need to know about AI Foundation in daily work.

## For administrators

**Your tasks**

- Keep the API keys valid in **AI Universe → AI Foundation → AI Providers**.
- Keep one default provider and model.
- Watch the AI use and costs in **AI Usage** and on the **Dashboard**.
- Decide who may use what in **AI Permissions**.

### Admin checklist

1. Check that a default provider is switched on in **AI Providers**.
2. Click **Test connection** on your important providers.
3. Try the AI features in your AI extensions.
4. Check the usage (requests and tokens) regularly to control costs.

## For editors

Editors usually don't work in AI Foundation. You use the AI features of other extensions, for example AI Assistant or AI Chatbot.

**An AI feature doesn't work?**

1. Try once more.
2. Copy the exact error message.
3. Send it to your administrator, together with the module and page where it happened.

## For non-technical stakeholders

- Reducing duplicated AI integration work across extensions.
- Centralizing provider and model governance.
- Improving consistency of AI capabilities across teams.

## What to expect operationally

- AI services sometimes limit requests or are briefly unavailable.
- Different AI models (and versions) can give different results.
- Usage numbers may be cached, so they are not always live.

## Known boundaries

- AI Foundation shows nothing on your website by itself. Visitors only see AI through other extensions (for example AI Chatbot).
- The AI features editors use come from these other extensions.

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

Practical guidance for editors, administrators, and stakeholders using **T3AF** (`EXT:ns_t3af`) in daily workflows.

Daily responsibilities:

- Keep provider API keys valid in T3AF > AI Providers.
- Maintain the default provider and model selections.
- Monitor usage statistics across all configured AI providers in T3AF > AI Usage and the Dashboard.
- Keep credentials and access permissions under control.

1. Confirm a default provider is enabled in **AI Providers**.
2. Run **Test connection** on critical provider rows.
3. Test extension-dependent AI features in your connected modules.
4. Review provider usage statistics regularly (requests, tokens, and consumption) for cost and rate control.

Editors usually do not configure providers directly. They interact with features built by other extensions that depend on T3AF.

When AI features fail in a backend module:

- Retry once.
- Capture exact error text.
- Inform the administrator with module and page context.

T3AF helps organizations by:

- Some providers have rate limits and temporary outages.
- Model behavior can differ between providers and versions.
- Usage statistics cover configured AI providers from a centralized view and may be cached (not always real-time).

- No standalone frontend plugin is provided by this extension.
- This package is a service layer; UI features come from dependent extensions.
*/}
