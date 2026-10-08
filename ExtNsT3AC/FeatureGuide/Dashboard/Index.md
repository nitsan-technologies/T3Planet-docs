---
title: "Dashboard"
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AC"
  - "Dashboard"
sidebarTitle: "Dashboard"
---

## Purpose

The **Dashboard** is the start page of **AI Universe → AI Chatbot/Search**. It shows at a glance whether everything is set up, which AI is used, how visitors use the chatbot and whether your content has been learned.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmraci4jy0dt1qmhxv2wo4p5p?utm_source=link" loading="lazy" title="T3AC Dashboard Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>
The Dashboard gives an overview of your AI training pipeline for the current site.

{/* ## What you see

- Which AI/embedding model is in use (e.g. OpenAI, Gemini, Mistral, Custom).
- Status of the **Search** and **Chatbot** modules (if installed): active/inactive, AI engine, base model, embedding model.
- Status of your data sources and training (e.g. how many items are pending, completed, or failed).
- **Training Pipeline** section: data sources count, queue size, and a link to CLI reference.
- **Usage Analytics** summary (e.g. total interactions, search queries, chat sessions over the last 7 days).
- A link to the **Scheduler** to run or check the automatic training task.

## Scheduler link

From the Dashboard you can open the TYPO3 Scheduler and locate the automatic training task (typically named **T3AC Training** for this site). Use **Run All** or **Run Task Now** to process the training queue immediately. */}

## What you see

The Dashboard is shared by AI Chatbot and AI Search.

- **AI Foundation Setup Checklist** – what is done and what is still missing.
- **One card per product** (**Chatbot Extension**, **Search Extension**) – the AI used (**AI Engine**, **Base Model**, **Embedding Model**), the **Avg Response** time and a **Configure** button.
- **Usage Analytics** – **Total Interactions** and **Positive** / **Negative** feedback for the last 30 days. Click **View Details** for more.
- **Training Pipeline** – each data source with its progress. Buttons: **Refresh**, **View Queue** and **Run All**.
- Shortcuts at the bottom: **Manage Data Sources**, **Training Pipeline** and **CLI Reference**.

![AI Chatbot/Search Dashboard with setup checklist, product cards, Usage Analytics and Training Pipeline](./images/dashboard.webp)

## Scheduler link

The AI learns your content in the background with the task **T3CS Training (Site N)** (N = the ID of your website's start page).

<Tip>
Want to start learning right away? Click **Run All**.
</Tip>

## Related

- [Data Source](/en/latest/ExtNsT3AC/FeatureGuide/DataSource/Index)
- [Training Center](/en/latest/ExtNsT3AC/FeatureGuide/TrainingCenter/Index)
- [Usage Analytics](/en/latest/ExtNsT3AC/FeatureGuide/UsageAnalytics/Index)
- [AI Usage & Logs in AI Foundation](/en/latest/ExtNsT3AF/Configuration/AIUsageAndLogs/Index)
