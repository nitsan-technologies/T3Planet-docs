---
title: "AI Agent"
description: "Configure AI Chatbot from a chat in the TYPO3 backend with the AI agent of AI Foundation (T3AF). New in 14.5.0."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AC"
  - "AI Agent"
  - "T3AF"
sidebarTitle: "AI Agent"
---

<a id="ai-agent"></a>

<Info>
**New to the AI Agent?** The AI Agent is a chat assistant from AI Foundation (T3AF) that sits in the TYPO3 backend. You tell it in plain words what to change in AI Chatbot. It prepares the change, and you approve it in the conversation.

**Where to find it:** click **Ask AI Agent** in the backend top bar, or press <kbd>Ctrl/Cmd+Shift+K</kbd>. You manage it in **AI Foundation > AI Agent** (module menu **AI Universe > AI Foundation**). See [Where the AI agent opens](/en/latest/ExtNsT3AF/AskAiAgent/WhereOpens/Index).

**What you need:** AI Foundation (`ns_t3af`) 2.0.5 or newer, AI Chatbot & Search (`ns_t3cs`) 14.5.0 or newer, and AI Chatbot 14.5.0 on TYPO3 v13 or v14. You also need an AI provider with tool calling, and editors need **AI Agent access** in their backend user group. See [Before you start](/en/latest/ExtNsT3AF/AskAiAgent/BeforeYouStart/Index).

**Get started**

1. Update AI Foundation to 2.0.5, then AI Chatbot and T3CS to 14.5.0, and flush the caches.
2. Click **Ask AI Agent** in the backend top bar (or press <kbd>Ctrl/Cmd+Shift+K</kbd>).
3. Type what you want, for example "Show me the current AI Chatbot settings", then read the change card and click **Apply**, or cancel it.

For full details, see the [T3AF AI Agent docs](/en/latest/ExtNsT3AF/AskAiAgent/Index).
</Info>

From version 14.5.0 you can configure AI Chatbot from a conversation with the **AI Agent** of AI Foundation (T3AF), instead of only from the chatbot settings form. The AI Agent reads your current settings and applies the changes you confirm.

**Tools in the AI Agent:** from 14.5.0, the AI Chatbot tools (`t3ac_*`), the AI Search tools (`t3as_*`) and the AI Chatbot & Search tools (`t3cs_*`) all work inside the AI Foundation (T3AF) agent. Each group is available when its extension is installed.

**What you need**

- AI Chatbot **14.5.0** or newer on **TYPO3 v13.4 or v14.3** (TYPO3 v12 is not supported)
- **AI Foundation** (`ns_t3af`) **2.0.5** or newer – the AI Agent runs in AI Foundation
- **AI Chatbot & Search base** (`ns_t3cs`) **14.5.0** or newer

**Example requests**

- "Change the greeting of our chatbot to: Hello, how can I help you?"
- "Rename the chatbot to Support Bot."
- "Move the chatbot widget to the left bottom on mobile."
- "Show at most 3 source links under the answers."

**What the AI Agent checks before it saves**

- It reads the current settings first and changes only the fields you named.
- It asks you to confirm before it saves a change.
- A value the settings form would not accept is refused, and nothing is saved.
- An editor without permission to change the chatbot is refused.
- A non-admin editor can change only a chatbot whose site root is inside their web mount.
- If several chatbots exist on the site and you did not name one, it asks which one you mean.

<Accordion title="AI Agent tools for AI Chatbot (14.5.0)">

| Tool | What it does |
|---|---|
| `t3ac_chatbot_list` | List chatbots with their ID, title, site root page, language and whether they are active |
| `t3ac_chatbot_settings_get` | Read the settings of one chatbot (appearance, greeting, instructions, language, site) |
| `t3ac_chatbot_settings` | Change the settings of one chatbot. Only the fields you name change |

The greeting visitors see is the **first message**. The **instructions** are the internal rules for the bot and change only when you ask for that.

</Accordion>

<Accordion title="AI Search (T3AS) tools in the AI Agent (14.5.0)">

These tools are available when AI Search (`ns_t3as`) is installed.

| Tool | What it does |
|---|---|
| `t3as_search_settings_get` | Read the AI Search widget settings of a site |
| `t3as_search_settings` | Change the AI Search widget settings of a site. Only the fields you name change |
| `t3as_list_predefined_questions` | List the predefined (suggested) questions |
| `t3as_predefined_questions_create` | Add one predefined question |

</Accordion>

<Accordion title="AI Chatbot & Search (T3CS) tools in the AI Agent (14.5.0)">

These tools come from AI Chatbot & Search (`ns_t3cs`) and also work inside the T3AF agent.

| Tool | What it does |
|---|---|
| `t3cs_list_datasources` | List the data sources |
| `t3cs_save_datasource` | Create or change a data source |
| `t3cs_sync_datasource` | Mark a data source for sync |
| `t3cs_list_queue_items` | List items in the training queue |
| `t3cs_reset_failed_queue_item` | Put a failed queue item back to Pending |
| `t3cs_training_summary` | Show training queue counts |
| `t3cs_usage_analytics_summary` | Show usage analytics numbers |

</Accordion>

See also: [AI Foundation](/en/latest/ExtNsT3AF/Index) · [Changelog](/en/latest/ExtNsT3AC/Changelog/Index)
