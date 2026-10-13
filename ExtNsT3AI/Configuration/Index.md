---
title: "Configuration"
description: "Set up T3AI step by step in AI Foundation: AI provider and API keys, the T3AI AI Features cards, permissions, AI Usage and Logs, Scheduler and CLI, and the AI agent."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "Configuration"
sidebarTitle: "Configuration"
---

T3AI has no extension configuration of its own. **Admin Tools > Settings > Configure extensions** no longer lists `ns_t3ai`. Everything is configured in **AI Universe > AI Foundation**, and the features are used in **AI Universe > AI Assistant**.

**The basic idea in 4 steps**

1. **Connect an AI provider** in AI Foundation > AI Providers ([AI provider & API keys](/en/latest/ExtNsT3AI/Configuration/AIProviders/Index)).
2. **Set the T3AI defaults** on the six AI Assistant cards in AI Foundation > AI Features ([AI Features cards](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index)).
3. **Give editors access** in AI Foundation > AI Permissions ([Permissions](/en/latest/ExtNsT3AI/Configuration/Permissions/Index)).
4. **Check the setup** on the **AI Foundation** tab of the AI Assistant module. The **AI Foundation Setup Checklist** shows done, warning, and open steps, with links to each.

**Follow the pages in this order.** Pages 1–3 are the basic setup. The others are optional or for later.

<CardGroup cols={2}>
  <Card title="1. AI provider & API keys" icon="plug" href="/en/latest/ExtNsT3AI/Configuration/AIProviders/Index">
    Provider mode, providers for text, translation, and images, and the default provider.
  </Card>
  <Card title="2. AI Features cards" icon="sliders-horizontal" href="/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index">
    General Settings, AI SEO, AI Pages, AI Content, AI Translation, AI Media, and Basic Auth.
  </Card>
  <Card title="3. Permissions" icon="shield" href="/en/latest/ExtNsT3AI/Configuration/Permissions/Index">
    Module, feature, and record access per backend user group.
  </Card>
  <Card title="4. AI Usage & AI Logs" icon="scroll-text" href="/en/latest/ExtNsT3AI/Configuration/AIUsageAndLogs/Index">
    T3AI requests, tokens, costs, and error messages.
  </Card>
  <Card title="5. Scheduler & CLI" icon="terminal" href="/en/latest/ExtNsT3AI/Configuration/SchedulerAndCLI/Index">
    Process the Mass Translation and Mass SEO queues, and console commands.
  </Card>
  <Card title="6. Ask AI agent & MCP" icon="bot" href="/en/latest/ExtNsT3AI/Configuration/AgentAndMCP/Index">
    The 33 T3AI tools in the AI agent and the MCP server.
  </Card>
  <Card title="7. Where your old settings moved" icon="map" href="/en/latest/ExtNsT3AI/Configuration/WhereToFindIt/Index">
    Only after an upgrade: where each old `ns_t3ai` setting is now.
  </Card>
</CardGroup>

<Note>
Sites protected by HTTP Basic Authentication need the Basic Auth username and password in **AI Features > Access & Notifications**. See [AI Features cards](/en/latest/ExtNsT3AI/Configuration/AIFeatures/Index#access-and-notifications).
</Note>
