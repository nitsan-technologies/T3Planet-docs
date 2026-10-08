---
title: "Providers & MCP Tools"
description: "The AI provider AI Chatbot uses, and MCP tools for teams that work with AI assistants."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AC"
  - "AI Providers"
  - "MCP"
sidebarTitle: "Providers & MCP Tools"
---

<a id="mcp-tools"></a>

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmrabygkm0chzqmhx3nanm13o?utm_source=link" loading="lazy" title="T3AC Providers and MCP Tools Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>
T3AC uses T3AF for provider selection and any shared MCP-based integrations.
Review this setup when you want to confirm the active provider, available models, and connected MCP tools that support chatbot workflows.

**MCP** (Model Context Protocol) lets an AI assistant, for example in your developer's code editor, read and change chatbot settings and data sources for you. This is optional and mainly for technical teams.

<Note>
MCP tools are for backend users. Give access only to people who may change these settings.
</Note>

<Accordion title="MCP tools for AI Chatbot">

| Tool | What it does |
|---|---|
| `t3ac_chatbot_settings` | Read or change the settings of a chatbot |
| `t3cs_list_datasources` | List the data sources |
| `t3cs_save_datasource` | Create or change a data source |
| `t3cs_sync_datasource` | Mark a data source for sync |
| `t3cs_list_queue_items` | List items in the training queue |
| `t3cs_reset_failed_queue_item` | Put a failed queue item back to Pending |
| `t3cs_training_summary` | Show training queue counts |
| `t3cs_usage_analytics_summary` | Show usage analytics numbers |

</Accordion>

See also: [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index) · [MCP Server](/en/latest/ExtNsT3AF/Integrations/MCPServer/Index) · [MCP Tools](/en/latest/ExtNsT3AF/Integrations/MCPTools/Index)
