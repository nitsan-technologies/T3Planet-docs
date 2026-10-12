---
title: "Troubleshooting"
description: "Common AI agent messages in AI Foundation and how to solve them: missing provider, no tool calling, no executable tools, missing button, and shortcut conflicts."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AF"
  - "ns_t3af"
  - "AI agent"
sidebarTitle: "Troubleshooting"
---

<a id="ask-ai-agent-troubleshooting"></a>

**"AI provider is not configured"**

No provider is available. Add one in **AI Foundation > AI Providers** and run **Test connection**.

**"Your current AI provider cannot run tools for natural-language requests"**

The selected model does not support tool calling. Start a new conversation with a tools-capable provider, or use `/` and `@` to run a tool directly.

**"No executable tools are available for your account"**

Your backend group has no permitted tools. Type `/` to see which tools are locked, and ask your administrator to check **AI Foundation > AI Permissions**.

**The Ask AI Agent button is missing**

Your backend group does not have the option **AI Agent access**. Ask your administrator to grant it.

**The keyboard shortcut opens Live Search**

<kbd>Ctrl/Cmd+K</kbd> belongs to Live Search by default. Use <kbd>Ctrl/Cmd+Shift+K</kbd>, or change the shortcut in **AI Foundation > AI Agent > Overview**. Reload other backend tabs afterwards.

**"The AI Agent is still working on your previous request"**

Wait until the current answer is complete, or click **Stop**.

Administrators can review requests, errors, and costs in [AI Usage & Logs](/en/latest/ExtNsT3AF/Configuration/AIUsageAndLogs/Index).
