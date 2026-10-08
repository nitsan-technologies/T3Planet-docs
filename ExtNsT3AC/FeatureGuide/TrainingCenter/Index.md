---
title: "Training Center"
description: "View the training queue items collected from all data sources and control training and cleanup."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AC"
  - "Training Center"
sidebarTitle: "Training Center"
---

## Purpose

The **Training Center** shows every piece of content the AI has learned or still needs to learn. Use it to check progress, fix failed items and start the training by hand.

You find it in **AI Universe → AI Chatbot/Search → Training Center**.

<div className="t3-embed"><iframe src="https://app.supademo.com/embed/cmracqklk0e92qmhxeuqwubf8?utm_source=link" loading="lazy" title="T3AC Training Center Demo" allow="clipboard-write; fullscreen" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe></div>
View the training queue (items collected from all data sources) and control training and cleanup.

## What you see

{/* - **Summary counts**: Total items, Pending, Embedding (processing), Completed, Failed, and Tokens used. */}

- **Counts** at the top: **Total**, **Pending**, **Processing**, **Completed**, **Failed** and **Tokens** (how much AI was used).
- **All Sources** – your data sources and how many items each has.
- **Training Queue** – a list of all items with **Item**, **Status**, **Tokens**, **Created** and **Actions**.
- **Filters** – by data source, by status (**All Statuses**) or by search text.

![Training Center with counts, data sources and the training queue](./images/training-center.webp)

**What the status means**

- **Pending** – waiting to be learned.
- **Processing / Embedding** – being learned right now.
- **Completed** – learned. The chatbot can use it.
- **Failed** – something went wrong. Try **Re-queue**.

## Actions

### Sync

Reads the content of the data source again (same as on the **Data Source** tab).

### Reset (Re-queue)

1. Select a **Failed** (or **Completed**) item.
2. Click **Re-queue**.
3. It goes back to **Pending** and is learned again at the next training run.

{/* ### Delete

Removes selected queue items. */}

### Delete

1. Select the items.
2. Click **Delete**.

The chatbot no longer uses this content.

<Info>
Deleted items will not be trained again unless they are added again by a new sync.
</Info>

{/* ### Run training

Use the link to the **Scheduler** module and run the **T3AC Training** task for this site.

When the task runs, it:

- Processes all **Pending** queue items (generates embeddings).
- Runs cleanup of old completed/failed items according to the retention setting. */}

### Run training

1. Click **Run Task Now**. The Scheduler opens.
2. Run the task **T3CS Training (Site N)** for your website.

The task learns all **Pending** items and removes old **Failed** items after the number of days in **Retention Days**. Learned items are kept.

{/* SUPADEMO NEEDED: Training Center: re-queue and run */}

## Training behaviour (simple terms)

- Only **Pending** items are learned.
- Learning means your text is sent to your AI service and the result is saved for the chatbot and AI Search.
- Afterwards the item is **Completed**, or **Failed** if there was an error.
- How often training runs depends on the **Sync Interval** of your data sources – and the Scheduler must be running on your server.

## Related

- [Data Source](/en/latest/ExtNsT3AC/FeatureGuide/DataSource/Index) – add or sync the content that is trained
- [Scheduler](/en/latest/ExtNsT3AC/FeatureGuide/DataSource/Index#scheduler) – the task **T3CS Training (Site N)**
- [Dashboard](/en/latest/ExtNsT3AC/FeatureGuide/Dashboard/Index) – training status and **Run All**

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

Queue item statuses:

- **Pending** – Waiting to be processed.
- **Processing / Embedding** – Currently being sent to the embeddings service.
- **Completed** – Successfully trained.
- **Failed** – Error during training.

Refreshes content from the data source into the queue (same as in the **Data Source** tab).

Puts a **failed** or **completed** item back to **Pending** so it will be processed again on the next training run.

- Only items in status **Pending** are processed when training runs.
- **Processing** means: the text is sent to the configured embeddings service, and the result is stored for search/chatbot usage.
- After success, the item is marked **Completed**; on error, **Failed**.
- How often training runs depends on the Sync interval of your data sources and on the Scheduler actually being triggered (e.g. via cron).
*/}
