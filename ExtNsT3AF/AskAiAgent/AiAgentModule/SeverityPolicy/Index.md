---
title: "Severity policy"
description: "The Severity policy tab of AI Foundation > AI Agent: how read, write, destructive, and unclassified tools behave in the AI agent."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AF"
  - "ns_t3af"
  - "AI agent"
sidebarTitle: "Severity policy"
---

<a id="ask-ai-agent-tab-severity"></a>

**Path:** **AI Foundation > AI Agent > Severity policy**

**What it shows:** how the AI agent treats each tool, based on the severity the tool declares.

| Severity | Behaviour in the AI agent |
|---|---|
| **Read** | Runs automatically. Results appear as tool-call steps in the chat. |
| **Write** | Prepares a change card. The change is written through the TYPO3 DataHandler only after you click **Apply**. |
| **Destructive** | Red change card with a two-step confirmation (**Confirm (1 of 2)**, then **Apply (2 of 2)**). |
| **Unclassified** | Locked. The tool cannot run until its extension declares a severity. |

Below the table, one card per severity lists the tools and the extension that provides them.

**What you do here:** check which tools can change data before you grant the AI agent to editors. To block individual tools, use the settings described in [Governance](/en/latest/ExtNsT3AF/AskAiAgent/AiAgentModule/Governance/Index).

<Info>
Write and destructive tools never write on their own. The AI agent always shows a change card and waits for your explicit approval.
</Info>
