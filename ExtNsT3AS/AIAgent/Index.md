---
title: "AI Agent"
description: "Configure AI Search from a chat in the TYPO3 backend with the AI agent of AI Foundation (T3AF). New in 14.5.0."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "AI Agent"
  - "T3AF"
sidebarTitle: "AI Agent"
---

<a id="ai-agent"></a>

<Info>
**New to the AI Agent?** The AI Agent is a chat assistant from AI Foundation (T3AF) that sits in the TYPO3 backend. You tell it in plain words what to change in AI Search. It prepares the change, and you approve it in the conversation.

**Where to find it:** click **Ask AI Agent** in the backend top bar, or press <kbd>Ctrl/Cmd+Shift+K</kbd>. You manage it in **AI Foundation > AI Agent** (module menu **AI Universe > AI Foundation**). See [Where the AI agent opens](/en/latest/ExtNsT3AF/AskAiAgent/WhereOpens/Index).

**What you need:** AI Foundation (`ns_t3af`) 2.0.5 or newer, AI Chatbot & Search (`ns_t3cs`) 14.5.0 or newer, and AI Search 14.5.0 on TYPO3 v13 or v14. You also need an AI provider with tool calling, and editors need **AI Agent access** in their backend user group. See [Before you start](/en/latest/ExtNsT3AF/AskAiAgent/BeforeYouStart/Index).

**Get started**

1. Update AI Foundation to 2.0.5, then AI Search and T3CS to 14.5.0, and flush the caches.
2. Click **Ask AI Agent** in the backend top bar (or press <kbd>Ctrl/Cmd+Shift+K</kbd>).
3. Type what you want, for example "Show me the current AI Search settings", then read the change card and click **Apply**, or cancel it.

For full details, see the [T3AF AI Agent docs](/en/latest/ExtNsT3AF/AskAiAgent/Index).
</Info>

From version 14.5.0 you can configure AI Search from a conversation with the **AI Agent** of AI Foundation (T3AF), instead of only from the Search settings form. The AI Agent reads your current settings and applies the changes you confirm.

**Tools in the AI Agent:** from 14.5.0, the AI Chatbot tools (`t3ac_*`), the AI Search tools (`t3as_*`) and the AI Chatbot & Search tools (`t3cs_*`) all work inside the AI Foundation (T3AF) agent. Each group is available when its extension is installed.

**What you need**

- AI Search **14.5.0** or newer on **TYPO3 v13.4 or v14.3** (TYPO3 v12 is not supported)
- **AI Foundation** (`ns_t3af`) **2.0.5** or newer – the AI Agent runs in AI Foundation
- **AI Chatbot & Search base** (`ns_t3cs`) **14.5.0** or newer

**Example requests**

- "Turn AI Search off."
- "Set the main colour of the search widget to #1a73e8."
- "Show 5 suggested questions."
- "Add the predefined question: What are your opening hours?"

**What the AI Agent checks before it saves**

- It reads the current settings first and changes only the fields you named.
- It asks you to confirm before it saves a change.
- A search setting the Search settings form would not save is refused, and nothing is saved (for example a colour must be `#` plus 3 to 8 hex digits).
- An editor without permission to change search settings is refused.
- A non-admin editor can change only settings for a site root inside their web mount.
- Before it adds a predefined question with a title that already exists in that folder and language, it warns you and does not create a second one unless you choose to.

<Accordion title="AI Agent tools for AI Search (14.5.0)">

| Tool | What it does |
|---|---|
| `t3as_search_settings_get` | Read the AI Search widget settings of a site |
| `t3as_search_settings` | Change the AI Search widget settings of a site (on/off, colours, widget position, number of questions, allowed domains, external CSS). Only the fields you name change |
| `t3as_list_predefined_questions` | List the predefined (suggested) questions by storage folder and language |
| `t3as_predefined_questions_create` | Add one predefined question to the storage folder |

There is no setting for how many results are shown or for the search box placeholder.

</Accordion>

<Accordion title="AI Chatbot (T3AC) tools in the AI Agent (14.5.0)">

These tools are available when AI Chatbot (`ns_t3ac`) is installed.

| Tool | What it does |
|---|---|
| `t3ac_chatbot_list` | List chatbots with their ID, title, site root page, language and whether they are active |
| `t3ac_chatbot_settings_get` | Read the settings of one chatbot |
| `t3ac_chatbot_settings` | Change the settings of one chatbot. Only the fields you name change |

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

See also: [AI Foundation](/en/latest/ExtNsT3AF/Index) · [Changelog](/en/latest/ExtNsT3AS/Changelog/Index)
