---
title: "Configurable Database Chunking for various types of Dataset Processing"
description: "This feature provides configurable database chunking to efficiently process large datasets while maintaining optimal performance and stability."
keywords:
  - "TYPO3"
  - "T3Planet"
  - "T3AS"
  - "Configurable Database Chunking for various types of Dataset Processing"
sidebarTitle: "DatabaseChunking"
---

## Overview

When AI Search reads a lot of content, it works in small portions (chunks) instead of all at once. This keeps your server from running out of memory or stopping halfway.

The default is **1000** records per portion. Most websites never need to change it.

## Configuration Steps

1. Go to **AI Universe → AI Foundation → AI Features**.
2. Open the **Training** card.
3. Change **Chunk Size** if needed (see the table below).
4. Optional: change **Batch Size** and **Retention Days**.
5. Click **Save Changes**.

![Training drawer in AI Foundation with Chunk Size, Batch Size and Retention Days](./images/training-settings.webp)

## Recommendations

| Your website | Chunk Size |
| --- | --- |
| Small (fewer than 10,000 records) | 1000 (default) or 500–800 |
| Medium (10,000–50,000 records) | 1000–1500 |
| Large (more than 50,000 records) | 1500–2000 – ask your hosting to watch memory use |

<Tip>
Training stops with a memory error? Make the **Chunk Size** smaller. Training is very slow and your server has plenty of memory? Make it bigger.
</Tip>

{/* Original text before the 8 Oct 2026 simplification (kept for reference):

This feature provides configurable database chunking to efficiently process large datasets while maintaining optimal performance and stability. Instead of loading all records in a single query, data is fetched and processed in smaller chunks, reducing memory usage and preventing execution timeouts.

The chunk size is configurable via the T3AF feature settings, allowing administrators to adjust it according to server capacity and dataset size.

## Default Configuration

By default, database chunking is enabled with a chunk size of **1000 records**.

If required, this value can be modified in **T3AF → AI Features → Training** to better suit the execution environment.

1. Open **T3AF** in the TYPO3 backend.
2. Go to **AI Features**.
3. Open the **Training** card (Embeddings pipeline).
4. Adjust **Chunk Size**, **Batch Size**, and **Retention Days** as needed.
5. Click **Save Changes**.

Configure **Chunk Size**, **Batch Size**, and **Retention Days** under **T3AF → AI Features → Training**.

**Chunk Size Guidelines:**

- **Small datasets (< 10,000 records):** Use default value (1000) or lower (500-800)
- **Medium datasets (10,000 - 50,000 records):** Use 1000-1500
- **Large datasets (> 50,000 records):** Use 1500-2000, but monitor server memory usage

<Note>
Adjusting the chunk size can significantly impact performance. Smaller chunks use less memory but may take longer to process. Larger chunks process faster but require more memory. Monitor your server’s memory usage when adjusting this value.
</Note>

## Benefits

- **Reduced Memory Usage:** Processing data in smaller chunks prevents memory exhaustion
- **Prevents Timeouts:** Smaller batches reduce the risk of PHP execution timeouts
- **Better Performance:** Optimized chunk sizes can improve overall processing speed
- **Flexible Configuration:** Administrators can adjust settings based on their specific environment
*/}
