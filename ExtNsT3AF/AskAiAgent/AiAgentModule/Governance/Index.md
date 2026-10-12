---
title: "Governance"
description: "The Governance tab of AI Foundation > AI Agent: credit and request caps, provider allowlist, model override, PII masking, turn guard, and blocked tools."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AF"
  - "ns_t3af"
  - "AI agent"
sidebarTitle: "Governance"
---

<a id="ask-ai-agent-tab-governance"></a>

**Path:** **AI Foundation > AI Agent > Governance**

**What it shows:** the limits that apply to AI agent turns, and where each limit is configured.

| Control | Effect on the AI agent |
|---|---|
| **Monthly credit cap** | Blocks turns when the group's monthly credits are used up. |
| **Daily request cap** | Blocks turns after the daily limit per backend user. |
| **Provider allowlist** | Rejects turns that request a provider that is not allowed. |
| **Model override** | Rejects a requested model when model override is not permitted. |
| **PII masking** | Redacts email addresses and phone numbers in answers. |
| **Turn guard** | Built into the AI agent: warns at 20 tool calls and stops the turn at 40 tool calls. |

**What you do here:** the tab is read-only. To change a limit:

1. Open **AI Foundation > AI Permissions**.
2. Select the backend user group.
3. In step **Limits**, set the caps, the provider allowlist, model override, and PII masking.
4. Under **AI Agent tools**, optionally enable **Read-only agent** (answers questions, prepares no changes) or enter **Blocked tools** as a comma-separated list, for example `file_delete,cache_clear`. The wildcard `*` is supported.
5. Save the group.

<Note>
When a user belongs to several groups, the strictest setting applies. See [AI Permissions](/en/latest/ExtNsT3AF/Configuration/AIPermissions/Index).
</Note>
