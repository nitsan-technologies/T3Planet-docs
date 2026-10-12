---
title: "Audit"
description: "The Audit tab of AI Foundation > AI Agent: what the AI agent records and the most recent agent tool invocations with correlation IDs."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AF"
  - "ns_t3af"
  - "AI agent"
sidebarTitle: "Audit"
---

<a id="ask-ai-agent-tab-audit"></a>

**Path:** **AI Foundation > AI Agent > Audit**

**What it shows:** what the AI agent records, and the most recent tool calls.

- **What is recorded** — tool invocations (metadata) and turn correlation IDs are stored. The full conversation transcript and raw prompt and response bodies are **not** stored in the audit log.
- **Recent agent tool invocations** — time, tool, result (**Success** or **Failed**), correlation ID, and a hash of the arguments. No payloads are stored.

**What you do here:**

1. Use the **Correlation** value to group all tool calls of one request.
2. Investigate rows with the result **Failed**.
3. For requests, errors, and costs across all AI features, open [AI Usage & Logs](/en/latest/ExtNsT3AF/Configuration/AIUsageAndLogs/Index).
