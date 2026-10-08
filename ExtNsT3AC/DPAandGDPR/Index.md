---
title: "Data Processing Agreement (DPA) & General Data Protection Regulation (GDPR)"
description: "T3AC controls for chatbot history storage, retention, and DPA/GDPR considerations."
keywords:
  - "TYPO3"
  - "T3AC"
  - "DPA"
  - "GDPR"
sidebarTitle: "DPA & GDPR"
---

This page helps you answer data protection (GDPR) questions about AI Chatbot: what is stored, what is sent to the AI service, and how to switch storage off or delete it.

## In short

- AI Chatbot can store the **conversations** (visitor messages and AI answers). This is on by default.
- To recognise returning visitors it stores a **coded (hashed) IP address** and a random **visitor ID** from the browser. Treat both as personal data.
- You can switch storage off. The chatbot keeps working.
- The visitor's messages and matching website content are sent to your AI service. The IP address, browser details and cookies are **not** sent.

## Save Chatbot History

1. Go to **AI Universe → AI Chatbot/Search**.
2. Click the **Chatbot** tab.
3. On **Configuration**, turn **Save chatbot history** on or off.
4. Click **Save Configuration**.

{/* 1. Open **AI Chatbot** in the TYPO3 backend.
2. Click the **Chatbot** tab.
3. In **Settings**, enable or disable **Save chatbot history**. */}

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmragm93i0mj0qmhx6fir2bke?embed_v=2&utm_source=embed" loading="lazy" title="T3AC Chatbot settings — Save chatbot history" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

