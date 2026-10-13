---
title: "Ask AI agent & MCP"
description: "T3AI adds 33 tools to the AI Foundation AI agent and MCP server; where the agent and MCP are configured and which pages describe each tool."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AI"
  - "AI agent"
  - "MCP"
sidebarTitle: "Ask AI agent & MCP"
---

T3AI adds 33 tools to the **Ask AI Agent** in the TYPO3 top bar and to the AI Foundation MCP server. Editors can create pages, write SEO texts, translate, manage the glossary and the mass queues, and generate images from the chat. The agent asks before it changes or deletes anything.

| What | Where |
|---|---|
| Conversation history and retention, continue after confirm, tool search, per-turn tool limits | **AI Foundation > AI Features > AI Agent** |
| Where the agent writes when you work in Live (draft workspace or Live) | **AI Foundation > MCP > MCP Server**, tab **Connect**, field **Workspace**. See [Live or draft workspace](/en/latest/ExtNsT3AI/AskAiAgent/HowItWorks/Index#live-or-draft-workspace) |
| Drafts mandatory for an editor group (workspace-only edits) | **AI Foundation > AI Permissions**, step **Governance & limits** of the group, **Workspace enforcement** |
| Agent conversations and audit trail | **AI Foundation > AI Agent** |
| MCP server, tokens, and the tools external clients may use | **AI Foundation > MCP** |
| Who may use the agent and which T3AI features | [Permissions](/en/latest/ExtNsT3AI/Configuration/Permissions/Index) |

The agent works with the editor's own backend permissions. Before a T3AI tool writes, it checks that the editor may edit the page, its content, or the record table.

## Read next

- [Ask AI agent](/en/latest/ExtNsT3AI/AskAiAgent/Index): how the agent works, step by step
- [T3AI tools](/en/latest/ExtNsT3AI/AskAiAgent/Tools/Index): all 33 tools with the matching feature page
- [Troubleshooting](/en/latest/ExtNsT3AI/AskAiAgent/Troubleshooting/Index)
- [MCP Server](/en/latest/ExtNsT3AF/Integrations/MCPServer/Index) and [MCP Tools](/en/latest/ExtNsT3AF/Integrations/MCPTools/Index) in AI Foundation

<Note>
Only give MCP access to people who may change T3AI content and settings.
</Note>

**Related:** [Permissions](/en/latest/ExtNsT3AI/Configuration/Permissions/Index) · [AI Usage & AI Logs](/en/latest/ExtNsT3AI/Configuration/AIUsageAndLogs/Index)
