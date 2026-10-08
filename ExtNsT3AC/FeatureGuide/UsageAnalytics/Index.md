---
title: "Usage Analytics"
description: "View recent search and chatbot activity if the corresponding extensions are installed."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AC"
  - "Usage Analytics"
sidebarTitle: "Usage Analytics"
---

## Purpose

**Usage Analytics** shows what visitors asked the chatbot (and AI Search) and how they rated the answers. Use it to see which questions come up often and where answers can be improved.

You find it in **AI Universe → AI Chatbot/Search → Usage Analytics**.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmracyax70em8qmhxmigmckrv?utm_source=link&embed_v=2&utm_source=embed" loading="lazy" title="T3AC Usage Analytics Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>

{/* ## What you see

### Chatbot

Recent conversations: e.g. IP, first input/output, message count, time. */}

## What you see

- **Total Interactions**, **Search Queries**, **Chat Sessions**, **Positive Feedback** and **Negative Feedback**
- **Interaction Logs** – a list of conversations and searches with the question, the answer and the time
- Click **View Details** to read the whole conversation, the feedback and the reference sources

![Usage Analytics with interaction counts, feedback and the interaction log](./images/usage-analytics.webp)

<Note>
The visitor's IP address is not stored in plain text. It is saved as a hash (a one-way code), so you cannot read the real IP.
</Note>

<Note>
Conversations only appear here if **Save chatbot history** is on (**Chatbot → Configuration**). Searches only appear if **Save search history** is on (**Search → Settings**).
</Note>

{/* Enable **Save chatbot history** in **Chatbot → Settings** so conversations appear in this log. Enable **Save search history** in **T3AS → Search → Settings** so search queries and answers appear here. */}

## Filtering and export

- **Search queries or responses** – search in the list.
- **All Modules** / **All Languages** – show only chatbot or search, or one language.
- **Export** – download the data.

## Deletion / cleanup

You can delete single entries, for example when a visitor asks you to:

- Deleting a **search** entry removes it from the search history.
- Deleting a **chatbot** entry can remove all conversations from the same visitor.

To delete old entries automatically, see [History cleanup](/en/latest/ExtNsT3AC/FeatureGuide/DataSource/Index#t3as-history-cleanup).

{/* When no data has been recorded yet, the message shown is: *“No interaction logs yet. Search and chatbot history will appear here when the modules are loaded and users interact.”* */}

When no data exists yet, you see: *"No interaction logs yet. Search and Chatbot history will appear here once users start interacting."*

## Related

- [AI Usage & Logs in AI Foundation](/en/latest/ExtNsT3AF/Configuration/AIUsageAndLogs/Index) – AI requests, tokens and log messages
- [AI Search Usage Analytics](/en/latest/ExtNsT3AS/Configuration/UsageAnalytics/Index) – the same tab for search
- [DPA & GDPR](/en/latest/ExtNsT3AC/DPAandGDPR/Index) – what is stored and for how long

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

View recent search and chatbot activity (if the corresponding extensions are installed).

- **Search queries or responses** – Search within the logs.
- **All Modules** / **All Languages** – Filter by module and language.
- **Export** – Download analytics data.

You can delete individual entries (for privacy or cleanup):

- Deleting **search** entries affects search history.
- Deleting **chatbot** entries can be per IP (all conversations from that IP).

To delete old usage history automatically, use the `t3af:history:cleanup` scheduler task. Set the **days** argument for the retention period (default `90`). See **Scheduler** in [Data Source](/en/latest/ExtNsT3AC/FeatureGuide/DataSource/Index).
*/}
