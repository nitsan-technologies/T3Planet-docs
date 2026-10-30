---
title: "Changelog"
description: "What is new in AI Chatbot (T3AC)."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AC"
  - "Changelog"
sidebarTitle: "Changelog"
---

<Tip>
**What's new in 14.5.0**

- The **AI agent** from AI Foundation (T3AF) is now available in the TYPO3 backend (**Ask AI Agent** in the top bar).
- The AI Chatbot (`t3ac_*`), AI Search (`t3as_*`) and AI Chatbot & Search (`t3cs_*`) tools all work inside it.
- Only **TYPO3 v13 and v14** are supported. If you run TYPO3 v12, stay on **14.4.0**.

[T3AF AI Agent docs](/en/latest/ExtNsT3AF/AskAiAgent/Index) · [Read about the AI Agent](/en/latest/ExtNsT3AC/AIAgent/Index)
</Tip>

## Version 14.5.0 (30 Oct 2026)

<Warning>
From version **14.5.0**, AI Chatbot supports only **TYPO3 v14 and v13** (13.4 or 14.3). TYPO3 v12 is no longer supported. If you run TYPO3 v12, stay on **14.4.0**, which keeps receiving bugfixes and security updates.
</Warning>

**Before you update**

1. Stay on 14.4.0 if you run TYPO3 v12.
2. Update **AI Foundation (T3AF)** to **2.0.5** first. The AI Agent needs AI Foundation 2.0.
3. Update **AI Chatbot & Search (T3CS)** to **14.5.0** together with AI Chatbot.
4. Take a full backup of the database and files.

**Requirements**

| Package | Version |
|---|---|
| TYPO3 (`typo3/cms-core`) | 13.4.0 – 14.99.99 |
| PHP | 8.2.0 – 8.5.99 |
| AI Foundation (`nitsan/ns-t3af`) | 2.0.5 – 2.99.99 |
| AI Chatbot & Search (`nitsan/ns-t3cs`) | 14.5.0 – 14.99.99 |
| T3Planet Shop (`nitsan/ns-license`) | 14.3.0 – 14.9.99 |

**New**

- AI Agent in the TYPO3 backend: configure AI Chatbot from a conversation. See [AI Agent](/en/latest/ExtNsT3AC/AIAgent/Index).
- The AI Chatbot tools (`t3ac_*`), AI Search tools (`t3as_*`) and AI Chatbot & Search tools (`t3cs_*`) all work inside the AI Foundation (T3AF) agent.

**Improved**

- Dropped support for TYPO3 v12. This release needs TYPO3 13.4 or 14.3.
- Shows a neutral message when T3Planet credits are used up, instead of a raw error.

**Fixed**

- The default no-answer text now shows the translated standard reply.
- The public chatbot API returns only widget fields. Custom CSS can no longer close the style tag.
- The AI Agent refuses writes without permission or outside the web mount.
- The feedback toast is easier to read.

**How to update**

With Composer:

```bash
composer update nitsan/ns-t3af nitsan/ns-t3cs nitsan/ns-t3ac
vendor/bin/typo3 cache:flush
```

Without Composer: open **T3Planet Shop** (System › T3Planet Shop on TYPO3 v14, Admin Tools › T3Planet Shop on TYPO3 v13), click **Check for Updates**, then **Update to 14.5.0** next to AI Chatbot, and flush caches. See [Update Guide](/en/latest/ExtNsT3AC/UpdateGuide/Index).
