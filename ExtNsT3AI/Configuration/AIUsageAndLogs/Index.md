---
title: "AI Usage & AI Logs"
description: "Find T3AI requests, tokens, costs, and errors in AI Foundation AI Usage and AI Logs, opened from the AI Usage menu of the AI Assistant module."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "AI Usage"
  - "AI Logs"
sidebarTitle: "AI Usage & AI Logs"
---

T3AI writes its requests and errors to AI Foundation. Open them from the **AI Usage** menu at the top right of the **AI Assistant** module, or directly in **AI Foundation > AI Usage** and **AI Foundation > AI Logs**.

![AI Usage menu in the AI Assistant module with the entries AI Usage and AI Logs](../images/t3ai-ai-usage-menu.webp)

<a id="ai-logs"></a>

## AI Logs

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrbpsdl20frlqmo521y5if8m?utm_source=link" loading="lazy" title="T3AI AI Logs Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

Events and errors, for example a provider without a required capability.

1. Filter by **Channel**: **AI Assistant Content**, **AI Assistant SEO**, **AI Assistant Translation**, **AI Assistant Media**, **AI Assistant Prompts**, **AI Assistant Bulk Ops**, or **AI Assistant Forms**.
2. Filter by **Level**: **Error**, **Warning**, or **Info**.
3. Open an entry to read the details.
4. Use **Export CSV** to share entries, and **Reset** to clear the filters.

<a id="statistics"></a>

## AI Usage

Request counts, tokens, costs, and the success rate.

- Filter the **Request Log** by **Module** `ns_t3ai` to list T3AI requests only.
- Narrow down by **Engine**, **Model**, **Scope** (for example `seo.meta_description`, `content_translate`, `image_generate`), **Request Type**, **Status**, and **User**. **User** shows the source, for example `backend_module`, `agent`, `mcp`, or `cli`.

![AI Usage Request Log filtered by Module ns_t3ai and Status Success, with the totals, the filters, and the request list](../images/t3ai-ai-usage-request-log.webp)

- Switch to **Usage Summary** for totals by provider, model, and extension. **Export Report** downloads the summary.

![AI Usage Summary with Usage by Provider, Top Models by Tokens, and Usage by Extension](../images/t3ai-ai-usage-summary.webp)

More: [AI Usage & Logs in AI Foundation](/en/latest/ExtNsT3AF/Configuration/AIUsageAndLogs/Index)

**Related:** [AI provider & API keys](/en/latest/ExtNsT3AI/Configuration/AIProviders/Index) · [Scheduler & CLI](/en/latest/ExtNsT3AI/Configuration/SchedulerAndCLI/Index) · [Known Problems](/en/latest/ExtNsT3AI/KnownProblems/Index)
