---
title: "AI Agent module tabs"
description: "The five tabs of AI Foundation > AI Agent in the TYPO3 backend: Overview, Severity policy, Governance, Audit, and Demand signals."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AF"
  - "ns_t3af"
  - "AI agent"
sidebarTitle: "AI Agent module tabs"
---

<a id="ask-ai-agent-tabs"></a>

**Path:** **AI Foundation > AI Agent**

The **AI Agent** module shows how the AI agent is configured on this installation. It has five tabs. Most of the information is read-only; the values come from the installed tools and from the backend user group settings in **AI Foundation > AI Permissions**.

1. Open **AI Foundation** in the module menu.
2. Click **AI Agent** in the module navigation.
3. Select one of the five tabs (number 4 in the screenshot under [Where the AI agent opens](/en/latest/ExtNsT3AF/AskAiAgent/WhereOpens/Index)). The summary below introduces each tab; each tab is described on its own page.

<Tabs>
  <Tab title="Overview">
    The current state of the AI agent: tool counters (**Registered tools**, **Executable now**, **Locked**, **Contributing extensions**), the **Keyboard shortcut** setting, **Availability**, **How tools register**, and **Tools by owning extension**. See [Tab: Overview](/en/latest/ExtNsT3AF/AskAiAgent/AiAgentModule/Overview/Index).
  </Tab>
  <Tab title="Severity policy">
    How the AI agent treats **read**, **write**, **destructive**, and **unclassified** tools, and one list of tools per severity. See [Tab: Severity policy](/en/latest/ExtNsT3AF/AskAiAgent/AiAgentModule/SeverityPolicy/Index).
  </Tab>
  <Tab title="Governance">
    The **control matrix**: monthly credit cap, daily request cap, provider allowlist, model override, PII masking, and turn guard, with the source of each limit and its effect on AI agent turns. See [Tab: Governance](/en/latest/ExtNsT3AF/AskAiAgent/AiAgentModule/Governance/Index).
  </Tab>
  <Tab title="Audit">
    **What is recorded** and the **recent agent tool invocations** (time, tool, result, correlation, arguments hash). See [Tab: Audit](/en/latest/ExtNsT3AF/AskAiAgent/AiAgentModule/Audit/Index).
  </Tab>
  <Tab title="Demand signals">
    **Locked tool activation signals** per extension and tool. Sharing with T3Planet is disabled; counts stay on this installation. See [Tab: Demand signals](/en/latest/ExtNsT3AF/AskAiAgent/AiAgentModule/DemandSignals/Index).
  </Tab>
</Tabs>

<Tip>
The AI agent **settings** (limits per turn, conversation retention, and the conversation list) are not in this module. Open **AI Foundation > AI Features**, find the **AI Agent** card, and click **Configure**. See [AI agent settings](/en/latest/ExtNsT3AF/AskAiAgent/FeatureSettings/Index).
</Tip>

## Tab pages

- [Tab: Overview](/en/latest/ExtNsT3AF/AskAiAgent/AiAgentModule/Overview/Index)
- [Tab: Severity policy](/en/latest/ExtNsT3AF/AskAiAgent/AiAgentModule/SeverityPolicy/Index)
- [Tab: Governance](/en/latest/ExtNsT3AF/AskAiAgent/AiAgentModule/Governance/Index)
- [Tab: Audit](/en/latest/ExtNsT3AF/AskAiAgent/AiAgentModule/Audit/Index)
- [Tab: Demand signals](/en/latest/ExtNsT3AF/AskAiAgent/AiAgentModule/DemandSignals/Index)