More about this setting: [Save chatbot history](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#t3ac-save-chatbot-history).

**When it is off:**

- New conversations are **not** saved.
- Visitors cannot reopen past chats, and thumbs up/down feedback is hidden.
- The chatbot still works. The current chat is kept for about **24 hours** in a short-term memory (cache) only.

<Warning>
Switching it off does not delete what was saved before. Delete old entries in **Usage Analytics**, or set up the automatic cleanup below.
</Warning>

## History cleanup

Old conversations can be deleted automatically, for example everything older than 30 or 90 days. See [History cleanup](/en/latest/ExtNsT3AC/FeatureGuide/DataSource/Index#t3as-history-cleanup), or ask your developer to run:

```bash
vendor/bin/typo3 t3af:history:cleanup
vendor/bin/typo3 t3af:history:cleanup 30
```

The first command uses the default retention of **90** days. Passing a number (for example `30`) deletes usage history older than that many days.

## Data Processing Agreement (DPA) Considerations

Write down in your privacy documentation:

- that conversations can be stored, and which identifiers are used (hashed IP, browser visitor ID)
- that a visitor ID is kept in the visitor's browser, also when history is off
- the short-term memory of about 24 hours when history is off
- that the spam protection (rate limiting) uses a hashed IP, even when history is off
- how long you keep conversations and how you delete them
- what is sent to your AI service (messages, matching website content, instructions)
- whether you use your own AI key or T3Planet Credits – see [T3Planet Credits](/en/latest/ExtNsT3AF/T3Planet-Credit-System/Index)
- your AI service's own DPA (for example, whether it trains on your data)
- the email transcript feature, if you use it

## Data Processing Agreement (DPA) Questions

<Accordion title="All questions and answers (for your data protection officer)">

| Question | Answer |
| --- | --- |
| Does T3AC process frontend visitor information? | **Yes**, when a visitor uses the chatbot. T3AC can store conversation text, a hashed IP, and a browser visitor id. It does **not** store a frontend-user (`fe_user`) ID or cookies as database fields. |
| Does T3AC store visitor conversations? | **Yes — when Save chatbot history is on (the default).** See tables below. |
| Can visitor logging be disabled while keeping the chatbot? | **Yes.** Turn **Save chatbot history** off. When off: new chats are not written to the three history tables; the Chatbot card in Usage Analytics is hidden; thumbs and past-chat reopen are hidden; live chat uses ephemeral cache (~24 hours); `chat_user_id` is still created for the live session. Existing rows stay until deleted or purged. See [Usage Analytics](/en/latest/ExtNsT3AC/FeatureGuide/UsageAnalytics/Index). |
| What is sent to the AI provider? | Visitor messages plus required RAG / context and system instructions. **Not sent** in the T3AC / AI Foundation payload: visitor IP, User-Agent, session ID, cookies, or the browser visitor id. |
| How long are records retained? | Until they are deleted — manually in Usage Analytics, or by `t3af:history:cleanup` when a Scheduler task is set up. There is no hard expiry on each row by itself. |
| Logging via AI Foundation? | Separate from T3AC history. AI Usage stores a **SHA-256 prompt fingerprint**, tokens, and timing — not the full conversation. Privacy level can reduce or stop AI Usage rows; it does **not** stop T3AC history. See [AI Usage & Logs](/en/latest/ExtNsT3AF/Configuration/AIUsageAndLogs/Index) and [AI Providers](/en/latest/ExtNsT3AF/Configuration/AIProviders/Index) (privacy level). |
| Does T3AC use conversations to train foundation models? | **No.** Whether a vendor trains on API data is governed by the provider contract / DPA, not by a switch inside T3AC. |
| MCP? | If the AI Foundation MCP server is on, backend users can read and change chatbot settings (`t3ac_chatbot_settings`) and manage data sources and training (`t3cs_*` tools). This is backend access, not processing of visitor data. Limit who may use MCP. See [MCP Server](/en/latest/ExtNsT3AF/Integrations/MCPServer/Index). |
| Email transcript? | If **Enable email transcript** is on, a visitor can enter an email address to get a copy of the chat. TYPO3 sends the email with your mail settings. Mention this feature in your privacy policy. |
| Can I turn the chatbot off on some pages? | **Yes.** In the page properties, tab **AI Chatbot / Search**, use **Disable Chatbot** → **Disabled for this Page** (and **Disable Recursive** for all sub-pages). |

</Accordion>

### Conversation storage tables

<Accordion title="For developers: where conversations are stored">
Chats are stored in your own TYPO3 database, not at T3Planet.

- All chat tables start with `tx_nst3ac_domain_model_chatbot_` (sessions, messages and the visitor link).
</Accordion>

### Which identifiers are stored?

<Accordion title="Table: stored identifiers">

| Data | Stored? | Note |
| --- | --- | --- |
| Full chat messages | **Yes** | When history is on |
| IP address | **Hashed (MD5)** | Not stored as plain IP. Still treat as personal data. |
| Browser visitor id | **Yes** | Created in the browser (`localStorage` `chat_user_id`) and sent to the server |
| Frontend user (`fe_user`) | **No** | — |
| Cookies as DB fields | **No** | Browser local storage is used for the visitor id |

</Accordion>

### Are there other places that still store visitor data?

<Accordion title="Table: other places">

| Place | What is stored |
| --- | --- |
| Browser local storage (`chat_user_id`) | Random visitor id, also when history is off |
| Ephemeral cache `ns_t3ac_ephemeral_chat` | Current live session only (~24 hours) when history is off |
| Rate limiter cache | Hashed client IP, independent of the history toggle |

</Accordion>


{/* Old table row, replaced above:
| MCP? | If AI Foundation MCP is enabled, T3AC tools can run chatbot operations through connected clients. That is backend/editor access, not public-visitor processing. Restrict MCP as an access-control topic. See [MCP Server](/en/latest/ExtNsT3AF/Integrations/MCPServer/Index). | */}

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

This page answers GDPR-related questions about visitor chatbot data and describes **technical data-management capabilities** in T3AC.

T3AC allows administrators to control whether visitor chatbot history is stored.

The **Save chatbot history** option is available under the AI Chatbot configuration. For this setting, see [Save chatbot history](/en/latest/ExtNsT3AC/FeatureGuide/Chatbot/Index#t3ac-save-chatbot-history).

### Backend steps

**When enabled**, T3AC can store chatbot-related history such as visitor conversations and generated answers.

**When disabled:**

- New chatbot conversations and answers are **not** stored as durable chatbot history.
- Past-chat reopen is not retained for new conversations.
- Thumbs-up/down feedback is hidden.
- Live chat still works. The current session is kept only in a short-lived server cache (`ns_t3ac_ephemeral_chat`, about **24 hours**), not as a durable TYPO3 log.

Disabling chatbot history affects **newly generated** chatbot and feedback data. Existing records are not automatically removed. Use the history cleanup scheduler to remove previously stored records.

Administrators should consider and document:

- Visitor chatbot data storage (messages, session metadata, visitor history)
- Identifiers: hashed IP (MD5) and browser visitor id — treat hashed IP as **pseudonymised personal data**, not anonymous data
- Browser `localStorage` key `chat_user_id` (still created for live chat when history is off)
- Ephemeral live-session cache (~24 hours) when history is off
- Rate limiting may hash the client IP independently of the history toggle
- Data retention and deletion
- Data sent to the AI provider (messages + RAG context; not IP/UA/cookies in the LLM payload)
- BYOK vs T3Planet Credits — see [T3Planet Credits](/en/latest/ExtNsT3AF/T3Planet-Credit-System/Index)
- Provider DPA / no model training

<Note>
This documentation describes technical data-management capabilities. It does not constitute legal advice.
</Note>
*/}

{/* Detailed developer notes (moved here on 2026-10-08 to keep the page short; not shown on the website):

<Accordion title="Table: where conversations are stored (for developers)">

| Table | What it holds |
| --- | --- |
| `tx_nst3ac_domain_model_chatbot_chat` | Session metadata |
| `tx_nst3ac_domain_model_chatbot_messages` | Visitor messages and AI replies; optional feedback |
| `tx_nst3ac_domain_model_chatbot_history` | Links a visitor to a chatbot session |

</Accordion>
*/}
