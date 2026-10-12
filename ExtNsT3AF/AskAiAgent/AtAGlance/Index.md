---
title: "At a glance"
description: "The essential AI agent workflow of AI Foundation on one screen: select the page, open, ask, approve, check, plus tools, settings, and the key warnings."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AF"
  - "ns_t3af"
  - "AI agent"
sidebarTitle: "At a glance"
---

<a id="ask-ai-agent-at-a-glance"></a>

The essential path, the key warnings, and where to find the settings. The AI agent always works on **the page you are editing**.

| Topic | Details |
|---|---|
| **1. Select the page** | Open the page you want to work on, for example in **Content > Layout**, and select it in the page tree. |
| **2. Open** | Click **Ask AI Agent** in the backend top bar, or press <kbd>Ctrl+Shift+K</kbd> (Windows, Linux) / <kbd>Cmd+Shift+K</kbd> (macOS). The context line shows the page the AI agent works on. See [Where the AI agent opens](/en/latest/ExtNsT3AF/AskAiAgent/WhereOpens/Index). |
| **3. Ask** | Describe the task for this page in your own words and press <kbd>Enter</kbd>. Read tools run immediately and answer. |
| **4. Approve** | Every change to the page is shown as a card marked **Preview — nothing changed yet**. Click **Apply** to write it or **Cancel** to discard it. |
| **5. Check** | The card shows **Changes applied** with links and **Undo**. |
| **Tools** | AI Foundation ships 62 tools, for example `pages_get`, `content_list`, `pages_search`, `pages_tree`, `explain_capabilities`, `ask_clarification` (read) and `write_table` (write). Type `/` to pick one directly. |
| **Settings** | **AI Foundation > AI Agent** with five tabs: **Overview**, **Severity policy**, **Governance**, **Audit**, **Demand signals**. See [AI Agent module tabs](/en/latest/ExtNsT3AF/AskAiAgent/AiAgentModule/Index). |

<Info>
- **Nothing is saved until you click** **Apply**.
- An applied change is saved in the **selected workspace**: in **Live** it is public immediately; in a draft workspace it stays in that workspace until it is published.
- **Delete needs two clicks** and cannot be undone.
- The AI agent has **your** permissions — never more.
- **Page context:** the AI agent works on the page shown in its context line, not on the backend as a whole.
</Info>
